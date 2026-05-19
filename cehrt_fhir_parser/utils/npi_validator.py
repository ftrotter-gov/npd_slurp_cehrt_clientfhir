"""
Cached NPI validation against the CMS NPI Registry.
"""

import csv
import re
import time
from pathlib import Path
from typing import Dict, Optional, Union

import requests


class NPIValidator:
    """
    Validate NPI numbers with a local CSV cache and CMS API fallback.

    Cache files live in one directory and match ``valid_npi.*.csv``. Each file
    must have ``npi`` and ``is_valid`` columns where ``is_valid`` is ``1`` or
    ``0``.
    """

    def __init__(self, *, cache_file_path: Optional[str] = None):
        if cache_file_path is None:
            self.cache_file_path = Path("./npi_validation_data/valid_npi.3.csv")
        else:
            self.cache_file_path = Path(cache_file_path)

        self.npi_cache: Dict[str, bool] = {}
        self.newly_validated_npis: Dict[str, bool] = {}
        self.api_fallback_count: int = 0
        self.api_fallback_threshold: int = 20

        self._load_cache()

    def _load_cache(self):
        """Load existing NPI validation results from cache CSV files."""
        cache_dir = self.cache_file_path.parent

        if not cache_dir.exists():
            raise FileNotFoundError(
                f"Cache directory does not exist: {cache_dir}\n"
                f"NPIValidator requires cache files to avoid slow API calls.\n"
                f"Please ensure the cache directory and valid_npi.*.csv files exist."
            )

        cache_files = list(cache_dir.glob("valid_npi.*.csv"))

        if not cache_files:
            raise FileNotFoundError(
                f"No cache files found with pattern valid_npi.*.csv in {cache_dir}\n"
                f"NPIValidator requires cache files to avoid slow API calls.\n"
                f"Please ensure valid_npi.*.csv files exist in the cache directory."
            )

        total_loaded = 0

        for cache_file in sorted(cache_files):
            try:
                with open(cache_file, "r", encoding="utf-8") as f:
                    reader = csv.DictReader(f)
                    file_count = 0

                    for row in reader:
                        npi = str(row.get("npi", "")).strip()
                        is_valid_str = str(row.get("is_valid", "")).strip()

                        if npi and is_valid_str:
                            self.npi_cache[npi] = is_valid_str == "1"
                            file_count += 1

                    print(f"Loaded {file_count} NPIs from {cache_file}")
                    total_loaded += file_count

            except Exception as e:
                print(f"Error loading cache file {cache_file}: {e}")

        print(f"Total loaded: {total_loaded} NPIs from {len(cache_files)} cache files")

    def _save_cache(self):
        """Append newly validated NPIs to the configured cache file."""
        if not self.newly_validated_npis:
            return

        try:
            self.cache_file_path.parent.mkdir(parents=True, exist_ok=True)
            file_exists = self.cache_file_path.exists()

            with open(self.cache_file_path, "a", newline="", encoding="utf-8") as f:
                fieldnames = ["npi", "is_valid"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)

                if not file_exists:
                    writer.writeheader()

                for npi, is_valid in self.newly_validated_npis.items():
                    writer.writerow({"npi": npi, "is_valid": 1 if is_valid else 0})

            print(
                f"NPIValidator: Saved {len(self.newly_validated_npis)} new NPI "
                f"validations to {self.cache_file_path}"
            )

        except Exception as e:
            print(f"NPIValidator: Error saving cache file: {e}")

    @staticmethod
    def _is_valid_npi_format(*, npi_value: str) -> bool:
        """Return true when the value contains exactly 10 digits."""
        if not npi_value:
            return False

        digits_only = re.sub(r"\D", "", str(npi_value))
        return len(digits_only) == 10

    @staticmethod
    def _validate_npi_via_api(
        *, npi_value: str, max_retries: int = 3, delay: float = 0.1
    ) -> Dict[str, Union[bool, str, int, None]]:
        """Validate an NPI against the CMS NPI Registry API."""
        if not NPIValidator._is_valid_npi_format(npi_value=npi_value):
            return {
                "is_valid_format": False,
                "is_valid_api": False,
                "api_error": "Invalid NPI format",
                "result_count": 0,
            }

        clean_npi = re.sub(r"\D", "", str(npi_value))
        url = f"https://npiregistry.cms.hhs.gov/api/?version=2.1&number={clean_npi}"

        for attempt in range(max_retries):
            try:
                if attempt > 0:
                    time.sleep(delay * (2 ** attempt))

                response = requests.get(url, timeout=10)
                response.raise_for_status()

                data = response.json()
                result_count = data.get("result_count", 0)

                return {
                    "is_valid_format": True,
                    "is_valid_api": result_count > 0,
                    "api_error": None,
                    "result_count": result_count,
                }

            except requests.exceptions.RequestException as e:
                if attempt == max_retries - 1:
                    return {
                        "is_valid_format": True,
                        "is_valid_api": False,
                        "api_error": f"API request failed: {str(e)}",
                        "result_count": 0,
                    }
                continue
            except Exception as e:
                return {
                    "is_valid_format": True,
                    "is_valid_api": False,
                    "api_error": f"Unexpected error: {str(e)}",
                    "result_count": 0,
                }

        return {
            "is_valid_format": True,
            "is_valid_api": False,
            "api_error": "Max retries exceeded",
            "result_count": 0,
        }

    def is_this_npi_valid(self, *, npi_value: str) -> bool:
        """Check cache first, then validate through the API and cache the result."""
        if not npi_value:
            return False

        clean_npi = re.sub(r"\D", "", str(npi_value))

        if clean_npi in self.npi_cache:
            return self.npi_cache[clean_npi]

        cache_size = len(self.npi_cache)
        print(
            f"Fall back to validating NPI via API: {clean_npi} "
            f"(Cache has {cache_size} NPIs loaded)"
        )
        api_result = self._validate_npi_via_api(npi_value=clean_npi)
        is_valid = bool(api_result.get("is_valid_api", False))

        self.npi_cache[clean_npi] = is_valid
        self.newly_validated_npis[clean_npi] = is_valid
        self.api_fallback_count += 1

        if self.api_fallback_count >= self.api_fallback_threshold:
            print(
                f"NPIValidator: Reached {self.api_fallback_count} API fallbacks, "
                "writing cache..."
            )
            self._save_cache()
            self.newly_validated_npis.clear()
            self.api_fallback_count = 0

        return is_valid

    def close(self):
        """Flush newly validated NPIs to the configured cache file."""
        self._save_cache()
        self.newly_validated_npis.clear()

    def __del__(self):
        try:
            self._save_cache()
        except Exception as e:
            print(f"Error in NPIValidator destructor: {e}")


import pytest

from cehrt_fhir_parser.utils.npi_validator import NPIValidator
from cehrt_fhir_parser.utils.validators import DataValidator


def test_npi_validator_uses_cache(npi_cache_dir, monkeypatch):
    validator = NPIValidator(cache_file_path=str(npi_cache_dir / "valid_npi.3.csv"))

    def fail_api_call(**kwargs):
        raise AssertionError("API should not be called for cached NPIs")

    monkeypatch.setattr(NPIValidator, "_validate_npi_via_api", staticmethod(fail_api_call))

    assert validator.is_this_npi_valid(npi_value="1234567890") is True
    assert validator.is_this_npi_valid(npi_value="1111111111") is False


def test_npi_validator_caches_api_fallback(npi_cache_dir, monkeypatch):
    validator = NPIValidator(cache_file_path=str(npi_cache_dir / "valid_npi.3.csv"))

    def api_result(**kwargs):
        return {
            "is_valid_format": True,
            "is_valid_api": True,
            "api_error": None,
            "result_count": 1,
        }

    monkeypatch.setattr(NPIValidator, "_validate_npi_via_api", staticmethod(api_result))

    assert validator.is_this_npi_valid(npi_value="1999999999") is True
    assert validator.npi_cache["1999999999"] is True
    assert validator.newly_validated_npis["1999999999"] is True


def test_npi_validator_requires_cache_files(tmp_path):
    cache_dir = tmp_path / "empty_npi_cache"
    cache_dir.mkdir()

    with pytest.raises(FileNotFoundError):
        NPIValidator(cache_file_path=str(cache_dir / "valid_npi.3.csv"))


def test_data_validator_format_validation():
    assert DataValidator._is_valid_npi_format("1234567890") is True
    assert DataValidator._is_valid_npi_format("0234567890") is False
    assert DataValidator._is_valid_npi_format("123456789") is False


def test_data_validator_can_use_injected_npi_validator():
    class FakeNPIValidator:
        def is_this_npi_valid(self, *, npi_value):
            return npi_value == "1234567890"

    validator = DataValidator(npi_validator=FakeNPIValidator())

    valid = validator.validate_npi(npi_value="1234567890")
    invalid = validator.validate_npi(npi_value="1999999999")

    assert valid["is_valid_api"] is True
    assert invalid["is_valid_api"] is False


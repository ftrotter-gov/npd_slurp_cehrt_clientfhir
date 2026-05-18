#!/usr/bin/env python3

"""
Many Identifier Analysis Looper

Analyzes organization JSON files to find records with multiple identifiers.
- Tracks records with 2+ NPI identifiers specifically
- Tracks records with 2+ identifiers of any type (excluding those with 2+ NPIs)
- No validation of identifier format - just counts
- Generates two outputs:
  1. Summary report with statistics
  2. Links document with GitHub URLs to all matching files
"""

import json
import random
import argparse
from pathlib import Path
from typing import Dict, List, Tuple
from collections import defaultdict
from EndPointLooperParent import EndPointLooperParent


class ManyIdentifierLooper(EndPointLooperParent):
    """
    Child class that analyzes identifier arrays in organization FHIR JSON files.
    Focuses on finding records with multiple identifiers, especially multiple NPIs.
    """
    
    def __init__(self):
        """Initialize the identifier analyzer with data tracking structures."""
        super().__init__()
        
        # Track files with multiple identifiers
        # Structure: [(filename, relative_path, npi_count, total_count), ...]
        self.multiple_npis_files: List[Tuple[str, str, int, int]] = []
        
        # Structure: [(filename, relative_path, total_count), ...]
        self.multiple_identifiers_files: List[Tuple[str, str, int]] = []
        
        # Statistics
        self.stats = {
            'multiple_npis': 0,
            'multiple_identifiers_non_npi': 0,
            'single_or_no_identifiers': 0
        }
        
        # Track current file's relative path
        self.current_relative_path = ""
    
    def discover_json_files(self, *, cache_directory: str, test_mode: bool = False) -> List[Path]:
        """
        Override parent method to ONLY search organization subdirectories.
        
        Args:
            cache_directory: Path to the CEHRT cache directory
            test_mode: If True, process 4 files each from 10 random subdirectories
            
        Returns:
            List of Path objects pointing to organization JSON files
        """
        # Try both relative path and resolved absolute path
        cache_path = Path(cache_directory)
        if not cache_path.exists():
            # Try alternative path locations
            alternative_paths = [
                Path("../../npd_ehr_scrape_cache/cache/fhir_json_cache/"),
                Path("../npd_ehr_scrape_cache/cache/fhir_json_cache/"),
                Path("npd_ehr_scrape_cache/cache/fhir_json_cache/"),
                Path("../../../npd_ehr_scrape_cache/cehrt_fhir_json/"),
                Path("../../npd_ehr_scrape_cache/cehrt_fhir_json/"),
                Path("../npd_ehr_scrape_cache/cehrt_fhir_json/"),
                Path("npd_ehr_scrape_cache/cehrt_fhir_json/"),
            ]
            
            cache_path_found = False
            for alt_path in alternative_paths:
                if alt_path.exists():
                    cache_path = alt_path
                    cache_path_found = True
                    break
            
            if not cache_path_found:
                try:
                    cache_path = Path(cache_directory).resolve()
                    if not cache_path.exists():
                        raise FileNotFoundError(f"ManyIdentifierLooper Error: Cache directory not found at {cache_directory}")
                except (OSError, RuntimeError):
                    raise FileNotFoundError(f"ManyIdentifierLooper Error: Cache directory not accessible: {cache_directory}")
        
        json_files = []
        
        # Get all subdirectories, sorted for consistent ordering
        subdirectories = [d for d in cache_path.iterdir() if d.is_dir()]
        subdirectories.sort()
        
        if test_mode:
            # Select 10 random subdirectories, or all if fewer than 10
            num_subdirs = min(10, len(subdirectories))
            if num_subdirs > 0:
                subdirectories = random.sample(subdirectories, num_subdirs)
        
        for subdirectory in subdirectories:
            subdir_json_files = []
            
            # ONLY look for JSON files in organization/ subdirectory
            organization_dir = subdirectory / "organization"
            if organization_dir.exists() and organization_dir.is_dir():
                subdir_json_files.extend(list(organization_dir.glob("*.json")))
            
            if test_mode:
                # Take only first 4 JSON files from each subdirectory
                subdir_json_files = subdir_json_files[:4]
            
            json_files.extend(subdir_json_files)
        
        self.total_files_found = len(json_files)
        return json_files
    
    def analyze_this_json_data(self, *, json_data: dict, source_filename: str) -> None:
        """
        Analyze JSON data to count identifiers and NPIs.
        
        Args:
            json_data: The JSON data as a dictionary
            source_filename: Name of the source file being processed
        """
        # Extract relative path - will be set properly in run_loop
        if not self.current_relative_path:
            self.current_relative_path = f"unknown_dir/organization/{source_filename}"
        
        # Look for identifier array under the 'resource' element
        npi_count = 0
        total_identifiers = 0
        
        if 'resource' in json_data and isinstance(json_data['resource'], dict):
            resource = json_data['resource']
            identifiers = resource.get('identifier', [])
            
            if isinstance(identifiers, list):
                total_identifiers = len(identifiers)
                
                # Count NPIs specifically
                for identifier in identifiers:
                    if isinstance(identifier, dict):
                        system = identifier.get('system')
                        if system == 'http://hl7.org/fhir/sid/us-npi':
                            npi_count += 1
        
        # Categorize based on counts
        if npi_count >= 2:
            # Priority: Records with 2+ NPIs go in the NPI category
            self.stats['multiple_npis'] += 1
            self.multiple_npis_files.append((
                source_filename,
                self.current_relative_path,
                npi_count,
                total_identifiers
            ))
        elif total_identifiers >= 2:
            # Records with 2+ identifiers (but less than 2 NPIs)
            self.stats['multiple_identifiers_non_npi'] += 1
            self.multiple_identifiers_files.append((
                source_filename,
                self.current_relative_path,
                total_identifiers
            ))
        else:
            # Single or no identifiers
            self.stats['single_or_no_identifiers'] += 1
    
    def generate_summary_markdown(self) -> str:
        """
        Generate a comprehensive summary of identifier analysis as markdown string.
        
        Returns:
            String containing the markdown summary report
        """
        lines = []
        lines.append("# Many Identifier Analysis Summary")
        lines.append("")
        lines.append("## What This Analysis Does")
        lines.append("This analysis examines organization JSON files to find records with multiple identifiers.")
        lines.append("It specifically tracks:")
        lines.append("- Records with 2 or more NPI identifiers (system: `http://hl7.org/fhir/sid/us-npi`)")
        lines.append("- Records with 2 or more identifiers of any type (excluding those with 2+ NPIs)")
        lines.append("")
        lines.append("**Note:** This analysis does NOT validate identifier format - it only counts identifiers.")
        lines.append("")
        lines.append("## Processing Results")
        lines.append(f"**Files Processed:** {self.processed_count}")
        lines.append(f"**Files Failed:** {self.failure_count}")
        lines.append(f"**Total Organization Files Found:** {self.total_files_found}")
        lines.append("")
        
        lines.append("## Identifier Analysis Results")
        lines.append("")
        lines.append("| Category | Count | Percentage |")
        lines.append("|----------|-------|------------|")
        
        total = self.processed_count if self.processed_count > 0 else 1
        
        lines.append(f"| Organizations with 2+ NPIs | {self.stats['multiple_npis']} | {self.stats['multiple_npis']/total*100:.1f}% |")
        lines.append(f"| Organizations with 2+ Identifiers (Non-NPI) | {self.stats['multiple_identifiers_non_npi']} | {self.stats['multiple_identifiers_non_npi']/total*100:.1f}% |")
        lines.append(f"| Organizations with Single/No Identifiers | {self.stats['single_or_no_identifiers']} | {self.stats['single_or_no_identifiers']/total*100:.1f}% |")
        lines.append("")
        lines.append(f"**Total Organizations Analyzed:** {self.processed_count}")
        lines.append("")
        
        # Add examples if available
        if self.multiple_npis_files:
            lines.append("## Example Organizations with Multiple NPIs")
            lines.append("")
            # Show first 3 examples
            for i, (filename, relative_path, npi_count, total_count) in enumerate(self.multiple_npis_files[:3]):
                web_url = self.get_web_url_of_cache_file(relative_path=relative_path)
                lines.append(f"{i+1}. {web_url} - {npi_count} NPIs (out of {total_count} total identifiers)")
            lines.append("")
            lines.append(f"*See ManyIdentifierLinks.md for complete list of all {len(self.multiple_npis_files)} organizations*")
            lines.append("")
        
        if self.multiple_identifiers_files:
            lines.append("## Example Organizations with Multiple Identifiers (Non-NPI)")
            lines.append("")
            # Show first 3 examples
            for i, (filename, relative_path, total_count) in enumerate(self.multiple_identifiers_files[:3]):
                web_url = self.get_web_url_of_cache_file(relative_path=relative_path)
                lines.append(f"{i+1}. {web_url} - {total_count} total identifiers")
            lines.append("")
            lines.append(f"*See ManyIdentifierLinks.md for complete list of all {len(self.multiple_identifiers_files)} organizations*")
            lines.append("")
        
        return "\n".join(lines)
    
    def generate_links_markdown(self) -> str:
        """
        Generate a markdown document with GitHub links to all matching organization files.
        
        Returns:
            String containing the markdown links document
        """
        lines = []
        lines.append("# Organizations with Multiple Identifiers - Complete List")
        lines.append("")
        lines.append("This document provides direct GitHub links to all organization JSON files that have multiple identifiers.")
        lines.append("")
        
        # Section 1: Organizations with Multiple NPIs
        lines.append("## Section 1: Organizations with Multiple NPIs")
        lines.append("")
        lines.append(f"Total organizations with 2+ NPIs: **{len(self.multiple_npis_files)}**")
        lines.append("")
        
        if self.multiple_npis_files:
            # Sort by NPI count (descending), then by filename
            sorted_npi_files = sorted(
                self.multiple_npis_files,
                key=lambda x: (-x[2], x[0])  # x[2] is npi_count
            )
            
            for i, (filename, relative_path, npi_count, total_count) in enumerate(sorted_npi_files, 1):
                web_url = self.get_web_url_of_cache_file(relative_path=relative_path)
                lines.append(f"{i}. {web_url} - **{npi_count} NPIs** (out of {total_count} total identifiers)")
        else:
            lines.append("*No organizations found with multiple NPIs.*")
        
        lines.append("")
        lines.append("---")
        lines.append("")
        
        # Section 2: Organizations with Multiple Identifiers (Non-NPI)
        lines.append("## Section 2: Organizations with Multiple Identifiers (Non-NPI)")
        lines.append("")
        lines.append(f"Total organizations with 2+ identifiers (but fewer than 2 NPIs): **{len(self.multiple_identifiers_files)}**")
        lines.append("")
        
        if self.multiple_identifiers_files:
            # Sort by total identifier count (descending), then by filename
            sorted_id_files = sorted(
                self.multiple_identifiers_files,
                key=lambda x: (-x[2], x[0])  # x[2] is total_count
            )
            
            for i, (filename, relative_path, total_count) in enumerate(sorted_id_files, 1):
                web_url = self.get_web_url_of_cache_file(relative_path=relative_path)
                lines.append(f"{i}. {web_url} - **{total_count} total identifiers**")
        else:
            lines.append("*No organizations found with multiple non-NPI identifiers.*")
        
        lines.append("")
        
        return "\n".join(lines)
    
    def print_summary(self) -> None:
        """
        Print a comprehensive summary of identifier analysis.
        """
        print("\n" + self.generate_summary_markdown())


def main():
    """Command-line interface for running the Many Identifier Looper"""
    parser = argparse.ArgumentParser(
        description="Analyze organization JSON files for multiple identifiers"
    )
    parser.add_argument(
        '--test-mode', 
        action='store_true',
        help="Run in test mode (process 4 files from 10 random subdirectories)"
    )
    parser.add_argument(
        '--summary_output',
        type=str,
        default='ManyIdentifierReport.md',
        help="Save summary markdown output to specified file (default: ManyIdentifierReport.md)"
    )
    parser.add_argument(
        '--links_output',
        type=str,
        default='ManyIdentifierLinks.md',
        help="Save links markdown output to specified file (default: ManyIdentifierLinks.md)"
    )
    
    args = parser.parse_args()
    
    try:
        # Create and run the analyzer
        analyzer = ManyIdentifierLooper()
        analyzer.run_loop(test_mode=args.test_mode)
        
        # Save summary markdown output
        summary_content = analyzer.generate_summary_markdown()
        with open(args.summary_output, 'w', encoding='utf-8') as f:
            f.write(summary_content)
        print(f"\nSummary report saved to: {args.summary_output}")
        
        # Save links markdown output
        links_content = analyzer.generate_links_markdown()
        with open(args.links_output, 'w', encoding='utf-8') as f:
            f.write(links_content)
        print(f"Links document saved to: {args.links_output}")
            
    except KeyboardInterrupt:
        print("\nAnalysis interrupted by user")
        return 1
    except Exception as e:
        print(f"Analysis failed: {str(e)}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())

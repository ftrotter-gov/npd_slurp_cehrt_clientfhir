#!/usr/bin/env python3
"""
StepTest_AnalyzeNPISystems.py

Analyzes all Organization JSON files in the cache to determine what NPI identifier
system URIs are actually being used in the wild.

This helps us understand:
- What system URIs vendors are using for NPIs
- How many would be caught by different filtering strategies
- Whether our current filters are too restrictive

Output: test_data/npi_system_analysis.csv
"""

import json
import csv
import argparse
import re
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Tuple
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv('data_files.env')


class NPISystemAnalyzer:
    """Analyzes NPI system URIs across all Organization resources in cache"""
    
    @staticmethod
    def is_valid_npi_format(*, value: str) -> bool:
        """Check if value matches 10-digit NPI format"""
        value_str = str(value).strip()
        return bool(re.match(r'^\d{10}$', value_str))
    
    @staticmethod
    def is_npi_like_identifier(*, system: str, value: str) -> bool:
        """
        Determine if an identifier looks like it could be an NPI.
        Uses the same logic as the parser.
        """
        system_lower = system.lower()
        
        # Check if system contains 'npi' OR value is 10 digits
        if 'npi' in system_lower:
            return True
        
        if NPISystemAnalyzer.is_valid_npi_format(value=value):
            return True
        
        return False
    
    @staticmethod
    def scan_cache_for_organizations(*, cache_dir: Path) -> List[Path]:
        """Find all Organization JSON files in the cache directory"""
        org_files = []
        
        print(f"Scanning cache directory: {cache_dir}")
        
        # Look for vendor directories with organization subdirectories
        if not cache_dir.exists():
            print(f"ERROR: Cache directory does not exist: {cache_dir}")
            return []
        
        # Walk through all subdirectories looking for organization/*.json files
        for vendor_dir in cache_dir.iterdir():
            if not vendor_dir.is_dir():
                continue
            
            org_dir = vendor_dir / 'organization'
            if org_dir.exists() and org_dir.is_dir():
                json_files = list(org_dir.glob('*.json'))
                org_files.extend(json_files)
                print(f"  Found {len(json_files)} Organization files in {vendor_dir.name}")
        
        print(f"\nTotal Organization JSON files found: {len(org_files)}")
        return org_files
    
    @staticmethod
    def extract_identifiers_from_org_file(*, file_path: Path) -> List[Tuple[str, str]]:
        """
        Extract all identifiers from an Organization JSON file.
        Returns list of (system, value) tuples.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Handle both bundle entry format and raw resource format
            if 'resource' in data:
                resource = data['resource']
            else:
                resource = data
            
            # Verify it's an Organization resource
            if resource.get('resourceType') != 'Organization':
                return []
            
            # Extract identifiers
            identifiers = resource.get('identifier', [])
            if not isinstance(identifiers, list):
                return []
            
            results = []
            for identifier in identifiers:
                if not isinstance(identifier, dict):
                    continue
                
                system = identifier.get('system', '')
                value = identifier.get('value', '')
                
                if system and value:
                    results.append((str(system), str(value)))
            
            return results
            
        except json.JSONDecodeError as e:
            print(f"  Warning: JSON decode error in {file_path.name}: {e}")
            return []
        except Exception as e:
            print(f"  Warning: Error processing {file_path.name}: {e}")
            return []
    
    @staticmethod
    def analyze_npi_systems(*, cache_dir: Path) -> Dict[str, Dict]:
        """
        Scan all Organization files and analyze NPI identifier systems.
        Returns dict of system_uri -> {count, examples, etc.}
        """
        print("\nPhase 1: Scanning Organization files...")
        org_files = NPISystemAnalyzer.scan_cache_for_organizations(cache_dir=cache_dir)
        
        if not org_files:
            print("ERROR: No Organization files found!")
            return {}
        
        print("\nPhase 2: Extracting identifiers...")
        system_data = defaultdict(lambda: {
            'count': 0,
            'example_value': None,
            'matches_us_npi_filter': False,
            'matches_npi_filter': False,
            'has_valid_10_digit': False
        })
        
        total_npi_like = 0
        processed_files = 0
        
        for file_path in org_files:
            identifiers = NPISystemAnalyzer.extract_identifiers_from_org_file(file_path=file_path)
            
            for system, value in identifiers:
                # Only count NPI-like identifiers
                if NPISystemAnalyzer.is_npi_like_identifier(system=system, value=value):
                    system_data[system]['count'] += 1
                    total_npi_like += 1
                    
                    # Store first example value
                    if system_data[system]['example_value'] is None:
                        system_data[system]['example_value'] = value
                    
                    # Check filter matches
                    system_lower = system.lower()
                    system_data[system]['matches_us_npi_filter'] = 'us-npi' in system_lower
                    system_data[system]['matches_npi_filter'] = 'npi' in system_lower
                    
                    # Check if example is valid 10-digit
                    if NPISystemAnalyzer.is_valid_npi_format(value=value):
                        system_data[system]['has_valid_10_digit'] = True
            
            processed_files += 1
            if processed_files % 1000 == 0:
                print(f"  Processed {processed_files}/{len(org_files)} files...")
        
        print(f"\nPhase 3: Analysis complete")
        print(f"  Files processed: {processed_files}")
        print(f"  NPI-like identifiers found: {total_npi_like}")
        print(f"  Unique system URIs: {len(system_data)}")
        
        return dict(system_data)
    
    @staticmethod
    def write_analysis_csv(*, system_data: Dict[str, Dict], output_file: Path):
        """Write analysis results to CSV file"""
        
        # Calculate total count for percentages
        total_count = sum(data['count'] for data in system_data.values())
        
        if total_count == 0:
            print("WARNING: No NPI-like identifiers found to analyze")
            return
        
        # Prepare rows
        rows = []
        for system_uri, data in system_data.items():
            percentage = (data['count'] / total_count) * 100
            
            row = {
                'system_uri': system_uri,
                'count': data['count'],
                'percentage': f"{percentage:.2f}",
                'example_npi_value': data['example_value'] or '',
                'matches_us_npi_filter': 'Yes' if data['matches_us_npi_filter'] else 'No',
                'matches_npi_filter': 'Yes' if data['matches_npi_filter'] else 'No',
                'is_valid_10_digit': 'Yes' if data['has_valid_10_digit'] else 'No'
            }
            rows.append(row)
        
        # Sort by count (descending)
        rows.sort(key=lambda x: x['count'], reverse=True)
        
        # Write CSV
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        fieldnames = [
            'system_uri',
            'count',
            'percentage',
            'example_npi_value',
            'matches_us_npi_filter',
            'matches_npi_filter',
            'is_valid_10_digit'
        ]
        
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        
        print(f"\nResults written to: {output_file}")
        print(f"Total systems analyzed: {len(rows)}")
        
        # Print summary
        print("\nTop 10 most common NPI system URIs:")
        print("-" * 80)
        for i, row in enumerate(rows[:10], 1):
            print(f"{i}. {row['system_uri']}")
            print(f"   Count: {row['count']} ({row['percentage']}%)")
            print(f"   Caught by 'us-npi' filter: {row['matches_us_npi_filter']}")
            print(f"   Caught by 'npi' filter: {row['matches_npi_filter']}")
            print()
    
    @staticmethod
    def run():
        """Main execution method"""
        parser = argparse.ArgumentParser(
            description='Analyze NPI system URIs in Organization cache files'
        )
        parser.add_argument(
            '--cache_dir',
            type=str,
            help='Path to cache directory containing vendor/organization subdirectories',
            default=None
        )
        parser.add_argument(
            '--output',
            type=str,
            help='Path to output CSV file',
            default='test_data/npi_system_analysis.csv'
        )
        
        args = parser.parse_args()
        
        # Get cache directory from argument or environment
        if args.cache_dir:
            cache_dir = Path(os.path.expandvars(args.cache_dir))
        else:
            # Try to get from environment
            cache_dir_env = os.getenv('CACHE_DIR', os.getenv('JSON_CACHE_DIR', ''))
            if cache_dir_env:
                cache_dir = Path(os.path.expandvars(cache_dir_env))
            else:
                print("ERROR: No cache directory specified!")
                print("Use --cache_dir argument or set CACHE_DIR environment variable")
                return
        
        output_file = Path(args.output)
        
        print("=" * 80)
        print("NPI System URI Analysis")
        print("=" * 80)
        print(f"Cache directory: {cache_dir}")
        print(f"Output file: {output_file}")
        print()
        
        # Analyze
        system_data = NPISystemAnalyzer.analyze_npi_systems(cache_dir=cache_dir)
        
        if not system_data:
            print("\nERROR: No data to analyze!")
            return
        
        # Write results
        NPISystemAnalyzer.write_analysis_csv(
            system_data=system_data,
            output_file=output_file
        )
        
        print("\nAnalysis complete!")


if __name__ == "__main__":
    NPISystemAnalyzer.run()

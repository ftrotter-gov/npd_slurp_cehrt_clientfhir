#!/usr/bin/env python3

"""
Cache Directory Validation Script
==================================
Analyzes cache directories to identify those that don't follow the modern layout
of having exactly two subdirectories: 'endpoint/' and 'organization/'

This helps identify outdated cache data that may need to be cleaned up.
"""

import os
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple
from dataclasses import dataclass
import argparse


@dataclass
class DirectoryIssue:
    """Represents an issue found in a cache directory."""
    directory_name: str
    issues: List[str]
    contents: List[str]


class CacheDirectoryAnalyzer:
    """Analyzes cache directories for compliance with modern layout."""
    
    EXPECTED_SUBDIRS = {'endpoint', 'organization'}
    
    @staticmethod
    def analyze_cache_directory(*, cache_path: str) -> Dict[str, any]:
        """
        Analyze all subdirectories in the cache path.
        
        Args:
            cache_path: Path to the cache directory to analyze
            
        Returns:
            Dictionary containing analysis results
        """
        cache_dir = Path(cache_path)
        
        if not cache_dir.exists():
            raise FileNotFoundError(f"AnalyzeCacheDirectories.py Error: Cache directory not found: {cache_path}")
        
        if not cache_dir.is_dir():
            raise NotADirectoryError(f"AnalyzeCacheDirectories.py Error: Path is not a directory: {cache_path}")
        
        # Get all subdirectories (not files)
        all_items = list(cache_dir.iterdir())
        subdirectories = [item for item in all_items if item.is_dir()]
        
        print(f"Scanning {len(subdirectories)} subdirectories in: {cache_path}")
        print(f"(Note: {len(all_items) - len(subdirectories)} files ignored)\n")
        
        valid_dirs = []
        invalid_dirs = []
        
        for subdir in subdirectories:
            issues = CacheDirectoryAnalyzer._check_directory_structure(directory_path=subdir)
            
            if issues:
                invalid_dirs.append(DirectoryIssue(
                    directory_name=subdir.name,
                    issues=issues,
                    contents=CacheDirectoryAnalyzer._get_directory_contents(directory_path=subdir)
                ))
            else:
                valid_dirs.append(subdir.name)
        
        return {
            'cache_path': cache_path,
            'total_subdirectories': len(subdirectories),
            'valid_directories': valid_dirs,
            'invalid_directories': invalid_dirs,
            'issue_summary': CacheDirectoryAnalyzer._summarize_issues(invalid_directories=invalid_dirs)
        }
    
    @staticmethod
    def _check_directory_structure(*, directory_path: Path) -> List[str]:
        """
        Check if a directory follows the modern layout.
        
        Args:
            directory_path: Path to the directory to check
            
        Returns:
            List of issue descriptions (empty if valid)
        """
        issues = []
        
        try:
            contents = list(directory_path.iterdir())
        except PermissionError:
            return [f"PermissionError: Cannot read directory contents"]
        except Exception as error:
            return [f"UnknownReadError: {str(error)}"]
        
        # Check if empty
        if not contents:
            issues.append("EMPTY: Directory contains no files or subdirectories")
            return issues
        
        # Get subdirectories and files separately
        subdirs = {item.name for item in contents if item.is_dir()}
        files = [item.name for item in contents if item.is_file()]
        
        # Check for unexpected files
        if files:
            issues.append(f"CONTAINS_FILES: Found {len(files)} file(s) in directory")
        
        # Check for missing required subdirectories
        missing_subdirs = CacheDirectoryAnalyzer.EXPECTED_SUBDIRS - subdirs
        if missing_subdirs:
            missing_list = ', '.join(sorted(missing_subdirs))
            issues.append(f"MISSING_SUBDIRS: Missing required subdirectories: {missing_list}")
        
        # Check for extra subdirectories
        extra_subdirs = subdirs - CacheDirectoryAnalyzer.EXPECTED_SUBDIRS
        if extra_subdirs:
            extra_list = ', '.join(sorted(extra_subdirs))
            issues.append(f"EXTRA_SUBDIRS: Found unexpected subdirectories: {extra_list}")
        
        # Special case: has the right subdirs but also has files
        if not missing_subdirs and not extra_subdirs and files:
            # Already noted in CONTAINS_FILES above
            pass
        
        return issues
    
    @staticmethod
    def _get_directory_contents(*, directory_path: Path) -> List[str]:
        """
        Get a list of all items in a directory.
        
        Args:
            directory_path: Path to the directory
            
        Returns:
            List of item names
        """
        try:
            contents = list(directory_path.iterdir())
            return [f"{item.name}{'/' if item.is_dir() else ''}" for item in contents]
        except Exception:
            return ["<unable to read contents>"]
    
    @staticmethod
    def _summarize_issues(*, invalid_directories: List[DirectoryIssue]) -> Dict[str, int]:
        """
        Create a summary of issue types and their counts.
        
        Args:
            invalid_directories: List of DirectoryIssue objects
            
        Returns:
            Dictionary mapping issue types to counts
        """
        summary = {
            'empty_directories': 0,
            'missing_subdirectories': 0,
            'extra_subdirectories': 0,
            'contains_files': 0,
            'permission_errors': 0,
            'other_errors': 0
        }
        
        for dir_issue in invalid_directories:
            for issue in dir_issue.issues:
                if issue.startswith('EMPTY'):
                    summary['empty_directories'] += 1
                elif issue.startswith('MISSING_SUBDIRS'):
                    summary['missing_subdirectories'] += 1
                elif issue.startswith('EXTRA_SUBDIRS'):
                    summary['extra_subdirectories'] += 1
                elif issue.startswith('CONTAINS_FILES'):
                    summary['contains_files'] += 1
                elif 'PermissionError' in issue:
                    summary['permission_errors'] += 1
                else:
                    summary['other_errors'] += 1
        
        return summary
    
    @staticmethod
    def print_report(*, analysis_results: Dict[str, any]) -> None:
        """
        Print a formatted report of the analysis results.
        
        Args:
            analysis_results: Dictionary containing analysis results
        """
        print("=" * 80)
        print("CACHE DIRECTORY ANALYSIS REPORT")
        print("=" * 80)
        print(f"Cache Path: {analysis_results['cache_path']}")
        print()
        
        total = analysis_results['total_subdirectories']
        valid_count = len(analysis_results['valid_directories'])
        invalid_count = len(analysis_results['invalid_directories'])
        
        print(f"Total subdirectories scanned: {total}")
        print(f"Valid (modern layout):         {valid_count} ({valid_count/total*100:.1f}%)")
        print(f"Invalid (issues found):        {invalid_count} ({invalid_count/total*100:.1f}%)")
        print()
        
        if invalid_count > 0:
            print("-" * 80)
            print("DIRECTORIES WITH ISSUES:")
            print("-" * 80)
            
            for idx, dir_issue in enumerate(analysis_results['invalid_directories'], 1):
                print(f"\n{idx}. {dir_issue.directory_name}/")
                for issue in dir_issue.issues:
                    print(f"   ✗ {issue}")
                print(f"   Contents: {', '.join(dir_issue.contents) if dir_issue.contents else '<empty>'}")
            
            print()
            print("-" * 80)
            print("SUMMARY BY ISSUE TYPE:")
            print("-" * 80)
            
            summary = analysis_results['issue_summary']
            for issue_type, count in summary.items():
                if count > 0:
                    issue_label = issue_type.replace('_', ' ').title()
                    print(f"  {issue_label}: {count}")
        else:
            print("\n✓ All directories follow the modern layout!")
        
        print()
        print("=" * 80)
    
    @staticmethod
    def export_to_file(*, analysis_results: Dict[str, any], output_path: str) -> None:
        """
        Export the analysis results to a text file.
        
        Args:
            analysis_results: Dictionary containing analysis results
            output_path: Path where the report file should be saved
        """
        with open(output_path, 'w') as file:
            file.write("=" * 80 + "\n")
            file.write("CACHE DIRECTORY ANALYSIS REPORT\n")
            file.write("=" * 80 + "\n")
            file.write(f"Cache Path: {analysis_results['cache_path']}\n\n")
            
            total = analysis_results['total_subdirectories']
            valid_count = len(analysis_results['valid_directories'])
            invalid_count = len(analysis_results['invalid_directories'])
            
            file.write(f"Total subdirectories scanned: {total}\n")
            file.write(f"Valid (modern layout):         {valid_count} ({valid_count/total*100:.1f}%)\n")
            file.write(f"Invalid (issues found):        {invalid_count} ({invalid_count/total*100:.1f}%)\n\n")
            
            if invalid_count > 0:
                file.write("-" * 80 + "\n")
                file.write("DIRECTORIES WITH ISSUES:\n")
                file.write("-" * 80 + "\n")
                
                for idx, dir_issue in enumerate(analysis_results['invalid_directories'], 1):
                    file.write(f"\n{idx}. {dir_issue.directory_name}/\n")
                    for issue in dir_issue.issues:
                        file.write(f"   - {issue}\n")
                    file.write(f"   Contents: {', '.join(dir_issue.contents) if dir_issue.contents else '<empty>'}\n")
                
                file.write("\n" + "-" * 80 + "\n")
                file.write("SUMMARY BY ISSUE TYPE:\n")
                file.write("-" * 80 + "\n")
                
                summary = analysis_results['issue_summary']
                for issue_type, count in summary.items():
                    if count > 0:
                        issue_label = issue_type.replace('_', ' ').title()
                        file.write(f"  {issue_label}: {count}\n")
            else:
                file.write("\nAll directories follow the modern layout!\n")
            
            file.write("\n" + "=" * 80 + "\n")
        
        print(f"\nReport exported to: {output_path}")


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        description='Analyze cache directories for compliance with modern layout',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Analyze default cache directory
  python AnalyzeCacheDirectories.py
  
  # Analyze specific cache directory
  python AnalyzeCacheDirectories.py --cache-path /path/to/cache
  
  # Export report to file
  python AnalyzeCacheDirectories.py --output cache_report.txt
        """
    )
    
    parser.add_argument(
        '--cache-path',
        default='../npd_slurp_cehrt_clientfhir_cache/cache/fhir_json_cache',
        help='Path to the cache directory to analyze (default: ../npd_slurp_cehrt_clientfhir_cache/cache/fhir_json_cache)'
    )
    
    parser.add_argument(
        '--output',
        help='Export report to the specified file path'
    )
    
    args = parser.parse_args()
    
    try:
        # Perform analysis
        results = CacheDirectoryAnalyzer.analyze_cache_directory(cache_path=args.cache_path)
        
        # Print report to console
        CacheDirectoryAnalyzer.print_report(analysis_results=results)
        
        # Export to file if requested
        if args.output:
            CacheDirectoryAnalyzer.export_to_file(
                analysis_results=results,
                output_path=args.output
            )
    
    except (FileNotFoundError, NotADirectoryError) as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)
    except Exception as error:
        print(f"AnalyzeCacheDirectories.py UnexpectedError: {error}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()

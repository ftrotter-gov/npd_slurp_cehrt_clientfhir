#!/usr/bin/env python3

"""
Cache Cleanup Script
====================
Removes cache directories that don't follow the modern layout and commits changes to git.

This script identifies and removes:
- Empty directories
- Directories missing required subdirectories (endpoint/ or organization/)
- Directories with unexpected extra subdirectories or files
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path
from typing import List, Set
import argparse


class CacheCleanupManager:
    """Manages cleanup of invalid cache directories."""
    
    EXPECTED_SUBDIRS = {'endpoint', 'organization'}
    
    @staticmethod
    def find_invalid_directories(*, cache_path: str) -> List[Path]:
        """
        Find all directories that don't follow the modern layout.
        
        Args:
            cache_path: Path to the cache directory to analyze
            
        Returns:
            List of Path objects for invalid directories
        """
        cache_dir = Path(cache_path)
        
        if not cache_dir.exists():
            raise FileNotFoundError(f"CleanupInvalidCache.py Error: Cache directory not found: {cache_path}")
        
        if not cache_dir.is_dir():
            raise NotADirectoryError(f"CleanupInvalidCache.py Error: Path is not a directory: {cache_path}")
        
        # Get all subdirectories (not files)
        subdirectories = [item for item in cache_dir.iterdir() if item.is_dir()]
        
        invalid_dirs = []
        
        for subdir in subdirectories:
            if not CacheCleanupManager._is_valid_directory(directory_path=subdir):
                invalid_dirs.append(subdir)
        
        return invalid_dirs
    
    @staticmethod
    def _is_valid_directory(*, directory_path: Path) -> bool:
        """
        Check if a directory follows the modern layout.
        
        Args:
            directory_path: Path to the directory to check
            
        Returns:
            True if valid, False otherwise
        """
        try:
            contents = list(directory_path.iterdir())
        except Exception:
            # If we can't read it, consider it invalid
            return False
        
        # Empty directories are invalid
        if not contents:
            return False
        
        # Get subdirectories and files
        subdirs = {item.name for item in contents if item.is_dir()}
        files = [item for item in contents if item.is_file()]
        
        # Files in the directory are invalid
        if files:
            return False
        
        # Must have exactly the expected subdirectories, no more, no less
        if subdirs != CacheCleanupManager.EXPECTED_SUBDIRS:
            return False
        
        return True
    
    @staticmethod
    def delete_directories(*, directories: List[Path], dry_run: bool = False) -> None:
        """
        Delete the specified directories.
        
        Args:
            directories: List of directory paths to delete
            dry_run: If True, only print what would be deleted without actually deleting
        """
        if not directories:
            print("No directories to delete.")
            return
        
        print(f"\n{'DRY RUN - ' if dry_run else ''}Deleting {len(directories)} invalid directories:")
        print("=" * 80)
        
        for idx, dir_path in enumerate(directories, 1):
            print(f"{idx}. {dir_path.name}")
            if not dry_run:
                try:
                    shutil.rmtree(dir_path)
                    print(f"   ✓ Deleted")
                except Exception as error:
                    print(f"   ✗ Error deleting: {error}")
        
        print("=" * 80)
        if dry_run:
            print("\nDRY RUN: No files were actually deleted.")
        else:
            print(f"\nSuccessfully deleted {len(directories)} directories.")
    
    @staticmethod
    def git_remove_and_commit(*, cache_path: str, directories: List[Path], dry_run: bool = False) -> None:
        """
        Stage deletions in git and commit the changes.
        
        Args:
            cache_path: Path to the cache directory
            directories: List of directory paths that were deleted
            dry_run: If True, only show git commands without executing them
        """
        if not directories:
            print("\nNo git changes to commit.")
            return
        
        print("\n" + "=" * 80)
        print("GIT OPERATIONS")
        print("=" * 80)
        
        cache_dir = Path(cache_path).resolve()
        
        # Get relative paths from the git repository root
        try:
            # Find git root
            result = subprocess.run(
                ['git', 'rev-parse', '--show-toplevel'],
                cwd=cache_dir,
                capture_output=True,
                text=True,
                check=True
            )
            git_root = Path(result.stdout.strip())
            
            # Calculate relative paths
            relative_paths = []
            for dir_path in directories:
                rel_path = dir_path.resolve().relative_to(git_root)
                relative_paths.append(str(rel_path))
            
        except subprocess.CalledProcessError as error:
            print(f"Error finding git repository: {error}")
            return
        except Exception as error:
            print(f"Error calculating relative paths: {error}")
            return
        
        # Stage the deletions
        print(f"\nStaging {len(relative_paths)} deletions...")
        for rel_path in relative_paths:
            git_cmd = ['git', 'rm', '-rf', rel_path]
            print(f"  git rm -rf {rel_path}")
            
            if not dry_run:
                try:
                    subprocess.run(
                        git_cmd,
                        cwd=git_root,
                        capture_output=True,
                        text=True,
                        check=True
                    )
                    print(f"    ✓ Staged")
                except subprocess.CalledProcessError as error:
                    # Directory might not be tracked by git, which is fine
                    if "did not match any files" in error.stderr or "pathspec" in error.stderr:
                        print(f"    ⚠ Not tracked by git (skipped)")
                    else:
                        print(f"    ✗ Error: {error.stderr.strip()}")
        
        # Commit the changes
        commit_message = f"Remove {len(directories)} invalid cache directories\n\nDirectories removed:\n"
        for dir_path in directories:
            commit_message += f"- {dir_path.name}\n"
        
        print(f"\nCommitting changes...")
        commit_cmd = ['git', 'commit', '-m', commit_message]
        
        if dry_run:
            print(f"\nDRY RUN - Would execute:")
            print(f"  git commit -m '{commit_message[:50]}...'")
        else:
            try:
                result = subprocess.run(
                    commit_cmd,
                    cwd=git_root,
                    capture_output=True,
                    text=True,
                    check=True
                )
                print(f"✓ Changes committed successfully")
                print(f"\n{result.stdout}")
            except subprocess.CalledProcessError as error:
                if "nothing to commit" in error.stdout or "nothing to commit" in error.stderr:
                    print("⚠ No changes were tracked by git (nothing to commit)")
                else:
                    print(f"✗ Error committing: {error.stderr.strip()}")
        
        print("=" * 80)


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        description='Clean up invalid cache directories and commit changes to git',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Dry run (see what would be deleted without actually deleting)
  python CleanupInvalidCache.py --dry-run
  
  # Actually delete and commit
  python CleanupInvalidCache.py
  
  # Use custom cache path
  python CleanupInvalidCache.py --cache-path /path/to/cache
        """
    )
    
    parser.add_argument(
        '--cache-path',
        default='../npd_slurp_cehrt_clientfhir_cache/cache/fhir_json_cache',
        help='Path to the cache directory to clean (default: ../npd_slurp_cehrt_clientfhir_cache/cache/fhir_json_cache)'
    )
    
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be deleted without actually deleting anything'
    )
    
    args = parser.parse_args()
    
    try:
        print("=" * 80)
        print("CACHE CLEANUP SCRIPT")
        print("=" * 80)
        print(f"Cache path: {args.cache_path}")
        print(f"Mode: {'DRY RUN (no changes will be made)' if args.dry_run else 'LIVE (will delete and commit)'}")
        print("=" * 80)
        
        # Find invalid directories
        print("\nScanning for invalid directories...")
        invalid_dirs = CacheCleanupManager.find_invalid_directories(cache_path=args.cache_path)
        
        if not invalid_dirs:
            print("\n✓ No invalid directories found. Cache is clean!")
            return
        
        print(f"\nFound {len(invalid_dirs)} invalid directories.")
        
        if not args.dry_run:
            # Confirm before proceeding
            print("\n⚠ WARNING: This will permanently delete these directories!")
            response = input("Do you want to proceed? (yes/no): ")
            if response.lower() not in ['yes', 'y']:
                print("\nAborted by user.")
                return
        
        # Delete the directories
        CacheCleanupManager.delete_directories(
            directories=invalid_dirs,
            dry_run=args.dry_run
        )
        
        # Commit to git
        if not args.dry_run:
            CacheCleanupManager.git_remove_and_commit(
                cache_path=args.cache_path,
                directories=invalid_dirs,
                dry_run=args.dry_run
            )
        
        print("\n✓ Cleanup complete!")
        if args.dry_run:
            print("  Run without --dry-run to actually perform the cleanup.")
        
    except (FileNotFoundError, NotADirectoryError) as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\nAborted by user.")
        sys.exit(1)
    except Exception as error:
        print(f"CleanupInvalidCache.py UnexpectedError: {error}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()

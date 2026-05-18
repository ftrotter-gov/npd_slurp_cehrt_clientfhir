"""
Merge parallel processing outputs into final CSV files
"""
import argparse
import pandas as pd
from pathlib import Path
import sys
from typing import Dict, List, Any
import json
from datetime import datetime


def discover_process_directories(*, output_dir: Path) -> List[Path]:
    """Discover all process_* directories"""
    process_dirs = []
    for item in output_dir.iterdir():
        if item.is_dir() and item.name.startswith('process_'):
            process_dirs.append(item)
    return sorted(process_dirs)


def discover_table_names(*, process_dirs: List[Path]) -> set:
    """Discover all unique table names from CSV files"""
    table_names = set()
    
    for proc_dir in process_dirs:
        for csv_file in proc_dir.glob('*.csv'):
            # Remove process prefix (e.g., p1_, p2_) from filename
            filename = csv_file.stem
            if '_' in filename:
                # Split on first underscore to remove prefix
                parts = filename.split('_', 1)
                if len(parts) == 2:
                    table_name = parts[1]
                    table_names.add(table_name)
    
    return table_names


def merge_table_csvs(*, 
                    table_name: str, 
                    process_dirs: List[Path], 
                    output_dir: Path) -> Dict[str, any]:
    """
    Merge CSV files for a single table from all process directories
    
    Returns statistics about the merge operation
    """
    dfs = []
    source_counts = {}
    
    print(f"Merging table: {table_name}")
    
    # Read CSV files from each process directory
    for proc_dir in process_dirs:
        proc_id = proc_dir.name.replace('process_', '')
        
        # Look for files with different prefixes (p1_, p2_, p3_, p4_)
        csv_pattern = f"{proc_id}_{table_name}.csv"
        csv_path = proc_dir / csv_pattern
        
        if csv_path.exists():
            try:
                df = pd.read_csv(csv_path)
                if not df.empty:
                    dfs.append(df)
                    source_counts[proc_id] = len(df)
                    print(f"  {proc_id}: {len(df)} records")
            except Exception as e:
                print(f"  Warning: Could not read {csv_path}: {e}")
    
    if not dfs:
        print(f"  No data found for {table_name}")
        return {
            'table_name': table_name,
            'total_before_dedup': 0,
            'total_after_dedup': 0,
            'duplicates_removed': 0,
            'source_counts': source_counts
        }
    
    # Concatenate all DataFrames
    merged_df = pd.concat(dfs, ignore_index=True)
    total_before = len(merged_df)
    
    # Deduplicate
    try:
        # Use all columns for deduplication except timestamps
        subset_cols = [col for col in merged_df.columns if 'created_at' not in col.lower()]
        if subset_cols:
            merged_df = merged_df.drop_duplicates(subset=subset_cols, keep='first')
    except TypeError as e:
        print(f"  Warning: Cannot deduplicate {table_name} due to unhashable types: {e}")
        print(f"  Keeping all records without deduplication")
    
    total_after = len(merged_df)
    duplicates = total_before - total_after
    
    # Export merged CSV
    output_path = output_dir / f"{table_name}.csv"
    merged_df.to_csv(
        output_path,
        index=False,
        na_rep='',
        quoting=1,  # QUOTE_MINIMAL
        date_format='%Y-%m-%d %H:%M:%S'
    )
    
    print(f"  Merged: {total_after} records (removed {duplicates} duplicates)")
    print(f"  Output: {output_path}")
    
    return {
        'table_name': table_name,
        'total_before_dedup': total_before,
        'total_after_dedup': total_after,
        'duplicates_removed': duplicates,
        'source_counts': source_counts
    }


def merge_parallel_outputs(*, output_dir: Path) -> Dict[str, any]:
    """
    Merge all parallel processing outputs
    
    Args:
        output_dir: Directory containing process_* subdirectories
        
    Returns:
        Dictionary with merge statistics
    """
    start_time = datetime.now()
    
    print("\n" + "="*70)
    print("MERGING PARALLEL PROCESSING OUTPUTS")
    print("="*70)
    print(f"Output directory: {output_dir}")
    print("="*70 + "\n")
    
    # Discover process directories
    process_dirs = discover_process_directories(output_dir=output_dir)
    
    if not process_dirs:
        print("ERROR: No process_* directories found!")
        print("Expected structure: output_dir/process_p1/, process_p2/, etc.")
        return {
            'status': 'error',
            'error': 'No process directories found'
        }
    
    print(f"Found {len(process_dirs)} process directories:")
    for proc_dir in process_dirs:
        csv_count = len(list(proc_dir.glob('*.csv')))
        print(f"  {proc_dir.name}: {csv_count} CSV files")
    
    # Discover all table names
    table_names = discover_table_names(process_dirs=process_dirs)
    print(f"\nFound {len(table_names)} unique tables to merge\n")
    
    # Merge each table
    merge_stats = []
    for i, table_name in enumerate(sorted(table_names), 1):
        print(f"[{i}/{len(table_names)}] ", end='')
        stats = merge_table_csvs(
            table_name=table_name,
            process_dirs=process_dirs,
            output_dir=output_dir
        )
        merge_stats.append(stats)
        print()
    
    # Calculate summary statistics
    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()
    
    total_records_before = sum(s['total_before_dedup'] for s in merge_stats)
    total_records_after = sum(s['total_after_dedup'] for s in merge_stats)
    total_duplicates = sum(s['duplicates_removed'] for s in merge_stats)
    
    summary = {
        'status': 'success',
        'start_time': start_time.isoformat(),
        'end_time': end_time.isoformat(),
        'duration_seconds': duration,
        'process_directories': len(process_dirs),
        'tables_merged': len(table_names),
        'total_records_before_dedup': total_records_before,
        'total_records_after_dedup': total_records_after,
        'total_duplicates_removed': total_duplicates,
        'table_statistics': merge_stats
    }
    
    # Save merge report
    report_path = output_dir / 'merge_report.json'
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    
    print("="*70)
    print("MERGE SUMMARY")
    print("="*70)
    print(f"Duration: {duration:.1f} seconds")
    print(f"Tables merged: {len(table_names)}")
    print(f"Total records before dedup: {total_records_before:,}")
    print(f"Total records after dedup: {total_records_after:,}")
    print(f"Duplicates removed: {total_duplicates:,}")
    print(f"\nMerge report saved to: {report_path}")
    print("="*70 + "\n")
    
    return summary


def create_argument_parser():
    """Create command-line argument parser"""
    parser = argparse.ArgumentParser(
        description='Merge parallel FHIR processing outputs into final CSV files',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Merge outputs from parallel processing
  python -m cehrt_fhir_parser.merge_parallel_outputs --output-dir ./csv_output
  
This script expects the output directory to contain process_* subdirectories
created by parallel processing (process_p1, process_p2, process_p3, process_p4).
        """
    )
    
    parser.add_argument(
        '--output-dir',
        type=str,
        required=True,
        help='Directory containing process_* subdirectories with CSV files to merge'
    )
    
    return parser


def main():
    """Main entry point"""
    parser = create_argument_parser()
    args = parser.parse_args()
    
    output_dir = Path(args.output_dir)
    
    if not output_dir.exists():
        print(f"ERROR: Output directory does not exist: {output_dir}", file=sys.stderr)
        sys.exit(1)
    
    if not output_dir.is_dir():
        print(f"ERROR: Output path is not a directory: {output_dir}", file=sys.stderr)
        sys.exit(1)
    
    try:
        result = merge_parallel_outputs(output_dir=output_dir)
        
        if result['status'] == 'success':
            print("SUCCESS: Merge completed!")
            print(f"\nFinal CSV files are in: {output_dir}")
            print("Process subdirectories can be safely deleted if merge was successful.")
            sys.exit(0)
        else:
            print(f"ERROR: Merge failed: {result.get('error', 'Unknown error')}")
            sys.exit(1)
            
    except Exception as e:
        print(f"\nERROR: Merge failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()

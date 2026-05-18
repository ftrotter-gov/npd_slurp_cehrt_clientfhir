"""
Parallel processing orchestrator for FHIR cache processing
"""
import multiprocessing as mp
from pathlib import Path
from typing import List, Dict, Any
import sys
from datetime import datetime


def assign_vendors_to_processes(*, vendor_dirs: List[Path]) -> Dict[str, List[Path]]:
    """
    Assign vendor directories to 4 processes:
    - Process 1: athenahealth only
    - Process 2: epic only  
    - Process 3: First half of remaining vendors
    - Process 4: Second half of remaining vendors
    """
    athena = [v for v in vendor_dirs if 'athenahealth' in v.name.lower()]
    epic = [v for v in vendor_dirs if 'epic' in v.name.lower()]
    remaining = [v for v in vendor_dirs if v not in athena and v not in epic]
    
    # Sort remaining for consistent splitting
    remaining = sorted(remaining, key=lambda x: x.name)
    
    mid = len(remaining) // 2
    
    process_assignments = {
        'p1': athena,
        'p2': epic,
        'p3': remaining[:mid],
        'p4': remaining[mid:]
    }
    
    return process_assignments


def run_single_process(process_id: str, 
                      vendor_dirs: List[Path], 
                      cache_root: Path,
                      output_dir: Path,
                      test_mode: bool = False) -> Dict[str, Any]:
    """
    Run processing for a single process with assigned vendors
    
    This function runs in a separate process and handles its own imports
    to avoid shared state issues.
    
    Note: This function does not use named-only parameters (no leading *)
    because it's called via multiprocessing.Pool.starmap which passes
    positional arguments.
    """
    from .processor import FHIRCacheProcessor
    import json
    
    print(f"\n{'='*60}")
    print(f"Process {process_id} starting")
    print(f"Assigned vendors: {[v.name for v in vendor_dirs]}")
    print(f"{'='*60}\n")
    
    if not vendor_dirs:
        print(f"Process {process_id}: No vendors assigned, exiting early")
        return {
            'process_id': process_id,
            'status': 'skipped',
            'vendors_processed': 0,
            'error': None
        }
    
    try:
        # Create process-specific output directory
        process_output_dir = output_dir / f"process_{process_id}"
        process_output_dir.mkdir(parents=True, exist_ok=True)
        
        # Initialize processor
        processor = FHIRCacheProcessor(
            cache_root=cache_root,
            output_dir=process_output_dir
        )
        
        # Process only assigned vendors
        print(f"Process {process_id}: Processing {len(vendor_dirs)} vendor(s)...")
        
        all_resources = []
        for i, vendor_dir in enumerate(vendor_dirs, 1):
            print(f"\nProcess {process_id} [{i}/{len(vendor_dirs)}]: Processing vendor: {vendor_dir.name}")
            
            from .processor import VendorProcessor
            
            vendor_processor = VendorProcessor(
                vendor_path=vendor_dir,
                vendor_name=vendor_dir.name,
                run_tracker=processor.run_tracker,
                test_mode=test_mode
            )
            
            # Add vendor to PostgreSQL tables
            processor.postgres_manager.add_vendor(
                vendor_uuid=vendor_processor.vendor_uuid,
                vendor_name=vendor_processor.vendor_name,
                directory_path=str(vendor_dir)
            )
            
            # Process resources
            vendor_resources = vendor_processor.process_all_resources()
            all_resources.extend(vendor_resources)
            
            # Add resources to PostgreSQL tables
            processor._add_resources_to_tables(
                resources=vendor_resources, 
                vendor_uuid=vendor_processor.vendor_uuid
            )
        
        # Post-processing for this process
        print(f"\nProcess {process_id}: Post-processing...")
        processor._populate_lookup_tables(resources=all_resources)
        processor._add_field_coverage_logs()
        processor.postgres_manager.deduplicate_all_tables()
        
        # Export CSV files with process prefix
        print(f"\nProcess {process_id}: Exporting CSV files...")
        csv_files = processor.postgres_manager.export_csv_files_with_prefix(
            output_dir=process_output_dir,
            prefix=f"{process_id}_"
        )
        
        # Generate summary
        summary_report = processor._generate_summary_report(resources=all_resources)
        
        # Save process-specific report
        report_path = process_output_dir / f"processing_report_{process_id}.json"
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(summary_report, f, indent=2, ensure_ascii=False)
        
        print(f"\n{'='*60}")
        print(f"Process {process_id} COMPLETED")
        print(f"Vendors processed: {len(vendor_dirs)}")
        print(f"Resources processed: {len(all_resources)}")
        print(f"CSV files exported: {len(csv_files)}")
        print(f"{'='*60}\n")
        
        return {
            'process_id': process_id,
            'status': 'success',
            'vendors_processed': len(vendor_dirs),
            'resources_processed': len(all_resources),
            'csv_files': len(csv_files),
            'error': None
        }
        
    except Exception as e:
        import traceback
        error_msg = f"{str(e)}\n{traceback.format_exc()}"
        print(f"\nERROR in Process {process_id}: {error_msg}")
        return {
            'process_id': process_id,
            'status': 'failed',
            'vendors_processed': 0,
            'error': error_msg
        }


def run_parallel_processing(*,
                           cache_root: Path,
                           output_dir: Path,
                           test_mode: bool = False,
                           num_workers: int = 4) -> Dict[str, Any]:
    """
    Run parallel processing with multiple workers
    
    Args:
        cache_root: Root directory of FHIR cache
        output_dir: Output directory for all results
        test_mode: Whether to run in test mode
        num_workers: Number of parallel workers (default 4)
        
    Returns:
        Dictionary with overall processing results
    """
    from .processor import FHIRCacheProcessor
    
    start_time = datetime.now()
    
    print("\n" + "="*70)
    print("PARALLEL FHIR CACHE PROCESSOR")
    print("="*70)
    print(f"Workers: {num_workers}")
    print(f"Cache root: {cache_root}")
    print(f"Output directory: {output_dir}")
    if test_mode:
        print("Mode: TEST (limited processing)")
    else:
        print("Mode: FULL processing")
    print("="*70 + "\n")
    
    # Get all vendor directories
    processor = FHIRCacheProcessor(cache_root=cache_root, output_dir=output_dir)
    vendor_dirs = processor._get_vendor_directories()
    
    print(f"Found {len(vendor_dirs)} vendor directories")
    
    if not vendor_dirs:
        print("No vendor directories found!")
        return {'status': 'no_vendors', 'error': 'No vendor directories found'}
    
    # Assign vendors to processes
    assignments = assign_vendors_to_processes(vendor_dirs=vendor_dirs)
    
    print("\nVendor assignments:")
    for proc_id, vendors in assignments.items():
        print(f"  {proc_id}: {len(vendors)} vendor(s) - {[v.name for v in vendors][:3]}{'...' if len(vendors) > 3 else ''}")
    
    # Create process arguments as tuples for starmap
    process_args = []
    for proc_id, vendors in assignments.items():
        if vendors:  # Only create process if it has vendors
            process_args.append((
                proc_id,
                vendors,
                cache_root,
                output_dir,
                test_mode
            ))
    
    print(f"\nSpawning {len(process_args)} worker processes...")
    print("="*70 + "\n")
    
    # Run processes in parallel
    with mp.Pool(processes=len(process_args)) as pool:
        results = pool.starmap(run_single_process, process_args)
    
    # Analyze results
    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()
    
    successful = [r for r in results if r['status'] == 'success']
    failed = [r for r in results if r['status'] == 'failed']
    
    print("\n" + "="*70)
    print("PARALLEL PROCESSING SUMMARY")
    print("="*70)
    print(f"Total duration: {duration:.1f} seconds ({duration/60:.1f} minutes)")
    print(f"Workers completed successfully: {len(successful)}/{len(results)}")
    print(f"Workers failed: {len(failed)}")
    
    if successful:
        total_vendors = sum(r['vendors_processed'] for r in successful)
        total_resources = sum(r.get('resources_processed', 0) for r in successful)
        print(f"Total vendors processed: {total_vendors}")
        print(f"Total resources processed: {total_resources}")
    
    if failed:
        print("\nFailed processes:")
        for r in failed:
            print(f"  {r['process_id']}: {r['error'][:100]}...")
    
    print("\n" + "="*70)
    print("Next step: Run merge_parallel_outputs.py to combine CSV files")
    print("="*70 + "\n")
    
    return {
        'status': 'completed',
        'duration_seconds': duration,
        'workers_successful': len(successful),
        'workers_failed': len(failed),
        'results': results
    }

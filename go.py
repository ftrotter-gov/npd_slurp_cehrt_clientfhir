#!/usr/bin/env python3

"""
EHR FHIR NPI Slurp Pipeline
Complete data processing pipeline for FHIR endpoint analysis

Uses legacy pipeline for data download and new cehrt_fhir_parser for processing.
"""

import sys
import os
import subprocess
import time
import glob
import argparse
from pathlib import Path


def load_env_file(*, env_file_path="data_files.env"):
    """Load environment variables from a .env file with variable expansion support."""
    if not os.path.exists(env_file_path):
        print(f"Warning: Environment file '{env_file_path}' not found. Using defaults.")
        return
    
    with open(env_file_path, 'r') as f:
        for line in f:
            line = line.strip()
            # Skip empty lines and comments
            if not line or line.startswith('#'):
                continue
            
            # Parse KEY=VALUE format
            if '=' in line:
                key, value = line.split('=', 1)
                key = key.strip()
                value = value.strip()
                # Only set if not already in environment and value is not empty
                if key and value and key not in os.environ:
                    # Expand environment variables in the value (e.g., ${NPD_ETL_DIR})
                    expanded_value = os.path.expandvars(value)
                    os.environ[key] = expanded_value


def get_env_var(*, key, default_value):
    """Get environment variable with a default fallback."""
    return os.environ.get(key, default_value)


def check_virtual_env():
    """
    Check if virtual environment is activated and requirements are installed.
    
    This is a critical safety check that prevents the pipeline from running
    without proper Python dependencies. Returns immediately with exit code 1
    if VIRTUAL_ENV is not set or required packages are missing.
    
    Raises:
        SystemExit: Exits with code 1 if virtual environment is not detected or requirements not met
    """
    # Check if virtual environment is activated
    if not os.environ.get('VIRTUAL_ENV'):
        print("=" * 60)
        print("ERROR: Virtual environment is NOT activated!")
        print("=" * 60)
        print("")
        print("The pipeline requires an active virtual environment to run.")
        print("")
        print("To set up and activate the virtual environment:")
        print("")
        print("1. Create virtual environment (if not done):")
        print("   python3 -m venv venv")
        print("")
        print("2. Activate the virtual environment:")
        print("   source venv/bin/activate")
        print("")
        print("3. Install requirements:")
        print("   pip install -r requirements.txt")
        print("")
        print("4. Re-run this command")
        print("=" * 60)
        sys.exit(1)
    
    # Check if required packages are installed
    required_packages = ['pandas', 'phonenumbers', 'requests', 'dotenv']
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print("=" * 60)
        print("ERROR: Required Python packages are NOT installed!")
        print("=" * 60)
        print("")
        print(f"Missing packages: {', '.join(missing_packages)}")
        print("")
        print("To install requirements, run:")
        print("  pip install -r requirements.txt")
        print("")
        print("Then re-run this command.")
        print("=" * 60)
        sys.exit(1)


def check_file_has_data(*, file_path: str, min_lines: int = 2) -> bool:
    """
    Check if a file exists and has data (more than just headers).
    
    Args:
        file_path: Path to the file
        min_lines: Minimum number of lines (default 2: header + at least 1 data row)
    
    Returns:
        True if file exists and has enough lines, False otherwise
    """
    try:
        with open(file_path, 'r') as f:
            line_count = sum(1 for _ in f)
        return line_count >= min_lines
    except FileNotFoundError:
        return False
    except Exception:
        return False


def run_step(*, step_num, description, command_args, success_message=None):
    """
    Run a pipeline step with proper error handling and logging.
    
    Args:
        step_num: Step number for display
        description: Description of what this step does
        command_args: List of command arguments to execute
        success_message: Optional custom success message
    """
    print(f"Step {step_num}: {description}...")
    
    try:
        # Run the command
        result = subprocess.run(command_args, check=True, capture_output=False)
        
        # Success message
        success_msg = success_message or f"✓ Step {step_num} completed"
        print(success_msg)
        print("")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Step {step_num} failed with return code {e.returncode}")
        print(f"Command: {' '.join(command_args)}")
        sys.exit(1)
    except FileNotFoundError as e:
        print(f"❌ Step {step_num} failed: {e}")
        print(f"Command: {' '.join(command_args)}")
        sys.exit(1)


def parse_step_args(*, steps_arg):
    """
    Parse step arguments into a list of step numbers.
    
    Args:
        steps_arg: List of step arguments (e.g., ['10', '20', '30'] or ['10-30', '40'])
        
    Returns:
        Set of step numbers to run
    """
    if not steps_arg:
        return {10, 20, 30, 45, 52, 89, 90}  # Default: modern pipeline only
    
    steps_to_run = set()
    
    for arg in steps_arg:
        if '-' in arg:
            # Handle range (e.g., '10-30')
            start, end = arg.split('-', 1)
            try:
                # For ranges, add all valid step numbers in between
                start_num = int(start)
                end_num = int(end)
                valid_steps = [10, 20, 30, 45, 52, 89, 90]
                for step in valid_steps:
                    if start_num <= step <= end_num:
                        steps_to_run.add(step)
            except ValueError:
                print(f"Warning: Invalid step range '{arg}', skipping")
        else:
            # Handle individual step
            try:
                steps_to_run.add(int(arg))
            except ValueError:
                print(f"Warning: Invalid step number '{arg}', skipping")
    
    return steps_to_run


def run_step_10():
    """Step 10: Extract list sources from Lantern CSV."""
    run_step(
        step_num=10,
        description="Extracting list sources from Lantern CSV",
        command_args=[
            "python", "Step10_extract_list_source_from_lantern_csv.py",
            "--input_file", get_env_var(key="LANTERN_CSV_INPUT", default_value="local_data/lantern_csv/fhir_endpoints.csv"),
            "--output_file", get_env_var(key="LIST_SOURCES_SUMMARY", default_value="../npd_slurp_cehrt_clientfhir_cache/list_sources_summary.csv")
        ]
    )


def run_step_20():
    """Step 20: Download service JSON files."""
    run_step(
        step_num=20,
        description="Downloading CEHRT JSON files",
        command_args=[
            "python", "Step20_download_list_source_json.py",
            "--input_file", get_env_var(key="LIST_SOURCES_SUMMARY", default_value="../npd_slurp_cehrt_clientfhir_cache/list_sources_summary.csv"),
            "--output_dir", get_env_var(key="CEHRT_CACHE_DIR", default_value="../npd_slurp_cehrt_clientfhir_cache/cache/fhir_json_cache/"),
            "--delay", get_env_var(key="DOWNLOAD_DELAY", default_value="1.0")
        ]
    )


def run_step_30():
    """Step 30: Parse FHIR bundles."""
    run_step(
        step_num=30,
        description="Parsing FHIR bundles into individual resource files",
        command_args=[
            "python", "Step30_parse_source_bundle.py",
            "--input_dir", get_env_var(key="SERVICE_JSON_DIR", default_value="../npd_slurp_cehrt_clientfhir_cache/cache/fhir_json_cache/")
        ]
    )


def run_step_45():
    """Step 45: Process FHIR cache with cehrt_fhir_parser (OOP implementation)."""
    cache_dir = get_env_var(key="SERVICE_JSON_DIR", default_value="../npd_slurp_cehrt_clientfhir_cache/cache/fhir_json_cache/")
    output_dir = get_env_var(key="V2_PARSER_CSV_DIR", default_value="../npd_slurp_cehrt_clientfhir_cache/cache/parser_output/")
    
    print("FHIR Cache Parser (OOP Implementation):")
    print("  - Processing FHIR cache with modern OOP parser")
    print("  - Generating both FHIR analysis and NPD-compliant CSV files")
    print("  - Validating NPIs with 9M+ cached entries")
    print("  - Creating complete data lineage and coverage reports")
    print("  - PARALLEL MODE: Using 4 workers (athenahealth, epic, and 2 other splits)")
    
    parser_command = [
        "python", "-m", "cehrt_fhir_parser.cli",
        "--cache-dir", cache_dir,
        "--output-dir", output_dir,
        "--parallel"
    ]
    
    # Add test mode if requested
    if os.environ.get("TEST_MODE", "").lower() in ["true", "1", "yes"]:
        parser_command.append("--test")
        print("  - TEST MODE: Processing limited data for validation")
    
    # Add verbose mode if requested
    if os.environ.get("VERBOSE_MODE", "").lower() in ["true", "1", "yes"]:
        parser_command.append("--verbose")
        print("  - VERBOSE MODE: Detailed processing output")
    
    run_step(
        step_num=45,
        description="",  # Already printed above
        command_args=parser_command,
        success_message="✓ FHIR cache processing completed with cehrt_fhir_parser"
    )
    
    # Merge the parallel processing outputs and clean up
    print("\nStep 45b: Merging parallel processing outputs...")
    
    merge_command = [
        "python", "-m", "cehrt_fhir_parser.merge_parallel_outputs",
        "--output-dir", output_dir
    ]
    
    try:
        subprocess.run(merge_command, check=True, capture_output=False)
        print("✓ Merge completed successfully")
        print("")
        
        # Clean up process subdirectories
        print("Step 45c: Cleaning up process subdirectories...")
        process_dirs = glob.glob(os.path.join(output_dir, "process_*"))
        
        if process_dirs:
            import shutil
            for proc_dir in process_dirs:
                try:
                    shutil.rmtree(proc_dir)
                    print(f"  Removed: {os.path.basename(proc_dir)}")
                except Exception as e:
                    print(f"  Warning: Could not remove {proc_dir}: {e}")
            
            print("✓ Cleanup completed")
            print("")
        else:
            print("  No process subdirectories found to clean up")
            print("")
            
    except subprocess.CalledProcessError as e:
        print(f"❌ Merge failed with return code {e.returncode}")
        print("Process subdirectories have been left in place for debugging")
        sys.exit(1)


def run_step_52():
    """Step 52: Discover endpoints from Step 45 output (MODERN)."""
    input_dir = get_env_var(key="V2_PARSER_CSV_DIR", default_value="../npd_slurp_cehrt_clientfhir_cache/cache/parser_output/")
    output_file = get_env_var(key="ENRICHED_ENDPOINTS", default_value="../npd_slurp_cehrt_clientfhir_cache/cache/summary_data/step52_enriched_endpoints.csv")
    
    # Check prerequisite: Step 45 must have produced endpoint_instance.csv
    endpoint_file = Path(input_dir) / 'endpoint_instance.csv'
    if not endpoint_file.exists() or not check_file_has_data(file_path=str(endpoint_file), min_lines=2):
        print(f"⚠️  Step 52: SKIPPED - Prerequisite data missing")
        print(f"   Required: {endpoint_file} (with data)")
        print(f"   Reason: Step 45 hasn't produced endpoint data")
        print(f"   Note: Run Step 45 first with valid data")
        print("")
        return
    
    run_step(
        step_num=52,
        description="Discovering FHIR endpoints from Step 45 output (metadata, SMART, OpenAPI, Swagger)",
        command_args=[
            "python", "Step52_DiscoverEndpoints.py",
            "--input_dir", input_dir,
            "--output_file", output_file
        ]
    )


def run_step_89():
    """Step 89: Generate CEHRT Dashboard CSV."""
    enriched_endpoints_path = get_env_var(key="ENRICHED_ENDPOINTS", default_value="../npd_slurp_cehrt_clientfhir_cache/cache/summary_data/step52_enriched_endpoints.csv")
    output_csv_path = get_env_var(key="CEHRT_FHIR_REPORT_CSV", default_value="CEHRT_FHIR_Report.csv")
    
    # Check prerequisite: Step 52 must have produced data
    if not check_file_has_data(file_path=enriched_endpoints_path, min_lines=2):
        print(f"⚠️  Step 89: SKIPPED - Prerequisite data missing")
        print(f"   Required: {enriched_endpoints_path} (with data)")
        print(f"   Reason: Step 52 hasn't produced enriched endpoints")
        print(f"   Note: Run Step 52 first with valid data")
        print("")
        return
    
    run_step(
        step_num=89,
        description="Generating CEHRT Dashboard CSV with compliance data (aggregated by EHR vendor)",
        command_args=[
            "python", "Step89_GenerateCEHRTDashboardCSV.py",
            "--enriched_endpoints_path", enriched_endpoints_path,
            "--output_csv_path", output_csv_path
        ]
    )


def run_step_90():
    """Step 90: Make CEHRT Dashboard Markdown."""
    input_csv_path = get_env_var(key="CEHRT_FHIR_REPORT_CSV", default_value="CEHRT_FHIR_Report.csv")
    output_md_path = get_env_var(key="CEHRT_FHIR_REPORT_MD", default_value="CEHRT_FHIR_Report.md")
    
    # Check prerequisite: Step 89 must have produced data
    if not check_file_has_data(file_path=input_csv_path, min_lines=2):
        print(f"⚠️  Step 90: SKIPPED - Prerequisite data missing")
        print(f"   Required: {input_csv_path} (with data)")
        print(f"   Reason: Step 89 hasn't produced the dashboard CSV")
        print(f"   Note: Run Steps 40, 50, 60, and 89 first with valid data")
        print("")
        return
    
    run_step(
        step_num=90,
        description="Generating CEHRT Dashboard Markdown report",
        command_args=[
            "python", "Step90_MakeCEHRTDashboard.py",
            "--input_csv_path", input_csv_path,
            "--output_md_path", output_md_path
        ]
    )


def main():
    """Main pipeline execution."""
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description='EHR FHIR NPI Slurp Pipeline',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python go.py                       # Run all steps (10-90)
  python go.py --steps 10 20         # Run steps 10 and 20
  python go.py --steps 10-52         # Run steps 10 through 52
  python go.py --steps 45            # Run only step 45
  python go.py --steps 89 90         # Run dashboard generation only
  
Steps:
  10 - Extract list sources from Lantern CSV
  20 - Download CEHRT JSON files
  30 - Parse FHIR bundles into individual resource files
  45 - Process FHIR cache with modern parser (NPI validation, parallel processing)
  52 - Discover FHIR endpoints (metadata, SMART, OpenAPI, Swagger)
  89 - Generate CEHRT Dashboard CSV
  90 - Make CEHRT Dashboard Markdown report
  
Pipeline: 10 → 20 → 30 → 45 → 52 → 89 → 90
        """
    )
    
    parser.add_argument(
        '--steps',
        nargs='*',
        metavar='STEP',
        help='Specify which steps to run (10, 20, 30, 45, 52, 89, 90). Can specify individual steps (10 20 30) or ranges (10-52). Default: all steps'
    )
    
    args = parser.parse_args()
    
    # Parse which steps to run
    steps_to_run = parse_step_args(steps_arg=args.steps)
    
    print("Starting EHR FHIR NPI Slurp Pipeline...")
    print("========================================")
    print(f"Running steps: {sorted(steps_to_run)}")
    print("")
    
    # Load environment variables from data_files.env
    load_env_file()
    
    # Check virtual environment
    check_virtual_env()

    # Define step functions
    step_functions = {
        10: run_step_10,
        20: run_step_20,
        30: run_step_30,
        45: run_step_45,
        52: run_step_52,
        89: run_step_89,
        90: run_step_90
    }
    
    # Phase headers
    if any(step in steps_to_run for step in [10, 20, 30]):
        print("PHASE 1: DATA DOWNLOAD & PREPARATION")
        print("Downloading and parsing FHIR data from CEHRT vendors")
        print("")
    
    # Run steps in order
    for step_num in sorted(steps_to_run):
        if step_num in step_functions:
            if step_num == 45:
                print("\nPHASE 2: DATA PROCESSING")
                print("Processing FHIR data with modern parser")
                print("")
            elif step_num == 89:
                print("\nPHASE 3: DASHBOARD GENERATION")
                print("Creating CEHRT vendor compliance dashboard")
                print("")
            
            step_functions[step_num]()
        else:
            print(f"Warning: Step {step_num} not found, skipping")

    # Success summary
    print("========================================")
    print("Pipeline completed successfully!")
    print("")
    
    # Show summary based on what was run
    if 90 in steps_to_run:
        output_md = get_env_var(key="CEHRT_FHIR_REPORT_MD", default_value="CEHRT_FHIR_Report.md")
        print("Dashboard Generation Complete:")
        print(f"  - View dashboard: {output_md}")
        print("")
    


if __name__ == "__main__":
    main()

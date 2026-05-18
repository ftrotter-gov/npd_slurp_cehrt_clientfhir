#!/usr/bin/env python3
"""
This file accepts a fhir_endpoints.csv file, and outputs a new file which is the distinct "list_source" URLS in the data. 
The structure of that file is: 

list_source,api_developer_name,distinct_url_count

as matching the source fhir_endpoints.csv file header which has the file headers: 
"url","api_information_source_name","created_at","updated","list_source","api_developer_name","capability_fhir_version","format","http_response","http_response_time_second","smart_http_response","errors","kind","requested_fhir_version","source","cap_stat_exists"

The first thing to do is verify that the --input_file parameter has a first line of column headers that matches the above.. and error out if does not. 

Then this script uses pandas to query the table (in sql style) with 

SELECT
    list_source,
    api_developer_name,
    COUNT(DISTINCT(url)) AS distinct_url_count
FROM input_csv_file

and writes the results out to the --output_file file as a CSV file. 

If the --input_file is not provided, the script will attempt to download the latest CSV from 
https://lantern.healthit.gov/api/daily/download and save it to the local_data/lantern_csv/ directory
with a timestamp. If the download fails, it will use the most recent previously downloaded file.
"""

import argparse
import pandas as pd
import sys
import os
import requests
import glob
from datetime import datetime
from urllib.parse import urlparse

def download_lantern_csv(*, download_dir):
    """
    Downloads the latest CSV from Lantern API and saves it with a timestamp.
    
    Args:
        download_dir: Directory to save the downloaded file
    
    Returns:
        Path to the downloaded file if successful, None otherwise
    """
    lantern_api_url = "https://lantern.healthit.gov/api/daily/download"
    
    # Ensure directory exists
    os.makedirs(download_dir, exist_ok=True)
    
    # Generate timestamped filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = f"fhir_endpoints_{timestamp}.csv"
    output_path = os.path.join(download_dir, output_filename)
    
    try:
        print(f"Attempting to download from {lantern_api_url}...")
        response = requests.get(lantern_api_url, timeout=60)
        response.raise_for_status()  # Raise exception for bad status codes
        
        # Save the downloaded content
        with open(output_path, 'wb') as f:
            f.write(response.content)
        
        print(f"Successfully downloaded to: {output_path}")
        return output_path
        
    except requests.exceptions.RequestException as e:
        print(f"Step10_extract_list_source_from_lantern_csv.py Error downloading from Lantern API: {str(e)}")
        return None
    except Exception as e:
        print(f"Step10_extract_list_source_from_lantern_csv.py Unexpected error during download: {str(e)}")
        return None


def get_most_recent_lantern_csv(*, download_dir):
    """
    Finds the most recent lantern CSV file in the download directory.
    
    Args:
        download_dir: Directory containing downloaded CSV files
    
    Returns:
        Path to the most recent file, or None if no files found
    """
    # Look for timestamped files first
    pattern = os.path.join(download_dir, "fhir_endpoints_*.csv")
    files = glob.glob(pattern)
    
    # Also check for the standard filename
    standard_file = os.path.join(download_dir, "fhir_endpoints.csv")
    if os.path.exists(standard_file):
        files.append(standard_file)
    
    if not files:
        print(f"Step10_extract_list_source_from_lantern_csv.py Error: No lantern CSV files found in {download_dir}")
        return None
    
    # Get the most recent file by modification time
    most_recent = max(files, key=os.path.getmtime)
    print(f"Using most recent lantern CSV file: {most_recent}")
    return most_recent


def is_valid_url(url):
    """
    Validate if a string is a valid URL.
    Returns True if valid, False otherwise.
    """
    if not url or not isinstance(url, str):
        return False
    
    try:
        parsed = urlparse(url.strip())
        # Must have scheme (http/https) and netloc (domain)
        return bool(parsed.scheme and parsed.netloc and parsed.scheme in ['http', 'https'])
    except Exception:
        return False

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Extract distinct list_source URLs from FHIR endpoints CSV')
    parser.add_argument('--input_file', required=False, help='Input CSV file path (optional - will download if not provided)')
    parser.add_argument('--output_file', required=True, help='Output CSV file path')
    parser.add_argument('--download_dir', default='local_data/lantern_csv', 
                        help='Directory for downloading/storing lantern CSV files (default: local_data/lantern_csv)')
    parser.add_argument('--skip_download', action='store_true', 
                        help='Skip download attempt and only use existing files')
    
    args = parser.parse_args()
    
    # Expand environment variables in paths (e.g., ${NPD_ETL_DIR})
    input_file_path = os.path.expandvars(args.input_file) if args.input_file else None
    output_file_path = os.path.expandvars(args.output_file)
    download_dir = os.path.expandvars(args.download_dir)
    
    # Determine if we need to download/use fallback
    need_to_download = False
    
    if not input_file_path:
        # No input file specified - definitely need to download
        print("No input file specified, attempting to download from Lantern API...")
        need_to_download = True
    elif not os.path.exists(input_file_path):
        # Input file specified but doesn't exist - try to download
        print(f"Input file '{input_file_path}' does not exist.")
        print("Attempting to download from Lantern API or use fallback...")
        need_to_download = True
    
    # Handle download/fallback logic if needed
    if need_to_download:
        if not args.skip_download:
            # Try to download the latest file
            downloaded_file = download_lantern_csv(download_dir=download_dir)
            if downloaded_file:
                input_file_path = downloaded_file
            else:
                print("Download failed, attempting to use most recent existing file...")
                input_file_path = get_most_recent_lantern_csv(download_dir=download_dir)
        else:
            print("Download skipped, using most recent existing file...")
            input_file_path = get_most_recent_lantern_csv(download_dir=download_dir)
        
        if not input_file_path:
            print(f"Step10_extract_list_source_from_lantern_csv.py Error: No input file available and download failed")
            sys.exit(1)
    
    # Final check - at this point input_file_path should exist
    if not os.path.exists(input_file_path):
        print(f"Step10_extract_list_source_from_lantern_csv.py Error: Input file '{input_file_path}' does not exist")
        sys.exit(1)


    # Expected column headers (updated to match current Lantern API format)
    expected_headers = [
        "url", "api_information_source_name", "created_at", "updated", 
        "list_source", "api_developer_name", "capability_fhir_version", 
        "format", "http_response", "http_response_time_second", "smart_http_response", 
        "errors", "kind", "requested_fhir_version", "source","cap_stat_exists"
    ]
    
    try:
        # Read the CSV file
        df = pd.read_csv(input_file_path)
        
        # Verify headers match expected format
        actual_headers = list(df.columns)
        if actual_headers != expected_headers:
            print("Error: CSV headers do not match expected format.")
            print(f"Expected: {expected_headers}")
            print(f"Actual: {actual_headers}")
            sys.exit(1)
        
        # Filter out rows with invalid list_source URLs
        initial_row_count = len(df)
        df['is_valid_list_source'] = df['list_source'].apply(is_valid_url)
        df_valid = df[df['is_valid_list_source']].copy()
        df_valid = df_valid.drop('is_valid_list_source', axis=1)
        
        invalid_count = initial_row_count - len(df_valid)
        if invalid_count > 0:
            print(f"Warning: Filtered out {invalid_count} rows with invalid list_source URLs")
        
        # Group by list_source and api_developer_name, count distinct URLs
        result = df_valid.groupby(['list_source', 'api_developer_name'])['url'].nunique().reset_index()
        result.rename(columns={'url': 'distinct_url_count'}, inplace=True)
        
        # Sort by list_source for consistent output
        result = result.sort_values('list_source')
        
        # Write results to output file
        result.to_csv(output_file_path, index=False)
        
        print(f"Successfully processed {len(df_valid)} valid rows (out of {initial_row_count} total) from '{input_file_path}'")
        print(f"Generated {len(result)} distinct list_source entries in '{output_file_path}'")
        
    except Exception as e:
        print(f"Error processing file: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()

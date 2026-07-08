#!/usr/bin/env python3
"""
Step89_GenerateCEHRTDashboardCSV_v2.py

SIMPLIFIED VERSION - Uses vendor_name directly from enriched_endpoints.csv

Generates a CSV file (CEHRT_FHIR_Report.csv) with compliance results aggregated by EHR vendor.
This file is used as input for the dashboard markdown generator.

- Reads data/output_data/enriched_endpoints.csv for endpoint compliance
- Aggregates compliance per vendor using the vendor_name column directly
- No HTTP requests, no domain mapping - just pure aggregation

Columns: Vendor, Reachable, Has ONPI, HTTPS ORG URL, Findable Metadata, Findable SMART, 
         Findable OpenAPI Docs, Findable OpenAPI JSON, Findable Swagger, Findable Swagger JSON
"""

import csv
import argparse
import re
from collections import Counter

CHECKS = [
    ("Reachable", "reachable"),
    ("Has ONPI", "has_onpi"),
    ("HTTPS ORG URL", "https_org_url"),
    ("Findable Metadata", "capability_url"),
    ("Findable SMART", "smart_url"),
    ("Findable OpenAPI Docs", "openapi_docs_url"),
    ("Findable OpenAPI JSON", "openapi_json_url"),
    ("Findable Swagger", "swagger_url"),
    ("Findable Swagger JSON", "swagger_json_url"),
]

def is_valid_npi(npi_value):
    """Check if NPI is a valid 10-digit number"""
    return bool(re.match(r'^\d{10}$', str(npi_value).strip()))

def is_valid_https_url(url):
    """Check if URL starts with https://"""
    return str(url).strip().startswith('https://')

def is_valid_url(url):
    """Check if URL starts with http:// or https://"""
    url_str = str(url).strip()
    return url_str.startswith('http://') or url_str.startswith('https://')

def check_reachable(row):
    """Check if any endpoint URL is reachable (has a valid URL)"""
    for col in ["capability_url", "smart_url", "openapi_docs_url",
                "openapi_json_url", "swagger_url", "swagger_json_url"]:
        if is_valid_url(row.get(col, "")):
            return True
    return False

def check_has_onpi(row):
    """Check if NPI is present and valid"""
    npi = row.get("npi", "").strip()
    return is_valid_npi(npi)

def check_https_org_url(row):
    """Check if org URL is HTTPS"""
    https_org_url = row.get("https_org_url", "").strip()
    if is_valid_https_url(https_org_url):
        return https_org_url
    
    # Fallback to org_fhir_url
    org_fhir_url = row.get("org_fhir_url", "").strip()
    if is_valid_https_url(org_fhir_url):
        return org_fhir_url
    
    return ""

def check_endpoint_found(row, col):
    """Check if endpoint URL is found and valid"""
    return is_valid_url(row.get(col, ""))

def clean_vendor_name(vendor_name_with_hash):
    """
    Remove hash suffix from vendor names.
    Example: athenahealth_inc_53f1f907e6919c0dd81ced0591b93f43 -> athenahealth_inc
    """
    if not vendor_name_with_hash:
        return "Unknown"
    
    # Split by underscore and check if last part is a hash (32 hex chars)
    parts = vendor_name_with_hash.rsplit('_', 1)
    if len(parts) == 2 and len(parts[1]) == 32 and all(c in '0123456789abcdef' for c in parts[1]):
        return parts[0]
    return vendor_name_with_hash

def aggregate_vendor_compliance(enriched_path):
    """
    Aggregate compliance results by vendor using vendor_name column directly.
    Returns a dict: clean_vendor_name -> {check_name: value, ...}
    """
    vendor_results = {}
    vendor_name_mapping = {}  # Track hash -> clean name mapping
    
    print(f"Reading enriched_endpoints from: {enriched_path}")
    
    # First pass: collect all vendor names and count occurrences of clean names
    vendor_hash_to_clean = {}
    clean_name_counts = Counter()
    
    with open(enriched_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            vendor_hash = row.get("vendor_name", "").strip()
            if vendor_hash:
                clean_name = clean_vendor_name(vendor_hash)
                vendor_hash_to_clean[vendor_hash] = clean_name
                clean_name_counts[clean_name] += 1
    
    # Create final vendor names with numeric suffixes for duplicates
    clean_name_usage = Counter()
    final_vendor_names = {}
    
    for vendor_hash, clean_name in vendor_hash_to_clean.items():
        if clean_name_counts[clean_name] > 1:
            # Multiple vendors with same clean name
            clean_name_usage[clean_name] += 1
            if clean_name_usage[clean_name] == 1:
                final_name = clean_name
            else:
                final_name = f"{clean_name}_{clean_name_usage[clean_name]}"
        else:
            final_name = clean_name
        final_vendor_names[vendor_hash] = final_name
    
    # Second pass: aggregate data
    with open(enriched_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        row_count = 0
        
        for row in reader:
            row_count += 1
            
            # Get vendor name and convert to clean name
            vendor_hash = row.get("vendor_name", "").strip()
            if not vendor_hash:
                vendor = "Unknown"
            else:
                vendor = final_vendor_names.get(vendor_hash, clean_vendor_name(vendor_hash))
            
            # Initialize vendor if not seen before
            if vendor not in vendor_results:
                vendor_results[vendor] = {
                    "Reachable": False,
                    "Has ONPI": False,
                    "HTTPS ORG URL": "",
                    "Findable Metadata": "",
                    "Findable SMART": "",
                    "Findable OpenAPI Docs": "",
                    "Findable OpenAPI JSON": "",
                    "Findable Swagger": "",
                    "Findable Swagger JSON": ""
                }
            
            # Update boolean checks (any TRUE makes it TRUE for the vendor)
            if check_reachable(row):
                vendor_results[vendor]["Reachable"] = True
            if check_has_onpi(row):
                vendor_results[vendor]["Has ONPI"] = True
            
            # Update HTTPS ORG URL - store the actual URL if found (first one wins)
            https_org_url = check_https_org_url(row)
            if https_org_url and not vendor_results[vendor]["HTTPS ORG URL"]:
                vendor_results[vendor]["HTTPS ORG URL"] = https_org_url
            
            # Update endpoint URLs - store the actual URL if found (first one wins)
            if check_endpoint_found(row, "capability_url") and not vendor_results[vendor]["Findable Metadata"]:
                vendor_results[vendor]["Findable Metadata"] = row.get("capability_url", "")
            if check_endpoint_found(row, "smart_url") and not vendor_results[vendor]["Findable SMART"]:
                vendor_results[vendor]["Findable SMART"] = row.get("smart_url", "")
            if check_endpoint_found(row, "openapi_docs_url") and not vendor_results[vendor]["Findable OpenAPI Docs"]:
                vendor_results[vendor]["Findable OpenAPI Docs"] = row.get("openapi_docs_url", "")
            if check_endpoint_found(row, "openapi_json_url") and not vendor_results[vendor]["Findable OpenAPI JSON"]:
                vendor_results[vendor]["Findable OpenAPI JSON"] = row.get("openapi_json_url", "")
            if check_endpoint_found(row, "swagger_url") and not vendor_results[vendor]["Findable Swagger"]:
                vendor_results[vendor]["Findable Swagger"] = row.get("swagger_url", "")
            if check_endpoint_found(row, "swagger_json_url") and not vendor_results[vendor]["Findable Swagger JSON"]:
                vendor_results[vendor]["Findable Swagger JSON"] = row.get("swagger_json_url", "")
    
    print(f"Processed {row_count} rows")
    print(f"Found {len(vendor_results)} unique vendors")
    
    return vendor_results

def main():
    parser = argparse.ArgumentParser(description='Generate CEHRT Dashboard CSV (Simplified Version)')
    parser.add_argument('--enriched_endpoints_path', required=True, help='Path to enriched_endpoints.csv file')
    parser.add_argument('--output_csv_path', required=True, help='Path to output CSV file')
    
    args = parser.parse_args()
    
    enriched_path = args.enriched_endpoints_path
    output_csv = args.output_csv_path

    print("Aggregating compliance results per vendor...")
    vendor_results = aggregate_vendor_compliance(enriched_path)
    
    print("Writing dashboard CSV output...")
    with open(output_csv, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        header = ["Vendor"] + [c[0] for c in CHECKS]
        writer.writerow(header)
        
        # Sort: most green (most True columns) at the top, then alphabetically
        def green_count(results):
            count = 0
            for check_name, _ in CHECKS:
                value = results[check_name]
                # Count True for boolean checks, or non-empty URLs for endpoint checks
                if isinstance(value, bool):
                    count += 1 if value else 0
                else:  # URL string
                    count += 1 if value.strip() else 0
            return count
        
        sorted_vendors = sorted(
            vendor_results.items(),
            key=lambda x: (-green_count(x[1]), x[0].lower())
        )
        
        for vendor, results in sorted_vendors:
            row = [vendor]
            for check_name, _ in CHECKS:
                value = results[check_name]
                # For CSV output, convert to True/False string or URL
                if isinstance(value, bool):
                    row.append(str(value))
                else:  # URL string
                    # Store the URL itself in CSV for dashboard to use
                    row.append(value if value.strip() else "False")
            writer.writerow(row)

    print(f"Dashboard CSV written to {output_csv}")
    print(f"Total vendors: {len(vendor_results)}")

if __name__ == "__main__":
    main()

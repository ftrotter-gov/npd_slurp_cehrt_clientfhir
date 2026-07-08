#!/usr/bin/env python3
"""
Quick script to fix vendor_name column in enriched_endpoints.csv
by pulling the correct vendor names from endpoint_instance.csv
"""

import csv
from urllib.parse import urlparse

def main():
    # Load vendor mapping from endpoint_instance.csv
    print("Loading vendor mapping from endpoint_instance.csv...")
    url_to_vendor = {}
    
    with open('../npd_slurp_cehrt_clientfhir_cache/cache/parser_output/endpoint_instance.csv', 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            address = row.get('address', '').strip()
            vendor_name = row.get('vendor_name', '').strip()
            if address and vendor_name:
                url_to_vendor[address] = vendor_name
    
    print(f"Loaded {len(url_to_vendor)} URL to vendor mappings")
    
    # Read and fix enriched_endpoints.csv
    print("Reading enriched_endpoints.csv...")
    fixed_rows = []
    fixed_count = 0
    
    with open('../npd_slurp_cehrt_clientfhir_cache/cache/summary_data/step52_enriched_endpoints.csv', 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            org_fhir_url = row.get('org_fhir_url', '').strip()
            
            # Look up correct vendor name
            if org_fhir_url in url_to_vendor:
                correct_vendor = url_to_vendor[org_fhir_url]
                if row['vendor_name'] != correct_vendor:
                    fixed_count += 1
                row['vendor_name'] = correct_vendor
            
            fixed_rows.append(row)
    
    print(f"Fixed {fixed_count} vendor names out of {len(fixed_rows)} rows")
    
    # Write fixed file
    print("Writing fixed enriched_endpoints.csv...")
    fieldnames = ['org_fhir_url', 'npi', 'vendor_name', 'https_org_url', 'capability_url', 'smart_url',
                  'openapi_docs_url', 'openapi_json_url', 'swagger_url', 'swagger_json_url']
    
    with open('../npd_slurp_cehrt_clientfhir_cache/cache/summary_data/step52_enriched_endpoints.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(fixed_rows)
    
    print("Done! enriched_endpoints.csv has been fixed.")

if __name__ == "__main__":
    main()

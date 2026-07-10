#!/usr/bin/env python3
"""
Quick test to verify Step52 can load NPI data correctly from both
Organizations and Endpoints after the bug fix.
"""

import sys
from pathlib import Path

# Add Step52 to path
sys.path.insert(0, str(Path(__file__).parent))

from Step52_DiscoverEndpoints import EndpointDiscovery

def test_npi_loading():
    """Test that Step52 properly loads NPI data"""
    
    print("=" * 80)
    print("Testing Step52 NPI Loading After Bug Fix")
    print("=" * 80)
    
    # Use the actual parser output directory
    input_dir = "../npd_slurp_cehrt_clientfhir_cache/cache/parser_output/"
    
    print(f"\nLoading data from: {input_dir}")
    
    # Load the data
    endpoint_data = EndpointDiscovery.load_step45_data(input_dir=input_dir)
    
    print(f"\nTotal records loaded: {len(endpoint_data)}")
    
    # Count records with NPIs
    records_with_npi = sum(1 for _, npi, _ in endpoint_data if npi and npi.strip())
    records_without_npi = len(endpoint_data) - records_with_npi
    
    print(f"Records WITH NPI: {records_with_npi}")
    print(f"Records WITHOUT NPI: {records_without_npi}")
    
    if records_with_npi > 0:
        percentage = (records_with_npi / len(endpoint_data)) * 100
        print(f"Percentage with NPI: {percentage:.2f}%")
    
    # Show sample records with NPIs
    print("\n" + "=" * 80)
    print("Sample Records WITH NPIs (first 5):")
    print("=" * 80)
    
    samples_shown = 0
    for org_url, npi, vendor_name in endpoint_data:
        if npi and npi.strip() and samples_shown < 5:
            print(f"\nVendor: {vendor_name}")
            print(f"URL: {org_url[:80]}...")
            print(f"NPI: {npi}")
            samples_shown += 1
    
    # Group by vendor
    vendor_npi_counts = {}
    for _, npi, vendor_name in endpoint_data:
        if vendor_name not in vendor_npi_counts:
            vendor_npi_counts[vendor_name] = {'total': 0, 'with_npi': 0}
        vendor_npi_counts[vendor_name]['total'] += 1
        if npi and npi.strip():
            vendor_npi_counts[vendor_name]['with_npi'] += 1
    
    print("\n" + "=" * 80)
    print("Top 10 Vendors by Number of Organizations with NPIs:")
    print("=" * 80)
    
    sorted_vendors = sorted(
        vendor_npi_counts.items(),
        key=lambda x: x[1]['with_npi'],
        reverse=True
    )
    
    for i, (vendor, counts) in enumerate(sorted_vendors[:10], 1):
        percentage = (counts['with_npi'] / counts['total'] * 100) if counts['total'] > 0 else 0
        print(f"{i}. {vendor}")
        print(f"   Organizations with NPI: {counts['with_npi']}/{counts['total']} ({percentage:.1f}%)")
    
    # Verdict
    print("\n" + "=" * 80)
    print("TEST VERDICT:")
    print("=" * 80)
    
    if records_with_npi == 0:
        print("❌ FAILED: No NPIs were loaded!")
        print("   The bug is still present.")
        return False
    elif records_with_npi < 100000:
        print("⚠️  WARNING: Some NPIs loaded but seems low")
        print(f"   Expected ~670,000 but got {records_with_npi}")
        return False
    else:
        print("✅ SUCCESS: NPIs are being loaded correctly!")
        print(f"   Loaded {records_with_npi} records with NPIs")
        print("   The bug has been fixed!")
        return True

if __name__ == "__main__":
    success = test_npi_loading()
    sys.exit(0 if success else 1)

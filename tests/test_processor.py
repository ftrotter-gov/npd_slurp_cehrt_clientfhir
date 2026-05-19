import json

import pandas as pd

from cehrt_fhir_parser import FHIRCacheProcessor


def test_processor_exports_expected_csvs(fhir_cache_dir, tmp_path):
    output_dir = tmp_path / "output"
    processor = FHIRCacheProcessor(cache_root=fhir_cache_dir, output_dir=output_dir)

    report = processor.process_entire_cache(test_mode=False)

    assert report["processing_summary"]["files_processed"] == 2
    assert report["resource_counts"] == {"Organization": 1, "Endpoint": 1}
    assert (output_dir / "organization.csv").exists()
    assert (output_dir / "endpoint_instance.csv").exists()
    assert (output_dir / "npd_endpoint_instance.csv").exists()
    assert (output_dir / "field_coverage_log.csv").exists()

    endpoint_df = pd.read_csv(output_dir / "endpoint_instance.csv")
    assert endpoint_df.loc[0, "address"] == "https://example.org/fhir/R4"
    assert endpoint_df.loc[0, "vendor_name"] == "example_vendor"


def test_processor_returns_empty_report_for_empty_cache(tmp_path):
    cache_dir = tmp_path / "empty_cache"
    cache_dir.mkdir()
    output_dir = tmp_path / "output"

    processor = FHIRCacheProcessor(cache_root=cache_dir, output_dir=output_dir)
    report = processor.process_entire_cache(test_mode=False)

    assert report["files_processed"] == 0
    assert report["files_failed"] == 0
    assert report["vendors_processed"] == 0


from pathlib import Path

import pandas as pd

from cehrt_fhir_parser.merge_parallel_outputs import merge_parallel_outputs
from cehrt_fhir_parser.parallel_runner import assign_vendors_to_processes


def test_assign_vendors_to_processes_splits_special_vendors():
    vendor_dirs = [
        Path("athenahealth_inc"),
        Path("epic_systems"),
        Path("alpha_vendor"),
        Path("beta_vendor"),
    ]

    assignments = assign_vendors_to_processes(vendor_dirs=vendor_dirs)

    assert assignments["p1"] == [Path("athenahealth_inc")]
    assert assignments["p2"] == [Path("epic_systems")]
    assert assignments["p3"] == [Path("alpha_vendor")]
    assert assignments["p4"] == [Path("beta_vendor")]


def test_merge_parallel_outputs_merges_prefixed_csvs(tmp_path):
    p1 = tmp_path / "process_p1"
    p2 = tmp_path / "process_p2"
    p1.mkdir()
    p2.mkdir()

    pd.DataFrame([{"id": "1", "name": "one"}]).to_csv(p1 / "p1_ehr_vendor.csv", index=False)
    pd.DataFrame([{"id": "2", "name": "two"}]).to_csv(p2 / "p2_ehr_vendor.csv", index=False)

    result = merge_parallel_outputs(output_dir=tmp_path)

    assert result["status"] == "success"
    assert result["tables_merged"] == 1
    merged = pd.read_csv(tmp_path / "ehr_vendor.csv")
    assert list(merged["id"].astype(str)) == ["1", "2"]
    assert (tmp_path / "merge_report.json").exists()


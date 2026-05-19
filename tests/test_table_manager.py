from cehrt_fhir_parser.output import PostgreSQLTableManager


def test_table_manager_adds_and_deduplicates_records(tmp_path):
    manager = PostgreSQLTableManager()
    records = [
        {"id": "vendor-1", "name": "Vendor", "is_cms_aligned_network": False},
        {"id": "vendor-1", "name": "Vendor", "is_cms_aligned_network": False},
    ]

    manager.add_records(table_name="ehr_vendor", records=records)
    assert manager.get_summary_stats()["ehr_vendor"] == 2

    manager.deduplicate_all_tables()
    assert manager.get_summary_stats()["ehr_vendor"] == 1

    exported = manager.export_csv_files(output_dir=tmp_path)
    assert tmp_path / "ehr_vendor.csv" in exported


def test_unknown_table_is_ignored():
    manager = PostgreSQLTableManager()

    manager.add_records(table_name="does_not_exist", records=[{"id": "1"}])

    assert "does_not_exist" not in manager.tables


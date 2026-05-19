from pathlib import Path

import pytest

from cehrt_fhir_parser.cli import generate_report_filename, validate_arguments


def test_validate_arguments_creates_output_directory(fhir_cache_dir, tmp_path):
    output_dir = tmp_path / "created_output"

    cache_path, output_path = validate_arguments(
        cache_dir=str(fhir_cache_dir),
        output_dir=str(output_dir),
    )

    assert cache_path == fhir_cache_dir
    assert output_path == output_dir
    assert output_dir.exists()


def test_validate_arguments_exits_for_missing_cache(tmp_path):
    with pytest.raises(SystemExit):
        validate_arguments(
            cache_dir=str(tmp_path / "missing"),
            output_dir=str(tmp_path / "output"),
        )


def test_generate_report_filename_uses_output_dir_for_relative_name(tmp_path):
    report_path = generate_report_filename(
        output_dir=tmp_path,
        custom_filename="report.json",
    )

    assert report_path == tmp_path / "report.json"


def test_generate_report_filename_keeps_absolute_name(tmp_path):
    absolute = tmp_path / "absolute_report.json"

    report_path = generate_report_filename(
        output_dir=tmp_path / "unused",
        custom_filename=str(absolute),
    )

    assert report_path == absolute


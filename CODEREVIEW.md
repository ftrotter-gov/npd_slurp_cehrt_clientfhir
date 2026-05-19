# Code Review: Legacy Pipeline Refactor

Review date: 2026-05-18

## Summary

The repository has been reduced to one supported implementation: the `cehrt_fhir_parser` package. The legacy step-based pipeline, standalone resolver scripts, root-level script tests, and stale AI planning docs have been removed.

The supported workflow is now:

```bash
python -m cehrt_fhir_parser.cli \
  --cache-dir ../npd_ehr_scrape_cache/cache/fhir_json_cache \
  --output-dir ./csv_output
```

Tests now live under `tests/` and are written for `pytest`.

## Completed Refactor

### Removed Legacy Code

Deleted the root-level legacy pipeline:

- `go.py`
- `slurp.py`
- `Step10_extract_list_source_from_lantern_csv.py`
- `Step20_download_list_source_json.py`
- `Step30_parse_source_bundle.py`
- `Step40_extract_csv_data.py`
- `Step50_simple_clean_output.py`
- `Step60_CalculateOpenEndpoints.py`
- `Step89_GenerateCEHRTDashboardCSV.py`
- `Step90_MakeCEHRTDashboard.py`
- `FilenameUtils.py`

Deleted standalone resolver code that was not used by the package:

- `FHIRResolver.py`
- `FHIR_URL_Results.py`
- `fhir_test_cli.py`

Deleted stale root-level script tests:

- `test_fhir_resolver.py`
- `test_filename_utils.py`
- `test_fixes.py`
- `test_migration.py`
- `test_npi_1588997233.py`
- `test_npi_validator.py`
- `test_parser.py`
- `test_pipeline.py`

Deleted stale planning/misc code:

- `AI_Instructions/`
- `misc_scripts/`
- `data_files.env`
- `NPIValidator_README.md`

### Package Cleanup

`NPIValidator` moved from the repo root into:

```text
cehrt_fhir_parser/utils/npi_validator.py
```

`cehrt_fhir_parser/utils/validators.py` now imports the validator with a package-relative import. The previous `sys.path.append(...)` import hack has been removed.

### Test Harness

Added `pyproject.toml` with:

- package metadata
- runtime dependencies
- test dependency group
- pytest configuration
- console script entry point

Added pytest tests under `tests/`:

- `tests/test_cli.py`
- `tests/test_parallel_merge.py`
- `tests/test_processor.py`
- `tests/test_resource_factories.py`
- `tests/test_table_manager.py`
- `tests/test_validators.py`
- `tests/conftest.py`

The tests generate fixture data in temporary directories. They do not require network access or `../npd_ehr_scrape_cache`.

### Documentation

`README.md` now documents only the package parser workflow. The legacy pipeline instructions and `StepXX` workflow have been removed.

`.gitignore` now excludes local Python caches, test/build artifacts, and generated parser output.

## Current Supported Surface

Production code:

```text
cehrt_fhir_parser/
  cli.py
  processor.py
  parallel_runner.py
  merge_parallel_outputs.py
  models/
  output/
  utils/
```

Tests:

```text
tests/
```

Reference docs/data that remain:

- `README.md`
- `docs/`
- `data_model/`
- `CODEREVIEW.md`
- `code.json`
- CMS repository policy files

## Verification Commands

Use these after installing dependencies:

```bash
python -m compileall cehrt_fhir_parser tests
python -m pytest -q
rg "Step10|Step20|Step30|Step40|Step50|Step60|Step89|Step90|FilenameUtils|FHIRResolver|go.py|slurp.py" -g '*.py'
```

The `rg` check is scoped to Python files so this review document can still mention deleted legacy names.

## Residual Risks

- The active shell environment did not initially have `pytest`, `pandas`, or `phonenumbers` installed. Use `python -m pip install -e ".[test]"` in a virtual environment before running the suite.
- Some generated data/report directories may still exist locally but are now ignored by `.gitignore`.
- The parser still defaults to `./npi_validation_data/valid_npi.3.csv` for production NPI cache writes. Tests use temporary fixture cache files.


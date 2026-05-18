# Code Review: Legacy Pipeline Removal and Test Migration

Review date: 2026-05-18

## Executive Summary

The repository currently contains two overlapping systems:

1. The rewritten parser in `cehrt_fhir_parser/`.
2. A legacy root-level pipeline made of `go.py`, `slurp.py`, `Step*.py`, and several helper scripts.

The rewritten parser is the right center of gravity. The main blocker to removing the legacy code is that a few root-level modules and tests still keep it alive. Most importantly, `cehrt_fhir_parser.utils.validators` imports the root-level `NPIValidator.py`, so that file is not dead yet.

The cleanup should happen in this order:

1. Establish a runnable test environment.
2. Move the still-live root-level code into the package.
3. Move tests into `tests/` and delete tests that only preserve legacy behavior.
4. Remove the legacy scripts.
5. Update README and other docs so they no longer describe removed workflows.

## Current Architecture

### Rewritten Parser

The rewritten implementation is under `cehrt_fhir_parser/`.

Important files:

- `cehrt_fhir_parser/cli.py`: primary CLI entry point.
- `cehrt_fhir_parser/processor.py`: cache traversal and orchestration.
- `cehrt_fhir_parser/models/`: `Organization` and `Endpoint` resource models.
- `cehrt_fhir_parser/output/`: CSV/table export logic.
- `cehrt_fhir_parser/parallel_runner.py`: parallel processing.
- `cehrt_fhir_parser/merge_parallel_outputs.py`: merge phase for parallel output.

The expected input shape is:

```text
cache_root/
  vendor_name/
    organization/
      *.json
    endpoint/
      *.json
```

This package does not import the `Step*.py` files. It does still import `NPIValidator.py` from the repo root.

### Legacy Pipeline

The legacy pipeline is spread across:

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

`go.py` is mixed: it invokes old steps and also invokes the rewritten parser as step 45. Its default step set still includes the legacy pipeline, so it should not remain as the primary interface if the goal is a clean rewrite.

### Standalone Resolver Code

These files appear separate from the rewritten parser:

- `FHIRResolver.py`
- `FHIR_URL_Results.py`
- `fhir_test_cli.py`
- `test_fhir_resolver.py`

They are not used by `cehrt_fhir_parser/`. If the resolver is still useful, move it into a separate package or documented tool. If not, delete it with the rest of the legacy surface.

## What Is Not Dead Yet

### `NPIValidator.py`

`cehrt_fhir_parser/utils/validators.py` currently appends the repo root to `sys.path` and imports `NPIValidator` from there. That means `NPIValidator.py` is production code for the rewritten parser, even though it lives beside legacy scripts.

Recommendation:

- Move `NPIValidator.py` to `cehrt_fhir_parser/utils/npi_validator.py`.
- Replace the `sys.path.append(...)` import hack with a relative package import.
- Update tests to use small fixture cache files instead of real cache data or the public API.

### Cache Creation Steps

`Step10`, `Step20`, and `Step30` create or reshape the FHIR cache. The rewritten parser processes an existing cache, but it does not download Lantern data or split bundles itself.

Decision needed:

- If this repository should only parse an existing cache, delete `Step10`, `Step20`, and `Step30`.
- If this repository must still create the cache, rewrite those responsibilities into a package module or move them to a separate scrape/cache repository.

## Strong Removal Candidates

These can be removed after the tests and docs stop referencing them:

| Files | Reason | Blocker |
| --- | --- | --- |
| `Step40_extract_csv_data.py` | Replaced by `cehrt_fhir_parser` resource models and processor. | Tests still import it. |
| `Step50_simple_clean_output.py` | Legacy post-processing path for Step40 output. | README and `go.py` still document/invoke it. |
| `Step60_CalculateOpenEndpoints.py` | Legacy endpoint discovery path. | Dashboard steps and docs still refer to it. |
| `Step89_GenerateCEHRTDashboardCSV.py` | Legacy dashboard aggregation. | Decide whether dashboard output is still required. |
| `Step90_MakeCEHRTDashboard.py` | Legacy dashboard rendering. | Decide whether dashboard output is still required. |
| `FilenameUtils.py` | Only used by Step20 and legacy tests. | Remove after Step20 is gone. |
| `slurp.py` | Standalone HTI-1 probe, not part of rewritten parser. | Confirm no user workflow depends on it. |
| `go.py` | Mixed old/new orchestrator. | Replace with direct CLI usage or a thin new wrapper. |
| `FHIRResolver.py`, `FHIR_URL_Results.py`, `fhir_test_cli.py` | Separate resolver tool, not used by parser. | Confirm it is not intentionally kept for payer/EHR experiments. |

## Outdated Tests

The tests are currently root-level scripts. Several are not good long-term tests because they preserve the legacy pipeline instead of validating the rewritten parser.

### Delete or Rewrite

- `test_pipeline.py`
  - Imports `Step10`, `Step20`, `Step30`, and `Step40`.
  - Tests legacy-safe filename behavior.
  - Uses root-level `NPIValidator`.

- `test_migration.py`
  - Imports `go.py`.
  - Expects paths that do not match the current `data_files.env`.
  - Checks directories outside the repo, which makes it environment-dependent.

- `test_filename_utils.py`
  - Only validates `FilenameUtils.py`, which should disappear with Step20.

- `test_fhir_resolver.py`
  - Keep only if `FHIRResolver.py` remains as a supported tool.

- `test_npi_1588997233.py`
  - Expects `prod_data/valid_npi_list.csv`, but current `NPIValidator.py` defaults to `npi_validation_data/valid_npi.3.csv`.
  - Should be replaced with fixture-based cache tests.

### Keep and Convert

- `test_parser.py`
  - Convert into pytest tests under `tests/`.
  - Remove print-driven pass/fail logic.
  - Assert exact output records and generated CSVs.

- `test_fixes.py`
  - Convert useful assertions into focused tests for imports, table manager behavior, resource creation, and validator fallback.

- `test_npi_validator.py`
  - Rewrite to use fixture cache files and monkeypatched API calls.

## Proposed Test Layout

Move tests into:

```text
tests/
  conftest.py
  fixtures/
    fhir_cache/
      test_vendor/
        organization/
          entry_Organization_001.json
        endpoint/
          entry_Endpoint_001.json
    npi_cache/
      valid_npi.1.csv
  test_cli.py
  test_processor.py
  test_resource_factories.py
  test_organization_model.py
  test_endpoint_model.py
  test_table_manager.py
  test_validators.py
  test_parallel_merge.py
```

Test principles:

- Tests should not require network access.
- Tests should not require `../npd_ehr_scrape_cache`.
- Tests should use `tmp_path` for generated output.
- Tests should assert records and CSV columns, not just "script imports successfully".
- Tests should not call destructors or depend on interpreter shutdown to write cache files.

## Environment Problems Found

The current checkout does not have a runnable test setup by default:

- `python -m pytest -q` failed because `pytest` is not installed.
- Direct test runs failed because `pandas` and `phonenumbers` are not installed in the active Python environment.
- There is no `pyproject.toml`, `setup.cfg`, or `pytest.ini`.

Recommendation:

- Add a `pyproject.toml`.
- Declare runtime dependencies from `requirements.txt`.
- Add test dependencies such as `pytest`.
- Make `python -m pytest -q` the single test command.

## Documentation That Needs Updating

### `README.md`

The README currently documents both systems. Once legacy code is removed:

- Remove the "Option 2: Legacy Pipeline" section.
- Remove the detailed `Legacy Pipeline Steps` section.
- Remove instructions to inspect or run `go.py`.
- Update the testing section from `pytest` to the exact supported command after adding test config.
- Remove "Adding New Steps" guidance that mentions `StepXX` files and `go.sh`.

### `NPIValidator_README.md`

This file is stale relative to `NPIValidator.py`.

Examples:

- It says the default cache is `./local_data/prod_data/valid_npi_list.csv`.
- The implementation defaults to `./npi_validation_data/valid_npi.3.csv`.
- It documents columns `npi,is_invalid`.
- The implementation reads columns `npi,is_valid`.

Either update it after moving the validator into the package, or delete it and fold the necessary details into package docs.

### `data_files.env`

If `go.py` and legacy steps are removed, most of `data_files.env` becomes legacy configuration. Keep only settings that are still consumed by supported entry points, or remove the file and require explicit CLI arguments.

## Removal Plan

### Phase 1: Stabilize Test Harness

1. Add project test config.
2. Add `tests/` with fixture data.
3. Convert current parser tests to pytest style.
4. Confirm the parser works on a tiny fixture cache.

Required command:

```bash
python -m pytest -q
```

### Phase 2: Move Live Shared Code Into Package

1. Move `NPIValidator.py` into `cehrt_fhir_parser/utils/`.
2. Replace root-level imports with package-relative imports.
3. Add NPI fixture tests for:
   - cache hit
   - cache miss with mocked API
   - missing cache behavior
   - invalid format behavior
4. Remove `sys.path.append(...)` from package code.

### Phase 3: Remove Legacy Entry Points

1. Delete or replace `go.py`.
2. Delete `Step40`, `Step50`, `Step60`, `Step89`, and `Step90`.
3. Delete `FilenameUtils.py` if Step20 is removed.
4. Delete `slurp.py` if it is not a supported tool.
5. Decide whether `Step10`, `Step20`, and `Step30` belong in this repo. If not, delete them.
6. Decide whether `FHIRResolver.py` belongs in this repo. If not, delete it with `FHIR_URL_Results.py`, `fhir_test_cli.py`, and `test_fhir_resolver.py`.

### Phase 4: Clean Docs and Generated Files

1. Update README to describe only the supported parser.
2. Remove stale AI instruction files if they are no longer used as repo documentation.
3. Move generated reports and parser output out of the code repo, or document why they are checked in.
4. Remove `__pycache__/` from the working tree and make sure `.gitignore` covers generated files.

## Dead Code Verification

Use these checks after each removal phase:

```bash
python -m compileall cehrt_fhir_parser tests
python -m pytest -q
rg "Step10|Step20|Step30|Step40|Step50|Step60|Step89|Step90|FilenameUtils|FHIRResolver|go.py|slurp.py"
```

Optional static analysis:

```bash
python -m vulture cehrt_fhir_parser tests --min-confidence 80
```

Treat `vulture` output as a review queue, not an automatic delete list. CLI handlers, factory methods, and package exports can look unused to static analysis.

## Definition of Done

The cleanup is complete when:

- `python -m pytest -q` passes from a clean checkout.
- Tests live under `tests/`.
- No root-level `test_*.py` files remain.
- No package code imports from root-level modules using `sys.path`.
- README describes one supported parser workflow.
- `rg "Step[0-9]+_|FilenameUtils|FHIRResolver|slurp.py|go.py"` returns no production references, unless a specific tool was intentionally kept.
- NPI validation tests use local fixtures and mocked API calls.
- Generated data, reports, and cache outputs are either ignored or intentionally documented.


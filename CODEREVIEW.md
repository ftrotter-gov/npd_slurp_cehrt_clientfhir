# Code Review: Legacy Pipeline Restoration

Review date: 2026-05-19 (Updated: Restored legacy pipeline)

## Summary

**UPDATE 2026-05-19**: Legacy pipeline has been **RESTORED**. The repository now supports BOTH implementations:

1. **New `cehrt_fhir_parser` package** - Parser-only tool for processing pre-cached FHIR data
2. **Legacy step-based pipeline** - Complete end-to-end pipeline including data acquisition, parsing, analysis, and dashboard generation

The supported workflow is now:

```bash
python -m cehrt_fhir_parser.cli \
  --cache-dir ../npd_slurp_cehrt_clientfhir_cache/cache/fhir_json_cache \
  --output-dir ./csv_output
```

Tests now live under `tests/` and are written for `pytest`.

## Legacy Pipeline Restoration (2026-05-19)

### Restored Files

The following legacy pipeline files have been restored from git commit 475f07f:

- ✅ `go.py` - Master orchestrator that runs all pipeline steps
- ✅ `slurp.py` - HTTP-based FHIR endpoint probing and data acquisition
- ✅ `Step10_extract_list_source_from_lantern_csv.py` - Downloads and parses Lantern.healthit.gov data
- ✅ `Step20_download_list_source_json.py` - Downloads FHIR bundles from list sources
- ✅ `Step30_parse_source_bundle.py` - Breaks FHIR bundles into individual entry files
- ✅ `Step40_extract_csv_data.py` - Extracts and normalizes CSV data
- ✅ `Step50_simple_clean_output.py` - Cleans and deduplicates output
- ✅ `Step60_CalculateOpenEndpoints.py` - Probes for metadata, SMART, OpenAPI, and Swagger endpoints
- ✅ `Step89_GenerateCEHRTDashboardCSV.py` - Generates vendor compliance CSV
- ✅ `Step90_MakeCEHRTDashboard.py` - Generates markdown dashboard with icon badges
- ✅ `FilenameUtils.py` - Filename utility functions
- ✅ `NPIValidator.py` - NPI validation with CMS API integration

### Rationale for Restoration

The legacy pipeline provides critical functionality that was not replicated in the `cehrt_fhir_parser` package:

1. **End-to-end data acquisition** from Lantern.healthit.gov
2. **Active endpoint probing** to discover FHIR capabilities
3. **Vendor compliance dashboards** for stakeholder reporting
4. **Bundle decomposition** for raw FHIR data

Both pipelines now coexist to serve different use cases:
- Use **legacy pipeline** for complete data acquisition and analysis
- Use **new package** for fast parsing of pre-existing cached data

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

The tests generate fixture data in temporary directories. They do not require network access or the cache directory.

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

## Missing Functionality Analysis

This section documents functionality present in the legacy pipeline (`go.py`, `slurp.py`, `StepXX` files) that is **NOT** replicated in the current `cehrt_fhir_parser` package.

### Legacy Pipeline Overview

The old pipeline performed these steps:

1. **go.py** - Master orchestrator running all steps sequentially
2. **slurp.py** - HTTP-based FHIR endpoint probing and data acquisition
3. **Step10_extract_list_source_from_lantern_csv.py** - Download and parse Lantern.healthit.gov CSV
4. **Step20_download_list_source_json.py** - Download FHIR bundles from list sources
5. **Step30_parse_source_bundle.py** - Break FHIR bundles into individual entry files
6. **Step40_extract_csv_data.py** - Extract and normalize CSV data from entries
7. **Step50_simple_clean_output.py** - Clean and deduplicate outputs
8. **Step60_CalculateOpenEndpoints.py** - Probe for metadata, SMART, OpenAPI, Swagger URLs
9. **Step89_GenerateCEHRTDashboardCSV.py** - Generate vendor compliance CSV
10. **Step90_MakeCEHRTDashboard.py** - Generate markdown dashboard with icon badges

### Current Package Scope

The `cehrt_fhir_parser` package is a **parser-only** tool that:

- Reads pre-existing cached FHIR JSON files
- Extracts and normalizes data into PostgreSQL-compatible CSVs
- Validates NPIs against CMS registry
- Tracks field coverage per vendor
- Generates processing reports

### Removed Functionality (NOT in new package)

#### 1. Data Acquisition (slurp.py, Step10, Step20)

**What it did:**
- Downloaded latest FHIR endpoints CSV from Lantern.healthit.gov API
- Extracted unique list sources by EHR vendor
- Made HTTP requests to FHIR list source URLs to download Bundle JSON

**Status:** ❌ **NOT IMPLEMENTED** - The new parser assumes data is already cached

**Rationale:** Data acquisition is now handled by separate caching infrastructure

#### 2. Bundle Decomposition (Step30)

**What it did:**
- Parsed FHIR Bundle JSON files
- Extracted individual `entry` elements
- Wrote separate JSON files per resource (Organization, Endpoint)
- Organized by resource type into subdirectories

**Status:** ⚠️ **PARTIALLY ASSUMED** - The parser expects pre-decomposed files in `vendor/organization/` and `vendor/endpoint/` directories

**Impact:** If input cache still contains Bundle files instead of individual entries, the parser will fail

#### 3. Endpoint Discovery & Probing (Step60)

**What it did:**
- For each unique org domain, tested multiple directory levels
- Probed for FHIR metadata endpoint (`/metadata`)
- Probed for SMART configuration (`/.well-known/smart-configuration`)
- Probed for OpenAPI documentation (`/api-docs`, `/openapi.json`)
- Probed for Swagger documentation (`/swagger`, `/swagger.json`)
- Validated response content types and structure
- Generated enriched CSV with discovered endpoint URLs

**Status:** ❌ **NOT IMPLEMENTED** - No HTTP probing or endpoint discovery

**Impact:** 
- Cannot discover capability statements
- Cannot determine SMART-on-FHIR support
- Cannot find API documentation endpoints
- Lose visibility into vendor API maturity

**Output files no longer generated:**
- `step52_enriched_endpoints.csv` (org_fhir_url, npi, capability_url, smart_url, openapi_docs_url, openapi_json_url, swagger_url, swagger_json_url)

#### 4. Vendor Compliance Dashboard (Step89, Step90)

**What it did:**

**Step89_GenerateCEHRTDashboardCSV.py:**
- Loaded vendor mapping from list_sources_summary.csv
- Aggregated compliance checks per vendor:
  - Reachable (any endpoint responds)
  - Has ONPI (valid 10-digit NPI)
  - HTTPS ORG URL (organization uses HTTPS)
  - Findable Metadata (capability statement URL)
  - Findable SMART (SMART config URL)
  - Findable OpenAPI Docs/JSON
  - Findable Swagger/JSON
- Generated `CEHRT_FHIR_Report.csv` for dashboard consumption

**Step90_MakeCEHRTDashboard.py:**
- Read compliance CSV
- Generated markdown table with icon badges
- Used shield.io for status indicators
- Displayed green check/fire icons for passing checks
- Displayed red X for failing checks
- Sorted vendors by compliance score
- Output: `CEHRT_FHIR_Report.md` in project root

**Status:** ❌ **NOT IMPLEMENTED** - No dashboard generation

**Impact:**
- No vendor compliance scoring
- No visual summary of FHIR ecosystem maturity
- Cannot track vendor progress over time
- Lose stakeholder-friendly reporting format

**Output files no longer generated:**
- `CEHRT_FHIR_Report.csv`
- `CEHRT_FHIR_Report.md`

#### 5. Lantern CSV Integration (Step10)

**What it did:**
- Downloaded daily FHIR endpoints CSV from https://lantern.healthit.gov/api/daily/download
- Parsed certified_api_developer_name and list_source columns
- Generated list_sources_summary.csv with vendor metadata
- Fell back to cached copy if download failed

**Status:** ❌ **NOT IMPLEMENTED** - No Lantern integration

**Impact:**
- Cannot automatically discover new vendors
- Cannot track changes in Lantern data over time
- Lose official CEHRT vendor name mappings

#### 6. Old CSV Output Format (Step40)

**What it produced:**
- `step40_distinct_organizations.csv` (org_id, org_name, vendor_name, address_count, endpoint_count, npi_count, etc.)
- `step40_distinct_addresses.csv`
- `step40_distinct_endpoints.csv`
- `step40_distinct_phones.csv`
- `step40_distinct_contact_urls.csv`
- `step40_distinct_contact_emails.csv`
- `step40_org_to_npi.csv`
- `step40_org_to_phone.csv`
- `step40_org_to_address.csv`
- `step40_org_to_endpoint.csv`
- `step40_org_to_contact_url.csv`

**New package produces:**
- `organization.csv`
- `endpoint_instance.csv`
- `fhir_organization_address.csv`
- `fhir_organization_phone.csv`
- `fhir_organization_email.csv`
- Plus NPD-prefixed variants and lookup tables

**Status:** ⚠️ **SCHEMA CHANGED** - Different column names and structure

**Impact:** Downstream tools expecting old CSV format will break

### Functionality Successfully Migrated

✅ **FHIR Resource Parsing** - Organization and Endpoint resource extraction
✅ **NPI Validation** - Format and CMS API validation with caching
✅ **Address Normalization** - US/international/nonstandard address handling
✅ **Phone Normalization** - International phone number parsing and validation
✅ **Contact Data** - Email and URL extraction
✅ **Identifier Handling** - NPI and other identifier types
✅ **Field Tracking** - Coverage analysis per vendor
✅ **PostgreSQL Compatibility** - Schema and CSV export for database import
✅ **Test Mode** - Limited file processing for validation
✅ **Parallel Processing** - Multi-worker processing with merge step

### Recommendations

1. **Document the separation of concerns**: The parser is now focused solely on parsing cached data. Data acquisition and analysis should be handled by separate tools.

2. **Create companion tools** if the removed functionality is still needed:
   - `cehrt_fhir_cache_builder` - For data acquisition (Step10-30)
   - `cehrt_fhir_analyzer` - For endpoint probing (Step60)
   - `cehrt_fhir_reporter` - For dashboard generation (Step89-90)

3. **Maintain backward compatibility** if downstream systems depend on old CSV formats:
   - Add `--legacy-format` flag to export old schema
   - Create mapping/migration scripts

4. **Document input requirements** clearly:
   - Cache must contain individual entry files, not bundles
   - Expected directory structure: `vendor/organization/*.json` and `vendor/endpoint/*.json`
   - Each JSON file must have `fullUrl` and `resource` at top level

## Residual Risks

- The active shell environment did not initially have `pytest`, `pandas`, or `phonenumbers` installed. Use `python -m pip install -e ".[test]"` in a virtual environment before running the suite.
- Some generated data/report directories may still exist locally but are now ignored by `.gitignore`.
- The parser still defaults to `./npi_validation_data/valid_npi.3.csv` for production NPI cache writes. Tests use temporary fixture cache files.
- **Breaking Change**: Downstream tools expecting `step40_*.csv` files or `CEHRT_FHIR_Report.*` files will not find them.
- **Missing Visibility**: No longer tracking vendor FHIR ecosystem maturity (metadata, SMART config, API docs availability).
- **Manual Cache Management**: Users must maintain the FHIR JSON cache separately; no built-in download/update mechanism.


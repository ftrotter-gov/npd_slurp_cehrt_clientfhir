# CEHRT FHIR Cache Parser

This project processes cached CEHRT FHIR JSON resources into normalized CSV files for endpoint analysis and PostgreSQL import.

The parser assumes FHIR JSON data is already available in a cache directory. Cache acquisition and legacy step-based processing have been removed from this codebase.

## Problem Documentation

- [Understanding Endpoints in SaaS vs on-prem EHR instances](./docs/fhir_tenancy_explained.md)

## Input Layout

The parser expects vendor directories with `organization/` and `endpoint/` subdirectories:

```text
cache_root/
  vendor_name/
    organization/
      entry_Organization_001.json
    endpoint/
      entry_Endpoint_001.json
```

Each JSON file should be a FHIR Bundle entry with a top-level `fullUrl` and nested `resource`.

## Quick Start

Create and activate a virtual environment, then install the package with test dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[test]"
```

Process a FHIR cache:

```bash
python -m cehrt_fhir_parser.cli \
  --cache-dir ../npd_slurp_cehrt_clientfhir_cache/cache/fhir_json_cache \
  --output-dir ./csv_output
```

Run a limited development pass:

```bash
python -m cehrt_fhir_parser.cli \
  --cache-dir ../npd_slurp_cehrt_clientfhir_cache/cache/fhir_json_cache \
  --output-dir ./csv_output \
  --test \
  --verbose
```

Run in parallel and merge outputs:

```bash
python -m cehrt_fhir_parser.cli \
  --cache-dir ../npd_slurp_cehrt_clientfhir_cache/cache/fhir_json_cache \
  --output-dir ./csv_output \
  --parallel

python -m cehrt_fhir_parser.merge_parallel_outputs --output-dir ./csv_output
```

## Output Files

The parser emits CSV files only for tables that have data.

### FHIR Analysis Tables

- `ehr_vendor.csv`
- `organization.csv`
- `endpoint_instance.csv`
- `endpoint_instance_to_other_id.csv`
- `endpoint_instance_to_payload.csv`
- `endpoint_connection_type.csv`
- `environment_type.csv`
- `data_lineage.csv`
- `field_coverage_log.csv`
- `fhir_organization_address.csv`
- `fhir_organization_phone.csv`
- `fhir_organization_email.csv`
- `fhir_organization_contact_url.csv`

### NPD-Oriented Tables

- `npd_endpoint_instance.csv`
- `npd_endpoint_instance_to_other_id.csv`
- `npd_endpoint_instance_to_payload.csv`
- `npd_organization_to_address.csv`
- `npd_organization_to_phone.csv`
- `npd_address.csv`
- `npd_address_us.csv`
- `npd_address_international.csv`
- `npd_address_nonstandard.csv`
- `npd_fhir_address_use.csv`
- `npd_fhir_email_use.csv`
- `npd_fhir_phone_use.csv`

Each run also writes a JSON processing report with resource counts, table statistics, field coverage, and error counts.

## Validation

NPI validation is handled by `cehrt_fhir_parser.utils.npi_validator.NPIValidator`.

The validator loads all files matching `valid_npi.*.csv` from `./npi_validation_data/` by default. Cache files must use this format:

```csv
npi,is_valid
1234567890,1
1111111111,0
```

If no cache is available, the parser continues with format-only NPI validation. Tests use fixture cache files and do not call the public NPI API.

Phone numbers are parsed and normalized with `phonenumbers`. URLs and email addresses use local format validation.

## Development

Run tests:

```bash
python -m pytest -q
```

Useful verification after refactors:

```bash
python -m compileall cehrt_fhir_parser tests
python -m pytest -q
rg "Step10|Step20|Step30|Step40|Step50|Step60|Step89|Step90|FilenameUtils|FHIRResolver|go.py|slurp.py"
```

## Project Layout

```text
cehrt_fhir_parser/
  cli.py
  processor.py
  parallel_runner.py
  merge_parallel_outputs.py
  models/
  output/
  utils/
tests/
  fixtures are generated in pytest tmp paths
```

## Policies

### Open Source Policy

We adhere to the [CMS Open Source Policy](https://github.com/CMSGov/cms-open-source-policy). If you have any questions, contact [opensource@cms.hhs.gov](mailto:opensource@cms.hhs.gov).

### Security and Responsible Disclosure Policy

Vulnerability reports can be submitted through [Bugcrowd](https://bugcrowd.com/cms-vdp). Reports may be submitted anonymously. If you share contact information, we will acknowledge receipt within 3 business days.

### Software Bill of Materials

A Software Bill of Materials is a formal record containing the details and supply-chain relationships of components used in building software.

## Public Domain

This project is in the public domain within the United States, and copyright and related rights in the work worldwide are waived through the [CC0 1.0 Universal public domain dedication](https://creativecommons.org/publicdomain/zero/1.0/) as indicated in [LICENSE](LICENSE).

All contributions to this project will be released under the CC0 dedication. By submitting a pull request or issue, you are agreeing to comply with this waiver of copyright interest.

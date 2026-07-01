# EHR FHIR Entity Slurp

A data processing pipeline for extracting and normalizing EHR FHIR endpoint data from healthcare providers. Processes data from the [Lantern Dashboard](https://lantern.healthit.gov/) to generate PostgreSQL-ready datasets for healthcare interoperability analysis.

**Project Home**: [/DSACMS/npd_ehr_fhir_npi_slurp](https://github.com/DSACMS/npd_ehr_fhir_npi_slurp)  
**Cache Repository**: [npd_ehr_scrape_cache](https://github.com/ftrotter-gov/npd_ehr_scrape_cache)

## Quick Start

### Prerequisites

* Python 3.8+
* Virtual environment (recommended)

### Installation

```bash
# Clone the repository
git clone https://github.com/DSACMS/npd_ehr_fhir_npi_slurp
cd npd_ehr_fhir_npi_slurp

# Set up virtual environment
source source_me_to_get_venv.sh

# Install dependencies
pip install -r requirements.txt
```

### Running the Complete Pipeline

Download the FHIR endpoints CSV from the [Lantern Dashboard downloads page](https://lantern.healthit.gov/?tab=downloads_tab) and place it in `local_data/prod_data/fhir_endpoints.csv`, then:

```bash
# Run all steps from beginning to end
python go.py

# Run in test mode (processes limited data)
TEST_MODE=true python go.py

# Run with verbose output
VERBOSE_MODE=true python go.py
```

## Pipeline Stages

The pipeline consists of 4 main stages. You can run the complete pipeline with `go.py` or start at any stage by running individual steps:

### Stage 1: Extract List Sources

Analyzes Lantern CSV data to identify unique EHR vendor endpoints.

```bash
python Step10_extract_list_source_from_lantern_csv.py \
  --input_file local_data/lantern_csv/fhir_endpoints.csv \
  --output_file ../npd_ehr_scrape_cache/list_sources_summary.csv
```

**Output**: `list_sources_summary.csv` with distinct vendor list sources

### Stage 2: Download Service Data

Downloads FHIR Bundle JSON files from EHR vendor endpoints.

```bash
python Step20_download_list_source_json.py \
  --input_file ../npd_ehr_scrape_cache/list_sources_summary.csv \
  --output_dir ../npd_ehr_scrape_cache/cache/fhir_json_cache/ \
  --delay 1.0
```

**Output**: JSON files organized by vendor in cache directory

### Stage 3: Parse FHIR Bundles

Breaks down large FHIR bundles into individual resource files.

```bash
python Step30_parse_source_bundle.py \
  --input_dir ../npd_ehr_scrape_cache/cache/fhir_json_cache/
```

**Output**: Individual JSON files for each FHIR resource (Organization, Endpoint, etc.)

### Stage 4: Process & Normalize (New Parser)

Processes FHIR cache data into PostgreSQL-ready CSV files with NPI validation.

```bash
# Full processing
python -m parser.cli \
  --cache-dir ../npd_ehr_scrape_cache/cache/fhir_json_cache/ \
  --output-dir ./parser_output

# Test mode (first 100 files per vendor)
python -m parser.cli \
  --cache-dir ../npd_ehr_scrape_cache/cache/fhir_json_cache/ \
  --output-dir ./parser_output \
  --test

# Verbose mode
python -m parser.cli \
  --cache-dir ../npd_ehr_scrape_cache/cache/fhir_json_cache/ \
  --output-dir ./parser_output \
  --verbose
```

**Output**: CSV files ready for PostgreSQL import (see [Output Files](#output-files) below)

### Skipping Stages

If you already have data from previous runs, you can start at any stage:

```bash
# Skip stages 1-2 if you already have the cache
# Just run stages 3-4
python Step30_parse_source_bundle.py --input_dir ../npd_ehr_scrape_cache/cache/fhir_json_cache/
python -m parser.cli --cache-dir ../npd_ehr_scrape_cache/cache/fhir_json_cache/ --output-dir ./parser_output

# Skip all download/parsing if cache is already parsed
# Just run stage 4 (processing)
python -m parser.cli --cache-dir ../npd_ehr_scrape_cache/cache/fhir_json_cache/ --output-dir ./parser_output
```

## Output Files

The pipeline generates two sets of CSV files:

### NPD Schema Files (PostgreSQL Ready)

These files match the `full_npd.sql` schema and are ready for database import:

* **`npd_endpoint_instance.csv`** - Clean endpoint data with all fields
* **`npd_endpoint_instance_to_other_id.csv`** - NPI relationships with validation results
* **`npd_endpoint_instance_to_payload.csv`** - Payload type mappings

### FHIR Analysis Files (Debugging & Research)

Additional files for data analysis and debugging:

* **`organization.csv`** - FHIR Organization resources with metadata
* **`endpoint_instance.csv`** - FHIR Endpoint resources with validation
* **`ehr_vendor.csv`** - EHR vendor information
* **`data_lineage.csv`** - Complete traceability records
* **`field_coverage_log.csv`** - Data processing coverage analysis
* **`processing_report_[timestamp].json`** - Detailed processing statistics

### Importing to PostgreSQL

```bash
# Create schema
psql -d your_database -f data_model/full_npd.sql

# Import CSV files
psql -d your_database -c "\COPY npd_endpoint_instance FROM 'parser_output/npd_endpoint_instance.csv' CSV HEADER"
psql -d your_database -c "\COPY npd_endpoint_instance_to_other_id FROM 'parser_output/npd_endpoint_instance_to_other_id.csv' CSV HEADER"
psql -d your_database -c "\COPY npd_endpoint_instance_to_payload FROM 'parser_output/npd_endpoint_instance_to_payload.csv' CSV HEADER"
```

## Key Features

* **NPI Validation**: Real-time validation with 9M+ cached NPIs, falls back to CMS NPI Registry API
* **Data Deduplication**: Hash-based deduplication using UUID5 for consistent IDs
* **Field Coverage Tracking**: Comprehensive analysis of data completeness
* **Error Handling**: Detailed error tracking and reporting
* **Test Mode**: Process limited data for development and validation
* **Progress Tracking**: Visual progress indicators for long-running operations

## Configuration

Create or edit `data_files.env` to customize paths:

```bash
# Input/Output Paths
LANTERN_CSV_INPUT=local_data/lantern_csv/fhir_endpoints.csv
LIST_SOURCES_SUMMARY=../npd_ehr_scrape_cache/list_sources_summary.csv
CEHRT_CACHE_DIR=../npd_ehr_scrape_cache/cache/fhir_json_cache/
SERVICE_JSON_DIR=../npd_ehr_scrape_cache/cache/fhir_json_cache/
PARSER_OUTPUT_DIR=./parser_output

# Performance Tuning
DOWNLOAD_DELAY=1.0  # Seconds between downloads
FHIR_REQUEST_TIMEOUT=30  # API request timeout

# Processing Options
TEST_MODE=false  # Set to true for limited processing
VERBOSE_MODE=false  # Set to true for detailed output
```

## Common Use Cases

### Full Production Run

```bash
python go.py
```

### Development & Testing

```bash
# Process just 100 files per vendor
TEST_MODE=true python go.py

# Or run parser directly in test mode
python -m parser.cli --cache-dir ./test_cache --output-dir ./test_output --test
```

### Reprocess Existing Cache

```bash
# Skip download steps, just reprocess
python -m parser.cli \
  --cache-dir ../npd_ehr_scrape_cache/cache/fhir_json_cache/ \
  --output-dir ./parser_output
```

### Update Only New Data

```bash
# Download new data (stages 1-2)
python Step10_extract_list_source_from_lantern_csv.py --input_file local_data/lantern_csv/fhir_endpoints.csv --output_file ../npd_ehr_scrape_cache/list_sources_summary.csv
python Step20_download_list_source_json.py --input_file ../npd_ehr_scrape_cache/list_sources_summary.csv --output_dir ../npd_ehr_scrape_cache/cache/fhir_json_cache/

# Parse and process (stages 3-4)
python Step30_parse_source_bundle.py --input_dir ../npd_ehr_scrape_cache/cache/fhir_json_cache/
python -m parser.cli --cache-dir ../npd_ehr_scrape_cache/cache/fhir_json_cache/ --output-dir ./parser_output
```

## Data Validation

### NPI Validation
* Format validation (10-digit requirement)
* API validation against CMS NPI Registry
* Cache-based validation using 9M+ pre-validated NPIs (see [NPIValidator_README.md](NPIValidator_README.md))

### Data Quality Requirements
Organizations must have:
* At least one valid NPI identifier
* At least one FHIR endpoint
* Valid organizational name

## Troubleshooting

### Virtual Environment Issues

```bash
source source_me_to_get_venv.sh
```

### Missing Dependencies

```bash
pip install -r requirements.txt
```

### Low Success Rate Warning

If you see "WARNING: Low success rate", check:
* Processing report JSON for detailed error logs
* Network connectivity to FHIR endpoints
* Input data quality in Lantern CSV

### NPI Cache Errors

The NPI validator now uses `atexit` for reliable cache saving. No action needed - cache saves automatically on program exit without errors.

## Documentation

* **[NPIValidator_README.md](NPIValidator_README.md)** - NPI validation system details
* **[docs/fhir_tenancy_explained.md](./docs/fhir_tenancy_explained.md)** - Understanding SAAS vs on-prem EHR endpoints
* **[data_model/full_npd.sql](data_model/full_npd.sql)** - PostgreSQL database schema

## Development

### Running Tests

```bash
pytest                    # Run all tests
pytest --cov=.           # Run with coverage
python test_parser.py    # Test parser specifically
```

### Project Structure

```
├── Step10-Step90_*.py   # Pipeline stage scripts
├── parser/              # New FHIR cache parser (recommended)
│   ├── cli.py          # Command-line interface
│   ├── processor.py    # Main processing logic
│   └── output/         # CSV exporters
├── go.py               # Complete pipeline runner
├── NPIValidator.py     # NPI validation with caching
├── data_model/         # PostgreSQL schema
└── local_data/         # Input data directory
```

## Policies

### Open Source Policy

We adhere to the [CMS Open Source Policy](https://github.com/CMSGov/cms-open-source-policy). Questions? Email [opensource@cms.hhs.gov](mailto:opensource@cms.hhs.gov).

### Security and Responsible Disclosure

Submit vulnerability reports through [Bugcrowd](https://bugcrowd.com/cms-vdp). Reports may be submitted anonymously.

### Software Bill of Materials (SBOM)

SBOM available at: [Network Dependencies](https://github.com/DSACMS/npd_ehr_fhir_npi_slurp/network/dependencies)

For more information about SBOMs: <https://www.cisa.gov/sbom>

## License

This project is in the public domain within the United States, and copyright and related rights in the work worldwide are waived through the [CC0 1.0 Universal public domain dedication](https://creativecommons.org/publicdomain/zero/1.0/) as indicated in [LICENSE](LICENSE).

All contributions to this project will be released under the CC0 dedication. By submitting a pull request or issue, you are agreeing to comply with this waiver of copyright interest.

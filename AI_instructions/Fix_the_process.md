Here is the output from the previous run of go.py: 



```bash

⚠️  Step 50: SKIPPED - Prerequisite data missing
   Required: ../npd_slurp_cehrt_clientfhir_cache/cache/summary_data/step40_org_to_npi.csv (with data)
   Reason: Step 40 produced no valid organizations
   Note: Organizations need both a valid NPI and FHIR endpoint

⚠️  Step 60: SKIPPED - Prerequisite data missing
   Required: ../npd_slurp_cehrt_clientfhir_cache/cache/summary_data/step50_clean_npi_to_org_fhir_url.csv (with data)
   Reason: Step 50 produced no clean NPI mappings
   Note: Run Steps 40 and 50 first with valid data


PHASE 3: DASHBOARD GENERATION
Creating CEHRT vendor compliance dashboard

⚠️  Step 89: SKIPPED - Prerequisite data missing
   Required: ../npd_slurp_cehrt_clientfhir_cache/cache/summary_data/step60_enriched_endpoints.csv (with data)
   Reason: Step 60 hasn't produced enriched endpoints
   Note: Run Steps 40, 50, and 60 first with valid data

⚠️  Step 90: SKIPPED - Prerequisite data missing
   Required: ../npd_slurp_cehrt_clientfhir_cache/cache/summary_data/step89_CEHRT_FHIR_Report.csv (with data)
   Reason: Step 89 hasn't produced the dashboard CSV
   Note: Run Steps 40, 50, 60, and 89 first with valid data

========================================
Pipeline completed successfully!

Dashboard Generation Complete:
  - View dashboard: ../npd_slurp_cehrt_clientfhir_cache/cache/summary_data/step90_CEHRT_FHIR_Report.md

Data Processing Complete:
  - Normalized CSV files: ../npd_slurp_cehrt_clientfhir_cache/cache/summary_data//
  - Clean NPI to Org mapping: ../npd_slurp_cehrt_clientfhir_cache/cache/summary_data/step50_clean_npi_to_org_fhir_url.csv
  - Enriched endpoints: ../npd_slurp_cehrt_clientfhir_cache/cache/summary_data/step60_enriched_endpoints.csv

Available Options:
  - Set TEST_MODE=true             : Process only a small subset of data (for testing pipeline)
  - Set PARTIAL_TEST_VALIDATION=true : Skip some validation checks (for faster processing)
  - Set VERBOSE_MODE=true          : Enable verbose processing output

Note: TEST_MODE and PARTIAL_TEST_VALIDATION are independent options:
  - TEST_MODE limits the amount of data processed (small subset)
  - PARTIAL_TEST_VALIDATION affects validation thoroughness (all data, less validation)
  - Both default to 'false' (full data processing with full validation)

Performance Notes:
  - Step 45 uses parallel processing with 4 workers (~4x faster)
  - Automatically merges outputs and cleans up process subdirectories

Testing:
  - Run tests: python test_parser.py


```

Here is what is problematic. First, the output of ALL the steps should be ../npd_ehr_scrape_cache/
These scripts themselves should be generating the csv files that step 89 and 90 need. 

All of this text is not relevant to figuring out what happened on a run and needs to be removed: 

```
Available Options:
  - Set TEST_MODE=true             : Process only a small subset of data (for testing pipeline)
  - Set PARTIAL_TEST_VALIDATION=true : Skip some validation checks (for faster processing)
  - Set VERBOSE_MODE=true          : Enable verbose processing output

Note: TEST_MODE and PARTIAL_TEST_VALIDATION are independent options:
  - TEST_MODE limits the amount of data processed (small subset)
  - PARTIAL_TEST_VALIDATION affects validation thoroughness (all data, less validation)
  - Both default to 'false' (full data processing with full validation)

Performance Notes:
  - Step 45 uses parallel processing with 4 workers (~4x faster)
  - Automatically merges outputs and cleans up process subdirectories

Testing:
  - Run tests: python test_parser.py

```
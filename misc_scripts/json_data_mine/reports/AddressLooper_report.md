# Address Component Analysis Summary

## What This Analysis Does
This analysis examines address entries in FHIR JSON files and dynamically discovers all 
address subcomponents present in the data. It tracks the presence of address fields and 
calculates percentages for each subcomponent found (such as line, city, state, postalCode, country, etc.).

- **Discovery Method:** Dynamic scanning of all address dictionary keys
- **Components Tracked:** All subfields found in address objects (not just predefined ones)
- **Percentage Calculations:** Based on files that have address fields
- **Examples:** Longest/shortest/random by filename length

## Processing Results
**Files Processed:** 403431
**Files Failed:** 1

## Address Field Presence

| Category | Count | Percentage | Longest Example | Shortest Example | Random Example |
|----------|-------|------------|-----------------|------------------|----------------|
| Has Address | 298339 | 74.0% | [entry_Organization_1811435a7ea-7a1b883e-e0f0-4cb2-b938-4b6fd8d60f0c.json](https://github.com/ftrotter-gov/npd_ehr_scrape_cache/blob/main/cache/fhir_json_cache/abeo_solutions_inc_87133ed24a4073af176beaf74cd27a1e/organization/entry_Organization_1811435a7ea-7a1b883e-e0f0-4cb2-b938-4b6fd8d60f0c.json) | [entry_Organization_001.json](https://github.com/ftrotter-gov/npd_ehr_scrape_cache/blob/main/cache/fhir_json_cache/1life_healthcare_inc_b8bf6b68b0098021b1122dda499a9ab0/organization/entry_Organization_001.json) | [entry_Organization_001.json](https://github.com/ftrotter-gov/npd_ehr_scrape_cache/blob/main/cache/fhir_json_cache/1life_healthcare_inc_b8bf6b68b0098021b1122dda499a9ab0/organization/entry_Organization_001.json) |
| No Address | 105092 | 26.0% | [entry_Endpoint_idFA6NjJ01p.WnqGN2lfXufQ.json](https://github.com/ftrotter-gov/npd_ehr_scrape_cache/blob/main/cache/fhir_json_cache/aarista_technology_llc_98dd118c306868b25684644c95fe4c75/endpoint/entry_Endpoint_idFA6NjJ01p.WnqGN2lfXufQ.json) | [entry_Endpoint_test.json](https://github.com/ftrotter-gov/npd_ehr_scrape_cache/blob/main/cache/fhir_json_cache/adaptamed_llc_47d439f4130f7692caea161fa0b4d2bd/endpoint/entry_Endpoint_test.json) | [entry_Endpoint_endpoint-2.json](https://github.com/ftrotter-gov/npd_ehr_scrape_cache/blob/main/cache/fhir_json_cache/abeo_solutions_inc_87133ed24a4073af176beaf74cd27a1e/endpoint/entry_Endpoint_endpoint-2.json) |

## Address Component Breakdown
*(Percentages are of files that have address fields)*

| Component | Count | Percentage |
|-----------|-------|------------|
| City | 289723 | 97.1% |
| Country | 149535 | 50.1% |
| District | 66 | 0.0% |
| Extension | 433 | 0.1% |
| Line | 289472 | 97.0% |
| Period | 314 | 0.1% |
| Postalcode | 289850 | 97.2% |
| State | 290639 | 97.4% |
| Text | 85227 | 28.6% |
| Type | 84987 | 28.5% |
| Use | 1513 | 0.5% |

# Many Identifier Analysis Summary

## What This Analysis Does
This analysis examines organization JSON files to find records with multiple identifiers.
It specifically tracks:
- Records with 2 or more NPI identifiers (system: `http://hl7.org/fhir/sid/us-npi`)
- Records with 2 or more identifiers of any type (excluding those with 2+ NPIs)

**Note:** This analysis does NOT validate identifier format - it only counts identifiers.

## Processing Results
**Files Processed:** 287917
**Files Failed:** 0
**Total Organization Files Found:** 287917

## Identifier Analysis Results

| Category | Count | Percentage |
|----------|-------|------------|
| Organizations with 2+ NPIs | 39624 | 13.8% |
| Organizations with 2+ Identifiers (Non-NPI) | 11557 | 4.0% |
| Organizations with Single/No Identifiers | 236736 | 82.2% |

**Total Organizations Analyzed:** 287917

## Example Organizations with Multiple NPIs

1. [entry_Organization_8a4d7af1-56f7-4984-b3c7-2d2c8b342cda.json](https://github.com/ftrotter-gov/npd_ehr_scrape_cache/blob/main/cache/fhir_json_cache/altera_digital_health_inc_7fe8700d09f67caebfa9fcb284271f4b/organization/entry_Organization_8a4d7af1-56f7-4984-b3c7-2d2c8b342cda.json) - 3 NPIs (out of 7 total identifiers)
2. [entry_Organization_0e0f6263-8324-4891-851f-110d5d5f0ab3.json](https://github.com/ftrotter-gov/npd_ehr_scrape_cache/blob/main/cache/fhir_json_cache/altera_digital_health_inc_7fe8700d09f67caebfa9fcb284271f4b/organization/entry_Organization_0e0f6263-8324-4891-851f-110d5d5f0ab3.json) - 4 NPIs (out of 6 total identifiers)
3. [entry_Organization_fa7e99fe-e04b-4dde-adda-7ec41d8f6638.json](https://github.com/ftrotter-gov/npd_ehr_scrape_cache/blob/main/cache/fhir_json_cache/altera_digital_health_inc_7fe8700d09f67caebfa9fcb284271f4b/organization/entry_Organization_fa7e99fe-e04b-4dde-adda-7ec41d8f6638.json) - 2 NPIs (out of 3 total identifiers)

*See ManyIdentifierLinks.md for complete list of all 39624 organizations*

## Example Organizations with Multiple Identifiers (Non-NPI)

1. [entry_Organization_29561.json](https://github.com/ftrotter-gov/npd_ehr_scrape_cache/blob/main/cache/fhir_json_cache/advancedmd_e00d17d2867b01b204becffa2224ee67/organization/entry_Organization_29561.json) - 3 total identifiers
2. [entry_Organization_45640.json](https://github.com/ftrotter-gov/npd_ehr_scrape_cache/blob/main/cache/fhir_json_cache/advancedmd_e00d17d2867b01b204becffa2224ee67/organization/entry_Organization_45640.json) - 3 total identifiers
3. [entry_Organization_38370.json](https://github.com/ftrotter-gov/npd_ehr_scrape_cache/blob/main/cache/fhir_json_cache/advancedmd_e00d17d2867b01b204becffa2224ee67/organization/entry_Organization_38370.json) - 3 total identifiers

*See ManyIdentifierLinks.md for complete list of all 11557 organizations*

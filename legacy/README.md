# Legacy Pipeline Files

This directory contains archived files from the original pipeline implementation that have been replaced by the modern pipeline.

## Archived Files

### Step40_extract_csv_data.py
**Replaced by:** Step 45 (cehrt_fhir_parser)  
**Original Purpose:** Extract CSV data from FHIR JSON files  
**Why Archived:** The modern Step 45 parser provides:
- More comprehensive data extraction
- NPI validation with 9M+ cached entries
- NPD-compliant schema output
- Better error handling and logging
- Parallel processing capabilities

### Step50_simple_clean_output.py
**Replaced by:** Step 45 (built-in validation)  
**Original Purpose:** Clean and validate org_to_npi mappings  
**Why Archived:** Step 45 includes:
- Built-in NPI validation during processing
- URL validation
- Cleaner data model from the start
- No separate cleaning step needed

### Step60_CalculateOpenEndpoints.py
**Replaced by:** Step 52 (Step52_DiscoverEndpoints.py)  
**Original Purpose:** Discover FHIR endpoints (metadata, SMART, OpenAPI, Swagger)  
**Why Archived:** Step 52 provides:
- Same endpoint discovery functionality
- Reads from Step 45's modern output format
- Better integration with modern pipeline
- Cleaner code structure

## Pipeline Comparison

### Legacy Pipeline (Archived)
```
10 → 20 → 30 → 40 → 50 → 60 → 89 → 90
```

### Modern Pipeline (Current)
```
10 → 20 → 30 → 45 → 52 → 89 → 90
```

## Backward Compatibility

These files are kept in the `legacy/` directory for reference and backward compatibility:

- **Still functional:** You can still run the legacy pipeline using go.py
- **Not recommended:** The modern pipeline is faster, more accurate, and better maintained
- **Reference only:** Useful for understanding the evolution of the pipeline

## Running Legacy Pipeline

If you need to run the legacy pipeline (not recommended):

```bash
# Ensure files are in the root directory
cp legacy/Step40_extract_csv_data.py .
cp legacy/Step50_simple_clean_output.py .
cp legacy/Step60_CalculateOpenEndpoints.py .

# Run legacy pipeline
python go.py --steps 10 20 30 40 50 60 89 90
```

## Migration Notes

If you're migrating from the legacy to modern pipeline:

1. **No data migration needed**: Both pipelines read from the same cache
2. **Output differences**: Step 45 produces NPD-compliant schema (preferred)
3. **Dashboard compatible**: Step 89/90 work with both pipelines automatically
4. **Recommended**: Use modern pipeline for all new runs

## Questions?

See the main README.md for modern pipeline documentation and usage examples.

---

**Archived:** July 2026  
**Reason:** Replaced by more efficient and comprehensive modern pipeline

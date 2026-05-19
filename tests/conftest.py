import json
from pathlib import Path

import pytest


@pytest.fixture
def sample_organization_entry():
    return {
        "fullUrl": "https://example.com/Organization/org-1",
        "resource": {
            "resourceType": "Organization",
            "id": "org-1",
            "name": "Example Clinic",
            "active": True,
            "identifier": [
                {
                    "system": "http://hl7.org/fhir/sid/us-npi",
                    "value": "1234567890",
                }
            ],
            "address": [
                {
                    "line": ["100 Main St", "Suite 200"],
                    "city": "Baltimore",
                    "state": "MD",
                    "postalCode": "21201",
                    "country": "US",
                    "use": "work",
                }
            ],
            "telecom": [
                {"system": "phone", "value": "+1 410 555 1212", "use": "work"},
                {"system": "email", "value": "info@example.org", "use": "work"},
                {"system": "url", "value": "https://example.org", "use": "work"},
            ],
            "endpoint": [{"reference": "Endpoint/endpoint-1"}],
        },
    }


@pytest.fixture
def sample_endpoint_entry():
    return {
        "fullUrl": "https://example.com/Endpoint/endpoint-1",
        "resource": {
            "resourceType": "Endpoint",
            "id": "endpoint-1",
            "status": "active",
            "connectionType": {
                "system": "http://terminology.hl7.org/CodeSystem/endpoint-connection-type",
                "code": "hl7-fhir-rest",
                "display": "HL7 FHIR REST",
            },
            "name": "Example FHIR Endpoint",
            "address": "https://example.org/fhir/R4",
            "payloadType": [
                {
                    "coding": [
                        {
                            "system": "http://ihe.net/fhir/ihe.formatcode.fhir/CodeSystem/formatcode",
                            "code": "urn:ihe:pcc:xphr:2007",
                        }
                    ]
                }
            ],
            "payloadMimeType": ["application/fhir+json"],
        },
    }


@pytest.fixture
def fhir_cache_dir(tmp_path, sample_organization_entry, sample_endpoint_entry):
    vendor_dir = tmp_path / "cache" / "example_vendor" 
    org_dir = vendor_dir / "organization"
    endpoint_dir = vendor_dir / "endpoint"
    org_dir.mkdir(parents=True)
    endpoint_dir.mkdir(parents=True)

    (org_dir / "entry_Organization_001.json").write_text(
        json.dumps(sample_organization_entry), encoding="utf-8"
    )
    (endpoint_dir / "entry_Endpoint_001.json").write_text(
        json.dumps(sample_endpoint_entry), encoding="utf-8"
    )

    return tmp_path / "cache"


@pytest.fixture
def npi_cache_dir(tmp_path):
    cache_dir = tmp_path / "npi_cache"
    cache_dir.mkdir()
    (cache_dir / "valid_npi.1.csv").write_text(
        "npi,is_valid\n1234567890,1\n1111111111,0\n",
        encoding="utf-8",
    )
    return cache_dir


from cehrt_fhir_parser.models.factories import create_fhir_resource_from_json


def test_create_organization_resource(sample_organization_entry):
    resource = create_fhir_resource_from_json(
        json_data=sample_organization_entry,
        vendor_name="example_vendor",
    )

    assert resource is not None
    assert resource.resource_type == "Organization"
    assert resource.original_id == "org-1"
    assert resource.name == "Example Clinic"

    records = resource.to_postgres_records()
    assert records["organization"][0]["name"] == "Example Clinic"
    assert records["endpoint_instance_to_other_id"][0]["other_id"] == "1234567890"
    assert records["fhir_organization_phone"]
    assert records["fhir_organization_email"]
    assert records["fhir_organization_contact_url"]


def test_create_endpoint_resource(sample_endpoint_entry):
    resource = create_fhir_resource_from_json(
        json_data=sample_endpoint_entry,
        vendor_name="example_vendor",
    )

    assert resource is not None
    assert resource.resource_type == "Endpoint"
    assert resource.original_id == "endpoint-1"
    assert resource.address == "https://example.org/fhir/R4"

    records = resource.to_postgres_records()
    assert records["endpoint_instance"][0]["endpoint_connection_type_id"] == "hl7-fhir-rest"
    assert records["npd_endpoint_instance"][0]["address"] == "https://example.org/fhir/R4"
    assert records["endpoint_instance_to_payload"][0]["payload_type_id"] == "urn:ihe:pcc:xphr:2007"


def test_unsupported_resource_returns_none():
    resource = create_fhir_resource_from_json(
        json_data={
            "fullUrl": "https://example.com/Patient/1",
            "resource": {"resourceType": "Patient", "id": "1"},
        },
        vendor_name="example_vendor",
    )

    assert resource is None


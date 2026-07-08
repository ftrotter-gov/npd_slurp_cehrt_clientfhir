#!/usr/bin/env python3
"""
Step52_DiscoverEndpoints.py

This script reads endpoint data from Step 45 (modern parser) and enriches it by discovering
well-known FHIR endpoints at various directory levels for each unique domain.

Replaces the legacy endpoint discovery pipeline (old Steps 40/50/60) with a modern version
that reads from Step 45's output format.

For each domain, it tests directory levels to find:
- Capability Statement (/metadata)
- Smart Config (/.well-known/smart-configuration)
- OpenAPI docs (/api-docs)
- OpenAPI JSON (/openapi.json)
- Swagger (/swagger)
- Swagger JSON (/swagger.json)

Usage:
    python Step52_DiscoverEndpoints.py --input_dir ./parser_output --output_file enriched_endpoints.csv
"""

import argparse
import csv
import requests
import os
from urllib.parse import urlparse
from typing import List, Tuple, Dict
from pathlib import Path
import time
import logging
import urllib3.exceptions

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class EndpointDiscovery:
    """Class for discovering FHIR endpoints from Step 45 output"""
    
    # Define the endpoints we're looking for
    ENDPOINTS = {
        'capability_url': '/metadata',
        'smart_url': '/.well-known/smart-configuration',
        'openapi_docs_url': '/api-docs',
        'openapi_json_url': '/openapi.json',
        'swagger_url': '/swagger',
        'swagger_json_url': '/swagger.json'
    }
    
    @staticmethod
    def parse_arguments():
        """Parse command line arguments"""
        parser = argparse.ArgumentParser(description='Discover FHIR endpoints from Step 45 output')
        parser.add_argument('--input_dir', required=True, help='Path to Step 45 output directory')
        parser.add_argument('--output_file', default='enriched_endpoints.csv', help='Path to output CSV file')
        return parser.parse_args()
    
    @staticmethod
    def load_step45_data(*, input_dir: str) -> List[Tuple[str, str, str]]:
        """Load endpoint and NPI data from Step 45 output files"""
        data = []
        
        # Read endpoint_instance.csv from fhir_analysis directory (has full metadata)
        endpoint_file = Path(input_dir) / 'fhir_analysis' / 'endpoint_instance.csv'
        npi_file = Path(input_dir) / 'fhir_analysis' / 'endpoint_to_npi.csv'
        
        if not endpoint_file.exists():
            logger.error(f"Endpoint file not found: {endpoint_file}")
            return []
        
        # First, load NPI mappings from npd_endpoint_instance_to_other_id.csv
        npi_map = {}  # endpoint_uuid -> list of NPIs
        if npi_file.exists():
            try:
                with open(npi_file, 'r', newline='', encoding='utf-8') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        # Updated column names to match actual CSV structure
                        endpoint_uuid = row.get('endpoint_instance_id', '').strip()
                        other_id = row.get('other_id', '').strip()
                        system = row.get('system', '').strip()
                        
                        # Check if this is an NPI (system contains 'us-npi')
                        if endpoint_uuid and other_id and 'us-npi' in system.lower():
                            if endpoint_uuid not in npi_map:
                                npi_map[endpoint_uuid] = []
                            npi_map[endpoint_uuid].append(other_id)
            except Exception as e:
                logger.warning(f"Error reading NPI mappings: {e}")
        
        # Now load endpoint data
        try:
            with open(endpoint_file, 'r', newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                
                for row in reader:
                    # Step 45 uses 'address' for endpoint URL, 'id' for UUID
                    endpoint_url = row.get('address', '').strip()
                    endpoint_uuid = row.get('id', '').strip()
                    # Use vendor_name for aggregation by EHR vendor (not individual org name)
                    vendor_name = row.get('vendor_name', '').strip()
                    
                    if endpoint_url:
                        # Get NPIs for this endpoint (may be multiple or none)
                        npis = npi_map.get(endpoint_uuid, [''])
                        
                        # Create a row for each NPI (or one row with empty NPI if none)
                        for npi in npis if npis else ['']:
                            data.append((endpoint_url, npi, vendor_name))
                        
        except FileNotFoundError:
            logger.error(f"Input file not found: {endpoint_file}")
            return []
        except Exception as e:
            logger.error(f"Error reading input file: {e}")
            return []
        
        logger.info(f"Loaded {len(data)} endpoint records from Step 45 output")
        return data
    
    @staticmethod
    def extract_unique_domains(*, endpoint_data: List[Tuple[str, str, str]]) -> Dict[str, str]:
        """Extract unique domains and map them to a sample full URL"""
        domain_to_sample_url = {}
        
        for endpoint_url, _, _ in endpoint_data:
            try:
                parsed = urlparse(endpoint_url)
                domain = f"{parsed.scheme}://{parsed.netloc}/"
                
                # Store the first full URL we see for this domain as sample
                if domain not in domain_to_sample_url:
                    domain_to_sample_url[domain] = endpoint_url
                    
            except Exception as e:
                logger.warning(f"Failed to parse URL {endpoint_url}: {e}")
                continue
        
        logger.info(f"Found {len(domain_to_sample_url)} unique domains")
        return domain_to_sample_url
    
    @staticmethod
    def get_directory_levels(*, url: str) -> List[str]:
        """Get all directory levels from a URL for testing"""
        try:
            parsed = urlparse(url)
            base_url = f"{parsed.scheme}://{parsed.netloc}"
            
            # Start with just the domain
            levels = [base_url + "/"]
            
            # Add each directory level
            if parsed.path and parsed.path != '/':
                path_parts = [p for p in parsed.path.split('/') if p]
                current_path = ""
                
                for part in path_parts:
                    current_path += "/" + part
                    levels.append(base_url + current_path + "/")
            
            return levels
            
        except Exception as e:
            logger.warning(f"Failed to get directory levels for {url}: {e}")
            return []
    
    @staticmethod
    def test_endpoint_at_level(*, base_url: str, endpoint_path: str, timeout: int = 10) -> bool:
        """Test if an endpoint exists at a given base URL level"""
        try:
            test_url = base_url.rstrip('/') + endpoint_path
            response = requests.get(test_url, timeout=timeout, allow_redirects=True)
            
            # Accept 200-299 status codes as successful
            return 200 <= response.status_code < 300
            
        except urllib3.exceptions.HeaderParsingError as e:
            # Custom headers are fine - consider endpoint responsive
            logger.debug(f"Endpoint {base_url}{endpoint_path} has custom headers but is responsive: {e}")
            return True
        except Exception as e:
            # Handle any other HeaderParsingError variants
            if "HeaderParsingError" in str(e) or "MissingHeaderBodySeparatorDefect" in str(e):
                logger.debug(f"Endpoint {base_url}{endpoint_path} has custom headers but is responsive: {e}")
                return True
            
            logger.debug(f"Endpoint {base_url}{endpoint_path} not responsive: {e}")
            return False
    
    @staticmethod
    def discover_endpoints_for_domain(*, domain: str, sample_url: str) -> Dict[str, str]:
        """Discover all endpoints for a given domain"""
        logger.info(f"Discovering endpoints for domain: {domain}")
        
        # Get all directory levels to test
        levels = EndpointDiscovery.get_directory_levels(url=sample_url)
        
        # Initialize results with error messages
        results = {}
        for endpoint_name in EndpointDiscovery.ENDPOINTS.keys():
            results[endpoint_name] = f"Error - failed to find {endpoint_name.replace('_', ' ')}"
        
        # Test each level for each endpoint
        for level in levels:
            logger.debug(f"Testing level: {level}")
            
            for endpoint_name, endpoint_path in EndpointDiscovery.ENDPOINTS.items():
                # Skip if we already found this endpoint
                if not results[endpoint_name].startswith("Error"):
                    continue
                
                if EndpointDiscovery.test_endpoint_at_level(base_url=level, endpoint_path=endpoint_path):
                    found_url = level.rstrip('/') + endpoint_path
                    results[endpoint_name] = found_url
                    logger.info(f"Found {endpoint_name}: {found_url}")
                
                # Add small delay between requests
                time.sleep(0.1)
            
            # Add delay between levels
            time.sleep(0.5)
        
        # Check if no URLs were found at all and warn
        found_any_url = any(not result.startswith("Error") for result in results.values())
        if not found_any_url:
            logger.warning(f"No FHIR endpoints found for domain: {domain}")
        
        return results
    
    @staticmethod
    def choose_https_org_url(*, org_fhir_url: str, endpoints: Dict[str, str]) -> str:
        """Choose the best HTTPS organizational URL from available options"""
        
        # First preference: use the original org_fhir_url if it's HTTPS
        if org_fhir_url.startswith('https://'):
            return org_fhir_url
        
        # Second preference: look for working HTTPS endpoints in priority order
        endpoint_priority = ['capability_url', 'smart_url', 'openapi_docs_url', 'swagger_url', 'openapi_json_url', 'swagger_json_url']
        
        for endpoint_name in endpoint_priority:
            endpoint_url = endpoints.get(endpoint_name, '')
            if endpoint_url.startswith('https://'):
                return endpoint_url
        
        # Third preference: use the original org_fhir_url even if it's HTTP
        if org_fhir_url.startswith('http://'):
            return org_fhir_url
        
        # Fourth preference: look for any working HTTP endpoints
        for endpoint_name in endpoint_priority:
            endpoint_url = endpoints.get(endpoint_name, '')
            if endpoint_url.startswith('http://'):
                return endpoint_url
        
        # Last resort: return the original URL
        return org_fhir_url
    
    @staticmethod
    def generate_enriched_output(*, endpoint_data: List[Tuple[str, str, str]], domain_endpoints: Dict[str, Dict[str, str]]) -> List[Dict[str, str]]:
        """Generate enriched output data"""
        enriched_data = []
        
        for org_fhir_url, npi, vendor_name in endpoint_data:
            try:
                parsed = urlparse(org_fhir_url)
                domain = f"{parsed.scheme}://{parsed.netloc}/"
                
                # Get endpoints for this domain
                endpoints = domain_endpoints.get(domain, {})
                
                # Choose the best HTTPS organizational URL
                https_org_url = EndpointDiscovery.choose_https_org_url(
                    org_fhir_url=org_fhir_url,
                    endpoints=endpoints
                )
                
                # Create enriched row
                row = {
                    'org_fhir_url': org_fhir_url,
                    'npi': npi,
                    'vendor_name': vendor_name,
                    'https_org_url': https_org_url,
                    'capability_url': endpoints.get('capability_url', 'Error - failed to find capability url'),
                    'smart_url': endpoints.get('smart_url', 'Error - failed to find smart url'),
                    'openapi_docs_url': endpoints.get('openapi_docs_url', 'Error - failed to find openapi docs url'),
                    'openapi_json_url': endpoints.get('openapi_json_url', 'Error - failed to find openapi json url'),
                    'swagger_url': endpoints.get('swagger_url', 'Error - failed to find swagger url'),
                    'swagger_json_url': endpoints.get('swagger_json_url', 'Error - failed to find swagger json url'),
                }
                
                enriched_data.append(row)
                
            except Exception as e:
                logger.warning(f"Error processing URL {org_fhir_url}: {e}")
                continue
        
        return enriched_data
    
    @staticmethod
    def write_output_csv(*, enriched_data: List[Dict[str, str]], output_file: str):
        """Write enriched data to output CSV file"""
        if not enriched_data:
            logger.warning("No enriched data to write")
            return
        
        try:
            fieldnames = ['org_fhir_url', 'npi', 'vendor_name', 'https_org_url', 'capability_url', 'smart_url', 
                         'openapi_docs_url', 'openapi_json_url', 'swagger_url', 'swagger_json_url']
            
            with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(enriched_data)
            
            logger.info(f"Successfully wrote {len(enriched_data)} records to {output_file}")
            
        except Exception as e:
            logger.error(f"Error writing output file: {e}")
    
    @staticmethod
    def run():
        """Main execution method"""
        # Parse arguments
        args = EndpointDiscovery.parse_arguments()
        
        logger.info("Starting Step 52: Endpoint Discovery")
        logger.info(f"Input directory: {args.input_dir}")
        logger.info(f"Output file: {args.output_file}")
        
        # Load Step 45 data
        logger.info("Loading endpoint data from Step 45 output...")
        endpoint_data = EndpointDiscovery.load_step45_data(input_dir=args.input_dir)
        
        if not endpoint_data:
            logger.error("No endpoint data loaded. Exiting.")
            return
        
        # Extract unique domains
        logger.info("Extracting unique domains...")
        domain_to_sample_url = EndpointDiscovery.extract_unique_domains(endpoint_data=endpoint_data)
        
        # Discover endpoints for each domain
        logger.info("Discovering endpoints for each domain...")
        domain_endpoints = {}
        
        for domain, sample_url in domain_to_sample_url.items():
            endpoints = EndpointDiscovery.discover_endpoints_for_domain(
                domain=domain,
                sample_url=sample_url
            )
            domain_endpoints[domain] = endpoints
        
        # Generate enriched output
        logger.info("Generating enriched output...")
        enriched_data = EndpointDiscovery.generate_enriched_output(
            endpoint_data=endpoint_data,
            domain_endpoints=domain_endpoints
        )
        
        # Write output
        logger.info("Writing output file...")
        EndpointDiscovery.write_output_csv(
            enriched_data=enriched_data,
            output_file=args.output_file
        )
        
        logger.info("Step 52 completed successfully!")


if __name__ == "__main__":
    EndpointDiscovery.run()

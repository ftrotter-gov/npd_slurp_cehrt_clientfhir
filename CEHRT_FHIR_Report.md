# CEHRT FHIR Vendor Compliance Dashboard

This dashboard lists CEHRT vendors in order of their compliance with a scrappable FHIR ecosystem. Each column represents a compliance check, and each cell shows a shield.io badge indicating pass (green) or fail (red).

<style>
.center-cell {
  text-align: center;
  vertical-align: middle;
}
.header-col {
  white-space: nowrap;
}
</style>

<table>
  <thead>
    <tr>
      <th class="header-col">Vendor</th>
      <th class="header-col">Reachable</th>
      <th class="header-col">Has ONPI</th>
      <th class="header-col">HTTPS ORG URL</th>
      <th class="header-col">Findable Metadata</th>
      <th class="header-col">Findable SMART</th>
      <th class="header-col">Findable OpenAPI Docs</th>
      <th class="header-col">Findable OpenAPI JSON</th>
      <th class="header-col">Findable Swagger</th>
      <th class="header-col">Findable Swagger JSON</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>chn_tech_solutions_llc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://ice3.mychn.org/apis/default/fhir"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://ice3.mychn.org/apis/default/fhir" ></a></td>
      <td class="center-cell"><a href="https://ice3.mychn.org/apis/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://ice3.mychn.org/apis/metadata" ></a></td>
      <td class="center-cell"><a href="https://ice3.mychn.org/apis/default/fhir/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://ice3.mychn.org/apis/default/fhir/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><a href="https://ice3.mychn.org/apis/api-docs"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI Docs: Pass" title="Click to visit: https://ice3.mychn.org/apis/api-docs" ></a></td>
      <td class="center-cell"><a href="https://ice3.mychn.org/apis/openapi.json"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI JSON: Pass" title="Click to visit: https://ice3.mychn.org/apis/openapi.json" ></a></td>
      <td class="center-cell"><a href="https://ice3.mychn.org/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://ice3.mychn.org/swagger" ></a></td>
      <td class="center-cell"><a href="https://ice3.mychn.org/apis/swagger.json"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger JSON: Pass" title="Click to visit: https://ice3.mychn.org/apis/swagger.json" ></a></td>
    </tr>
    <tr>
      <td>cloudcraft_llc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://fhirapi.naiacorp.net/fhir/cloudcraft/basepractice/r4"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhirapi.naiacorp.net/fhir/cloudcraft/basepractice/r4" ></a></td>
      <td class="center-cell"><a href="https://fhirapi.naiacorp.net/fhir/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhirapi.naiacorp.net/fhir/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhirapi.naiacorp.net/fhir/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhirapi.naiacorp.net/fhir/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><a href="https://fhirapi.naiacorp.net/api-docs"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI Docs: Pass" title="Click to visit: https://fhirapi.naiacorp.net/api-docs" ></a></td>
      <td class="center-cell"><a href="https://fhirapi.naiacorp.net/openapi.json"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI JSON: Pass" title="Click to visit: https://fhirapi.naiacorp.net/openapi.json" ></a></td>
      <td class="center-cell"><a href="https://fhirapi.naiacorp.net/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://fhirapi.naiacorp.net/swagger" ></a></td>
      <td class="center-cell"><a href="https://fhirapi.naiacorp.net/swagger.json"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger JSON: Pass" title="Click to visit: https://fhirapi.naiacorp.net/swagger.json" ></a></td>
    </tr>
    <tr>
      <td>drchrono_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://drchrono-fhirpresentation.everhealthsoftware.com/fhir/drchrono/307566/r4"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://drchrono-fhirpresentation.everhealthsoftware.com/fhir/drchrono/307566/r4" ></a></td>
      <td class="center-cell"><a href="https://drchrono-fhirpresentation.everhealthsoftware.com/fhir/drchrono/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://drchrono-fhirpresentation.everhealthsoftware.com/fhir/drchrono/metadata" ></a></td>
      <td class="center-cell"><a href="https://drchrono-fhirpresentation.everhealthsoftware.com/fhir/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://drchrono-fhirpresentation.everhealthsoftware.com/fhir/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><a href="https://drchrono-fhirpresentation.everhealthsoftware.com/fhir/drchrono/api-docs"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI Docs: Pass" title="Click to visit: https://drchrono-fhirpresentation.everhealthsoftware.com/fhir/drchrono/api-docs" ></a></td>
      <td class="center-cell"><a href="https://drchrono-fhirpresentation.everhealthsoftware.com/fhir/drchrono/openapi.json"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI JSON: Pass" title="Click to visit: https://drchrono-fhirpresentation.everhealthsoftware.com/fhir/drchrono/openapi.json" ></a></td>
      <td class="center-cell"><a href="https://drchrono-fhirpresentation.everhealthsoftware.com/fhir/drchrono/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://drchrono-fhirpresentation.everhealthsoftware.com/fhir/drchrono/swagger" ></a></td>
      <td class="center-cell"><a href="https://drchrono-fhirpresentation.everhealthsoftware.com/fhir/drchrono/swagger.json"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger JSON: Pass" title="Click to visit: https://drchrono-fhirpresentation.everhealthsoftware.com/fhir/drchrono/swagger.json" ></a></td>
    </tr>
    <tr>
      <td>dss_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://fhirjuno-prod-web.dssinc.com/fhir/communityhealthhospitals/01ho/r4"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhirjuno-prod-web.dssinc.com/fhir/communityhealthhospitals/01ho/r4" ></a></td>
      <td class="center-cell"><a href="https://fhirjuno-prod-web.dssinc.com/fhir/communityhealthhospitals/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhirjuno-prod-web.dssinc.com/fhir/communityhealthhospitals/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhirjuno-prod-web.dssinc.com/fhir/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhirjuno-prod-web.dssinc.com/fhir/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><a href="https://fhirjuno-prod-web.dssinc.com/fhir/communityhealthhospitals/api-docs"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI Docs: Pass" title="Click to visit: https://fhirjuno-prod-web.dssinc.com/fhir/communityhealthhospitals/api-docs" ></a></td>
      <td class="center-cell"><a href="https://fhirjuno-prod-web.dssinc.com/fhir/communityhealthhospitals/openapi.json"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI JSON: Pass" title="Click to visit: https://fhirjuno-prod-web.dssinc.com/fhir/communityhealthhospitals/openapi.json" ></a></td>
      <td class="center-cell"><a href="https://fhirjuno-prod-web.dssinc.com/fhir/communityhealthhospitals/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://fhirjuno-prod-web.dssinc.com/fhir/communityhealthhospitals/swagger" ></a></td>
      <td class="center-cell"><a href="https://fhirjuno-prod-web.dssinc.com/fhir/communityhealthhospitals/swagger.json"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger JSON: Pass" title="Click to visit: https://fhirjuno-prod-web.dssinc.com/fhir/communityhealthhospitals/swagger.json" ></a></td>
    </tr>
    <tr>
      <td>dynamic_health_it_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://dynamicfhirpresentation.dynamicfhirsandbox.com/fhir/dhit/tenant01/r4"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://dynamicfhirpresentation.dynamicfhirsandbox.com/fhir/dhit/tenant01/r4" ></a></td>
      <td class="center-cell"><a href="https://dynamicfhirpresentation.dynamicfhirsandbox.com/fhir/dhit/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://dynamicfhirpresentation.dynamicfhirsandbox.com/fhir/dhit/metadata" ></a></td>
      <td class="center-cell"><a href="https://dynamicfhirpresentation.dynamicfhirsandbox.com/fhir/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://dynamicfhirpresentation.dynamicfhirsandbox.com/fhir/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><a href="https://dynamicfhirpresentation.dynamicfhirsandbox.com/fhir/dhit/api-docs"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI Docs: Pass" title="Click to visit: https://dynamicfhirpresentation.dynamicfhirsandbox.com/fhir/dhit/api-docs" ></a></td>
      <td class="center-cell"><a href="https://dynamicfhirpresentation.dynamicfhirsandbox.com/fhir/dhit/openapi.json"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI JSON: Pass" title="Click to visit: https://dynamicfhirpresentation.dynamicfhirsandbox.com/fhir/dhit/openapi.json" ></a></td>
      <td class="center-cell"><a href="https://dynamicfhirpresentation.dynamicfhirsandbox.com/fhir/dhit/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://dynamicfhirpresentation.dynamicfhirsandbox.com/fhir/dhit/swagger" ></a></td>
      <td class="center-cell"><a href="https://dynamicfhirpresentation.dynamicfhirsandbox.com/fhir/dhit/swagger.json"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger JSON: Pass" title="Click to visit: https://dynamicfhirpresentation.dynamicfhirsandbox.com/fhir/dhit/swagger.json" ></a></td>
    </tr>
    <tr>
      <td>enable_healthcare_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://ehifhir.ehiconnect.com/fhir/ehi/fe663a72b27bdc613873fbbb512f6f67/r4"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://ehifhir.ehiconnect.com/fhir/ehi/fe663a72b27bdc613873fbbb512f6f67/r4" ></a></td>
      <td class="center-cell"><a href="https://ehifhir.ehiconnect.com/fhir/ehi/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://ehifhir.ehiconnect.com/fhir/ehi/metadata" ></a></td>
      <td class="center-cell"><a href="https://ehifhir.ehiconnect.com/fhir/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://ehifhir.ehiconnect.com/fhir/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><a href="https://ehifhir.ehiconnect.com/fhir/ehi/api-docs"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI Docs: Pass" title="Click to visit: https://ehifhir.ehiconnect.com/fhir/ehi/api-docs" ></a></td>
      <td class="center-cell"><a href="https://ehifhir.ehiconnect.com/fhir/ehi/openapi.json"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI JSON: Pass" title="Click to visit: https://ehifhir.ehiconnect.com/fhir/ehi/openapi.json" ></a></td>
      <td class="center-cell"><a href="https://ehifhir.ehiconnect.com/fhir/ehi/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://ehifhir.ehiconnect.com/fhir/ehi/swagger" ></a></td>
      <td class="center-cell"><a href="https://ehifhir.ehiconnect.com/fhir/ehi/swagger.json"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger JSON: Pass" title="Click to visit: https://ehifhir.ehiconnect.com/fhir/ehi/swagger.json" ></a></td>
    </tr>
    <tr>
      <td>first_insight_corporation</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://fhir.maximeyes.com/api/villageoptical/R4"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir.maximeyes.com/api/villageoptical/R4" ></a></td>
      <td class="center-cell"><a href="https://fhir.maximeyes.com/api/villageoptical/R4/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhir.maximeyes.com/api/villageoptical/R4/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhir.maximeyes.com/api/villageoptical/R4/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhir.maximeyes.com/api/villageoptical/R4/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><a href="http://hl7.org/api-docs"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI Docs: Pass" title="Click to visit: http://hl7.org/api-docs" ></a></td>
      <td class="center-cell"><a href="http://hl7.org/openapi.json"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI JSON: Pass" title="Click to visit: http://hl7.org/openapi.json" ></a></td>
      <td class="center-cell"><a href="http://hl7.org/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: http://hl7.org/swagger" ></a></td>
      <td class="center-cell"><a href="http://hl7.org/swagger.json"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger JSON: Pass" title="Click to visit: http://hl7.org/swagger.json" ></a></td>
    </tr>
    <tr>
      <td>health_innovation_technologies_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://revolutionehr.dynamicfhir.com/fhir/revolutionehr/1929/r4"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://revolutionehr.dynamicfhir.com/fhir/revolutionehr/1929/r4" ></a></td>
      <td class="center-cell"><a href="https://revolutionehr.dynamicfhir.com/fhir/revolutionehr/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://revolutionehr.dynamicfhir.com/fhir/revolutionehr/metadata" ></a></td>
      <td class="center-cell"><a href="https://revolutionehr.dynamicfhir.com/fhir/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://revolutionehr.dynamicfhir.com/fhir/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><a href="https://revolutionehr.dynamicfhir.com/fhir/revolutionehr/api-docs"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI Docs: Pass" title="Click to visit: https://revolutionehr.dynamicfhir.com/fhir/revolutionehr/api-docs" ></a></td>
      <td class="center-cell"><a href="https://revolutionehr.dynamicfhir.com/fhir/revolutionehr/openapi.json"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI JSON: Pass" title="Click to visit: https://revolutionehr.dynamicfhir.com/fhir/revolutionehr/openapi.json" ></a></td>
      <td class="center-cell"><a href="https://revolutionehr.dynamicfhir.com/fhir/revolutionehr/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://revolutionehr.dynamicfhir.com/fhir/revolutionehr/swagger" ></a></td>
      <td class="center-cell"><a href="https://revolutionehr.dynamicfhir.com/fhir/revolutionehr/swagger.json"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger JSON: Pass" title="Click to visit: https://revolutionehr.dynamicfhir.com/fhir/revolutionehr/swagger.json" ></a></td>
    </tr>
    <tr>
      <td>health_samurai_inc_2</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://fhir-app-portal.aidbox.app/Organization/a9afd4c9-8443-3b5a-a486-07c3bb109b3f/fhir"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir-app-portal.aidbox.app/Organization/a9afd4c9-8443-3b5a-a486-07c3bb109b3f/fhir" ></a></td>
      <td class="center-cell"><a href="https://fhir-app-portal.aidbox.app/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhir-app-portal.aidbox.app/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhir-app-portal.aidbox.app/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhir-app-portal.aidbox.app/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><a href="https://fhir-app-portal.aidbox.app/api-docs"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI Docs: Pass" title="Click to visit: https://fhir-app-portal.aidbox.app/api-docs" ></a></td>
      <td class="center-cell"><a href="https://fhir-app-portal.aidbox.app/openapi.json"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI JSON: Pass" title="Click to visit: https://fhir-app-portal.aidbox.app/openapi.json" ></a></td>
      <td class="center-cell"><a href="https://fhir-app-portal.aidbox.app/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://fhir-app-portal.aidbox.app/swagger" ></a></td>
      <td class="center-cell"><a href="https://fhir-app-portal.aidbox.app/swagger.json"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger JSON: Pass" title="Click to visit: https://fhir-app-portal.aidbox.app/swagger.json" ></a></td>
    </tr>
    <tr>
      <td>isalus_healthcare</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://isalus-fhirpresentation.everhealthsoftware.com/fhir/isalus/a997/r4"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://isalus-fhirpresentation.everhealthsoftware.com/fhir/isalus/a997/r4" ></a></td>
      <td class="center-cell"><a href="https://isalus-fhirpresentation.everhealthsoftware.com/fhir/isalus/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://isalus-fhirpresentation.everhealthsoftware.com/fhir/isalus/metadata" ></a></td>
      <td class="center-cell"><a href="https://isalus-fhirpresentation.everhealthsoftware.com/fhir/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://isalus-fhirpresentation.everhealthsoftware.com/fhir/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><a href="https://isalus-fhirpresentation.everhealthsoftware.com/fhir/isalus/api-docs"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI Docs: Pass" title="Click to visit: https://isalus-fhirpresentation.everhealthsoftware.com/fhir/isalus/api-docs" ></a></td>
      <td class="center-cell"><a href="https://isalus-fhirpresentation.everhealthsoftware.com/fhir/isalus/openapi.json"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI JSON: Pass" title="Click to visit: https://isalus-fhirpresentation.everhealthsoftware.com/fhir/isalus/openapi.json" ></a></td>
      <td class="center-cell"><a href="https://isalus-fhirpresentation.everhealthsoftware.com/fhir/isalus/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://isalus-fhirpresentation.everhealthsoftware.com/fhir/isalus/swagger" ></a></td>
      <td class="center-cell"><a href="https://isalus-fhirpresentation.everhealthsoftware.com/fhir/isalus/swagger.json"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger JSON: Pass" title="Click to visit: https://isalus-fhirpresentation.everhealthsoftware.com/fhir/isalus/swagger.json" ></a></td>
    </tr>
    <tr>
      <td>juno_health</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://fhirjuno-prod-web.dssinc.com/fhir/communityhealthhospitals/03ho/r4"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhirjuno-prod-web.dssinc.com/fhir/communityhealthhospitals/03ho/r4" ></a></td>
      <td class="center-cell"><a href="https://fhirjuno-prod-web.dssinc.com/fhir/communityhealthhospitals/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhirjuno-prod-web.dssinc.com/fhir/communityhealthhospitals/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhirjuno-prod-web.dssinc.com/fhir/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhirjuno-prod-web.dssinc.com/fhir/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><a href="https://fhirjuno-prod-web.dssinc.com/fhir/communityhealthhospitals/api-docs"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI Docs: Pass" title="Click to visit: https://fhirjuno-prod-web.dssinc.com/fhir/communityhealthhospitals/api-docs" ></a></td>
      <td class="center-cell"><a href="https://fhirjuno-prod-web.dssinc.com/fhir/communityhealthhospitals/openapi.json"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI JSON: Pass" title="Click to visit: https://fhirjuno-prod-web.dssinc.com/fhir/communityhealthhospitals/openapi.json" ></a></td>
      <td class="center-cell"><a href="https://fhirjuno-prod-web.dssinc.com/fhir/communityhealthhospitals/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://fhirjuno-prod-web.dssinc.com/fhir/communityhealthhospitals/swagger" ></a></td>
      <td class="center-cell"><a href="https://fhirjuno-prod-web.dssinc.com/fhir/communityhealthhospitals/swagger.json"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger JSON: Pass" title="Click to visit: https://fhirjuno-prod-web.dssinc.com/fhir/communityhealthhospitals/swagger.json" ></a></td>
    </tr>
    <tr>
      <td>md_logic_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://mdlogiccloud.com/api/fhir/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://mdlogiccloud.com/api/fhir/" ></a></td>
      <td class="center-cell"><a href="https://mdlogiccloud.com/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://mdlogiccloud.com/metadata" ></a></td>
      <td class="center-cell"><a href="https://mdlogiccloud.com/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://mdlogiccloud.com/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><a href="https://mdlogiccloud.com/api-docs"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI Docs: Pass" title="Click to visit: https://mdlogiccloud.com/api-docs" ></a></td>
      <td class="center-cell"><a href="https://mdlogiccloud.com/openapi.json"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI JSON: Pass" title="Click to visit: https://mdlogiccloud.com/openapi.json" ></a></td>
      <td class="center-cell"><a href="https://mdlogiccloud.com/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://mdlogiccloud.com/swagger" ></a></td>
      <td class="center-cell"><a href="https://mdlogiccloud.com/swagger.json"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger JSON: Pass" title="Click to visit: https://mdlogiccloud.com/swagger.json" ></a></td>
    </tr>
    <tr>
      <td>medconnect_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://api.medconnecthealth.com/fhir/medconnecthealth/wuc/r4"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://api.medconnecthealth.com/fhir/medconnecthealth/wuc/r4" ></a></td>
      <td class="center-cell"><a href="https://api.medconnecthealth.com/fhir/medconnecthealth/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://api.medconnecthealth.com/fhir/medconnecthealth/metadata" ></a></td>
      <td class="center-cell"><a href="https://api.medconnecthealth.com/fhir/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://api.medconnecthealth.com/fhir/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><a href="https://api.medconnecthealth.com/fhir/medconnecthealth/api-docs"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI Docs: Pass" title="Click to visit: https://api.medconnecthealth.com/fhir/medconnecthealth/api-docs" ></a></td>
      <td class="center-cell"><a href="https://api.medconnecthealth.com/fhir/medconnecthealth/openapi.json"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI JSON: Pass" title="Click to visit: https://api.medconnecthealth.com/fhir/medconnecthealth/openapi.json" ></a></td>
      <td class="center-cell"><a href="https://api.medconnecthealth.com/fhir/medconnecthealth/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://api.medconnecthealth.com/fhir/medconnecthealth/swagger" ></a></td>
      <td class="center-cell"><a href="https://api.medconnecthealth.com/fhir/medconnecthealth/swagger.json"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger JSON: Pass" title="Click to visit: https://api.medconnecthealth.com/fhir/medconnecthealth/swagger.json" ></a></td>
    </tr>
    <tr>
      <td>myhelo_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://provider.myhelo.com/fhir/Organization/74"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://provider.myhelo.com/fhir/Organization/74" ></a></td>
      <td class="center-cell"><a href="https://provider.myhelo.com/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://provider.myhelo.com/metadata" ></a></td>
      <td class="center-cell"><a href="https://provider.myhelo.com/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://provider.myhelo.com/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><a href="https://provider.myhelo.com/api-docs"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI Docs: Pass" title="Click to visit: https://provider.myhelo.com/api-docs" ></a></td>
      <td class="center-cell"><a href="https://provider.myhelo.com/openapi.json"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI JSON: Pass" title="Click to visit: https://provider.myhelo.com/openapi.json" ></a></td>
      <td class="center-cell"><a href="https://provider.myhelo.com/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://provider.myhelo.com/swagger" ></a></td>
      <td class="center-cell"><a href="https://provider.myhelo.com/swagger.json"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger JSON: Pass" title="Click to visit: https://provider.myhelo.com/swagger.json" ></a></td>
    </tr>
    <tr>
      <td>streamline_healthcare_solutions</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://dhfhirpresentation.smartcarenet.com/fhir/volunteersofamericaofflorida/1942250303/r4"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://dhfhirpresentation.smartcarenet.com/fhir/volunteersofamericaofflorida/1942250303/r4" ></a></td>
      <td class="center-cell"><a href="https://dhfhirpresentation.smartcarenet.com/fhir/volunteersofamericaofflorida/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://dhfhirpresentation.smartcarenet.com/fhir/volunteersofamericaofflorida/metadata" ></a></td>
      <td class="center-cell"><a href="https://dhfhirpresentation.smartcarenet.com/fhir/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://dhfhirpresentation.smartcarenet.com/fhir/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><a href="https://dhfhirpresentation.smartcarenet.com/fhir/volunteersofamericaofflorida/api-docs"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI Docs: Pass" title="Click to visit: https://dhfhirpresentation.smartcarenet.com/fhir/volunteersofamericaofflorida/api-docs" ></a></td>
      <td class="center-cell"><a href="https://dhfhirpresentation.smartcarenet.com/fhir/volunteersofamericaofflorida/openapi.json"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI JSON: Pass" title="Click to visit: https://dhfhirpresentation.smartcarenet.com/fhir/volunteersofamericaofflorida/openapi.json" ></a></td>
      <td class="center-cell"><a href="https://dhfhirpresentation.smartcarenet.com/fhir/volunteersofamericaofflorida/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://dhfhirpresentation.smartcarenet.com/fhir/volunteersofamericaofflorida/swagger" ></a></td>
      <td class="center-cell"><a href="https://dhfhirpresentation.smartcarenet.com/fhir/volunteersofamericaofflorida/swagger.json"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger JSON: Pass" title="Click to visit: https://dhfhirpresentation.smartcarenet.com/fhir/volunteersofamericaofflorida/swagger.json" ></a></td>
    </tr>
    <tr>
      <td>teneleven_group</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://fhir.10e11.com/fhir/dhit/cca0001/r4"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir.10e11.com/fhir/dhit/cca0001/r4" ></a></td>
      <td class="center-cell"><a href="https://fhir.10e11.com/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhir.10e11.com/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhir.10e11.com/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhir.10e11.com/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><a href="https://fhir.10e11.com/api-docs"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI Docs: Pass" title="Click to visit: https://fhir.10e11.com/api-docs" ></a></td>
      <td class="center-cell"><a href="https://fhir.10e11.com/openapi.json"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI JSON: Pass" title="Click to visit: https://fhir.10e11.com/openapi.json" ></a></td>
      <td class="center-cell"><a href="https://fhir.10e11.com/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://fhir.10e11.com/swagger" ></a></td>
      <td class="center-cell"><a href="https://fhir.10e11.com/swagger.json"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger JSON: Pass" title="Click to visit: https://fhir.10e11.com/swagger.json" ></a></td>
    </tr>
    <tr>
      <td>triarq_practice_services</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://SIPC01-fhir.myqone.com/api/FHIR/R4/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://SIPC01-fhir.myqone.com/api/FHIR/R4/" ></a></td>
      <td class="center-cell"><a href="https://SIPC01-fhir.myqone.com/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://SIPC01-fhir.myqone.com/metadata" ></a></td>
      <td class="center-cell"><a href="https://SIPC01-fhir.myqone.com/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://SIPC01-fhir.myqone.com/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><a href="https://SIPC01-fhir.myqone.com/api-docs"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI Docs: Pass" title="Click to visit: https://SIPC01-fhir.myqone.com/api-docs" ></a></td>
      <td class="center-cell"><a href="https://SIPC01-fhir.myqone.com/openapi.json"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI JSON: Pass" title="Click to visit: https://SIPC01-fhir.myqone.com/openapi.json" ></a></td>
      <td class="center-cell"><a href="https://SIPC01-fhir.myqone.com/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://SIPC01-fhir.myqone.com/swagger" ></a></td>
      <td class="center-cell"><a href="https://SIPC01-fhir.myqone.com/swagger.json"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger JSON: Pass" title="Click to visit: https://SIPC01-fhir.myqone.com/swagger.json" ></a></td>
    </tr>
    <tr>
      <td>veradigm_2</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://fhir.fhirpoint.open.allscripts.com/fhirroute/open/10049550"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir.fhirpoint.open.allscripts.com/fhirroute/open/10049550" ></a></td>
      <td class="center-cell"><a href="https://fhirdev.fhirpointdev.open.allscripts.com/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhirdev.fhirpointdev.open.allscripts.com/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhirdev.fhirpointdev.open.allscripts.com/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhirdev.fhirpointdev.open.allscripts.com/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><a href="https://fhirdev.fhirpointdev.open.allscripts.com/api-docs"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI Docs: Pass" title="Click to visit: https://fhirdev.fhirpointdev.open.allscripts.com/api-docs" ></a></td>
      <td class="center-cell"><a href="https://fhirdev.fhirpointdev.open.allscripts.com/openapi.json"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI JSON: Pass" title="Click to visit: https://fhirdev.fhirpointdev.open.allscripts.com/openapi.json" ></a></td>
      <td class="center-cell"><a href="https://fhirdev.fhirpointdev.open.allscripts.com/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://fhirdev.fhirpointdev.open.allscripts.com/swagger" ></a></td>
      <td class="center-cell"><a href="https://fhirdev.fhirpointdev.open.allscripts.com/swagger.json"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger JSON: Pass" title="Click to visit: https://fhirdev.fhirpointdev.open.allscripts.com/swagger.json" ></a></td>
    </tr>
    <tr>
      <td>visionweb</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://dhpresentation.youruprise.com/fhir/ioc/4al9/r4"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://dhpresentation.youruprise.com/fhir/ioc/4al9/r4" ></a></td>
      <td class="center-cell"><a href="https://dhpresentation.youruprise.com/fhir/ioc/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://dhpresentation.youruprise.com/fhir/ioc/metadata" ></a></td>
      <td class="center-cell"><a href="https://dhpresentation.youruprise.com/fhir/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://dhpresentation.youruprise.com/fhir/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><a href="https://dhpresentation.youruprise.com/fhir/ioc/api-docs"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI Docs: Pass" title="Click to visit: https://dhpresentation.youruprise.com/fhir/ioc/api-docs" ></a></td>
      <td class="center-cell"><a href="https://dhpresentation.youruprise.com/fhir/ioc/openapi.json"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI JSON: Pass" title="Click to visit: https://dhpresentation.youruprise.com/fhir/ioc/openapi.json" ></a></td>
      <td class="center-cell"><a href="https://dhpresentation.youruprise.com/fhir/ioc/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://dhpresentation.youruprise.com/fhir/ioc/swagger" ></a></td>
      <td class="center-cell"><a href="https://dhpresentation.youruprise.com/fhir/ioc/swagger.json"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger JSON: Pass" title="Click to visit: https://dhpresentation.youruprise.com/fhir/ioc/swagger.json" ></a></td>
    </tr>
    <tr>
      <td>aarista_technology_llc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://emrfhirpresentation.aarista.com/fhir/aarista/neighborhoodphysicianspractice/r4"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://emrfhirpresentation.aarista.com/fhir/aarista/neighborhoodphysicianspractice/r4" ></a></td>
      <td class="center-cell"><a href="https://emrfhirpresentation.aarista.com/fhir/aarista/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://emrfhirpresentation.aarista.com/fhir/aarista/metadata" ></a></td>
      <td class="center-cell"><a href="https://emrfhirpresentation.aarista.com/fhir/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://emrfhirpresentation.aarista.com/fhir/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><a href="https://emrfhirpresentation.aarista.com/fhir/aarista/api-docs"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI Docs: Pass" title="Click to visit: https://emrfhirpresentation.aarista.com/fhir/aarista/api-docs" ></a></td>
      <td class="center-cell"><a href="https://emrfhirpresentation.aarista.com/fhir/aarista/openapi.json"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI JSON: Pass" title="Click to visit: https://emrfhirpresentation.aarista.com/fhir/aarista/openapi.json" ></a></td>
      <td class="center-cell"><a href="https://emrfhirpresentation.aarista.com/fhir/aarista/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://emrfhirpresentation.aarista.com/fhir/aarista/swagger" ></a></td>
      <td class="center-cell"><a href="https://emrfhirpresentation.aarista.com/fhir/aarista/swagger.json"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger JSON: Pass" title="Click to visit: https://emrfhirpresentation.aarista.com/fhir/aarista/swagger.json" ></a></td>
    </tr>
    <tr>
      <td>axxess</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://fhirpresentationdev.axxessweb.com/fhir/dhit/basepractice/r4"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhirpresentationdev.axxessweb.com/fhir/dhit/basepractice/r4" ></a></td>
      <td class="center-cell"><a href="https://fhirpresentationdev.axxessweb.com/fhir/dhit/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhirpresentationdev.axxessweb.com/fhir/dhit/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhirpresentationdev.axxessweb.com/fhir/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhirpresentationdev.axxessweb.com/fhir/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><a href="https://fhirpresentationdev.axxessweb.com/fhir/dhit/api-docs"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI Docs: Pass" title="Click to visit: https://fhirpresentationdev.axxessweb.com/fhir/dhit/api-docs" ></a></td>
      <td class="center-cell"><a href="https://fhirpresentationdev.axxessweb.com/fhir/dhit/openapi.json"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI JSON: Pass" title="Click to visit: https://fhirpresentationdev.axxessweb.com/fhir/dhit/openapi.json" ></a></td>
      <td class="center-cell"><a href="https://fhirpresentationdev.axxessweb.com/fhir/dhit/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://fhirpresentationdev.axxessweb.com/fhir/dhit/swagger" ></a></td>
      <td class="center-cell"><a href="https://fhirpresentationdev.axxessweb.com/fhir/dhit/swagger.json"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger JSON: Pass" title="Click to visit: https://fhirpresentationdev.axxessweb.com/fhir/dhit/swagger.json" ></a></td>
    </tr>
    <tr>
      <td>azalea_health</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://app.azaleahealth.com/fhir/R4/135243"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://app.azaleahealth.com/fhir/R4/135243" ></a></td>
      <td class="center-cell"><a href="https://app.azaleahealth.com/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://app.azaleahealth.com/metadata" ></a></td>
      <td class="center-cell"><a href="https://app.azaleahealth.com/fhir/R4/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://app.azaleahealth.com/fhir/R4/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><a href="https://app.azaleahealth.com/api-docs"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI Docs: Pass" title="Click to visit: https://app.azaleahealth.com/api-docs" ></a></td>
      <td class="center-cell"><a href="https://app.azaleahealth.com/openapi.json"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI JSON: Pass" title="Click to visit: https://app.azaleahealth.com/openapi.json" ></a></td>
      <td class="center-cell"><a href="https://app.azaleahealth.com/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://app.azaleahealth.com/swagger" ></a></td>
      <td class="center-cell"><a href="https://app.azaleahealth.com/swagger.json"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger JSON: Pass" title="Click to visit: https://app.azaleahealth.com/swagger.json" ></a></td>
    </tr>
    <tr>
      <td>azalea_health_3</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://chartmakerapi.sticomputer.com"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://chartmakerapi.sticomputer.com" ></a></td>
      <td class="center-cell"><a href="https://chartmakerapi.sticomputer.com/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://chartmakerapi.sticomputer.com/metadata" ></a></td>
      <td class="center-cell"><a href="https://chartmakerapi.sticomputer.com/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://chartmakerapi.sticomputer.com/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><a href="https://chartmakerapi.sticomputer.com/api-docs"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI Docs: Pass" title="Click to visit: https://chartmakerapi.sticomputer.com/api-docs" ></a></td>
      <td class="center-cell"><a href="https://chartmakerapi.sticomputer.com/openapi.json"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI JSON: Pass" title="Click to visit: https://chartmakerapi.sticomputer.com/openapi.json" ></a></td>
      <td class="center-cell"><a href="https://chartmakerapi.sticomputer.com/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://chartmakerapi.sticomputer.com/swagger" ></a></td>
      <td class="center-cell"><a href="https://chartmakerapi.sticomputer.com/swagger.json"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger JSON: Pass" title="Click to visit: https://chartmakerapi.sticomputer.com/swagger.json" ></a></td>
    </tr>
    <tr>
      <td>broadstreet_health_llc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://portal.arsanahealth.com/api/fhir"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://portal.arsanahealth.com/api/fhir" ></a></td>
      <td class="center-cell"><a href="https://portal.arsanahealth.com/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://portal.arsanahealth.com/metadata" ></a></td>
      <td class="center-cell"><a href="https://portal.arsanahealth.com/api/fhir/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://portal.arsanahealth.com/api/fhir/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><a href="https://portal.arsanahealth.com/api-docs"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI Docs: Pass" title="Click to visit: https://portal.arsanahealth.com/api-docs" ></a></td>
      <td class="center-cell"><a href="https://portal.arsanahealth.com/openapi.json"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI JSON: Pass" title="Click to visit: https://portal.arsanahealth.com/openapi.json" ></a></td>
      <td class="center-cell"><a href="https://portal.arsanahealth.com/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://portal.arsanahealth.com/swagger" ></a></td>
      <td class="center-cell"><a href="https://portal.arsanahealth.com/swagger.json"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger JSON: Pass" title="Click to visit: https://portal.arsanahealth.com/swagger.json" ></a></td>
    </tr>
    <tr>
      <td>compulink_healthcare_solutions</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://fhir.compulinkadvantage.com/13971/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir.compulinkadvantage.com/13971/" ></a></td>
      <td class="center-cell"><a href="https://fhir.compulinkadvantage.com/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhir.compulinkadvantage.com/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhir.compulinkadvantage.com/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhir.compulinkadvantage.com/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><a href="https://fhir.compulinkadvantage.com/api-docs"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI Docs: Pass" title="Click to visit: https://fhir.compulinkadvantage.com/api-docs" ></a></td>
      <td class="center-cell"><a href="https://fhir.compulinkadvantage.com/openapi.json"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI JSON: Pass" title="Click to visit: https://fhir.compulinkadvantage.com/openapi.json" ></a></td>
      <td class="center-cell"><a href="https://fhir.compulinkadvantage.com/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://fhir.compulinkadvantage.com/swagger" ></a></td>
      <td class="center-cell"><a href="https://fhir.compulinkadvantage.com/swagger.json"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger JSON: Pass" title="Click to visit: https://fhir.compulinkadvantage.com/swagger.json" ></a></td>
    </tr>
    <tr>
      <td>darena_solutions_llc_dba_darena_health</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://app.meldrx.com/api/fhir/rt_thetherapyvillage"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://app.meldrx.com/api/fhir/rt_thetherapyvillage" ></a></td>
      <td class="center-cell"><a href="https://app.meldrx.com/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://app.meldrx.com/metadata" ></a></td>
      <td class="center-cell"><a href="https://app.meldrx.com/api/fhir/rt_thetherapyvillage/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://app.meldrx.com/api/fhir/rt_thetherapyvillage/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><a href="https://app.meldrx.com/api-docs"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI Docs: Pass" title="Click to visit: https://app.meldrx.com/api-docs" ></a></td>
      <td class="center-cell"><a href="https://app.meldrx.com/openapi.json"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI JSON: Pass" title="Click to visit: https://app.meldrx.com/openapi.json" ></a></td>
      <td class="center-cell"><a href="https://app.meldrx.com/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://app.meldrx.com/swagger" ></a></td>
      <td class="center-cell"><a href="https://app.meldrx.com/swagger.json"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger JSON: Pass" title="Click to visit: https://app.meldrx.com/swagger.json" ></a></td>
    </tr>
    <tr>
      <td>lille_group_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://portal.escribe.com/ehr/api/fhir/metadata"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://portal.escribe.com/ehr/api/fhir/metadata" ></a></td>
      <td class="center-cell"><a href="https://portal.escribe.com/ehr/api/fhir/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://portal.escribe.com/ehr/api/fhir/metadata" ></a></td>
      <td class="center-cell"><a href="https://portal.escribe.com/ehr/api/fhir/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://portal.escribe.com/ehr/api/fhir/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><a href="https://portal.escribe.com/ehr/api/fhir/api-docs"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI Docs: Pass" title="Click to visit: https://portal.escribe.com/ehr/api/fhir/api-docs" ></a></td>
      <td class="center-cell"><a href="https://portal.escribe.com/ehr/api/fhir/metadata/openapi.json"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI JSON: Pass" title="Click to visit: https://portal.escribe.com/ehr/api/fhir/metadata/openapi.json" ></a></td>
      <td class="center-cell"><a href="https://portal.escribe.com/ehr/api/fhir/metadata/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://portal.escribe.com/ehr/api/fhir/metadata/swagger" ></a></td>
      <td class="center-cell"><a href="https://portal.escribe.com/ehr/api/fhir/metadata/swagger.json"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger JSON: Pass" title="Click to visit: https://portal.escribe.com/ehr/api/fhir/metadata/swagger.json" ></a></td>
    </tr>
    <tr>
      <td>medical_informatics_engineering</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://rustagi.webchartnow.com/webchart.cgi/fhir/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://rustagi.webchartnow.com/webchart.cgi/fhir/" ></a></td>
      <td class="center-cell"><a href="https://rustagi.webchartnow.com/webchart.cgi/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://rustagi.webchartnow.com/webchart.cgi/metadata" ></a></td>
      <td class="center-cell"><a href="https://rustagi.webchartnow.com/webchart.cgi/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://rustagi.webchartnow.com/webchart.cgi/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><a href="https://rustagi.webchartnow.com/webchart.cgi/api-docs"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI Docs: Pass" title="Click to visit: https://rustagi.webchartnow.com/webchart.cgi/api-docs" ></a></td>
      <td class="center-cell"><a href="https://rustagi.webchartnow.com/webchart.cgi/openapi.json"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI JSON: Pass" title="Click to visit: https://rustagi.webchartnow.com/webchart.cgi/openapi.json" ></a></td>
      <td class="center-cell"><a href="https://rustagi.webchartnow.com/webchart.cgi/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://rustagi.webchartnow.com/webchart.cgi/swagger" ></a></td>
      <td class="center-cell"><a href="https://rustagi.webchartnow.com/webchart.cgi/swagger.json"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger JSON: Pass" title="Click to visit: https://rustagi.webchartnow.com/webchart.cgi/swagger.json" ></a></td>
    </tr>
    <tr>
      <td>medicus_clinical_llc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://fhirpresentation.assertus.com/fhir/medicus/greatmed/r4"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhirpresentation.assertus.com/fhir/medicus/greatmed/r4" ></a></td>
      <td class="center-cell"><a href="https://fhirpresentation.assertus.com/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhirpresentation.assertus.com/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhirpresentation.assertus.com/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhirpresentation.assertus.com/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><a href="https://fhirpresentation.assertus.com/api-docs"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI Docs: Pass" title="Click to visit: https://fhirpresentation.assertus.com/api-docs" ></a></td>
      <td class="center-cell"><a href="https://fhirpresentation.assertus.com/openapi.json"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI JSON: Pass" title="Click to visit: https://fhirpresentation.assertus.com/openapi.json" ></a></td>
      <td class="center-cell"><a href="https://fhirpresentation.assertus.com/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://fhirpresentation.assertus.com/swagger" ></a></td>
      <td class="center-cell"><a href="https://fhirpresentation.assertus.com/swagger.json"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger JSON: Pass" title="Click to visit: https://fhirpresentation.assertus.com/swagger.json" ></a></td>
    </tr>
    <tr>
      <td>micromd_llc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://micromd.dynamicfhir.com/fhir/micromd/basepractice/r4"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://micromd.dynamicfhir.com/fhir/micromd/basepractice/r4" ></a></td>
      <td class="center-cell"><a href="https://micromd.dynamicfhir.com/fhir/micromd/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://micromd.dynamicfhir.com/fhir/micromd/metadata" ></a></td>
      <td class="center-cell"><a href="https://micromd.dynamicfhir.com/fhir/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://micromd.dynamicfhir.com/fhir/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><a href="https://micromd.dynamicfhir.com/fhir/micromd/api-docs"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI Docs: Pass" title="Click to visit: https://micromd.dynamicfhir.com/fhir/micromd/api-docs" ></a></td>
      <td class="center-cell"><a href="https://micromd.dynamicfhir.com/fhir/micromd/openapi.json"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI JSON: Pass" title="Click to visit: https://micromd.dynamicfhir.com/fhir/micromd/openapi.json" ></a></td>
      <td class="center-cell"><a href="https://micromd.dynamicfhir.com/fhir/micromd/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://micromd.dynamicfhir.com/fhir/micromd/swagger" ></a></td>
      <td class="center-cell"><a href="https://micromd.dynamicfhir.com/fhir/micromd/swagger.json"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger JSON: Pass" title="Click to visit: https://micromd.dynamicfhir.com/fhir/micromd/swagger.json" ></a></td>
    </tr>
    <tr>
      <td>nextech</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://api.intellechart.net/icp-fhir-api/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://api.intellechart.net/icp-fhir-api/" ></a></td>
      <td class="center-cell"><a href="https://api.intellechart.net/icp-fhir-api/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://api.intellechart.net/icp-fhir-api/metadata" ></a></td>
      <td class="center-cell"><a href="https://api.intellechart.net/icp-fhir-api/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://api.intellechart.net/icp-fhir-api/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><a href="https://api.intellechart.net/icp-fhir-api/api-docs"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI Docs: Pass" title="Click to visit: https://api.intellechart.net/icp-fhir-api/api-docs" ></a></td>
      <td class="center-cell"><a href="https://api.intellechart.net/icp-fhir-api/openapi.json"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI JSON: Pass" title="Click to visit: https://api.intellechart.net/icp-fhir-api/openapi.json" ></a></td>
      <td class="center-cell"><a href="https://api.intellechart.net/icp-fhir-api/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://api.intellechart.net/icp-fhir-api/swagger" ></a></td>
      <td class="center-cell"><a href="https://api.intellechart.net/icp-fhir-api/swagger.json"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger JSON: Pass" title="Click to visit: https://api.intellechart.net/icp-fhir-api/swagger.json" ></a></td>
    </tr>
    <tr>
      <td>office_ally_llc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://fhirpt.officeally.com/fhir/officeally/14234/r4"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhirpt.officeally.com/fhir/officeally/14234/r4" ></a></td>
      <td class="center-cell"><a href="https://fhirpt.officeally.com/fhir/officeally/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhirpt.officeally.com/fhir/officeally/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhirpt.officeally.com/fhir/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhirpt.officeally.com/fhir/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><a href="https://fhirpt.officeally.com/fhir/officeally/api-docs"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI Docs: Pass" title="Click to visit: https://fhirpt.officeally.com/fhir/officeally/api-docs" ></a></td>
      <td class="center-cell"><a href="https://fhirpt.officeally.com/fhir/officeally/openapi.json"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI JSON: Pass" title="Click to visit: https://fhirpt.officeally.com/fhir/officeally/openapi.json" ></a></td>
      <td class="center-cell"><a href="https://fhirpt.officeally.com/fhir/officeally/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://fhirpt.officeally.com/fhir/officeally/swagger" ></a></td>
      <td class="center-cell"><a href="https://fhirpt.officeally.com/fhir/officeally/swagger.json"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger JSON: Pass" title="Click to visit: https://fhirpt.officeally.com/fhir/officeally/swagger.json" ></a></td>
    </tr>
    <tr>
      <td>ot_emr_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://demo.onetouchemr.com/fhir/r4"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://demo.onetouchemr.com/fhir/r4" ></a></td>
      <td class="center-cell"><a href="https://demo.onetouchemr.com/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://demo.onetouchemr.com/metadata" ></a></td>
      <td class="center-cell"><a href="https://demo.onetouchemr.com/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://demo.onetouchemr.com/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><a href="https://demo.onetouchemr.com/api-docs"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI Docs: Pass" title="Click to visit: https://demo.onetouchemr.com/api-docs" ></a></td>
      <td class="center-cell"><a href="https://demo.onetouchemr.com/openapi.json"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI JSON: Pass" title="Click to visit: https://demo.onetouchemr.com/openapi.json" ></a></td>
      <td class="center-cell"><a href="https://demo.onetouchemr.com/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://demo.onetouchemr.com/swagger" ></a></td>
      <td class="center-cell"><a href="https://demo.onetouchemr.com/swagger.json"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger JSON: Pass" title="Click to visit: https://demo.onetouchemr.com/swagger.json" ></a></td>
    </tr>
    <tr>
      <td>pce_systems</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://w3.pcesecure.com/cgi-bin/WebObjects/HIEAdmin.woa/MUPIX/v2"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://w3.pcesecure.com/cgi-bin/WebObjects/HIEAdmin.woa/MUPIX/v2" ></a></td>
      <td class="center-cell"><a href="https://w3.pcesecure.com/cgi-bin/WebObjects/HIEAdmin.woa/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://w3.pcesecure.com/cgi-bin/WebObjects/HIEAdmin.woa/metadata" ></a></td>
      <td class="center-cell"><a href="https://w3.pcesecure.com/cgi-bin/WebObjects/HIEAdmin.woa/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://w3.pcesecure.com/cgi-bin/WebObjects/HIEAdmin.woa/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><a href="https://w3.pcesecure.com/cgi-bin/WebObjects/HIEAdmin.woa/api-docs"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI Docs: Pass" title="Click to visit: https://w3.pcesecure.com/cgi-bin/WebObjects/HIEAdmin.woa/api-docs" ></a></td>
      <td class="center-cell"><a href="https://w3.pcesecure.com/cgi-bin/WebObjects/HIEAdmin.woa/openapi.json"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI JSON: Pass" title="Click to visit: https://w3.pcesecure.com/cgi-bin/WebObjects/HIEAdmin.woa/openapi.json" ></a></td>
      <td class="center-cell"><a href="https://w3.pcesecure.com/cgi-bin/WebObjects/HIEAdmin.woa/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://w3.pcesecure.com/cgi-bin/WebObjects/HIEAdmin.woa/swagger" ></a></td>
      <td class="center-cell"><a href="https://w3.pcesecure.com/cgi-bin/WebObjects/HIEAdmin.woa/swagger.json"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger JSON: Pass" title="Click to visit: https://w3.pcesecure.com/cgi-bin/WebObjects/HIEAdmin.woa/swagger.json" ></a></td>
    </tr>
    <tr>
      <td>prime_clinical_systems</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://fhirpresentation.pcsdataxchg.com/fhir/dhit/basepractice/r4"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhirpresentation.pcsdataxchg.com/fhir/dhit/basepractice/r4" ></a></td>
      <td class="center-cell"><a href="https://fhirpresentation.pcsdataxchg.com/fhir/dhit/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhirpresentation.pcsdataxchg.com/fhir/dhit/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhirpresentation.pcsdataxchg.com/fhir/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhirpresentation.pcsdataxchg.com/fhir/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><a href="https://fhirpresentation.pcsdataxchg.com/fhir/dhit/api-docs"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI Docs: Pass" title="Click to visit: https://fhirpresentation.pcsdataxchg.com/fhir/dhit/api-docs" ></a></td>
      <td class="center-cell"><a href="https://fhirpresentation.pcsdataxchg.com/fhir/dhit/openapi.json"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI JSON: Pass" title="Click to visit: https://fhirpresentation.pcsdataxchg.com/fhir/dhit/openapi.json" ></a></td>
      <td class="center-cell"><a href="https://fhirpresentation.pcsdataxchg.com/fhir/dhit/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://fhirpresentation.pcsdataxchg.com/fhir/dhit/swagger" ></a></td>
      <td class="center-cell"><a href="https://fhirpresentation.pcsdataxchg.com/fhir/dhit/swagger.json"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger JSON: Pass" title="Click to visit: https://fhirpresentation.pcsdataxchg.com/fhir/dhit/swagger.json" ></a></td>
    </tr>
    <tr>
      <td>prime_clinical_systems_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://fhirpresentation.pcsdataxchg.com/fhir/dhit/basepractice/r4"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhirpresentation.pcsdataxchg.com/fhir/dhit/basepractice/r4" ></a></td>
      <td class="center-cell"><a href="https://fhirpresentation.pcsdataxchg.com/fhir/dhit/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhirpresentation.pcsdataxchg.com/fhir/dhit/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhirpresentation.pcsdataxchg.com/fhir/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhirpresentation.pcsdataxchg.com/fhir/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><a href="https://fhirpresentation.pcsdataxchg.com/fhir/dhit/api-docs"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI Docs: Pass" title="Click to visit: https://fhirpresentation.pcsdataxchg.com/fhir/dhit/api-docs" ></a></td>
      <td class="center-cell"><a href="https://fhirpresentation.pcsdataxchg.com/fhir/dhit/openapi.json"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI JSON: Pass" title="Click to visit: https://fhirpresentation.pcsdataxchg.com/fhir/dhit/openapi.json" ></a></td>
      <td class="center-cell"><a href="https://fhirpresentation.pcsdataxchg.com/fhir/dhit/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://fhirpresentation.pcsdataxchg.com/fhir/dhit/swagger" ></a></td>
      <td class="center-cell"><a href="https://fhirpresentation.pcsdataxchg.com/fhir/dhit/swagger.json"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger JSON: Pass" title="Click to visit: https://fhirpresentation.pcsdataxchg.com/fhir/dhit/swagger.json" ></a></td>
    </tr>
    <tr>
      <td>procentive</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://fhir.procentive.com/fhir/procentive/basepractice/r4"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir.procentive.com/fhir/procentive/basepractice/r4" ></a></td>
      <td class="center-cell"><a href="https://fhir.procentive.com/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhir.procentive.com/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhir.procentive.com/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhir.procentive.com/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><a href="https://fhir.procentive.com/api-docs"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI Docs: Pass" title="Click to visit: https://fhir.procentive.com/api-docs" ></a></td>
      <td class="center-cell"><a href="https://fhir.procentive.com/openapi.json"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI JSON: Pass" title="Click to visit: https://fhir.procentive.com/openapi.json" ></a></td>
      <td class="center-cell"><a href="https://fhir.procentive.com/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://fhir.procentive.com/swagger" ></a></td>
      <td class="center-cell"><a href="https://fhir.procentive.com/swagger.json"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger JSON: Pass" title="Click to visit: https://fhir.procentive.com/swagger.json" ></a></td>
    </tr>
    <tr>
      <td>qualifacts_systems_llc_4</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://fhir.insynchcs.com/insync/seniorconnections-200/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir.insynchcs.com/insync/seniorconnections-200/" ></a></td>
      <td class="center-cell"><a href="https://fhir.insynchcs.com/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhir.insynchcs.com/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhir.insynchcs.com/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhir.insynchcs.com/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><a href="https://fhir.insynchcs.com/api-docs"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI Docs: Pass" title="Click to visit: https://fhir.insynchcs.com/api-docs" ></a></td>
      <td class="center-cell"><a href="https://fhir.insynchcs.com/openapi.json"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI JSON: Pass" title="Click to visit: https://fhir.insynchcs.com/openapi.json" ></a></td>
      <td class="center-cell"><a href="https://fhir.insynchcs.com/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://fhir.insynchcs.com/swagger" ></a></td>
      <td class="center-cell"><a href="https://fhir.insynchcs.com/swagger.json"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger JSON: Pass" title="Click to visit: https://fhir.insynchcs.com/swagger.json" ></a></td>
    </tr>
    <tr>
      <td>radysans_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://ehr.cutecharts.com/radysans-webapi"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://ehr.cutecharts.com/radysans-webapi" ></a></td>
      <td class="center-cell"><a href="https://ehrwebapi.cutecharts.com/radywebapi/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://ehrwebapi.cutecharts.com/radywebapi/metadata" ></a></td>
      <td class="center-cell"><a href="https://ehrwebapi.cutecharts.com/radywebapi/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://ehrwebapi.cutecharts.com/radywebapi/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><a href="https://ehrwebapi.cutecharts.com/radywebapi/api-docs"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI Docs: Pass" title="Click to visit: https://ehrwebapi.cutecharts.com/radywebapi/api-docs" ></a></td>
      <td class="center-cell"><a href="https://ehrwebapi.cutecharts.com/radywebapi/openapi.json"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI JSON: Pass" title="Click to visit: https://ehrwebapi.cutecharts.com/radywebapi/openapi.json" ></a></td>
      <td class="center-cell"><a href="https://ehrwebapi.cutecharts.com/radywebapi/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://ehrwebapi.cutecharts.com/radywebapi/swagger" ></a></td>
      <td class="center-cell"><a href="https://ehrwebapi.cutecharts.com/radywebapi/swagger.json"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger JSON: Pass" title="Click to visit: https://ehrwebapi.cutecharts.com/radywebapi/swagger.json" ></a></td>
    </tr>
    <tr>
      <td>tebra_technologies_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://fhir.prd.cloud.tebra.com/fhir-request"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir.prd.cloud.tebra.com/fhir-request" ></a></td>
      <td class="center-cell"><a href="https://fhir.prd.cloud.tebra.com/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhir.prd.cloud.tebra.com/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhir.prd.cloud.tebra.com/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhir.prd.cloud.tebra.com/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><a href="https://fhir.prd.cloud.tebra.com/api-docs"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI Docs: Pass" title="Click to visit: https://fhir.prd.cloud.tebra.com/api-docs" ></a></td>
      <td class="center-cell"><a href="https://fhir.prd.cloud.tebra.com/openapi.json"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI JSON: Pass" title="Click to visit: https://fhir.prd.cloud.tebra.com/openapi.json" ></a></td>
      <td class="center-cell"><a href="https://fhir.prd.cloud.tebra.com/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://fhir.prd.cloud.tebra.com/swagger" ></a></td>
      <td class="center-cell"><a href="https://fhir.prd.cloud.tebra.com/swagger.json"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger JSON: Pass" title="Click to visit: https://fhir.prd.cloud.tebra.com/swagger.json" ></a></td>
    </tr>
    <tr>
      <td>tronshealth_llc_2</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://akpc.tronshealth.com/fhirv4.0"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://akpc.tronshealth.com/fhirv4.0" ></a></td>
      <td class="center-cell"><a href="https://akpc.tronshealth.com/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://akpc.tronshealth.com/metadata" ></a></td>
      <td class="center-cell"><a href="https://akpc.tronshealth.com/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://akpc.tronshealth.com/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><a href="https://akpc.tronshealth.com/api-docs"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI Docs: Pass" title="Click to visit: https://akpc.tronshealth.com/api-docs" ></a></td>
      <td class="center-cell"><a href="https://akpc.tronshealth.com/openapi.json"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI JSON: Pass" title="Click to visit: https://akpc.tronshealth.com/openapi.json" ></a></td>
      <td class="center-cell"><a href="https://akpc.tronshealth.com/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://akpc.tronshealth.com/swagger" ></a></td>
      <td class="center-cell"><a href="https://akpc.tronshealth.com/swagger.json"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger JSON: Pass" title="Click to visit: https://akpc.tronshealth.com/swagger.json" ></a></td>
    </tr>
    <tr>
      <td>varian_medical_systems</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://varian.dynamicfhir.com/fhir/varian/basepractice/r4"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://varian.dynamicfhir.com/fhir/varian/basepractice/r4" ></a></td>
      <td class="center-cell"><a href="https://varian.dynamicfhir.com/fhir/varian/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://varian.dynamicfhir.com/fhir/varian/metadata" ></a></td>
      <td class="center-cell"><a href="https://varian.dynamicfhir.com/fhir/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://varian.dynamicfhir.com/fhir/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><a href="https://varian.dynamicfhir.com/fhir/varian/api-docs"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI Docs: Pass" title="Click to visit: https://varian.dynamicfhir.com/fhir/varian/api-docs" ></a></td>
      <td class="center-cell"><a href="https://varian.dynamicfhir.com/fhir/varian/openapi.json"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI JSON: Pass" title="Click to visit: https://varian.dynamicfhir.com/fhir/varian/openapi.json" ></a></td>
      <td class="center-cell"><a href="https://varian.dynamicfhir.com/fhir/varian/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://varian.dynamicfhir.com/fhir/varian/swagger" ></a></td>
      <td class="center-cell"><a href="https://varian.dynamicfhir.com/fhir/varian/swagger.json"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger JSON: Pass" title="Click to visit: https://varian.dynamicfhir.com/fhir/varian/swagger.json" ></a></td>
    </tr>
    <tr>
      <td>welligent_part_of_the_continuumcloud</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://fhir.qa.welligent.com/fhir/alleghanycountypublicschools/99/r4"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir.qa.welligent.com/fhir/alleghanycountypublicschools/99/r4" ></a></td>
      <td class="center-cell"><a href="https://fhir.qa.welligent.com/fhir/alleghanycountypublicschools/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhir.qa.welligent.com/fhir/alleghanycountypublicschools/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhir.qa.welligent.com/fhir/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhir.qa.welligent.com/fhir/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><a href="https://fhir.qa.welligent.com/fhir/alleghanycountypublicschools/api-docs"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI Docs: Pass" title="Click to visit: https://fhir.qa.welligent.com/fhir/alleghanycountypublicschools/api-docs" ></a></td>
      <td class="center-cell"><a href="https://fhir.qa.welligent.com/fhir/alleghanycountypublicschools/openapi.json"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI JSON: Pass" title="Click to visit: https://fhir.qa.welligent.com/fhir/alleghanycountypublicschools/openapi.json" ></a></td>
      <td class="center-cell"><a href="https://fhir.qa.welligent.com/fhir/alleghanycountypublicschools/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://fhir.qa.welligent.com/fhir/alleghanycountypublicschools/swagger" ></a></td>
      <td class="center-cell"><a href="https://fhir.qa.welligent.com/fhir/alleghanycountypublicschools/swagger.json"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger JSON: Pass" title="Click to visit: https://fhir.qa.welligent.com/fhir/alleghanycountypublicschools/swagger.json" ></a></td>
    </tr>
    <tr>
      <td>carecloud_health_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://api-datamanager.carecloud.com:8081/api/fhir/R4/DCM"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://api-datamanager.carecloud.com:8081/api/fhir/R4/DCM" ></a></td>
      <td class="center-cell"><a href="https://api-datamanager.carecloud.com:8081/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://api-datamanager.carecloud.com:8081/metadata" ></a></td>
      <td class="center-cell"><a href="https://api-datamanager.carecloud.com:8081/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://api-datamanager.carecloud.com:8081/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><a href="https://api-datamanager.carecloud.com:8081/api-docs"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI Docs: Pass" title="Click to visit: https://api-datamanager.carecloud.com:8081/api-docs" ></a></td>
      <td class="center-cell"><a href="https://api-datamanager.carecloud.com:8081/openapi.json"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI JSON: Pass" title="Click to visit: https://api-datamanager.carecloud.com:8081/openapi.json" ></a></td>
      <td class="center-cell"><a href="https://api-datamanager.carecloud.com:8081/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://api-datamanager.carecloud.com:8081/swagger" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>carecloud_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://api-datamanager.carecloud.com:8081/api/fhir/R4/DCM"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://api-datamanager.carecloud.com:8081/api/fhir/R4/DCM" ></a></td>
      <td class="center-cell"><a href="https://api-datamanager.carecloud.com:8081/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://api-datamanager.carecloud.com:8081/metadata" ></a></td>
      <td class="center-cell"><a href="https://api-datamanager.carecloud.com:8081/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://api-datamanager.carecloud.com:8081/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><a href="https://api-datamanager.carecloud.com:8081/api-docs"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI Docs: Pass" title="Click to visit: https://api-datamanager.carecloud.com:8081/api-docs" ></a></td>
      <td class="center-cell"><a href="https://api-datamanager.carecloud.com:8081/openapi.json"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI JSON: Pass" title="Click to visit: https://api-datamanager.carecloud.com:8081/openapi.json" ></a></td>
      <td class="center-cell"><a href="https://api-datamanager.carecloud.com:8081/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://api-datamanager.carecloud.com:8081/swagger" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>epic_systems_corporation</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://epicsoap.stormontvail.org/FHIRproxy/HOME/api/FHIR/R4"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://epicsoap.stormontvail.org/FHIRproxy/HOME/api/FHIR/R4" ></a></td>
      <td class="center-cell"><a href="https://epicsoap.stormontvail.org/FHIRproxy/HOME/api/FHIR/R4/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://epicsoap.stormontvail.org/FHIRproxy/HOME/api/FHIR/R4/metadata" ></a></td>
      <td class="center-cell"><a href="https://epicsoap.stormontvail.org/FHIRproxy/HOME/api/FHIR/R4/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://epicsoap.stormontvail.org/FHIRproxy/HOME/api/FHIR/R4/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><a href="https://interconnect.carelonhealth.com/api-docs"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI Docs: Pass" title="Click to visit: https://interconnect.carelonhealth.com/api-docs" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><a href="https://interconnect.carelonhealth.com/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://interconnect.carelonhealth.com/swagger" ></a></td>
      <td class="center-cell"><a href="https://lmcrcs.lexmed.com/swagger.json"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger JSON: Pass" title="Click to visit: https://lmcrcs.lexmed.com/swagger.json" ></a></td>
    </tr>
    <tr>
      <td>meridian_medical_management</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://api-datamanager.carecloud.com:8081/api/fhir/R4/DCM"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://api-datamanager.carecloud.com:8081/api/fhir/R4/DCM" ></a></td>
      <td class="center-cell"><a href="https://api-datamanager.carecloud.com:8081/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://api-datamanager.carecloud.com:8081/metadata" ></a></td>
      <td class="center-cell"><a href="https://api-datamanager.carecloud.com:8081/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://api-datamanager.carecloud.com:8081/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><a href="https://api-datamanager.carecloud.com:8081/api-docs"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI Docs: Pass" title="Click to visit: https://api-datamanager.carecloud.com:8081/api-docs" ></a></td>
      <td class="center-cell"><a href="https://api-datamanager.carecloud.com:8081/openapi.json"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI JSON: Pass" title="Click to visit: https://api-datamanager.carecloud.com:8081/openapi.json" ></a></td>
      <td class="center-cell"><a href="https://api-datamanager.carecloud.com:8081/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://api-datamanager.carecloud.com:8081/swagger" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>the_echo_group</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://hamilton.echoehr.com/fhir/r4/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://hamilton.echoehr.com/fhir/r4/" ></a></td>
      <td class="center-cell"><a href="https://hamilton.echoehr.com/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://hamilton.echoehr.com/metadata" ></a></td>
      <td class="center-cell"><a href="https://hamilton.echoehr.com/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://hamilton.echoehr.com/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><a href="https://hamilton.echoehr.com/openapi.json"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI JSON: Pass" title="Click to visit: https://hamilton.echoehr.com/openapi.json" ></a></td>
      <td class="center-cell"><a href="https://hamilton.echoehr.com/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://hamilton.echoehr.com/swagger" ></a></td>
      <td class="center-cell"><a href="https://hamilton.echoehr.com/swagger.json"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger JSON: Pass" title="Click to visit: https://hamilton.echoehr.com/swagger.json" ></a></td>
    </tr>
    <tr>
      <td>adaptamed_llc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://ehrfhir.ehryourway.com/api/v1"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://ehrfhir.ehryourway.com/api/v1" ></a></td>
      <td class="center-cell"><a href="https://ehrfhir.ehryourway.com/api/v1/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://ehrfhir.ehryourway.com/api/v1/metadata" ></a></td>
      <td class="center-cell"><a href="https://ehrfhir.ehryourway.com/api/v1/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://ehrfhir.ehryourway.com/api/v1/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><a href="https://ehrfhir.ehryourway.com/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://ehrfhir.ehryourway.com/swagger" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>cybermed_health_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://api.cybermedehr.com/fhir/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://api.cybermedehr.com/fhir/" ></a></td>
      <td class="center-cell"><a href="https://api.cybermedehr.com/fhir/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://api.cybermedehr.com/fhir/metadata" ></a></td>
      <td class="center-cell"><a href="https://api.cybermedehr.com/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://api.cybermedehr.com/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><a href="https://api.cybermedehr.com/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://api.cybermedehr.com/swagger" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>digidms_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://fhir.digidms.com/fhir"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir.digidms.com/fhir" ></a></td>
      <td class="center-cell"><a href="https://fhir.digidms.com/fhir/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhir.digidms.com/fhir/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhir.digidms.com/fhir/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhir.digidms.com/fhir/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><a href="https://fhir.digidms.com/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://fhir.digidms.com/swagger" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>doctome_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://fhir.ethizo.com/api/4.0.0"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir.ethizo.com/api/4.0.0" ></a></td>
      <td class="center-cell"><a href="https://fhir.ethizo.com/api/4.0.0/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhir.ethizo.com/api/4.0.0/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhir.ethizo.com/api/4.0.0/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhir.ethizo.com/api/4.0.0/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><a href="https://fhir.ethizo.com/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://fhir.ethizo.com/swagger" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>genius_solutions_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://inferno.healthit.gov/suites/custom/service_base_url/examples/CapabilityStatement"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://inferno.healthit.gov/suites/custom/service_base_url/examples/CapabilityStatement" ></a></td>
      <td class="center-cell"><a href="https://inferno.healthit.gov/suites/custom/service_base_url/examples/CapabilityStatement/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://inferno.healthit.gov/suites/custom/service_base_url/examples/CapabilityStatement/metadata" ></a></td>
      <td class="center-cell"><a href="https://gsehrwebapi.geniussolutions.com/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://gsehrwebapi.geniussolutions.com/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><a href="https://gsehrwebapi.geniussolutions.com/api-docs"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI Docs: Pass" title="Click to visit: https://gsehrwebapi.geniussolutions.com/api-docs" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><a href="https://gsehrwebapi.geniussolutions.com/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://gsehrwebapi.geniussolutions.com/swagger" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>lunar_systems_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://fhir-usa.unify.chbase.com/org/salem-ae4e49e4"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir-usa.unify.chbase.com/org/salem-ae4e49e4" ></a></td>
      <td class="center-cell"><a href="https://fhir-usa.unify.chbase.com/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhir-usa.unify.chbase.com/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhir-usa.unify.chbase.com/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhir-usa.unify.chbase.com/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><a href="https://fhir-usa.unify.chbase.com/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://fhir-usa.unify.chbase.com/swagger" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>magilen_enterprises_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://inferno.healthit.gov/suites/custom/service_base_url/examples/CapabilityStatement"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://inferno.healthit.gov/suites/custom/service_base_url/examples/CapabilityStatement" ></a></td>
      <td class="center-cell"><a href="https://inferno.healthit.gov/suites/custom/service_base_url/examples/CapabilityStatement/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://inferno.healthit.gov/suites/custom/service_base_url/examples/CapabilityStatement/metadata" ></a></td>
      <td class="center-cell"><a href="https://gsehrwebapi.geniussolutions.com/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://gsehrwebapi.geniussolutions.com/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><a href="https://gsehrwebapi.geniussolutions.com/api-docs"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI Docs: Pass" title="Click to visit: https://gsehrwebapi.geniussolutions.com/api-docs" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><a href="https://gsehrwebapi.geniussolutions.com/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://gsehrwebapi.geniussolutions.com/swagger" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>maxremind_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://fhir.maximus.care/api/r4"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir.maximus.care/api/r4" ></a></td>
      <td class="center-cell"><a href="https://fhir.maximus.care/api/r4/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhir.maximus.care/api/r4/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhir.maximus.care/api/r4/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhir.maximus.care/api/r4/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><a href="https://fhir.maximus.care/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://fhir.maximus.care/swagger" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>medaz_net_llc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://fhirapi.mhealthaz.com"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhirapi.mhealthaz.com" ></a></td>
      <td class="center-cell"><a href="https://fhirapi.mhealthaz.com/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhirapi.mhealthaz.com/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhirapi.mhealthaz.com/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhirapi.mhealthaz.com/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><a href="https://fhirapi.mhealthaz.com/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://fhirapi.mhealthaz.com/swagger" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>medcare_mso</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://fhirapi.medcaremso.com/api/R4/21010"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhirapi.medcaremso.com/api/R4/21010" ></a></td>
      <td class="center-cell"><a href="https://fhirapi.medcaremso.com/api/R4/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhirapi.medcaremso.com/api/R4/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhirapi.medcaremso.com/api/R4/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhirapi.medcaremso.com/api/R4/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><a href="https://fhirapi.medcaremso.com/api/R4/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://fhirapi.medcaremso.com/api/R4/swagger" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>mendelson_kornblum_orthopedic_spine_specialists</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://fhir.mkoss.com/fhir"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir.mkoss.com/fhir" ></a></td>
      <td class="center-cell"><a href="https://fhir.mkoss.com/fhir/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhir.mkoss.com/fhir/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhir.mkoss.com/fhir/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhir.mkoss.com/fhir/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><a href="https://fhir.mkoss.com/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://fhir.mkoss.com/swagger" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>omnimd_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://hapi.omnimd.com/fhir"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://hapi.omnimd.com/fhir" ></a></td>
      <td class="center-cell"><a href="https://hapi.omnimd.com/fhir/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://hapi.omnimd.com/fhir/metadata" ></a></td>
      <td class="center-cell"><a href="https://hapi.omnimd.com/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://hapi.omnimd.com/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><a href="https://hapi.omnimd.com/fhir/api-docs"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI Docs: Pass" title="Click to visit: https://hapi.omnimd.com/fhir/api-docs" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>omnimd_inc_2</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://hapi.omnimd.com/fhir/CapabilityStatement"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://hapi.omnimd.com/fhir/CapabilityStatement" ></a></td>
      <td class="center-cell"><a href="https://hapi.omnimd.com/fhir/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://hapi.omnimd.com/fhir/metadata" ></a></td>
      <td class="center-cell"><a href="https://hapi.omnimd.com/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://hapi.omnimd.com/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><a href="https://hapi.omnimd.com/fhir/api-docs"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI Docs: Pass" title="Click to visit: https://hapi.omnimd.com/fhir/api-docs" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>openemr_foundation</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://wellness.shsinc.net/apis/default/fhir"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://wellness.shsinc.net/apis/default/fhir" ></a></td>
      <td class="center-cell"><a href="https://snf.shsinc.net/apis/default/fhir/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://snf.shsinc.net/apis/default/fhir/metadata" ></a></td>
      <td class="center-cell"><a href="https://wellness.shsinc.net/apis/default/fhir/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://wellness.shsinc.net/apis/default/fhir/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><a href="https://wellness.shsinc.net/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://wellness.shsinc.net/swagger" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>pcis_gold</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://portal.premierfamily.net/fhir"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://portal.premierfamily.net/fhir" ></a></td>
      <td class="center-cell"><a href="https://portal.premierfamily.net/fhir/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://portal.premierfamily.net/fhir/metadata" ></a></td>
      <td class="center-cell"><a href="https://portal.premierfamily.net/fhir/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://portal.premierfamily.net/fhir/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><a href="https://portal.premierfamily.net/fhir/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://portal.premierfamily.net/fhir/swagger" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>1life_healthcare_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://api.prod.1life.com/fhir/4.0"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://api.prod.1life.com/fhir/4.0" ></a></td>
      <td class="center-cell"><a href="https://api.prod.1life.com/fhir/4.0/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://api.prod.1life.com/fhir/4.0/metadata" ></a></td>
      <td class="center-cell"><a href="https://api.prod.1life.com/fhir/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://api.prod.1life.com/fhir/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>altera_digital_health_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://pma0fhir.ma0.hos.ahcentral.com/R4/open-R4/USCore6.1"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://pma0fhir.ma0.hos.ahcentral.com/R4/open-R4/USCore6.1" ></a></td>
      <td class="center-cell"><a href="https://myhealth.ecmc.edu/R4/open-R4/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://myhealth.ecmc.edu/R4/open-R4/metadata" ></a></td>
      <td class="center-cell"><a href="https://myhealth.ecmc.edu/R4/open-R4/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://myhealth.ecmc.edu/R4/open-R4/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>athenahealth_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://api.platform.athenahealth.com/13103/brand/1/csg/1/fhir/r4"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://api.platform.athenahealth.com/13103/brand/1/csg/1/fhir/r4" ></a></td>
      <td class="center-cell"><a href="https://api.platform.athenahealth.com/13103/brand/1/csg/1/fhir/r4/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://api.platform.athenahealth.com/13103/brand/1/csg/1/fhir/r4/metadata" ></a></td>
      <td class="center-cell"><a href="https://api.platform.athenahealth.com/13103/brand/1/csg/1/fhir/r4/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://api.platform.athenahealth.com/13103/brand/1/csg/1/fhir/r4/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>avon_health</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://trial.avonhealth.com/fhir"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://trial.avonhealth.com/fhir" ></a></td>
      <td class="center-cell"><a href="https://trial.avonhealth.com/fhir/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://trial.avonhealth.com/fhir/metadata" ></a></td>
      <td class="center-cell"><a href="https://trial.avonhealth.com/fhir/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://trial.avonhealth.com/fhir/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>carefluence</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://admin.carefluence.com/r4core/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://admin.carefluence.com/r4core/" ></a></td>
      <td class="center-cell"><a href="https://admin.carefluence.com/r4core/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://admin.carefluence.com/r4core/metadata" ></a></td>
      <td class="center-cell"><a href="https://admin.carefluence.com/r4core/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://admin.carefluence.com/r4core/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><a href="https://admin.carefluence.com/r4core/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://admin.carefluence.com/r4core/swagger" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>carepaths_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://developer.carepaths.com/stubblefield/api/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://developer.carepaths.com/stubblefield/api/" ></a></td>
      <td class="center-cell"><a href="https://developer.carepaths.com/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://developer.carepaths.com/metadata" ></a></td>
      <td class="center-cell"><a href="https://developer.carepaths.com/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://developer.carepaths.com/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>caretracker_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://ac-fhir.harrisambulatory.com/ac-1672/fhir/r4"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://ac-fhir.harrisambulatory.com/ac-1672/fhir/r4" ></a></td>
      <td class="center-cell"><a href="https://ac-fhir.harrisambulatory.com/ac-1672/fhir/r4/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://ac-fhir.harrisambulatory.com/ac-1672/fhir/r4/metadata" ></a></td>
      <td class="center-cell"><a href="https://ac-fhir.harrisambulatory.com/ac-1672/fhir/r4/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://ac-fhir.harrisambulatory.com/ac-1672/fhir/r4/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><a href="https://ac-fhir.harrisambulatory.com/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://ac-fhir.harrisambulatory.com/swagger" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>comtron_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://bill.medgenehr.com:7043/fhir/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://bill.medgenehr.com:7043/fhir/" ></a></td>
      <td class="center-cell"><a href="https://bill.medgenehr.com:7043/fhir/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://bill.medgenehr.com:7043/fhir/metadata" ></a></td>
      <td class="center-cell"><a href="https://bill.medgenehr.com:7043/fhir/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://bill.medgenehr.com:7043/fhir/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>curemd_com_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://fhirendpoint.curemd.net/fhir/CM144"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhirendpoint.curemd.net/fhir/CM144" ></a></td>
      <td class="center-cell"><a href="https://fhirendpoint.curemd.net/fhir/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhirendpoint.curemd.net/fhir/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhirendpoint.curemd.net/fhir/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhirendpoint.curemd.net/fhir/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>cursahealth_llc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://fhirapi.cursahealth.com/r4"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhirapi.cursahealth.com/r4" ></a></td>
      <td class="center-cell"><a href="https://fhirapi.cursahealth.com/r4/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhirapi.cursahealth.com/r4/metadata" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><a href="https://fhirapi.cursahealth.com/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://fhirapi.cursahealth.com/swagger" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>cyfluent</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://www.cyfluentphr.com/fhirapi/RClayton/r4/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://www.cyfluentphr.com/fhirapi/RClayton/r4/" ></a></td>
      <td class="center-cell"><a href="https://www.cyfluentphr.com/fhirapi/RClayton/r4/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://www.cyfluentphr.com/fhirapi/RClayton/r4/metadata" ></a></td>
      <td class="center-cell"><a href="https://www.cyfluentphr.com/fhirapi/RClayton/r4/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://www.cyfluentphr.com/fhirapi/RClayton/r4/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>doc_tor_com</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://pic-fhir.harrisambulatory.com/BERNSTEIN-1828/fhir/r4"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://pic-fhir.harrisambulatory.com/BERNSTEIN-1828/fhir/r4" ></a></td>
      <td class="center-cell"><a href="https://pic-fhir.harrisambulatory.com/BERNSTEIN-1828/fhir/r4/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://pic-fhir.harrisambulatory.com/BERNSTEIN-1828/fhir/r4/metadata" ></a></td>
      <td class="center-cell"><a href="https://pic-fhir.harrisambulatory.com/BERNSTEIN-1828/fhir/r4/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://pic-fhir.harrisambulatory.com/BERNSTEIN-1828/fhir/r4/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><a href="https://pic-fhir.harrisambulatory.com/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://pic-fhir.harrisambulatory.com/swagger" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>eclinicalworks_llc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://fhir4.eclinicalworks.com/fhir/r4/HBJEAA"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir4.eclinicalworks.com/fhir/r4/HBJEAA" ></a></td>
      <td class="center-cell"><a href="https://fhir4.eclinicalworks.com/fhir/r4/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhir4.eclinicalworks.com/fhir/r4/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhir4.eclinicalworks.com/fhir/r4/HBJEAA/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhir4.eclinicalworks.com/fhir/r4/HBJEAA/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><a href="https://fhir4.eclinicalworks.com/fhir/r4/api-docs"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI Docs: Pass" title="Click to visit: https://fhir4.eclinicalworks.com/fhir/r4/api-docs" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>eclinicalworks_llc_2</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://fhir4.eclinicalworks.com/fhir/r4/HBJEAA"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir4.eclinicalworks.com/fhir/r4/HBJEAA" ></a></td>
      <td class="center-cell"><a href="https://fhir4.eclinicalworks.com/fhir/r4/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhir4.eclinicalworks.com/fhir/r4/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhir4.eclinicalworks.com/fhir/r4/HBJEAA/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhir4.eclinicalworks.com/fhir/r4/HBJEAA/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><a href="https://fhir4.eclinicalworks.com/fhir/r4/api-docs"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI Docs: Pass" title="Click to visit: https://fhir4.eclinicalworks.com/fhir/r4/api-docs" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>edvak_technologies_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://fhir-dev.edvak.com/fhir"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir-dev.edvak.com/fhir" ></a></td>
      <td class="center-cell"><a href="https://fhir-dev.edvak.com/fhir/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhir-dev.edvak.com/fhir/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhir-dev.edvak.com/fhir/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhir-dev.edvak.com/fhir/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><a href="https://fhir-dev.edvak.com/fhir/api-docs"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI Docs: Pass" title="Click to visit: https://fhir-dev.edvak.com/fhir/api-docs" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>ehana</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://fhir.ehana.com:9443/fhirserver/fhir/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir.ehana.com:9443/fhirserver/fhir/" ></a></td>
      <td class="center-cell"><a href="https://fhir.ehana.com:9443/fhirserver/fhir/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhir.ehana.com:9443/fhirserver/fhir/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhir.ehana.com:9443/fhirserver/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhir.ehana.com:9443/fhirserver/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>ehnote_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://interop.ehnote.com/fhir/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://interop.ehnote.com/fhir/" ></a></td>
      <td class="center-cell"><a href="https://interop.ehnote.com/fhir/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://interop.ehnote.com/fhir/metadata" ></a></td>
      <td class="center-cell"><a href="https://interop.ehnote.com/fhir/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://interop.ehnote.com/fhir/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><a href="https://interop.ehnote.com/fhir/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://interop.ehnote.com/fhir/swagger" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>emedpractice_llc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://fhirbackup.emedpractice.com:8443/CapabilityStatement"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhirbackup.emedpractice.com:8443/CapabilityStatement" ></a></td>
      <td class="center-cell"><a href="https://fhirbackup.emedpractice.com:8443/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhirbackup.emedpractice.com:8443/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhirbackup.emedpractice.com:8443/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhirbackup.emedpractice.com:8443/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><a href="https://fhirbackup.emedpractice.com:8443/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://fhirbackup.emedpractice.com:8443/swagger" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>ensoftek_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://drc-india.drcloudemr.com/drcloud/apis/default/fhir"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://drc-india.drcloudemr.com/drcloud/apis/default/fhir" ></a></td>
      <td class="center-cell"><a href="https://drc-india.drcloudemr.com/drcloud/apis/default/fhir/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://drc-india.drcloudemr.com/drcloud/apis/default/fhir/metadata" ></a></td>
      <td class="center-cell"><a href="https://drc-india.drcloudemr.com/drcloud/apis/default/fhir/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://drc-india.drcloudemr.com/drcloud/apis/default/fhir/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><a href="https://drc-india.drcloudemr.com/drcloud/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://drc-india.drcloudemr.com/drcloud/swagger" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>ensoftek_inc_2</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://drc-india.drcloudemr.com/drcloud/apis/default/fhir"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://drc-india.drcloudemr.com/drcloud/apis/default/fhir" ></a></td>
      <td class="center-cell"><a href="https://drc-india.drcloudemr.com/drcloud/apis/default/fhir/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://drc-india.drcloudemr.com/drcloud/apis/default/fhir/metadata" ></a></td>
      <td class="center-cell"><a href="https://drc-india.drcloudemr.com/drcloud/apis/default/fhir/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://drc-india.drcloudemr.com/drcloud/apis/default/fhir/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><a href="https://drc-india.drcloudemr.com/drcloud/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://drc-india.drcloudemr.com/drcloud/swagger" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>eyefinity_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://7eeye.ef.prod.fhir.ema-api.com/fhir/r4/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://7eeye.ef.prod.fhir.ema-api.com/fhir/r4/" ></a></td>
      <td class="center-cell"><a href="https://7eeye.ef.prod.fhir.ema-api.com/fhir/r4/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://7eeye.ef.prod.fhir.ema-api.com/fhir/r4/metadata" ></a></td>
      <td class="center-cell"><a href="https://7eeye.ef.prod.fhir.ema-api.com/fhir/r4/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://7eeye.ef.prod.fhir.ema-api.com/fhir/r4/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>eyefinity_inc_2</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://7eeye.ef.prod.fhir.ema-api.com/fhir/r4/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://7eeye.ef.prod.fhir.ema-api.com/fhir/r4/" ></a></td>
      <td class="center-cell"><a href="https://7eeye.ef.prod.fhir.ema-api.com/fhir/r4/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://7eeye.ef.prod.fhir.ema-api.com/fhir/r4/metadata" ></a></td>
      <td class="center-cell"><a href="https://7eeye.ef.prod.fhir.ema-api.com/fhir/r4/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://7eeye.ef.prod.fhir.ema-api.com/fhir/r4/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>eyemd_emr_healthcare_systems_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://smartonfhir.myeyecarerecords.com/fhir/EYE227530"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://smartonfhir.myeyecarerecords.com/fhir/EYE227530" ></a></td>
      <td class="center-cell"><a href="https://smartonfhir.myeyecarerecords.com/fhir/EYE227530/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://smartonfhir.myeyecarerecords.com/fhir/EYE227530/metadata" ></a></td>
      <td class="center-cell"><a href="https://smartonfhir.myeyecarerecords.com/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://smartonfhir.myeyecarerecords.com/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>ezemrx_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://services.ezemrx.com/ezEMRx/api-server/r4"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://services.ezemrx.com/ezEMRx/api-server/r4" ></a></td>
      <td class="center-cell"><a href="https://services.ezemrx.com/ezEMRx/api-server/r4/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://services.ezemrx.com/ezEMRx/api-server/r4/metadata" ></a></td>
      <td class="center-cell"><a href="https://services.ezemrx.com/ezEMRx/api-server/r4/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://services.ezemrx.com/ezEMRx/api-server/r4/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>flatiron_health</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://fhir.prod.flatiron.io/fhir"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir.prod.flatiron.io/fhir" ></a></td>
      <td class="center-cell"><a href="https://fhir.prod.flatiron.io/fhir/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhir.prod.flatiron.io/fhir/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhir.prod.flatiron.io/fhir/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhir.prod.flatiron.io/fhir/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>geniusdoc_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://api.geniusdoc.com:4434/GDAPIData"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://api.geniusdoc.com:4434/GDAPIData" ></a></td>
      <td class="center-cell"><a href="https://api.geniusdoc.com:4434/GDAPIData/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://api.geniusdoc.com:4434/GDAPIData/metadata" ></a></td>
      <td class="center-cell"><a href="https://api.geniusdoc.com:4434/GDAPIData/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://api.geniusdoc.com:4434/GDAPIData/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>harris_caretracker_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://ct-fhir.harrisambulatory.com/ct-15240/fhir/r4"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://ct-fhir.harrisambulatory.com/ct-15240/fhir/r4" ></a></td>
      <td class="center-cell"><a href="https://ct-fhir.harrisambulatory.com/ct-15240/fhir/r4/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://ct-fhir.harrisambulatory.com/ct-15240/fhir/r4/metadata" ></a></td>
      <td class="center-cell"><a href="https://ct-fhir.harrisambulatory.com/ct-15240/fhir/r4/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://ct-fhir.harrisambulatory.com/ct-15240/fhir/r4/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><a href="https://ct-fhir.harrisambulatory.com/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://ct-fhir.harrisambulatory.com/swagger" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>healogics_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://sfp-g10fhirproxy.azurewebsites.net/fhir"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://sfp-g10fhirproxy.azurewebsites.net/fhir" ></a></td>
      <td class="center-cell"><a href="https://sfp-g10fhirproxy.azurewebsites.net/fhir/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://sfp-g10fhirproxy.azurewebsites.net/fhir/metadata" ></a></td>
      <td class="center-cell"><a href="https://sfp-g10fhirproxy.azurewebsites.net/fhir/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://sfp-g10fhirproxy.azurewebsites.net/fhir/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>infinx_solutions_llc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://fhir.healthtogo.me/fhir/r4/imed.bourque"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir.healthtogo.me/fhir/r4/imed.bourque" ></a></td>
      <td class="center-cell"><a href="https://sandbox-r4.interopengine.com/fhir/r4/imedemr/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://sandbox-r4.interopengine.com/fhir/r4/imedemr/metadata" ></a></td>
      <td class="center-cell"><a href="https://sandbox-r4.interopengine.com/fhir/r4/imedemr/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://sandbox-r4.interopengine.com/fhir/r4/imedemr/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>infinx_solutions_llc_2</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://fhir.healthtogo.me/fhir/r4/imed.bourque"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir.healthtogo.me/fhir/r4/imed.bourque" ></a></td>
      <td class="center-cell"><a href="https://sandbox-r4.interopengine.com/fhir/r4/imedemr/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://sandbox-r4.interopengine.com/fhir/r4/imedemr/metadata" ></a></td>
      <td class="center-cell"><a href="https://sandbox-r4.interopengine.com/fhir/r4/imedemr/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://sandbox-r4.interopengine.com/fhir/r4/imedemr/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>infor_med_medical_information_systems_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://inferno.healthit.gov/suites/custom/service_base_url/examples/CapabilityStatement"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://inferno.healthit.gov/suites/custom/service_base_url/examples/CapabilityStatement" ></a></td>
      <td class="center-cell"><a href="https://inferno.healthit.gov/suites/custom/service_base_url/examples/CapabilityStatement/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://inferno.healthit.gov/suites/custom/service_base_url/examples/CapabilityStatement/metadata" ></a></td>
      <td class="center-cell"><a href="https://wc.praxisclouds.net/Erika/api/v1/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://wc.praxisclouds.net/Erika/api/v1/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><a href="https://wc.praxisclouds.net/Erika/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://wc.praxisclouds.net/Erika/swagger" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>mckesson_specialty_health_technology_products_llc_ontada</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://g2fhir.mckesson.com/xfhir"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://g2fhir.mckesson.com/xfhir" ></a></td>
      <td class="center-cell"><a href="https://g2fhir.mckesson.com/xfhir/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://g2fhir.mckesson.com/xfhir/metadata" ></a></td>
      <td class="center-cell"><a href="https://g2fhir.mckesson.com/xfhir/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://g2fhir.mckesson.com/xfhir/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>mckesson_specialty_health_technology_products_llc_ontada_2</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://g2fhir.mckesson.com/xfhir"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://g2fhir.mckesson.com/xfhir" ></a></td>
      <td class="center-cell"><a href="https://g2fhir.mckesson.com/xfhir/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://g2fhir.mckesson.com/xfhir/metadata" ></a></td>
      <td class="center-cell"><a href="https://g2fhir.mckesson.com/xfhir/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://g2fhir.mckesson.com/xfhir/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>md_charts_llc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://fhir246.mraemr.com:9443/fhir-server/api/v4/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir246.mraemr.com:9443/fhir-server/api/v4/" ></a></td>
      <td class="center-cell"><a href="https://fhir246.mraemr.com:9443/fhir-server/api/v4/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhir246.mraemr.com:9443/fhir-server/api/v4/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhir246.mraemr.com:9443/fhir-server/api/v4/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhir246.mraemr.com:9443/fhir-server/api/v4/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>medhost</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://fhir.yourcareuniverse.net/tenant/3da9ca85-20c5-41a0-bdcd-1c72cbc6cce2"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir.yourcareuniverse.net/tenant/3da9ca85-20c5-41a0-bdcd-1c72cbc6cce2" ></a></td>
      <td class="center-cell"><a href="https://fhir.yourcareuniverse.net/tenant/3da9ca85-20c5-41a0-bdcd-1c72cbc6cce2/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhir.yourcareuniverse.net/tenant/3da9ca85-20c5-41a0-bdcd-1c72cbc6cce2/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhir.yourcareuniverse.net/tenant/3da9ca85-20c5-41a0-bdcd-1c72cbc6cce2/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhir.yourcareuniverse.net/tenant/3da9ca85-20c5-41a0-bdcd-1c72cbc6cce2/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>medical_office_force_llc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://mofapi.medicalofficeforce.co/fhir/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://mofapi.medicalofficeforce.co/fhir/" ></a></td>
      <td class="center-cell"><a href="https://mofapi.medicalofficeforce.co/fhir/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://mofapi.medicalofficeforce.co/fhir/metadata" ></a></td>
      <td class="center-cell"><a href="https://mofapi.medicalofficeforce.co/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://mofapi.medicalofficeforce.co/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>medplum</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://api.medplum.com/fhir/R4"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://api.medplum.com/fhir/R4" ></a></td>
      <td class="center-cell"><a href="https://api.medplum.com/fhir/R4/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://api.medplum.com/fhir/R4/metadata" ></a></td>
      <td class="center-cell"><a href="https://api.medplum.com/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://api.medplum.com/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><a href="https://api.medplum.com/openapi.json"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI JSON: Pass" title="Click to visit: https://api.medplum.com/openapi.json" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>modernizing_medicine_gastroenterology_llc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://42e1cc73-f4ce-48dd-9d77-c5b7e0b6359b.gastro.prod.fhir.ema-api.com/fhir/r4/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://42e1cc73-f4ce-48dd-9d77-c5b7e0b6359b.gastro.prod.fhir.ema-api.com/fhir/r4/" ></a></td>
      <td class="center-cell"><a href="https://42e1cc73-f4ce-48dd-9d77-c5b7e0b6359b.gastro.prod.fhir.ema-api.com/fhir/r4/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://42e1cc73-f4ce-48dd-9d77-c5b7e0b6359b.gastro.prod.fhir.ema-api.com/fhir/r4/metadata" ></a></td>
      <td class="center-cell"><a href="https://42e1cc73-f4ce-48dd-9d77-c5b7e0b6359b.gastro.prod.fhir.ema-api.com/fhir/r4/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://42e1cc73-f4ce-48dd-9d77-c5b7e0b6359b.gastro.prod.fhir.ema-api.com/fhir/r4/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>modernizing_medicine_gastroenterology_llc_2</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://42e1cc73-f4ce-48dd-9d77-c5b7e0b6359b.gastro.prod.fhir.ema-api.com/fhir/r4/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://42e1cc73-f4ce-48dd-9d77-c5b7e0b6359b.gastro.prod.fhir.ema-api.com/fhir/r4/" ></a></td>
      <td class="center-cell"><a href="https://42e1cc73-f4ce-48dd-9d77-c5b7e0b6359b.gastro.prod.fhir.ema-api.com/fhir/r4/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://42e1cc73-f4ce-48dd-9d77-c5b7e0b6359b.gastro.prod.fhir.ema-api.com/fhir/r4/metadata" ></a></td>
      <td class="center-cell"><a href="https://42e1cc73-f4ce-48dd-9d77-c5b7e0b6359b.gastro.prod.fhir.ema-api.com/fhir/r4/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://42e1cc73-f4ce-48dd-9d77-c5b7e0b6359b.gastro.prod.fhir.ema-api.com/fhir/r4/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>modernizing_medicine_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://42e1cc73-f4ce-48dd-9d77-c5b7e0b6359b.gastro.prod.fhir.ema-api.com/fhir/r4/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://42e1cc73-f4ce-48dd-9d77-c5b7e0b6359b.gastro.prod.fhir.ema-api.com/fhir/r4/" ></a></td>
      <td class="center-cell"><a href="https://42e1cc73-f4ce-48dd-9d77-c5b7e0b6359b.gastro.prod.fhir.ema-api.com/fhir/r4/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://42e1cc73-f4ce-48dd-9d77-c5b7e0b6359b.gastro.prod.fhir.ema-api.com/fhir/r4/metadata" ></a></td>
      <td class="center-cell"><a href="https://42e1cc73-f4ce-48dd-9d77-c5b7e0b6359b.gastro.prod.fhir.ema-api.com/fhir/r4/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://42e1cc73-f4ce-48dd-9d77-c5b7e0b6359b.gastro.prod.fhir.ema-api.com/fhir/r4/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>modernizing_medicine_inc_2</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://42e1cc73-f4ce-48dd-9d77-c5b7e0b6359b.gastro.prod.fhir.ema-api.com/fhir/r4/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://42e1cc73-f4ce-48dd-9d77-c5b7e0b6359b.gastro.prod.fhir.ema-api.com/fhir/r4/" ></a></td>
      <td class="center-cell"><a href="https://42e1cc73-f4ce-48dd-9d77-c5b7e0b6359b.gastro.prod.fhir.ema-api.com/fhir/r4/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://42e1cc73-f4ce-48dd-9d77-c5b7e0b6359b.gastro.prod.fhir.ema-api.com/fhir/r4/metadata" ></a></td>
      <td class="center-cell"><a href="https://42e1cc73-f4ce-48dd-9d77-c5b7e0b6359b.gastro.prod.fhir.ema-api.com/fhir/r4/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://42e1cc73-f4ce-48dd-9d77-c5b7e0b6359b.gastro.prod.fhir.ema-api.com/fhir/r4/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>modernizing_medicine_inc_3</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://7eeye.ef.prod.fhir.ema-api.com/fhir/r4/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://7eeye.ef.prod.fhir.ema-api.com/fhir/r4/" ></a></td>
      <td class="center-cell"><a href="https://7eeye.ef.prod.fhir.ema-api.com/fhir/r4/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://7eeye.ef.prod.fhir.ema-api.com/fhir/r4/metadata" ></a></td>
      <td class="center-cell"><a href="https://7eeye.ef.prod.fhir.ema-api.com/fhir/r4/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://7eeye.ef.prod.fhir.ema-api.com/fhir/r4/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>modulemd</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://mmdpcf.modulemd.com/cf.fhir.r4/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://mmdpcf.modulemd.com/cf.fhir.r4/" ></a></td>
      <td class="center-cell"><a href="https://mmdpcf.modulemd.com/cf.fhir.r4/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://mmdpcf.modulemd.com/cf.fhir.r4/metadata" ></a></td>
      <td class="center-cell"><a href="https://mmdpcf.modulemd.com/cf.fhir.r4/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://mmdpcf.modulemd.com/cf.fhir.r4/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><a href="https://mmdpcf.modulemd.com/cf.fhir.r4/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://mmdpcf.modulemd.com/cf.fhir.r4/swagger" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>net_health</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://sfp-fhirprod.azurewebsites.net/fhir"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://sfp-fhirprod.azurewebsites.net/fhir" ></a></td>
      <td class="center-cell"><a href="https://sfp-fhirprod.azurewebsites.net/fhir/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://sfp-fhirprod.azurewebsites.net/fhir/metadata" ></a></td>
      <td class="center-cell"><a href="https://sfp-fhirprod.azurewebsites.net/fhir/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://sfp-fhirprod.azurewebsites.net/fhir/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>nextgen_healthcare</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://fhir.meditouchehr.com/api/fhir/r4"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir.meditouchehr.com/api/fhir/r4" ></a></td>
      <td class="center-cell"><a href="https://fhir.meditouchehr.com/api/fhir/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhir.meditouchehr.com/api/fhir/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhir.meditouchehr.com/api/fhir/r4/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhir.meditouchehr.com/api/fhir/r4/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>nextgen_healthcare_2</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://fhir.nextgen.com/nge/prod/fhir-api-r4/fhir/r4"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir.nextgen.com/nge/prod/fhir-api-r4/fhir/r4" ></a></td>
      <td class="center-cell"><a href="https://fhir.nextgen.com/nge/prod/fhir-api-r4/fhir/r4/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhir.nextgen.com/nge/prod/fhir-api-r4/fhir/r4/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhir.nextgen.com/nge/prod/fhir-api-r4/fhir/r4/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhir.nextgen.com/nge/prod/fhir-api-r4/fhir/r4/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>oracle_health</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://fhir-myrecord.cerner.com/r4/e60dd76f-2355-47fe-85cf-f04cc40e0a16/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir-myrecord.cerner.com/r4/e60dd76f-2355-47fe-85cf-f04cc40e0a16/" ></a></td>
      <td class="center-cell"><a href="https://fhir-myrecord.cerner.com/r4/e60dd76f-2355-47fe-85cf-f04cc40e0a16/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhir-myrecord.cerner.com/r4/e60dd76f-2355-47fe-85cf-f04cc40e0a16/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhir-myrecord.cerner.com/r4/e60dd76f-2355-47fe-85cf-f04cc40e0a16/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhir-myrecord.cerner.com/r4/e60dd76f-2355-47fe-85cf-f04cc40e0a16/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>patagonia_health</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://fhir.phemr.co:9443/fhirserver/fhir/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir.phemr.co:9443/fhirserver/fhir/" ></a></td>
      <td class="center-cell"><a href="https://fhir.phemr.co:9443/fhirserver/fhir/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhir.phemr.co:9443/fhirserver/fhir/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhir.phemr.co:9443/fhirserver/fhir/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhir.phemr.co:9443/fhirserver/fhir/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>patagonia_health_2</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://fhir.phemr.co:9443/fhirserver/fhir/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir.phemr.co:9443/fhirserver/fhir/" ></a></td>
      <td class="center-cell"><a href="https://fhir.phemr.co:9443/fhirserver/fhir/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhir.phemr.co:9443/fhirserver/fhir/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhir.phemr.co:9443/fhirserver/fhir/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhir.phemr.co:9443/fhirserver/fhir/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>physicians_emr_llc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://inferno.healthit.gov/suites/custom/service_base_url/examples/CapabilityStatement"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://inferno.healthit.gov/suites/custom/service_base_url/examples/CapabilityStatement" ></a></td>
      <td class="center-cell"><a href="https://inferno.healthit.gov/suites/custom/service_base_url/examples/CapabilityStatement/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://inferno.healthit.gov/suites/custom/service_base_url/examples/CapabilityStatement/metadata" ></a></td>
      <td class="center-cell"><a href="https://staging.pemr.com:93/api/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://staging.pemr.com:93/api/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>practice_ehr_llc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://fhir.practiceehr.com/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir.practiceehr.com/" ></a></td>
      <td class="center-cell"><a href="https://fhir.practiceehr.com/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhir.practiceehr.com/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhir.practiceehr.com/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhir.practiceehr.com/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><a href="https://fhir.practiceehr.com/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://fhir.practiceehr.com/swagger" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>practice_fusion</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://api.practicefusion.com/fhir/r4/v1/a64282f1-16e5-4731-a991-449745eeafc0"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://api.practicefusion.com/fhir/r4/v1/a64282f1-16e5-4731-a991-449745eeafc0" ></a></td>
      <td class="center-cell"><a href="https://api.practicefusion.com/fhir/r4/v1/a64282f1-16e5-4731-a991-449745eeafc0/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://api.practicefusion.com/fhir/r4/v1/a64282f1-16e5-4731-a991-449745eeafc0/metadata" ></a></td>
      <td class="center-cell"><a href="https://api.practicefusion.com/fhir/r4/v1/a64282f1-16e5-4731-a991-449745eeafc0/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://api.practicefusion.com/fhir/r4/v1/a64282f1-16e5-4731-a991-449745eeafc0/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>practicesuite_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://fhir.practicesuite.com:9443/fhirserver/fhir/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir.practicesuite.com:9443/fhirserver/fhir/" ></a></td>
      <td class="center-cell"><a href="https://fhir.practicesuite.com:9443/fhirserver/fhir/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhir.practicesuite.com:9443/fhirserver/fhir/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhir.practicesuite.com:9443/fhirserver/fhir/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhir.practicesuite.com:9443/fhirserver/fhir/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>prime_dataq_health_llc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://fhirservr4health-fhirdata.fhir.azurehealthcareapis.com"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhirservr4health-fhirdata.fhir.azurehealthcareapis.com" ></a></td>
      <td class="center-cell"><a href="https://fhirservr4health-fhirdata.fhir.azurehealthcareapis.com/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhirservr4health-fhirdata.fhir.azurehealthcareapis.com/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhirservr4health-fhirdata.fhir.azurehealthcareapis.com/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhirservr4health-fhirdata.fhir.azurehealthcareapis.com/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>pulse_systems_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://pul-fhir.harrisambulatory.com/PUL-120012/fhir/r4"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://pul-fhir.harrisambulatory.com/PUL-120012/fhir/r4" ></a></td>
      <td class="center-cell"><a href="https://pul-fhir.harrisambulatory.com/PUL-120012/fhir/r4/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://pul-fhir.harrisambulatory.com/PUL-120012/fhir/r4/metadata" ></a></td>
      <td class="center-cell"><a href="https://pul-fhir.harrisambulatory.com/PUL-120012/fhir/r4/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://pul-fhir.harrisambulatory.com/PUL-120012/fhir/r4/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><a href="https://pul-fhir.harrisambulatory.com/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://pul-fhir.harrisambulatory.com/swagger" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>qualifacts_systems_llc_3</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://fhir.qualifacts.org/insync/compliance2025-500243/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir.qualifacts.org/insync/compliance2025-500243/" ></a></td>
      <td class="center-cell"><a href="https://fhir.qualifacts.org/insync/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhir.qualifacts.org/insync/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhir.qualifacts.org/insync/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhir.qualifacts.org/insync/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><a href="https://fhir.qualifacts.org/insync/api-docs"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI Docs: Pass" title="Click to visit: https://fhir.qualifacts.org/insync/api-docs" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>retinex_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://retinexhealth-fhirdata.fhir.azurehealthcareapis.com"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://retinexhealth-fhirdata.fhir.azurehealthcareapis.com" ></a></td>
      <td class="center-cell"><a href="https://retinexhealth-fhirdata.fhir.azurehealthcareapis.com/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://retinexhealth-fhirdata.fhir.azurehealthcareapis.com/metadata" ></a></td>
      <td class="center-cell"><a href="https://retinexhealth-fhirdata.fhir.azurehealthcareapis.com/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://retinexhealth-fhirdata.fhir.azurehealthcareapis.com/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>solidpractice_technologies_llc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://prominis-fhir.solidpractice.com"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://prominis-fhir.solidpractice.com" ></a></td>
      <td class="center-cell"><a href="https://prominis-fhir.solidpractice.com/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://prominis-fhir.solidpractice.com/metadata" ></a></td>
      <td class="center-cell"><a href="https://prominis-fhir.solidpractice.com/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://prominis-fhir.solidpractice.com/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>streamlinemd_llc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://patientportal.streamlinemd.com/FHIRServer/FHIR"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://patientportal.streamlinemd.com/FHIRServer/FHIR" ></a></td>
      <td class="center-cell"><a href="https://patientportal.streamlinemd.com/FHIRServer/FHIR/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://patientportal.streamlinemd.com/FHIRServer/FHIR/metadata" ></a></td>
      <td class="center-cell"><a href="https://patientportal.streamlinemd.com/FHIRServer/FHIR/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://patientportal.streamlinemd.com/FHIRServer/FHIR/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><a href="https://patientportal.streamlinemd.com/FHIRServer/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://patientportal.streamlinemd.com/FHIRServer/swagger" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>theoria_medical_pllc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://theoriamedical-api.charteasy.com/fhir"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://theoriamedical-api.charteasy.com/fhir" ></a></td>
      <td class="center-cell"><a href="https://theoriamedical-api.charteasy.com/fhir/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://theoriamedical-api.charteasy.com/fhir/metadata" ></a></td>
      <td class="center-cell"><a href="https://theoriamedical-api.charteasy.com/fhir/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://theoriamedical-api.charteasy.com/fhir/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>trimed_technologies</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://fhir.trimed.cloud/fhir/r4"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir.trimed.cloud/fhir/r4" ></a></td>
      <td class="center-cell"><a href="https://fhir.trimed.cloud/fhir/r4/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhir.trimed.cloud/fhir/r4/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhir.trimed.cloud/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhir.trimed.cloud/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><a href="https://fhir.trimed.cloud/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://fhir.trimed.cloud/swagger" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>trimed_technologies_2</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://fhir.trimed.cloud"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir.trimed.cloud" ></a></td>
      <td class="center-cell"><a href="https://fhir.trimed.cloud/fhir/r4/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhir.trimed.cloud/fhir/r4/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhir.trimed.cloud/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhir.trimed.cloud/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><a href="https://fhir.trimed.cloud/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://fhir.trimed.cloud/swagger" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>trubridge_inc_2</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://fhir-usa.unify.chbase.com/org/salem-ae4e49e4"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir-usa.unify.chbase.com/org/salem-ae4e49e4" ></a></td>
      <td class="center-cell"><a href="https://fhir-usa.unify.chbase.com/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhir-usa.unify.chbase.com/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhir-usa.unify.chbase.com/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhir-usa.unify.chbase.com/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><a href="https://fhir-usa.unify.chbase.com/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://fhir-usa.unify.chbase.com/swagger" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>unity_health</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://dev-fhir.cinch-project.com/fhir"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://dev-fhir.cinch-project.com/fhir" ></a></td>
      <td class="center-cell"><a href="https://dev-fhir.cinch-project.com/fhir/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://dev-fhir.cinch-project.com/fhir/metadata" ></a></td>
      <td class="center-cell"><a href="https://dev-fhir.cinch-project.com/fhir/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://dev-fhir.cinch-project.com/fhir/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><a href="https://dev-fhir.cinch-project.com/fhir/api-docs"><img src="./icons/green_fire_openapi.200.png" alt="Findable OpenAPI Docs: Pass" title="Click to visit: https://dev-fhir.cinch-project.com/fhir/api-docs" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>us_monitoring_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://qafhir.usmon.com:9443/fhirserver/fhir/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://qafhir.usmon.com:9443/fhirserver/fhir/" ></a></td>
      <td class="center-cell"><a href="https://qafhir.usmon.com:9443/fhirserver/fhir/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://qafhir.usmon.com:9443/fhirserver/fhir/metadata" ></a></td>
      <td class="center-cell"><a href="https://qafhir.usmon.com:9443/fhirserver/fhir/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://qafhir.usmon.com:9443/fhirserver/fhir/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>veradigm</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://api.veradigmview.com/fhir/r4/v1/2f6b41e6-77d8-41c4-bf48-cad5cdd36494"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://api.veradigmview.com/fhir/r4/v1/2f6b41e6-77d8-41c4-bf48-cad5cdd36494" ></a></td>
      <td class="center-cell"><a href="https://api.veradigmview.com/fhir/r4/v1/2f6b41e6-77d8-41c4-bf48-cad5cdd36494/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://api.veradigmview.com/fhir/r4/v1/2f6b41e6-77d8-41c4-bf48-cad5cdd36494/metadata" ></a></td>
      <td class="center-cell"><a href="https://api.veradigmview.com/fhir/r4/v1/2f6b41e6-77d8-41c4-bf48-cad5cdd36494/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://api.veradigmview.com/fhir/r4/v1/2f6b41e6-77d8-41c4-bf48-cad5cdd36494/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>vohra_wound_physicians_management_llc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://fhir.vohrawoundteam.com:8443/fhir-server/api/v4"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir.vohrawoundteam.com:8443/fhir-server/api/v4" ></a></td>
      <td class="center-cell"><a href="https://fhir.vohrawoundteam.com:8443/fhir-server/api/v4/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhir.vohrawoundteam.com:8443/fhir-server/api/v4/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhir.vohrawoundteam.com:8443/fhir-server/api/v4/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhir.vohrawoundteam.com:8443/fhir-server/api/v4/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>wrs_health</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://fhir-server.sam.wrs.dev/r4"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir-server.sam.wrs.dev/r4" ></a></td>
      <td class="center-cell"><a href="https://fhir-server.sam.wrs.dev/r4/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhir-server.sam.wrs.dev/r4/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhir-server.sam.wrs.dev/r4/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhir-server.sam.wrs.dev/r4/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>advancedmd</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://providerapi.advancedmd.com/v1/r4/52625"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://providerapi.advancedmd.com/v1/r4/52625" ></a></td>
      <td class="center-cell"><a href="https://providerapi.advancedmd.com/v1/r4/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://providerapi.advancedmd.com/v1/r4/metadata" ></a></td>
      <td class="center-cell"><a href="https://providerapi.advancedmd.com/v1/r4/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://providerapi.advancedmd.com/v1/r4/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>agilon_health_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://product.mphrx.com/minerva/fhir/r4/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://product.mphrx.com/minerva/fhir/r4/" ></a></td>
      <td class="center-cell"><a href="https://product.mphrx.com/minerva/fhir/r4/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://product.mphrx.com/minerva/fhir/r4/metadata" ></a></td>
      <td class="center-cell"><a href="https://product.mphrx.com/minerva/fhir/r4/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://product.mphrx.com/minerva/fhir/r4/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>allegiancemd_software_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://fhir.allegiancemd.io/R4"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir.allegiancemd.io/R4" ></a></td>
      <td class="center-cell"><a href="https://fhir.allegiancemd.io/R4/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhir.allegiancemd.io/R4/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhir.allegiancemd.io/R4/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhir.allegiancemd.io/R4/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>applied_research_works_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://fhir.cozeva.com/4_0_0"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir.cozeva.com/4_0_0" ></a></td>
      <td class="center-cell"><a href="https://fhir.cozeva.com/4_0_0/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhir.cozeva.com/4_0_0/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhir.cozeva.com/4_0_0/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhir.cozeva.com/4_0_0/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>asp_md_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://fhirapi.asp.md:3030/aspmd/fhirserver/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhirapi.asp.md:3030/aspmd/fhirserver/" ></a></td>
      <td class="center-cell"><a href="https://fhirapi.asp.md:3030/aspmd/fhirserver/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhirapi.asp.md:3030/aspmd/fhirserver/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhirapi.asp.md:3030/aspmd/fhirserver/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhirapi.asp.md:3030/aspmd/fhirserver/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>astronaut_llc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://fhir.astronautehr.com:9443/fhirserver/fhir/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir.astronautehr.com:9443/fhirserver/fhir/" ></a></td>
      <td class="center-cell"><a href="https://fhir.astronautehr.com:9443/fhirserver/fhir/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhir.astronautehr.com:9443/fhirserver/fhir/metadata" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>azalea_health_2</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://api.azaleahealth.com/fhir/R4/hanover-hospital"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://api.azaleahealth.com/fhir/R4/hanover-hospital" ></a></td>
      <td class="center-cell"><a href="https://api.azaleahealth.com/fhir/R4/hanover-hospital/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://api.azaleahealth.com/fhir/R4/hanover-hospital/metadata" ></a></td>
      <td class="center-cell"><a href="https://api.azaleahealth.com/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://api.azaleahealth.com/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>benchmark_systems</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://springer.mdnavigatorclinical.com/prognocis/fhir/springer"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://springer.mdnavigatorclinical.com/prognocis/fhir/springer" ></a></td>
      <td class="center-cell"><a href="https://springer.mdnavigatorclinical.com/prognocis/fhir/springer/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://springer.mdnavigatorclinical.com/prognocis/fhir/springer/metadata" ></a></td>
      <td class="center-cell"><a href="https://springer.mdnavigatorclinical.com/prognocis/fhir/springer/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://springer.mdnavigatorclinical.com/prognocis/fhir/springer/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>bizmatics_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://isa.prognocis.com/prognocis/fhir/isa"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://isa.prognocis.com/prognocis/fhir/isa" ></a></td>
      <td class="center-cell"><a href="https://isa.prognocis.com/prognocis/fhir/isa/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://isa.prognocis.com/prognocis/fhir/isa/metadata" ></a></td>
      <td class="center-cell"><a href="https://isa.prognocis.com/prognocis/fhir/isa/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://isa.prognocis.com/prognocis/fhir/isa/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>bridge_patient_portal_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="HTTPS ORG URL: Fail" title="HTTPS ORG URL: Fail" ></td>
      <td class="center-cell"><a href="http://bpp.api.prod.bridgepatientportal.com/fhir/r4/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: http://bpp.api.prod.bridgepatientportal.com/fhir/r4/metadata" ></a></td>
      <td class="center-cell"><a href="http://bpp.api.prod.bridgepatientportal.com/fhir/r4/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: http://bpp.api.prod.bridgepatientportal.com/fhir/r4/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>bridge_patient_portal_inc_2</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="HTTPS ORG URL: Fail" title="HTTPS ORG URL: Fail" ></td>
      <td class="center-cell"><a href="http://bpp.api.prod.bridgepatientportal.com/fhir/r4/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: http://bpp.api.prod.bridgepatientportal.com/fhir/r4/metadata" ></a></td>
      <td class="center-cell"><a href="http://bpp.api.prod.bridgepatientportal.com/fhir/r4/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: http://bpp.api.prod.bridgepatientportal.com/fhir/r4/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>canvas_medical_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://fumage-stepwellcare.canvasmedical.com"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fumage-stepwellcare.canvasmedical.com" ></a></td>
      <td class="center-cell"><a href="https://fumage-iconhealth.canvasmedical.com/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fumage-iconhealth.canvasmedical.com/metadata" ></a></td>
      <td class="center-cell"><a href="https://fumage-iconhealth.canvasmedical.com/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fumage-iconhealth.canvasmedical.com/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>carbon_health_technologies_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://api-gateway.production.awscarbonhealth.com/hapi-fhir/fhir"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://api-gateway.production.awscarbonhealth.com/hapi-fhir/fhir" ></a></td>
      <td class="center-cell"><a href="https://api-gateway.production.awscarbonhealth.com/hapi-fhir/fhir/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://api-gateway.production.awscarbonhealth.com/hapi-fhir/fhir/metadata" ></a></td>
      <td class="center-cell"><a href="https://api-gateway.production.awscarbonhealth.com/hapi-fhir/fhir/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://api-gateway.production.awscarbonhealth.com/hapi-fhir/fhir/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>careexpand_llc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://auth-api.dev.careexpandcloud.com/fhir"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://auth-api.dev.careexpandcloud.com/fhir" ></a></td>
      <td class="center-cell"><a href="https://auth-api.dev.careexpandcloud.com/fhir/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://auth-api.dev.careexpandcloud.com/fhir/metadata" ></a></td>
      <td class="center-cell"><a href="https://auth-api.dev.careexpandcloud.com/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://auth-api.dev.careexpandcloud.com/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>dox_emr</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://doxpodfhir-prod-cus-app01.azurewebsites.net/api/Endpoint/1104"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://doxpodfhir-prod-cus-app01.azurewebsites.net/api/Endpoint/1104" ></a></td>
      <td class="center-cell"><a href="https://doxpodfhir-prod-cus-app01.azurewebsites.net/api/Endpoint/1104/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://doxpodfhir-prod-cus-app01.azurewebsites.net/api/Endpoint/1104/metadata" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><a href="https://doxpodfhir-prod-cus-app01.azurewebsites.net/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://doxpodfhir-prod-cus-app01.azurewebsites.net/swagger" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>e_healthline_com_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="HTTPS ORG URL: Fail" title="HTTPS ORG URL: Fail" ></td>
      <td class="center-cell"><a href="http://bpp.api.prod.bridgepatientportal.com/fhir/r4/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: http://bpp.api.prod.bridgepatientportal.com/fhir/r4/metadata" ></a></td>
      <td class="center-cell"><a href="http://bpp.api.prod.bridgepatientportal.com/fhir/r4/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: http://bpp.api.prod.bridgepatientportal.com/fhir/r4/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>firely_usa_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://secure.server.fire.ly/r4"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://secure.server.fire.ly/r4" ></a></td>
      <td class="center-cell"><a href="https://secure.server.fire.ly/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://secure.server.fire.ly/metadata" ></a></td>
      <td class="center-cell"><a href="https://secure.server.fire.ly/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://secure.server.fire.ly/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>foothold_technology_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://fhir.footholdtechnology.com/demodb"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir.footholdtechnology.com/demodb" ></a></td>
      <td class="center-cell"><a href="https://fhir.footholdtechnology.com/demodb/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhir.footholdtechnology.com/demodb/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhir.footholdtechnology.com/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhir.footholdtechnology.com/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>genensys_llc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://fhir.genensys.com/fhir"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir.genensys.com/fhir" ></a></td>
      <td class="center-cell"><a href="https://fhir.genensys.com/fhir/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhir.genensys.com/fhir/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhir.genensys.com/fhir/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhir.genensys.com/fhir/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>glenwood_systems_llc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://fhir.glaceemr.com/fhir_base_r4/fhir/primecare"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir.glaceemr.com/fhir_base_r4/fhir/primecare" ></a></td>
      <td class="center-cell"><a href="https://fhir.glaceemr.com/fhir_base_r4/fhir/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhir.glaceemr.com/fhir_base_r4/fhir/metadata" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>greenway_health_llc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://fhir-api.fhirprod.aws.greenwayhealth.com/fhir/R4/2.16.840.1.113883.3.140.71186"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir-api.fhirprod.aws.greenwayhealth.com/fhir/R4/2.16.840.1.113883.3.140.71186" ></a></td>
      <td class="center-cell"><a href="https://fhir-api.fhirprod.aws.greenwayhealth.com/fhir/R4/2.16.840.1.113883.3.140.71186/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhir-api.fhirprod.aws.greenwayhealth.com/fhir/R4/2.16.840.1.113883.3.140.71186/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhir-api.fhirprod.aws.greenwayhealth.com/fhir/R4/2.16.840.1.113883.3.140.71186/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhir-api.fhirprod.aws.greenwayhealth.com/fhir/R4/2.16.840.1.113883.3.140.71186/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>hcrcm_llc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://fhir.imperiumsoft.biz:8443/fhir"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir.imperiumsoft.biz:8443/fhir" ></a></td>
      <td class="center-cell"><a href="https://fhir.imperiumsoft.biz:8443/fhir/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhir.imperiumsoft.biz:8443/fhir/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhir.imperiumsoft.biz:8443/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhir.imperiumsoft.biz:8443/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>health_care_systems_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://hcswebportal.corporate.hcsinc.net/HCSClinicals_FHIR/api"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://hcswebportal.corporate.hcsinc.net/HCSClinicals_FHIR/api" ></a></td>
      <td class="center-cell"><a href="https://hcswebportal.corporate.hcsinc.net/HCSClinicals_FHIR/api/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://hcswebportal.corporate.hcsinc.net/HCSClinicals_FHIR/api/metadata" ></a></td>
      <td class="center-cell"><a href="https://hcswebportal.corporate.hcsinc.net/HCSClinicals_FHIR/api/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://hcswebportal.corporate.hcsinc.net/HCSClinicals_FHIR/api/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>health_samurai_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://smartbox.aidbox.app/tenant/cinic-one/patient/smart-api"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://smartbox.aidbox.app/tenant/cinic-one/patient/smart-api" ></a></td>
      <td class="center-cell"><a href="https://smartbox.aidbox.app/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://smartbox.aidbox.app/metadata" ></a></td>
      <td class="center-cell"><a href="https://smartbox.aidbox.app/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://smartbox.aidbox.app/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>healthie</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://app-70202.on-aptible.com/tenant/example-tenant/patient/smart-api"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://app-70202.on-aptible.com/tenant/example-tenant/patient/smart-api" ></a></td>
      <td class="center-cell"><a href="https://app-70202.on-aptible.com/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://app-70202.on-aptible.com/metadata" ></a></td>
      <td class="center-cell"><a href="https://app-70202.on-aptible.com/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://app-70202.on-aptible.com/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>helixbeat</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://fusion.helixbeat.com/fhir/R4"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fusion.helixbeat.com/fhir/R4" ></a></td>
      <td class="center-cell"><a href="https://fusion.helixbeat.com/fhir/R4/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fusion.helixbeat.com/fhir/R4/metadata" ></a></td>
      <td class="center-cell"><a href="https://fusion.helixbeat.com/fhir/R4/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fusion.helixbeat.com/fhir/R4/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>inmediata_health_group_llc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://www.secureemrplus.com/prognocis/fhir/neurocirugiadrlameiro"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://www.secureemrplus.com/prognocis/fhir/neurocirugiadrlameiro" ></a></td>
      <td class="center-cell"><a href="https://www.secureemrplus.com/prognocis/fhir/neurocirugiadrlameiro/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://www.secureemrplus.com/prognocis/fhir/neurocirugiadrlameiro/metadata" ></a></td>
      <td class="center-cell"><a href="https://www.secureemrplus.com/prognocis/fhir/neurocirugiadrlameiro/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://www.secureemrplus.com/prognocis/fhir/neurocirugiadrlameiro/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>inpracsys</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://sfp-proxy23604.azurewebsites.net/fhir"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://sfp-proxy23604.azurewebsites.net/fhir" ></a></td>
      <td class="center-cell"><a href="https://sfp-proxy23604.azurewebsites.net/fhir/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://sfp-proxy23604.azurewebsites.net/fhir/metadata" ></a></td>
      <td class="center-cell"><a href="https://sfp-proxy23604.azurewebsites.net/fhir/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://sfp-proxy23604.azurewebsites.net/fhir/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>intelichart_llc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://fhirapi.intelichart.com"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhirapi.intelichart.com" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><a href="https://fhirapi.intelichart.com/swagger"><img src="./icons/green_fire_swagger.200.png" alt="Findable Swagger: Pass" title="Click to visit: https://fhirapi.intelichart.com/swagger" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>magilen_enterprises_inc_2</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://inferno.healthit.gov/suites/custom/service_base_url/examples/CapabilityStatement"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://inferno.healthit.gov/suites/custom/service_base_url/examples/CapabilityStatement" ></a></td>
      <td class="center-cell"><a href="https://inferno.healthit.gov/suites/custom/service_base_url/examples/CapabilityStatement/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://inferno.healthit.gov/suites/custom/service_base_url/examples/CapabilityStatement/metadata" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>masslight</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://fhir-api.zapehr.com/r4"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir-api.zapehr.com/r4" ></a></td>
      <td class="center-cell"><a href="https://fhir-api.zapehr.com/r4/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhir-api.zapehr.com/r4/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhir-api.zapehr.com/r4/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhir-api.zapehr.com/r4/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>md_synergy_solutions_llc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://altheafhir.mdsynergy.com"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://altheafhir.mdsynergy.com" ></a></td>
      <td class="center-cell"><a href="https://altheafhir.mdsynergy.com/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://altheafhir.mdsynergy.com/metadata" ></a></td>
      <td class="center-cell"><a href="https://altheafhir.mdsynergy.com/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://altheafhir.mdsynergy.com/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>mdofficemanager</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://sandbox-r4.interopengine.com/fhir/r4/mdofficemanager"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://sandbox-r4.interopengine.com/fhir/r4/mdofficemanager" ></a></td>
      <td class="center-cell"><a href="https://sandbox-r4.interopengine.com/fhir/r4/imedemr/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://sandbox-r4.interopengine.com/fhir/r4/imedemr/metadata" ></a></td>
      <td class="center-cell"><a href="https://sandbox-r4.interopengine.com/fhir/r4/imedemr/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://sandbox-r4.interopengine.com/fhir/r4/imedemr/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>medent_community_computer_service_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://fhir.medent.com/fhir/R4/S8ck95b9"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir.medent.com/fhir/R4/S8ck95b9" ></a></td>
      <td class="center-cell"><a href="https://fhir.medent.com/fhir/R4/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhir.medent.com/fhir/R4/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhir.medent.com/fhir/R4/S8ck95b9/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhir.medent.com/fhir/R4/S8ck95b9/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>medical_information_technology_inc_meditech</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://mtrestapis-live01.trinity-health.org:443/v1/uscore/R4"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://mtrestapis-live01.trinity-health.org:443/v1/uscore/R4" ></a></td>
      <td class="center-cell"><a href="https://myrghapi.meditech.global:443/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://myrghapi.meditech.global:443/metadata" ></a></td>
      <td class="center-cell"><a href="https://myrghapi.meditech.global:443/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://myrghapi.meditech.global:443/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>medicalmine_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://ehr.charmtracker.com/api/ehr/v2/fhir/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://ehr.charmtracker.com/api/ehr/v2/fhir/" ></a></td>
      <td class="center-cell"><a href="https://ehr.charmtracker.com/api/ehr/v2/fhir/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://ehr.charmtracker.com/api/ehr/v2/fhir/metadata" ></a></td>
      <td class="center-cell"><a href="https://ehr.charmtracker.com/api/ehr/v2/fhir/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://ehr.charmtracker.com/api/ehr/v2/fhir/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>metasolutions_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://fhir.zoommd.com/drbnarayanan/r4/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir.zoommd.com/drbnarayanan/r4/" ></a></td>
      <td class="center-cell"><a href="https://fhir.zoommd.com/drbnarayanan/r4/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhir.zoommd.com/drbnarayanan/r4/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhir.zoommd.com/drbnarayanan/r4/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhir.zoommd.com/drbnarayanan/r4/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>navigating_cancer_llc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://api-portal.navigatingcare.com/tenant/texasoncology/patient/smart-api"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://api-portal.navigatingcare.com/tenant/texasoncology/patient/smart-api" ></a></td>
      <td class="center-cell"><a href="https://api-portal.navigatingcare.com/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://api-portal.navigatingcare.com/metadata" ></a></td>
      <td class="center-cell"><a href="https://api-portal.navigatingcare.com/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://api-portal.navigatingcare.com/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>navigating_cancer_llc_2</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://api-portal.navigatingcare.com/tenant/12/patient/smart-api"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://api-portal.navigatingcare.com/tenant/12/patient/smart-api" ></a></td>
      <td class="center-cell"><a href="https://api-portal.navigatingcare.com/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://api-portal.navigatingcare.com/metadata" ></a></td>
      <td class="center-cell"><a href="https://api-portal.navigatingcare.com/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://api-portal.navigatingcare.com/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>netsmart_technologies</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://fhir.netsmartcloud.com/provider/system-access/v2/ab41574f-0eb2-499d-ae49-5a4e6f763fc9"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir.netsmartcloud.com/provider/system-access/v2/ab41574f-0eb2-499d-ae49-5a4e6f763fc9" ></a></td>
      <td class="center-cell"><a href="https://fhir.netsmartcloud.com/provider/system-access/v2/ab41574f-0eb2-499d-ae49-5a4e6f763fc9/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhir.netsmartcloud.com/provider/system-access/v2/ab41574f-0eb2-499d-ae49-5a4e6f763fc9/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhir.netsmartcloud.com/provider/system-access/v2/ab41574f-0eb2-499d-ae49-5a4e6f763fc9/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhir.netsmartcloud.com/provider/system-access/v2/ab41574f-0eb2-499d-ae49-5a4e6f763fc9/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>nextech_2</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://select.nextech-api.com/api/r4"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://select.nextech-api.com/api/r4" ></a></td>
      <td class="center-cell"><a href="https://select.nextech-api.com/api/r4/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://select.nextech-api.com/api/r4/metadata" ></a></td>
      <td class="center-cell"><a href="https://select.nextech-api.com/api/r4/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://select.nextech-api.com/api/r4/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>novomedici_llc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://api.novoclinical.com/fhir"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://api.novoclinical.com/fhir" ></a></td>
      <td class="center-cell"><a href="https://api.novoclinical.com/fhir/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://api.novoclinical.com/fhir/metadata" ></a></td>
      <td class="center-cell"><a href="https://api.novoclinical.com/fhir/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://api.novoclinical.com/fhir/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>nth_technologies_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://galvon.nthtechnology.com/api/fhir.php/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://galvon.nthtechnology.com/api/fhir.php/" ></a></td>
      <td class="center-cell"><a href="https://galvon.nthtechnology.com/api/fhir.php/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://galvon.nthtechnology.com/api/fhir.php/metadata" ></a></td>
      <td class="center-cell"><a href="https://galvon.nthtechnology.com/api/fhir.php/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://galvon.nthtechnology.com/api/fhir.php/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>qualifacts_systems_llc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://AZVL.fhir.cbh4.crediblebh.com/R4/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://AZVL.fhir.cbh4.crediblebh.com/R4/" ></a></td>
      <td class="center-cell"><a href="https://AZVL.fhir.cbh4.crediblebh.com/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://AZVL.fhir.cbh4.crediblebh.com/metadata" ></a></td>
      <td class="center-cell"><a href="https://AZVL.fhir.cbh4.crediblebh.com/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://AZVL.fhir.cbh4.crediblebh.com/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>qualifacts_systems_llc_2</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://api.qualifacts.org/api/fhir/sheltercare/r4/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://api.qualifacts.org/api/fhir/sheltercare/r4/" ></a></td>
      <td class="center-cell"><a href="https://api.qualifacts.org/api/fhir/sheltercare/r4/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://api.qualifacts.org/api/fhir/sheltercare/r4/metadata" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>sai_systems_digital_llc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://pacehrapi2.azurewebsites.net/fhir"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://pacehrapi2.azurewebsites.net/fhir" ></a></td>
      <td class="center-cell"><a href="https://pacehrapi2.azurewebsites.net/fhir/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://pacehrapi2.azurewebsites.net/fhir/metadata" ></a></td>
      <td class="center-cell"><a href="https://pacehrapi2.azurewebsites.net/fhir/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://pacehrapi2.azurewebsites.net/fhir/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>saisystems_international</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://pacehrapi2.azurewebsites.net/fhir"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://pacehrapi2.azurewebsites.net/fhir" ></a></td>
      <td class="center-cell"><a href="https://pacehrapi2.azurewebsites.net/fhir/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://pacehrapi2.azurewebsites.net/fhir/metadata" ></a></td>
      <td class="center-cell"><a href="https://pacehrapi2.azurewebsites.net/fhir/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://pacehrapi2.azurewebsites.net/fhir/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>sevocity_a_division_of_conceptual_mindworks_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://api.sevocity.com/api/patients/v1/SEVGAP"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://api.sevocity.com/api/patients/v1/SEVGAP" ></a></td>
      <td class="center-cell"><a href="https://api.sevocity.com/api/patients/v1/SEVGAP/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://api.sevocity.com/api/patients/v1/SEVGAP/metadata" ></a></td>
      <td class="center-cell"><a href="https://api.sevocity.com/api/patients/v1/SEVGAP/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://api.sevocity.com/api/patients/v1/SEVGAP/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>softbir_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://fhir-dev.cloudmd365.com/api/v1/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir-dev.cloudmd365.com/api/v1/" ></a></td>
      <td class="center-cell"><a href="https://fhir-dev.cloudmd365.com/api/v1/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://fhir-dev.cloudmd365.com/api/v1/metadata" ></a></td>
      <td class="center-cell"><a href="https://fhir-dev.cloudmd365.com/api/v1/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhir-dev.cloudmd365.com/api/v1/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>systemedx_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://webservices2.systemedx.com/xnet/api/fhir"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://webservices2.systemedx.com/xnet/api/fhir" ></a></td>
      <td class="center-cell"><a href="https://webservices2.systemedx.com/xnet/api/fhir/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://webservices2.systemedx.com/xnet/api/fhir/metadata" ></a></td>
      <td class="center-cell"><a href="https://webservices2.systemedx.com/xnet/api/fhir/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://webservices2.systemedx.com/xnet/api/fhir/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>tenzing_medical_llc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="HTTPS ORG URL: Fail" title="HTTPS ORG URL: Fail" ></td>
      <td class="center-cell"><a href="http://tenzing.api.prod.bridgepatientportal.com/fhir/r4/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: http://tenzing.api.prod.bridgepatientportal.com/fhir/r4/metadata" ></a></td>
      <td class="center-cell"><a href="http://tenzing.api.prod.bridgepatientportal.com/fhir/r4/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: http://tenzing.api.prod.bridgepatientportal.com/fhir/r4/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>trubridge_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://thrive-gw.cpsi-cloud.com/api/smart/mcphers/id-osfac.14b747e9-3c6b-4361-ad09-a5d2d36d764d/fhir/r4"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://thrive-gw.cpsi-cloud.com/api/smart/mcphers/id-osfac.14b747e9-3c6b-4361-ad09-a5d2d36d764d/fhir/r4" ></a></td>
      <td class="center-cell"><a href="https://thrive-gw.cpsi-cloud.com/api/smart/mcphers/id-osfac.14b747e9-3c6b-4361-ad09-a5d2d36d764d/fhir/r4/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://thrive-gw.cpsi-cloud.com/api/smart/mcphers/id-osfac.14b747e9-3c6b-4361-ad09-a5d2d36d764d/fhir/r4/metadata" ></a></td>
      <td class="center-cell"><a href="https://thrive-gw.cpsi-cloud.com/api/smart/mcphers/id-osfac.14b747e9-3c6b-4361-ad09-a5d2d36d764d/fhir/r4/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://thrive-gw.cpsi-cloud.com/api/smart/mcphers/id-osfac.14b747e9-3c6b-4361-ad09-a5d2d36d764d/fhir/r4/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>vipa_health_solutions_llc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://inferno.healthit.gov/reference-server/r4"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://inferno.healthit.gov/reference-server/r4" ></a></td>
      <td class="center-cell"><a href="https://inferno.healthit.gov/suites/custom/service_base_url/examples/CapabilityStatement/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://inferno.healthit.gov/suites/custom/service_base_url/examples/CapabilityStatement/metadata" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>webedoctor_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://fhir.webedoctor.com:9443/fhir-server/api/v4/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir.webedoctor.com:9443/fhir-server/api/v4/" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><a href="https://fhir.webedoctor.com:9443/fhir-server/api/v4/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhir.webedoctor.com:9443/fhir-server/api/v4/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>willowglade_technologies_corporation</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://ccdoc.phn.care/tenant/NCS/patient/smart-api"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://ccdoc.phn.care/tenant/NCS/patient/smart-api" ></a></td>
      <td class="center-cell"><a href="https://ccdoc.phn.care/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://ccdoc.phn.care/metadata" ></a></td>
      <td class="center-cell"><a href="https://ccdoc.phn.care/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://ccdoc.phn.care/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>citiustech_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://www.citiustech.com/hubfs/citiustech-2024/products/perform/connect/patient/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://www.citiustech.com/hubfs/citiustech-2024/products/perform/connect/patient/" ></a></td>
      <td class="center-cell"><a href="https://www.citiustech.com/hubfs/citiustech-2024/products/perform/connect/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: https://www.citiustech.com/hubfs/citiustech-2024/products/perform/connect/metadata" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>core_solutions_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="HTTPS ORG URL: Fail" title="HTTPS ORG URL: Fail" ></td>
      <td class="center-cell"><a href="http://aidbox.cx360.net/metadata"><img src="./icons/green_fire_metadata.200.png" alt="Findable Metadata: Pass" title="Click to visit: http://aidbox.cx360.net/metadata" ></a></td>
      <td class="center-cell"><a href="http://aidbox.cx360.net/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: http://aidbox.cx360.net/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>objective_medical_systems_llc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://dxe.omshealth.com:6908/OAuth2/interface-connect-oms/api/FHIR/R4"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://dxe.omshealth.com:6908/OAuth2/interface-connect-oms/api/FHIR/R4" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><a href="https://dxe.omshealth.com:6908/OAuth2/interface-connect-oms/api/FHIR/R4/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://dxe.omshealth.com:6908/OAuth2/interface-connect-oms/api/FHIR/R4/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>oracle_health_2</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://fhir-myrecord-sc.cerner.com/r4/610e8cdb-2c3e-496a-b07b-c914f86e14f3/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir-myrecord-sc.cerner.com/r4/610e8cdb-2c3e-496a-b07b-c914f86e14f3/" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><a href="https://fhir-myrecord-sc.cerner.com/r4/610e8cdb-2c3e-496a-b07b-c914f86e14f3/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://fhir-myrecord-sc.cerner.com/r4/610e8cdb-2c3e-496a-b07b-c914f86e14f3/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>techsoft_inc</td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Reachable: Pass" title="Reachable: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://mdrfhirapi.mdronline.net/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://mdrfhirapi.mdronline.net/" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><a href="https://mdrfhirapi.mdronline.net/.well-known/smart-configuration"><img src="./icons/green_fire_smart.200.png" alt="Findable SMART: Pass" title="Click to visit: https://mdrfhirapi.mdronline.net/.well-known/smart-configuration" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>1life_healthcare_inc_2</td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Reachable: Fail" title="Reachable: Fail" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://healthlake.us-east-1.amazonaws.com/datastore/f7a9bd560802a0178bfce2d9a6e66ecc/r4"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://healthlake.us-east-1.amazonaws.com/datastore/f7a9bd560802a0178bfce2d9a6e66ecc/r4" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>agastha_inc</td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Reachable: Fail" title="Reachable: Fail" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://saas.agastha.com/AgAPI"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://saas.agastha.com/AgAPI" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>athenahealth_inc_2</td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Reachable: Fail" title="Reachable: Fail" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://af25sandbox.fhirapi.athenahealth.com/demo-mlAPIServer/fhir/r4"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://af25sandbox.fhirapi.athenahealth.com/demo-mlAPIServer/fhir/r4" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>brilogy_corporation</td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Reachable: Fail" title="Reachable: Fail" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://axeium.net/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://axeium.net/" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>claimpower_inc</td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Reachable: Fail" title="Reachable: Fail" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://fhirserver.justtest.in:9443/fhir-server/api/v4/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhirserver.justtest.in:9443/fhir-server/api/v4/" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>claimpower_inc_2</td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Reachable: Fail" title="Reachable: Fail" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://fhirserver.justtest.in:9443/fhir-server/api/v4/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhirserver.justtest.in:9443/fhir-server/api/v4/" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>clinicomp_intl</td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Reachable: Fail" title="Reachable: Fail" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://mum8.clinicomp.com:8445/fhir"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://mum8.clinicomp.com:8445/fhir" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>commure_d_b_a_athelas</td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Reachable: Fail" title="Reachable: Fail" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://onc.api.staging-ehr.athelas.com"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://onc.api.staging-ehr.athelas.com" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>criterions_software_inc</td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Reachable: Fail" title="Reachable: Fail" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://fhir.healthtogo.me/fhir/r4/criterions.djaliman"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir.healthtogo.me/fhir/r4/criterions.djaliman" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>dexter_solutions_inc</td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Reachable: Fail" title="Reachable: Fail" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://fhir.healthtogo.me/fhir/r4/ezdocs.bs"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir.healthtogo.me/fhir/r4/ezdocs.bs" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>ederm_systems_llc</td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Reachable: Fail" title="Reachable: Fail" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://fhir.ederm.io:9443/fhir-server/api/v4/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir.ederm.io:9443/fhir-server/api/v4/" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>enabledoc_llc</td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Reachable: Fail" title="Reachable: Fail" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://api.enablemyhealth.com/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://api.enablemyhealth.com/" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>endosoft_llc</td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Reachable: Fail" title="Reachable: Fail" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://fhirapi.endosoft.com/metadata"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhirapi.endosoft.com/metadata" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>ezcaretech_co_ltd</td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Reachable: Fail" title="Reachable: Fail" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://portal.ezcaretech.com:30122"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://portal.ezcaretech.com:30122" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>health_care_2000_inc</td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Reachable: Fail" title="Reachable: Fail" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://fhir.healthtogo.me/fhir/r4/mdvita.arturologronomd"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir.healthtogo.me/fhir/r4/mdvita.arturologronomd" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>keiser_computers_inc</td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Reachable: Fail" title="Reachable: Fail" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://fhir.drsdoc.com:9443/fhirserver/fhir/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir.drsdoc.com:9443/fhirserver/fhir/" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>mdflow_ehr_llc_dba_mdflow_systems</td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Reachable: Fail" title="Reachable: Fail" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://fhir.mdflow.com:8443/fhirserver/fhir/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir.mdflow.com:8443/fhirserver/fhir/" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>mdland</td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Reachable: Fail" title="Reachable: Fail" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://hapi-fhir.mdland.net/fhir/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://hapi-fhir.mdland.net/fhir/" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>mdofficemanager_2</td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Reachable: Fail" title="Reachable: Fail" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://fhir.geesemed.com:9443/fhir-server/api/v4/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir.geesemed.com:9443/fhir-server/api/v4/" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>mednet_medical_solutions</td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Reachable: Fail" title="Reachable: Fail" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://fhir.healthtogo.me/fhir/r4/mednetmedical.fsi"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir.healthtogo.me/fhir/r4/mednetmedical.fsi" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>medone_healthcare_partners</td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Reachable: Fail" title="Reachable: Fail" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://qafhir.medonehp.com:9443/fhir-server/api/v4/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://qafhir.medonehp.com:9443/fhir-server/api/v4/" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>medone_healthcare_partners_2</td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Reachable: Fail" title="Reachable: Fail" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://qafhir.medonehp.com:9443/fhir-server/api/v4/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://qafhir.medonehp.com:9443/fhir-server/api/v4/" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>moyae_inc</td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Reachable: Fail" title="Reachable: Fail" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://twholmbxki.execute-api.us-east-1.amazonaws.com/prod/tenant/eactx"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://twholmbxki.execute-api.us-east-1.amazonaws.com/prod/tenant/eactx" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>naphcare_inc</td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Reachable: Fail" title="Reachable: Fail" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://fhir.crystalpm.net:9443/fhirserver/fhir/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir.crystalpm.net:9443/fhirserver/fhir/" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>novomedici_llc_2</td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Reachable: Fail" title="Reachable: Fail" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://fhir.novoclinical.com/fhir/DEFAULT/metadata"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir.novoclinical.com/fhir/DEFAULT/metadata" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>office_practicum</td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Reachable: Fail" title="Reachable: Fail" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://applications.op.healthcare/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://applications.op.healthcare/" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>reli_med_solutions_llc</td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Reachable: Fail" title="Reachable: Fail" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://interface.relimedsolutions.com/fhir/r4/10018618/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://interface.relimedsolutions.com/fhir/r4/10018618/" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>sargas_pharmaceutical_adherence_and_compliance_international</td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Reachable: Fail" title="Reachable: Fail" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://qafhir.spacinternational.com:9443/fhirserver/fhir/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://qafhir.spacinternational.com:9443/fhirserver/fhir/" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>smartmd_technologies_inc</td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Reachable: Fail" title="Reachable: Fail" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://fhir.smartmd.com:9443/fhirserver/fhir/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir.smartmd.com:9443/fhirserver/fhir/" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>strateq_health_inc</td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Reachable: Fail" title="Reachable: Fail" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://testfhir.strateqhealth.com:9443/fhir-server/api/v4/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://testfhir.strateqhealth.com:9443/fhir-server/api/v4/" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>universal_ehr_inc</td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Reachable: Fail" title="Reachable: Fail" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://fhir.healthtogo.me/fhir/r4/universalehr.bdd"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir.healthtogo.me/fhir/r4/universalehr.bdd" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>vision_infonet_inc</td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Reachable: Fail" title="Reachable: Fail" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://fhir.mdcare.com:9443/fhir-server/api/v4/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir.mdcare.com:9443/fhir-server/api/v4/" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>zoobook_systems_llc</td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Reachable: Fail" title="Reachable: Fail" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><a href="https://fhir.healthtogo.me/fhir/r4/zoobook.journeytowellness"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir.healthtogo.me/fhir/r4/zoobook.journeytowellness" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>abeo_solutions_inc</td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Reachable: Fail" title="Reachable: Fail" ></td>
      <td class="center-cell"><img src="./icons/green_check.png" alt="Has ONPI: Pass" title="Has ONPI: Pass" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="HTTPS ORG URL: Fail" title="HTTPS ORG URL: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>advanced_data_systems_corporation</td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Reachable: Fail" title="Reachable: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://fhir-service.medicscloud.com/fhir/da/adsc_va8XWe7g7ObA5m7"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir-service.medicscloud.com/fhir/da/adsc_va8XWe7g7ObA5m7" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>advanced_data_systems_corporation_2</td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Reachable: Fail" title="Reachable: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://fhir-service.medicscloud.com/fhir/mc/adsc_v11NxJS9hXx60FT"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir-service.medicscloud.com/fhir/mc/adsc_v11NxJS9hXx60FT" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>braintree_health</td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Reachable: Fail" title="Reachable: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://fhirserver.braintreemd.com:9443/fhir-server/api/v4"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhirserver.braintreemd.com:9443/fhir-server/api/v4" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>chartpath_llc</td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Reachable: Fail" title="Reachable: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://fhir-api.chartpath.com:9443/fhir-server/api/v4/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir-api.chartpath.com:9443/fhir-server/api/v4/" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>dox_emr_2</td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Reachable: Fail" title="Reachable: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://doxpodfhir-dmezayd2cbead2f8.centralus-01.azurewebsites.net/api/Endpoint/1145"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://doxpodfhir-dmezayd2cbead2f8.centralus-01.azurewebsites.net/api/Endpoint/1145" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>edenlab_o</td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Reachable: Fail" title="Reachable: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://demo.kodjin.com/fhir/metadata"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://demo.kodjin.com/fhir/metadata" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>elation_health_inc</td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Reachable: Fail" title="Reachable: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://fhir.elationemr.com/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir.elationemr.com/" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>elekta_inc</td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Reachable: Fail" title="Reachable: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://prod-cus-eus2-hgv-21cc-smartonfhirgw-apim.elektacloud.com/smart-on-fhir-gateway"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://prod-cus-eus2-hgv-21cc-smartonfhirgw-apim.elektacloud.com/smart-on-fhir-gateway" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>health_information_management_systems_llc</td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Reachable: Fail" title="Reachable: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://fhir-api.hmsfirst.com/r4"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir-api.hmsfirst.com/r4" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>health_systems_technology_inc</td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Reachable: Fail" title="Reachable: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://portal.viewmymed.com"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://portal.viewmymed.com" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>indian_health_service</td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Reachable: Fail" title="Reachable: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://ihs4dhapim.ihs.gov/dev5/bulkfhir/r4/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://ihs4dhapim.ihs.gov/dev5/bulkfhir/r4/" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>integra_connect_newco_llc</td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Reachable: Fail" title="Reachable: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://portal.minerva.integracloud.com/minerva/fhir/r4/us-core/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://portal.minerva.integracloud.com/minerva/fhir/r4/us-core/" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>medpharm_services_llc</td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Reachable: Fail" title="Reachable: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://fhir-0300285.meditab.com/mps/fhir/R4"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir-0300285.meditab.com/mps/fhir/R4" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>microfour_inc</td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Reachable: Fail" title="Reachable: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://api.practicestudio.net/2376/fhir"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://api.practicestudio.net/2376/fhir" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>patient_first</td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Reachable: Fail" title="Reachable: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://fhirapis-qa2.patientfirst.com/smart"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhirapis-qa2.patientfirst.com/smart" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>pointclickcare_technologies_inc</td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Reachable: Fail" title="Reachable: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://connect.pointclickcare.com/fhir/R4/df2d4f2f-a8da-4417-aab5-24f9918efbcb/"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://connect.pointclickcare.com/fhir/R4/df2d4f2f-a8da-4417-aab5-24f9918efbcb/" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>practice_alternatives_inc</td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Reachable: Fail" title="Reachable: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://sandbox.pai.healthcare/preview/fhir"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://sandbox.pai.healthcare/preview/fhir" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>royal_health_inc</td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Reachable: Fail" title="Reachable: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://fhir.healthtogo.me/fhir/r4/royal.cmbs"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir.healthtogo.me/fhir/r4/royal.cmbs" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>sophrona_solutions_inc</td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Reachable: Fail" title="Reachable: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://aony1-fhir.practicegateway.net/smart"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://aony1-fhir.practicegateway.net/smart" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>tronshealth_llc</td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Reachable: Fail" title="Reachable: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://fhir.tronshealth.com"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://fhir.tronshealth.com" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>unknown</td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Reachable: Fail" title="Reachable: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://dssjess-dev-web.dssinc.com/fhir/jess/basepractice/r4"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://dssjess-dev-web.dssinc.com/fhir/jess/basepractice/r4" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
    <tr>
      <td>versasuite</td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Reachable: Fail" title="Reachable: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Has ONPI: Fail" title="Has ONPI: Fail" ></td>
      <td class="center-cell"><a href="https://proxy-fhir.versasuite.com"><img src="./icons/green_fire_org_endpoint.200.png" alt="HTTPS ORG URL: Pass" title="Click to visit: https://proxy-fhir.versasuite.com" ></a></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Metadata: Fail" title="Findable Metadata: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable SMART: Fail" title="Findable SMART: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI Docs: Fail" title="Findable OpenAPI Docs: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable OpenAPI JSON: Fail" title="Findable OpenAPI JSON: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger: Fail" title="Findable Swagger: Fail" ></td>
      <td class="center-cell"><img src="./icons/red_x.png" alt="Findable Swagger JSON: Fail" title="Findable Swagger JSON: Fail" ></td>
    </tr>
  </tbody>
</table>

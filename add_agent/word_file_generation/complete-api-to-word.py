from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from datetime import datetime
import os
import json
from word_generator import WordGenerator

app = FastAPI(title="Word Document Generator API", version="1.0.0")


# Pydantic models for request validation
class BasicInfo(BaseModel):
    mass_market_unit: str = Field(default="Technology")
    application_name: str = Field(default="Application")
    mal_name: str = Field(default="MAL001")
    author: str = Field(default="System Generated")


class ProjectAccess(BaseModel):
    group: str
    owners: str
    description: str
    environment: str


class FirewallRule(BaseModel):
    network: str
    actions: str
    sourceip: str
    destination: str
    port: str
    protocol: str
    direction: str


class IAMEntry(BaseModel):
    service: str
    principal: str
    environment: str
    permission: str


class ServiceAccount(BaseModel):
    service: str
    serviceaccount: str
    permission: str
    environment: str
    jsonkey: str


class TechnicalArchitecture(BaseModel):
    app_overview: Optional[str] = ""
    business_needs: Optional[str] = ""
    key_features: Optional[List[str]] = []
    user_stories: Optional[str] = ""
    technology_stack: Optional[List[str]] = []
    project_access: Optional[List[ProjectAccess]] = []
    firewall_rules: Optional[List[FirewallRule]] = []
    iam: Optional[List[IAMEntry]] = []
    service_accounts: Optional[List[ServiceAccount]] = []
    key_components: Optional[List[Dict[str, Any]]] = []
    logical_architecture: Optional[str] = ""
    deployment_model: Optional[str] = ""
    security: Optional[str] = ""
    app_solution_integration: Optional[str] = ""
    on_premises_dependencies: Optional[str] = ""
    external_dependencies: Optional[str] = ""
    data_flow: Optional[str] = ""


class OperationalSupportModel(BaseModel):
    component: str
    dev: str
    prod: str
    qa: str
    uat: str


class CostManagement(BaseModel):
    environment: str
    cost: float


class DevelopmentOperations(BaseModel):
    development_environment: Optional[str] = ""
    deployment_process: Optional[str] = ""
    operational_support_model: Optional[List[OperationalSupportModel]] = []
    cost_management: Optional[List[CostManagement]] = []
    monitoring_logging: Optional[str] = ""
    service_level_indicators: Optional[str] = ""
    service_level_objectives: Optional[str] = ""
    recovery_point_objectives: Optional[str] = ""
    recovery_time_objectives: Optional[str] = ""
    security_review_assessment: Optional[str] = ""
    sre_assessment: Optional[str] = ""
    governance: Optional[str] = ""


class DesignAssumption(BaseModel):
    assumptionid: str
    assumption: str
    validationcriteria: str


class Dependency(BaseModel):
    dependency: str
    provider: str
    daterequired: str
    reason: str


class DesignRisk(BaseModel):
    id: str
    risksimpactsandaction: str
    category: str
    likelihood: str
    dateacceptedorremoved: str


class KeyDecision(BaseModel):
    category: str
    dateacceptedorremoved: str
    dateraised: str
    decisiondescription: str
    id: str
    issuestatus: str
    likelihood: str


class RisksAssumptions(BaseModel):
    design_assumptions: Optional[List[DesignAssumption]] = []
    dependencies: Optional[List[Dependency]] = []
    design_risks: Optional[List[DesignRisk]] = []
    key_decisions: Optional[List[KeyDecision]] = []


class Appendix(BaseModel):
    abbreviations: Optional[Dict[str, str]] = {}
    glossary: Optional[Dict[str, str]] = {}
    resources_guidance: Optional[Dict[str, str]] = {}
    google_apis: Optional[Dict[str, str]] = {}
    references: Optional[str] = ""


class DocumentRequest(BaseModel):
    basic_info: BasicInfo
    technical_architecture: Optional[TechnicalArchitecture] = TechnicalArchitecture()
    development_operations: Optional[DevelopmentOperations] = DevelopmentOperations()
    risks_assumptions: Optional[RisksAssumptions] = RisksAssumptions()
    appendix: Optional[Appendix] = Appendix()
    images: Optional[List[Dict[str, Any]]] = []


class APIToWordGenerator:
    """Handles API data to Word document conversion"""

    def __init__(self):
        self.generator = WordGenerator()

    def process_api_data(self, api_data: DocumentRequest):
        """Convert API data to Word document format"""

        # Convert to Word document format
        word_data = {
            # Basic Information
            'mmUnit': api_data.basic_info.mass_market_unit,
            'apName': api_data.basic_info.application_name,
            'mName': api_data.basic_info.mal_name,
            'authorName': api_data.basic_info.author,
            'formattedDate': datetime.now().strftime('%Y-%m-%d'),

            # Application Overview
            'htmlAppOverviewData': self.convert_to_html(api_data.technical_architecture.app_overview),
            'htmlBNData': self.convert_to_html(api_data.technical_architecture.business_needs),
            'htmlKFData': self.convert_list_to_html(api_data.technical_architecture.key_features),
            'htmlUSData': self.convert_to_html(api_data.technical_architecture.user_stories),

            # Technical Architecture
            'htmlLAData': self.convert_to_html(api_data.technical_architecture.logical_architecture),
            'tsData': ', '.join(api_data.technical_architecture.technology_stack),
            'htmlDMData': self.convert_to_html(api_data.technical_architecture.deployment_model),

            # Tables
            'paData': [pa.dict() for pa in api_data.technical_architecture.project_access],
            'frData': [fr.dict() for fr in api_data.technical_architecture.firewall_rules],
            'iamData': [iam.dict() for iam in api_data.technical_architecture.iam],
            'servAccRows': [sa.dict() for sa in api_data.technical_architecture.service_accounts],
            'htmlKCDataTable': api_data.technical_architecture.key_components,

            # Development Operations
            'htmlDEData': self.convert_to_html(api_data.development_operations.development_environment),
            'htmlDPData': self.convert_to_html(api_data.development_operations.deployment_process),
            'osmData': [osm.dict() for osm in api_data.development_operations.operational_support_model],
            'cmData': [cm.dict() for cm in api_data.development_operations.cost_management],
            'htmlSLIData': self.convert_to_html(api_data.development_operations.service_level_indicators),
            'htmlSLOData': self.convert_to_html(api_data.development_operations.service_level_objectives),
            'htmlRPOData': self.convert_to_html(api_data.development_operations.recovery_point_objectives),
            'htmlRTOData': self.convert_to_html(api_data.development_operations.recovery_time_objectives),
            'mlData': api_data.development_operations.monitoring_logging,
            'sraParagraphData': api_data.development_operations.security_review_assessment,
            'sreParagraphData': api_data.development_operations.sre_assessment,
            'htmlGVData': self.convert_to_html(api_data.development_operations.governance),

            # Risks and Assumptions
            'daData': [da.dict() for da in api_data.risks_assumptions.design_assumptions],
            'dData': [d.dict() for d in api_data.risks_assumptions.dependencies],
            'drData': [dr.dict() for dr in api_data.risks_assumptions.design_risks],
            'kdData': [kd.dict() for kd in api_data.risks_assumptions.key_decisions],

            # Appendix
            'agData': self.format_abbreviations(api_data.appendix.abbreviations),
            'gData': self.format_glossary(api_data.appendix.glossary),
            'rgData': self.format_resources(api_data.appendix.resources_guidance),
            'googleAPIData': self.format_google_apis(api_data.appendix.google_apis),
            'htmlRFData': self.convert_to_html(api_data.appendix.references),

            # Additional required fields
            'htmlSecurityData': self.convert_to_html(api_data.technical_architecture.security),
            'htmlASIData': self.convert_to_html(api_data.technical_architecture.app_solution_integration),
            'htmlOPDData': self.convert_to_html(api_data.technical_architecture.on_premises_dependencies),
            'htmlEDData': self.convert_to_html(api_data.technical_architecture.external_dependencies),
            'htmlDataFlowData': self.convert_to_html(api_data.technical_architecture.data_flow),

            'fileName': f"{api_data.basic_info.mal_name}.xlsx",
            'images': api_data.images
        }

        return word_data

    def convert_to_html(self, text: str) -> str:
        """Convert plain text to HTML"""
        if not text:
            return ""

        if text.startswith('<'):
            return text
        return f"<p>{text}</p>"

    def convert_list_to_html(self, items: List[str]) -> str:
        """Convert list to HTML unordered list"""
        if not items:
            return ""

        html = "<ul>"
        for item in items:
            html += f"<li>{item}</li>"
        html += "</ul>"
        return html

    def format_abbreviations(self, data: Dict[str, str]) -> List[Dict[str, str]]:
        """Format abbreviations for the document"""
        return [{'abbreviationacronym': k, 'description': v} for k, v in data.items()]

    def format_glossary(self, data: Dict[str, str]) -> List[Dict[str, str]]:
        """Format glossary for the document"""
        return [{'term': k, 'definition': v} for k, v in data.items()]

    def format_resources(self, data: Dict[str, str]) -> List[Dict[str, str]]:
        """Format resources guidance for the document"""
        return [{'link': k, 'resource': v} for k, v in data.items()]

    def format_google_apis(self, data: Dict[str, str]) -> List[Dict[str, str]]:
        """Format Google APIs for the document"""
        return [{'service': k, 'api': v} for k, v in data.items()]

    def generate_document(self, api_data: DocumentRequest) -> str:
        """Generate Word document from API data"""
        # Process the API data
        word_data = self.process_api_data(api_data)

        # Generate the document
        filename = self.generator.generate_document(word_data)

        return filename


@app.post("/generate-word",
          summary="Generate Word Document",
          description="Generate a Word document from structured API data",
          response_description="The generated Word document file",
          tags=["Document Generation"])
async def generate_word_document(document_data: DocumentRequest):
    """
    Generate a Word document from the provided JSON data.

    The request should include:
    - basic_info: Basic information about the document
    - technical_architecture: Technical details
    - development_operations: Development and operations information
    - risks_assumptions: Risk and assumption data
    - appendix: Additional reference information
    """
    try:
        # Create generator instance
        generator = APIToWordGenerator()

        # Generate the document
        filename = generator.generate_document(document_data)

        # Check if file exists
        if not os.path.exists(filename):
            raise HTTPException(status_code=500, detail="Document generation failed")

        # Return the file
        return FileResponse(
            path=filename,
            media_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document',
            filename=filename,
            headers={"Content-Disposition": f"attachment; filename={filename}"}
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/", tags=["Info"])
async def root():
    """Root endpoint providing API information"""
    return {
        "message": "Word Document Generator API",
        "version": "1.0.0",
        "endpoints": {
            "/": "This information page",
            "/docs": "Interactive API documentation",
            "/generate-word": "Generate Word document endpoint"
        }
    }


@app.get("/health", tags=["Info"])
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}


# Example endpoint to show expected data structure
@app.get("/example", tags=["Info"])
async def get_example():
    """Get an example of the expected request structure"""
    return {
        "basic_info": {
            "mass_market_unit": "Enterprise Solutions",
            "application_name": "Customer Portal",
            "mal_name": "PORTAL001",
            "author": "John Smith"
        },
        "technical_architecture": {
            "app_overview": "The Customer Portal is a cloud-native application...",
            "business_needs": "The business requires a modern portal...",
            "key_features": ["Real-time dashboard", "User management", "Reporting"],
            "technology_stack": ["Python", "React", "PostgreSQL", "Docker"],
            "project_access": [
                {
                    "group": "admin-group",
                    "owners": "admin@company.com",
                    "description": "Full administrative access",
                    "environment": "Production"
                }
            ]
        },
        "development_operations": {
            "development_environment": "Local development using Docker Compose...",
            "deployment_process": "CI/CD pipeline using GitHub Actions...",
            "operational_support_model": [
                {
                    "component": "Frontend",
                    "dev": "Frontend Team",
                    "prod": "SRE Team",
                    "qa": "QA Team",
                    "uat": "Product Team"
                }
            ]
        }
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port=8001)

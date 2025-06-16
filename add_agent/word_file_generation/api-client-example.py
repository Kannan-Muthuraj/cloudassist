import requests
import json


def test_fastapi_word_generator():
    """Test the FastAPI Word Generator API"""

    # API URL
    api_url = "http://localhost:8000/generate-word"

    # Sample data
    document_data = {
        "basic_info": {
            "mass_market_unit": "Technology",
            "application_name": "Customer Portal",
            "mal_name": "PORTAL001",
            "author": "John Doe"
        },
        "technical_architecture": {
            "app_overview": "The Customer Portal is a cloud-native application designed to provide seamless customer experiences.",
            "business_needs": "The business requires a modern portal to reduce operational costs and improve customer satisfaction.",
            "key_features": [
                "Real-time dashboard",
                "User management",
                "Reporting capabilities",
                "API integration"
            ],
            "user_stories": "As a customer, I want to view my account details and track orders in real-time.",
            "technology_stack": ["Python", "React", "PostgreSQL", "Docker", "Kubernetes"],
            "project_access": [
                {
                    "group": "admin-group",
                    "owners": "admin@company.com",
                    "description": "Full administrative access",
                    "environment": "Production"
                }
            ],
            "firewall_rules": [
                {
                    "network": "10.0.0.0/24",
                    "actions": "Allow",
                    "sourceip": "0.0.0.0/0",
                    "destination": "10.0.0.1",
                    "port": "443",
                    "protocol": "TCP",
                    "direction": "Ingress"
                }
            ],
            "iam": [
                {
                    "service": "Cloud Storage",
                    "principal": "app-service@project.iam",
                    "environment": "Production",
                    "permission": "storage.admin, storage.viewer"
                }
            ]
        },
        "development_operations": {
            "development_environment": "Local development using Docker Compose with hot reloading.",
            "deployment_process": "CI/CD pipeline using GitHub Actions and ArgoCD.",
            "operational_support_model": [
                {
                    "component": "Frontend",
                    "dev": "Frontend Team",
                    "prod": "SRE Team",
                    "qa": "QA Team",
                    "uat": "Product Team"
                }
            ],
            "cost_management": [
                {
                    "environment": "Development",
                    "cost": 2500
                },
                {
                    "environment": "Production",
                    "cost": 15000
                }
            ],
            "monitoring_logging": "Monitoring with Prometheus and Grafana, logging with ELK stack.",
            "service_level_indicators": "Availability, latency, and error rate metrics.",
            "service_level_objectives": "99.9% availability, <200ms latency, <0.1% error rate.",
            "recovery_point_objectives": "15 minutes for critical data.",
            "recovery_time_objectives": "1 hour for full service restoration.",
            "security_review_assessment": "Passed security review with no critical findings.",
            "sre_assessment": "Application meets SRE standards for production deployment.",
            "governance": "Quarterly architecture reviews and monthly security assessments."
        },
        "risks_assumptions": {
            "design_assumptions": [
                {
                    "assumptionid": "A001",
                    "assumption": "Cloud resources will be available as needed",
                    "validationcriteria": "Vendor SLA compliance"
                }
            ],
            "dependencies": [
                {
                    "dependency": "Payment Gateway API",
                    "provider": "Stripe",
                    "daterequired": "2024-02-01",
                    "reason": "Payment processing capability"
                }
            ],
            "design_risks": [
                {
                    "id": "R001",
                    "risksimpactsandaction": "Data breach risk - Implement encryption and access controls",
                    "category": "Security",
                    "likelihood": "Medium",
                    "dateacceptedorremoved": "2024-01-20"
                }
            ]
        },
        "appendix": {
            "abbreviations": {
                "API": "Application Programming Interface",
                "SLA": "Service Level Agreement",
                "SRE": "Site Reliability Engineering"
            },
            "glossary": {
                "Microservice": "Small, autonomous service",
                "Container": "Lightweight, standalone package",
                "Orchestration": "Automated container management"
            },
            "resources_guidance": {
                "https://cloud.google.com/docs": "Google Cloud Documentation",
                "https://kubernetes.io/docs": "Kubernetes Documentation"
            },
            "google_apis": {
                "Cloud Storage": "storage.googleapis.com",
                "Cloud SQL": "sqladmin.googleapis.com"
            },
            "references": "1. Google Cloud Best Practices\n2. Kubernetes Security Guidelines"
        }
    }

    try:
        # Send POST request
        response = requests.post(
            api_url,
            json=document_data,
            headers={'Content-Type': 'application/json'}
        )

        # Check response
        if response.status_code == 200:
            # Save the file
            filename = f"{document_data['basic_info']['mal_name']}_generated.docx"
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f"Document generated successfully: {filename}")
        else:
            print(f"Error: {response.status_code}")
            print(response.text)

    except Exception as e:
        print(f"Error: {e}")


# Test other endpoints
def test_api_endpoints():
    """Test various API endpoints"""

    base_url = "http://localhost:8000"

    # Test root endpoint
    response = requests.get(f"{base_url}/")
    print("Root endpoint:", response.json())

    # Test health check
    response = requests.get(f"{base_url}/health")
    print("Health check:", response.json())

    # Test example endpoint
    response = requests.get(f"{base_url}/example")
    print("Example structure:", json.dumps(response.json(), indent=2))


if __name__ == "__main__":
    # Test the main endpoint
    test_fastapi_word_generator()

    # Test other endpoints
    # test_api_endpoints()

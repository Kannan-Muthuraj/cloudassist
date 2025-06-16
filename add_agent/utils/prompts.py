INPUT_PROMPT = """
You are an expert CSV anlayzer. Your task is to use the tool to provide the content inside provided csv file in JSON Format.
If app_name is same or repeated more than one it should be treated as one application.
Provide the Output in Expected Output format
**Expected Output Format**
Example 1:[
    {
    "mal_name": "netqt",
    "technology_stack": "GKE",
    "env_type": "dedicated/shared",
    "region": "us-central1",
    "env": "dev",
    "config_list": "Region=us-central1"
  },
  {
    "mal_name": "px",
    "technology_stack": "GCE",
    "env_type": "dedicated/shared",
    "region": "us-east4",
    "env": "prod, qa",
    "config_list": "Instance Type=e2-medium; region=us-central1; Disk Size=100, Region=us-central1; Database_version=POSTGRES_15; Tier=db-custom-16-65536",
  }
]
"""

VALIDATION_PROMPT = """
Your task is to get the inputs and send them according to the tools inputs.
***input***
{UserInput}

You will provide the output in JSON Format.
**Expected Output Format**
example: {
  "status": "valid",
  "m_name": "PX",
  "ap_name": "PARTNER EXPERIENCE",
  "mail": "NAIMESH.BHATT@LUMEN.COM",
  "user_input": "GKE",
  "service_domain": "Sales and Service",
  "technology_stack": [
    "GKE"
  ],
  "env_type": [
    "dedicated"
  ],
  "region": [
    "us-central1"
  ],
  "configuration": "region=us-central1"
}
"""

ADD_INSTRUCTION_PROMPT = """
Your task is to generate the ADD document and give according to the tools inputs.
**Input**
{ValidatedInput} and {UserInput}

I want you to give the tools output response as same in the JSON Format.
**Expected format**
Example 1:
 If app_name or mal_name or m_name is only NETQT.
 {
    "NETQT": {
        "technical_architecture": {
"project_access": {
    "2.02 Technology Stack": "GKE",
    "2.04 Project Access": [
        {
            "Description": "admin group",
            "Environment": "dev, qa, prod",
            "Group": "admin",
            "Owners": "nash.vedire@lumen.com,eric.gates@lumen.com,tejinder.singh@lumen.com,richard.e.nelson@lumen.com,<otherowner>"
        },
        {
            "Description": "dev team group",
            "Environment": "dev, qa, prod",
            "Group": "dev-team",
            "Owners": "nash.vedire@lumen.com,eric.gates@lumen.com,tejinder.singh@lumen.com,richard.e.nelson@lumen.com,<otherowner>"
        },
        {
            "Description": "viewer group",
            "Environment": "dev, qa, prod",
            "Group": "viewer",
            "Owners": "nash.vedire@lumen.com,eric.gates@lumen.com,tejinder.singh@lumen.com,richard.e.nelson@lumen.com,<otherowner>"
        },
        {
            "Description": "ops team group",
            "Environment": "dev, qa, prod",
            "Group": "ops-team",
            "Owners": "nash.vedire@lumen.com,eric.gates@lumen.com,tejinder.singh@lumen.com,richard.e.nelson@lumen.com,<otherowner>"
        }
    ]
},
"key_components": {
    "2.05 Key Components": {
        "- **2.5.1 Components**": [
            {
                "Service": "GKE",
                "dev": "$Machine Type:eg.\"e2-standard-4\"$\n            $Disk Size:\"100\"$\n            $Disk Type:\"pd-standard\"$\n            Region: \"us-central1\"\n            $POD:18$\n            $CPU&MEMORY:12 CPU & 64 GB (@ Cluster level)$\n            $SVS:18$\n            $CPU&MEMORY:16 CPUs & 64 GB (@ Cluster level)$\n            $sgs_gke_cp_cidr:/28$\n            $sgs_gke_node_cidr:TBD$\n            $sgs_gke_pods_cidr,:TBD$\n            $sgs_gke_svs_cidr:TBD$",
                "prod": "$Machine Type:eg.\"e2-standard-4\"$\n            $Disk Size:\"100\"$\n            $Disk Type:\"pd-standard\"$\n            Region: \"us-central1\"\n            $POD:12(4 replicas for each service) 2GB/pod$\n            $CPU&MEMORY:12 CPU & 64 GB (@ Cluster level)$\n            $SVS:12(4 replicas for each service) +Appd- 2pods + Splunk-2pods + ingress controller$\n            $CPU&MEMORY: 16 CPUs & 64 GB (@ Cluster level)$ \n            $sgs_gke_cp_cidr:/28$\n            $sgs_gke_node_cidr:TBD$ \n            $sgs_gke_pods_cidr,:TBD$\n            $sgs_gke_svs_cidr:TBD$",
                "qa": "$Machine Type:eg.\"e2-standard-4\"$\n            $Disk Size:\"100\"$\n            $Disk Type:\"pd-standard\"$\n            Region: \"us-central1\"\n            $POD:18$\n            $CPU&MEMORY:12 CPU & 64 GB (@ Cluster level)$\n            $SVS:18$\n            $CPU&MEMORY:16 CPUs & 64 GB (@ Cluster level)$  \n            $sgs_gke_cp_cidr:/28$\n            $sgs_gke_node_cidr:TBD$ \n            $sgs_gke_pods_cidr,:TBD$\n            $sgs_gke_svs_cidr:TBD$"
            },
            {
                "Service": "INTERNAL-DNS",
                "dev": "*.sgs.mm.gcp.dev.intranet",
                "prod": "*.sgs.mm.gcp.corp.intranet",
                "qa": "*.sgs.mm.gcp.qa.test.intranet"
            }
        ]
    }
},
"service_accounts": {
    "2.09 Service Accounts": [
        {
            "Environment": "dev, qa, prod",
            "JSON Key": "NA",
            "Permission": "Compute Instance Admin (v1), Compute Network User, Kubernetes Engine Admin, Kubernetes Engine Host Service Agent User, Kubernetes Engine Node Service Account, Secret Manager Secret Accessor",
            "Service": "GKE",
            "Service Account": "sa-gke"
        },
        {
            "Environment": "dev, qa, prod",
            "JSON Key": "Yes",
            "Permission": "Kubernetes Engine Admin",
            "Service": "GKE",
            "Service Account": "sa-cicd"
        }
    ]
},
"firewall": {
    "2.12 Firewall Rules": [
        {
            "Actions": "Allow",
            "Destination": "sgs_gke_cp_cidr, sgs_gke_node_cidr, sgs_gke_pods_cidr, sgs_gke_svs_cidr",
            "Direction": "Egress",
            "Network": "PRJ",
            "Port": "All",
            "Protocol": "TCP",
            "Source IP": "sgs_gke_cp_cidr, sgs_gke_node_cidr, sgs_gke_pods_cidr, sgs_gke_svs_cidr"
        },
        {
            "Actions": "Allow",
            "Destination": "sgs_gke_cp_cidr, sgs_gke_node_cidr, sgs_gke_pods_cidr, sgs_gke_svs_cidr",
            "Direction": "Ingress",
            "Network": "PRJ",
            "Port": "All",
            "Protocol": "TCP",
            "Source IP": "sgs_gke_cp_cidr, sgs_gke_node_cidr, sgs_gke_pods_cidr, sgs_gke_svs_cidr"
        },
        {
            "Actions": "Deny",
            "Destination": "sgs_gke_node_cidr",
            "Direction": "Ingress",
            "Network": "PRJ",
            "Port": "22",
            "Protocol": "TCP",
            "Source IP": "0.0.0.0/0"
        },
        {
            "Actions": "Allow",
            "Destination": "sgs_gke_cp_cidr",
            "Direction": "Egress",
            "Network": "PRJ",
            "Port": "443",
            "Protocol": "TCP",
            "Source IP": "NON SOX JUMP HOST CIDR"
        },
        {
            "Actions": "Allow",
            "Destination": "sgs_gke_node_cidr",
            "Direction": "Egress",
            "Network": "PRJ",
            "Port": "443",
            "Protocol": "TCP",
            "Source IP": "jenkins_us_central1_cidrs"
        }
    ]
},
"iam": {
    "2.13 IAM": [
        {
            "Environment": "dev, qa, prod",
            "Permission": "Secret Manager Secret Accessor, Secret Manager Secret Version Manager, Tech Support Editor, Logs Configuration Writer, Logs Viewer, Monitoring Alert Policy Editor, Monitoring Editor, Monitoring Notification Channel Editor, viewer",
            "Principal": "dev-team, ops-team",
            "Service": "Default"
        },
        {
            "Environment": "dev, qa, prod",
            "Permission": "viewer",
            "Principal": "viewer",
            "Service": "Default"
        },
        {
            "Environment": "dev, qa, prod",
            "Permission": "Kubernetes Engine Developer",
            "Principal": "dev-team, ops-team",
            "Service": "GKE"
        }
    ]
}
},
        "devops_and_operations": {
"devops": {
    "3. Development and Operations": {
        "3.1 Development Environment": "Developers will utilize Cloud Code for VS Code to interact with the GKE cluster.  The development environment will include a local Kubernetes cluster for testing and debugging.  Version control will be managed using Git, and code will be stored in a centralized repository. Continuous Integration/Continuous Delivery (CI/CD) pipelines will be implemented using tools such as Jenkins or Google Cloud Build to automate testing and deployment.",
        "3.2 Deployment Process": "The deployment process will leverage GKE's built-in capabilities for automated deployments.  Container images will be built and pushed to Google Container Registry (GCR). Kubernetes manifests will define the application's deployment specifications.  Deployments will be rolled out using techniques like blue/green deployments or canary deployments to minimize disruption.  Automated rollback mechanisms will be implemented to handle deployment failures."
    }
},
"ops": {
    "3.3 Operational Support Model": [
        {
            "Component": "GKE",
            "DEV": "App Team",
            "PROD": "App Team",
            "QA": "App Team",
            "UAT": "App Team"
        },
        {
            "Component": "API Gateway",
            "DEV": "App Team",
            "PROD": "App Team",
            "QA": "App Team",
            "UAT": "App Team"
        },
        {
            "Component": "DNS Records",
            "DEV": "MM Cloud Team",
            "PROD": "MM Cloud Team",
            "QA": "MM Cloud Team",
            "UAT": "MM Cloud Team"
        },
        {
            "Component": "SSL Certificates",
            "DEV": "MM Cloud Team",
            "PROD": "MM Cloud Team",
            "QA": "MM Cloud Team",
            "UAT": "MM Cloud Team"
        },
        {
            "Component": "Firewall Rules",
            "DEV": "MM Cloud Team",
            "PROD": "MM Cloud Team",
            "QA": "MM Cloud Team",
            "UAT": "MM Cloud Team"
        },
        {
            "Component": "Application Deployment Image",
            "DEV": "App Team",
            "PROD": "App Team",
            "QA": "App Team",
            "UAT": "App Team"
        },
        {
            "Component": "Application Logging",
            "DEV": "App Team",
            "PROD": "App Team",
            "QA": "App Team",
            "UAT": "App Team"
        }
    ]
},
"service": {
    "3.4.1 Service Level Indicators (SLI)": "An automated health check is performed to monitor service health.",
    "3.4.2 Service Level Objective (SLO)": "The service must maintain at least 99.5% availability."
},
"governance": {
    "3.4.3 Recovery Point Objective (RPO)": "The acceptable amount of data loss in a catastrophic failure must be specified (e.g., 1 minute, 1 hour, 1 day, etc.).",
    "3.4.4 Recovery Time Objective (RTO)": "The maximum acceptable downtime for the application following a catastrophic failure needs to be defined (e.g., 1 hour, 4 hours, 1 day, etc.).",
    "3.6 Governance": "Governance requirements (PCI, CMMC, SOX, etc.) and adherence processes or waivers need to be identified and documented."
}
},
        "risks_and_assumptions": {
"Design_Assumptions": {
    "4. Risks, Assumptions, and Decisions": {
        "4.1 Design Assumptions": [
            {
                "Assumption": "Connections from services in GCP to on-premises via interconnect using nginx, NAT'd IPs, and traceability are required.",
                "Assumption ID": "A1",
                "Validation Criteria": "Verify the interconnect is configured and tested, nginx is installed and configured, NAT'd IPs are configured, and traceability is implemented."
            },
            {
                "Assumption": "Dependencies are defined and documented.",
                "Assumption ID": "A2",
                "Validation Criteria": "Review the dependency table (Table 5) to ensure all dependencies are identified and documented."
            },
            {
                "Assumption": "Design risks are identified and mitigated.",
                "Assumption ID": "A3",
                "Validation Criteria": "Review the design risk table (Table 6) to ensure all risks are identified and mitigation strategies are in place."
            },
            {
                "Assumption": "Key decisions regarding interconnect setup and IP visibility are documented and implemented.",
                "Assumption ID": "A4",
                "Validation Criteria": "Review the key decisions table and verify that the interconnect setup and IP visibility are implemented as documented."
            }
        ]
    }
},
"Dependencies": {
    "4.2 Dependencies": [
        {
            "Date Required": "2025-05-27",
            "Dependency": "GKE",
            "Provider": "Google",
            "Reason": "Required for deploying containerized applications"
        },
        {
            "Date Required": "2025-05-27",
            "Dependency": "GCE",
            "Provider": "Google",
            "Reason": "Required for hosting virtual machines"
        },
        {
            "Date Required": "2025-05-27",
            "Dependency": "Vertex AI",
            "Provider": "Google",
            "Reason": "Required for building and deploying machine learning models"
        },
        {
            "Date Required": "2025-05-27",
            "Dependency": "Memorystore",
            "Provider": "Google",
            "Reason": "Required for caching data"
        },
        {
            "Date Required": "2025-05-27",
            "Dependency": "Google Load Balancer - External",
            "Provider": "Google",
            "Reason": "Required for load balancing traffic to services"
        },
        {
            "Date Required": "2025-05-27",
            "Dependency": "Cloud Run",
            "Provider": "Google",
            "Reason": "Required for running serverless applications"
        }
    ]
},
"Design_Risks": {
    "4.3 Design Risks": [
        {
            "Category": "Security",
            "Date Accepted/Removed": "2025-05-27",
            "ID": "DR-1",
            "Likelihood (Low/Med/High)": "Medium",
            "Risks Impacts and Actions": "Potential for unauthorized access to on-premises systems through the interconnect. Implement robust authentication and authorization mechanisms, including multi-factor authentication, to mitigate this risk."
        },
        {
            "Category": "Performance",
            "Date Accepted/Removed": "2025-05-27",
            "ID": "DR-2",
            "Likelihood (Low/Med/High)": "Medium",
            "Risks Impacts and Actions": "Latency issues due to network connectivity between GCP and on-premises systems. Utilize a high-speed interconnect with sufficient bandwidth and optimize network configurations to minimize latency."
        },
        {
            "Category": "Reliability",
            "Date Accepted/Removed": "2025-05-27",
            "ID": "DR-3",
            "Likelihood (Low/Med/High)": "Low",
            "Risks Impacts and Actions": "Interconnect failures may disrupt communication between GCP and on-premises systems. Implement redundancy and failover mechanisms, such as multiple interconnects, to ensure continued communication."
        },
        {
            "Category": "Cost",
            "Date Accepted/Removed": "2025-05-27",
            "ID": "DR-4",
            "Likelihood (Low/Med/High)": "Medium",
            "Risks Impacts and Actions": "High cost associated with using an interconnect and NAT services.  Evaluate cost-effective solutions and explore alternative connectivity options."
        },
        {
            "Category": "Complexity",
            "Date Accepted/Removed": "2025-05-27",
            "ID": "DR-5",
            "Likelihood (Low/Med/High)": "High",
            "Risks Impacts and Actions": "Managing the interconnect and associated security policies can be complex.  Provide clear documentation and training to ensure smooth operations and minimize complexity."
        }
    ]
},
"Key_Decisions": {
    "4.4 Key Decisions": [
        {
            "Category": "Connectivity",
            "Date Accepted/Removed": "2025-05-27",
            "Date Raised": "2025-05-13",
            "Decision Description": "Interconnect setup and IP visibility - How to ensure the on-premises IPs are visible within the GCP environment while maintaining security and traceability.",
            "ID": "D-001",
            "Likelihood": "High"
        },
        {
            "Category": "Security",
            "Date Accepted/Removed": "2025-05-27",
            "Date Raised": "2025-05-13",
            "Decision Description": "Implementation of security measures for the NATed IPs and the interconnect connection.",
            "ID": "D-002",
            "Likelihood": "High"
        },
        {
            "Category": "Performance",
            "Date Accepted/Removed": "2025-05-27",
            "Date Raised": "2025-05-13",
            "Decision Description": "Performance impact of NATing and the interconnect on overall application latency and response time.",
            "ID": "D-003",
            "Likelihood": "Medium"
        },
        {
            "Category": "Scalability",
            "Date Accepted/Removed": "2025-05-27",
            "Date Raised": "2025-05-13",
            "Decision Description": "Scalability of the interconnect and NAT solution to handle anticipated growth in data traffic.",
            "ID": "D-004",
            "Likelihood": "Medium"
        },
        {
            "Category": "Management",
            "Date Accepted/Removed": "2025-05-27",
            "Date Raised": "2025-05-13",
            "Decision Description": "Management and monitoring of the interconnect and NAT infrastructure within GCP.",
            "ID": "D-005",
            "Likelihood": "Medium"
        }
    ]
}
},
        "appendix": {
"Abbreviations": {
    "5. Appendix": {
        "5.1 Abbreviations and Glossary": {
            "5.1.1 Abbreviations": [
                {
                    "Abbreviation/Acronym": "GKE",
                    "Description": "Google Kubernetes Engine"
                },
                {
                    "Abbreviation/Acronym": "VERTEX AI",
                    "Description": "Vertex AI is a machine learning platform"
                }
            ]
        }
    }
},
"Glossary": {
    "5.1.2 Glossary": [
        {
            "Definition": "Relevant acronyms and terms for the project are defined in this section.",
            "Term": "Abbreviations and Glossary"
        },
        {
            "Definition": "Project-related abbreviations are defined here.",
            "Term": "Abbreviations"
        },
        {
            "Definition": "Project-related terms are defined here to aid in understanding the application.",
            "Term": "Glossary"
        },
        {
            "Definition": "External resources that the project interacts with to function properly. Explanations of these interactions and diagrams identifying the interaction points should be included.",
            "Term": "Required Project References"
        },
        {
            "Definition": "References to regulatory or standards required for this project, including versions adhered to, should be listed.",
            "Term": "Standards and other References"
        },
        {
            "Definition": "Cloud Center of Excellence",
            "Term": "Resource"
        },
        {
            "Definition": "Global Architecture Guiding Principles, Technology Architecture Working Group (TAWG), TAWG - Home",
            "Term": "Architecture"
        },
        {
            "Definition": "DevOps Transformation, DevOps Strategy, CI/CD Strategy, Orchestration and Workflow, Tool Selection and Considerations",
            "Term": "SP&T DevOps Transformation"
        },
        {
            "Definition": "Security Portal Home, Federal InfoSec, TMF Adherence, TM Forum",
            "Term": "Data Security"
        },
        {
            "Definition": "API Strategic Architecture, API Enablement",
            "Term": "API Enablement"
        },
        {
            "Definition": "App Modernization Team Room",
            "Term": "Application Modernization"
        },
        {
            "Definition": "DX Strategy",
            "Term": "Digital Transformation (DX)"
        },
        {
            "Definition": "Information Security Portal",
            "Term": "Information Security Policy"
        },
        {
            "Definition": "ARB Registration, SRB Registration",
            "Term": "ARB/SRB Review Process"
        },
        {
            "Definition": "VIA Project Initialization and GKE,VERTEX AI",
            "Term": "Value Identification Acceleration - VIA"
        }
    ]
},
"References": {
    "5.1.3 References": {
        "5.1.3.1 Required Project References": [],
        "5.1.3.2 Standards and other References": []
    }
},
"Resources_Guidance": {
    "5.2 Resources and Guidance": [
        {
            "Link": "CCoE Sharepoint, CCoE Team Room",
            "Resource": "Cloud Center of Excellence (CCOE)"
        },
        {
            "Link": "Global Architecture Guiding Principles, Technology Architecture Working Group (TAWG), TAWG - Home",
            "Resource": "Architecture"
        },
        {
            "Link": "DevOps Transformation, DevOps Strategy, CI/CD Strategy, Orchestration and Workflow, Tool Selection and Considerations",
            "Resource": "SP&T DevOps Transformation"
        },
        {
            "Link": "Security Portal Home, Federal InfoSec, TMF Adherence, TM Forum",
            "Resource": "Data Security"
        },
        {
            "Link": "API Strategic Architecture, API Enablement",
            "Resource": "API Enablement"
        },
        {
            "Link": "App Modernization Team Room",
            "Resource": "Application Modernization"
        },
        {
            "Link": "DX Strategy",
            "Resource": "Digital Transformation (DX)"
        },
        {
            "Link": "Information Security Portal",
            "Resource": "Information Security Policy"
        },
        {
            "Link": "ARB Registration, SRB Registration",
            "Resource": "ARB/SRB Review Process"
        },
        {
            "Link": "VIA Project Initialization and GKE,VERTEX AI",
            "Resource": "Value Identification Acceleration - VIA"
        }
    ],
    "5.3 Google APIs": [
        {
            "api": "secretmanager.googleapis.com, certificatemanager.googleapis.com, servicenetworking.googleapis.com, networkmanagement.googleapis.com, run.googleapis.com, sqladmin.googleapis.com, cloudfunctions.googleapis.com, vpcaccess.googleapis.com",
            "service": "DEFAULT"
        }
    ]
}
}
    }
}

Example 2:

if app_name or mal_name or m_name has NETQT and PX.
{
    "NETQT": {
        "technical_architecture": {
"project_access": {
    "2.02 Technology Stack": "GKE",
    "2.04 Project Access": [
        {
            "Description": "admin group",
            "Environment": "dev, qa, prod",
            "Group": "admin",
            "Owners": "nash.vedire@lumen.com,eric.gates@lumen.com,tejinder.singh@lumen.com,richard.e.nelson@lumen.com,<otherowner>"
        },
        {
            "Description": "dev team group",
            "Environment": "dev, qa, prod",
            "Group": "dev-team",
            "Owners": "nash.vedire@lumen.com,eric.gates@lumen.com,tejinder.singh@lumen.com,richard.e.nelson@lumen.com,<otherowner>"
        },
        {
            "Description": "viewer group",
            "Environment": "dev, qa, prod",
            "Group": "viewer",
            "Owners": "nash.vedire@lumen.com,eric.gates@lumen.com,tejinder.singh@lumen.com,richard.e.nelson@lumen.com,<otherowner>"
        },
        {
            "Description": "ops team group",
            "Environment": "dev, qa, prod",
            "Group": "ops-team",
            "Owners": "nash.vedire@lumen.com,eric.gates@lumen.com,tejinder.singh@lumen.com,richard.e.nelson@lumen.com,<otherowner>"
        }
    ]
},
"key_components": {
    "2.05 Key Components": {
        "- **2.5.1 Components**": [
            {
                "Service": "GKE",
                "dev": "$Machine Type:eg.\"e2-standard-4\"$\n            $Disk Size:\"100\"$\n            $Disk Type:\"pd-standard\"$\n            Region: \"us-central1\"\n            $POD:18$\n            $CPU&MEMORY:12 CPU & 64 GB (@ Cluster level)$\n            $SVS:18$\n            $CPU&MEMORY:16 CPUs & 64 GB (@ Cluster level)$\n            $sgs_gke_cp_cidr:/28$\n            $sgs_gke_node_cidr:TBD$\n            $sgs_gke_pods_cidr,:TBD$\n            $sgs_gke_svs_cidr:TBD$",
                "prod": "$Machine Type:eg.\"e2-standard-4\"$\n            $Disk Size:\"100\"$\n            $Disk Type:\"pd-standard\"$\n            Region: \"us-central1\"\n            $POD:12(4 replicas for each service) 2GB/pod$\n            $CPU&MEMORY:12 CPU & 64 GB (@ Cluster level)$\n            $SVS:12(4 replicas for each service) +Appd- 2pods + Splunk-2pods + ingress controller$\n            $CPU&MEMORY: 16 CPUs & 64 GB (@ Cluster level)$ \n            $sgs_gke_cp_cidr:/28$\n            $sgs_gke_node_cidr:TBD$ \n            $sgs_gke_pods_cidr,:TBD$\n            $sgs_gke_svs_cidr:TBD$",
                "qa": "$Machine Type:eg.\"e2-standard-4\"$\n            $Disk Size:\"100\"$\n            $Disk Type:\"pd-standard\"$\n            Region: \"us-central1\"\n            $POD:18$\n            $CPU&MEMORY:12 CPU & 64 GB (@ Cluster level)$\n            $SVS:18$\n            $CPU&MEMORY:16 CPUs & 64 GB (@ Cluster level)$  \n            $sgs_gke_cp_cidr:/28$\n            $sgs_gke_node_cidr:TBD$ \n            $sgs_gke_pods_cidr,:TBD$\n            $sgs_gke_svs_cidr:TBD$"
            },
            {
                "Service": "INTERNAL-DNS",
                "dev": "*.sgs.mm.gcp.dev.intranet",
                "prod": "*.sgs.mm.gcp.corp.intranet",
                "qa": "*.sgs.mm.gcp.qa.test.intranet"
            }
        ]
    }
},
"service_accounts": {
    "2.09 Service Accounts": [
        {
            "Environment": "dev, qa, prod",
            "JSON Key": "NA",
            "Permission": "Compute Instance Admin (v1), Compute Network User, Kubernetes Engine Admin, Kubernetes Engine Host Service Agent User, Kubernetes Engine Node Service Account, Secret Manager Secret Accessor",
            "Service": "GKE",
            "Service Account": "sa-gke"
        },
        {
            "Environment": "dev, qa, prod",
            "JSON Key": "Yes",
            "Permission": "Kubernetes Engine Admin",
            "Service": "GKE",
            "Service Account": "sa-cicd"
        }
    ]
},
"firewall": {
    "2.12 Firewall Rules": [
        {
            "Actions": "Allow",
            "Destination": "sgs_gke_cp_cidr, sgs_gke_node_cidr, sgs_gke_pods_cidr, sgs_gke_svs_cidr",
            "Direction": "Egress",
            "Network": "PRJ",
            "Port": "All",
            "Protocol": "TCP",
            "Source IP": "sgs_gke_cp_cidr, sgs_gke_node_cidr, sgs_gke_pods_cidr, sgs_gke_svs_cidr"
        },
        {
            "Actions": "Allow",
            "Destination": "sgs_gke_cp_cidr, sgs_gke_node_cidr, sgs_gke_pods_cidr, sgs_gke_svs_cidr",
            "Direction": "Ingress",
            "Network": "PRJ",
            "Port": "All",
            "Protocol": "TCP",
            "Source IP": "sgs_gke_cp_cidr, sgs_gke_node_cidr, sgs_gke_pods_cidr, sgs_gke_svs_cidr"
        },
        {
            "Actions": "Deny",
            "Destination": "sgs_gke_node_cidr",
            "Direction": "Ingress",
            "Network": "PRJ",
            "Port": "22",
            "Protocol": "TCP",
            "Source IP": "0.0.0.0/0"
        },
        {
            "Actions": "Allow",
            "Destination": "sgs_gke_cp_cidr",
            "Direction": "Egress",
            "Network": "PRJ",
            "Port": "443",
            "Protocol": "TCP",
            "Source IP": "NON SOX JUMP HOST CIDR"
        },
        {
            "Actions": "Allow",
            "Destination": "sgs_gke_node_cidr",
            "Direction": "Egress",
            "Network": "PRJ",
            "Port": "443",
            "Protocol": "TCP",
            "Source IP": "jenkins_us_central1_cidrs"
        }
    ]
},
"iam": {
    "2.13 IAM": [
        {
            "Environment": "dev, qa, prod",
            "Permission": "Secret Manager Secret Accessor, Secret Manager Secret Version Manager, Tech Support Editor, Logs Configuration Writer, Logs Viewer, Monitoring Alert Policy Editor, Monitoring Editor, Monitoring Notification Channel Editor, viewer",
            "Principal": "dev-team, ops-team",
            "Service": "Default"
        },
        {
            "Environment": "dev, qa, prod",
            "Permission": "viewer",
            "Principal": "viewer",
            "Service": "Default"
        },
        {
            "Environment": "dev, qa, prod",
            "Permission": "Kubernetes Engine Developer",
            "Principal": "dev-team, ops-team",
            "Service": "GKE"
        }
    ]
}
},
        "devops_and_operations": {
"devops": {
    "3. Development and Operations": {
        "3.1 Development Environment": "Developers will utilize Cloud Code for VS Code to interact with the GKE cluster.  The development environment will include a local Kubernetes cluster for testing and debugging.  Version control will be managed using Git, and code will be stored in a centralized repository. Continuous Integration/Continuous Delivery (CI/CD) pipelines will be implemented using tools such as Jenkins or Google Cloud Build to automate testing and deployment.",
        "3.2 Deployment Process": "The deployment process will leverage GKE's built-in capabilities for automated deployments.  Container images will be built and pushed to Google Container Registry (GCR). Kubernetes manifests will define the application's deployment specifications.  Deployments will be rolled out using techniques like blue/green deployments or canary deployments to minimize disruption.  Automated rollback mechanisms will be implemented to handle deployment failures."
    }
},
"ops": {
    "3.3 Operational Support Model": [
        {
            "Component": "GKE",
            "DEV": "App Team",
            "PROD": "App Team",
            "QA": "App Team",
            "UAT": "App Team"
        },
        {
            "Component": "API Gateway",
            "DEV": "App Team",
            "PROD": "App Team",
            "QA": "App Team",
            "UAT": "App Team"
        },
        {
            "Component": "DNS Records",
            "DEV": "MM Cloud Team",
            "PROD": "MM Cloud Team",
            "QA": "MM Cloud Team",
            "UAT": "MM Cloud Team"
        },
        {
            "Component": "SSL Certificates",
            "DEV": "MM Cloud Team",
            "PROD": "MM Cloud Team",
            "QA": "MM Cloud Team",
            "UAT": "MM Cloud Team"
        },
        {
            "Component": "Firewall Rules",
            "DEV": "MM Cloud Team",
            "PROD": "MM Cloud Team",
            "QA": "MM Cloud Team",
            "UAT": "MM Cloud Team"
        },
        {
            "Component": "Application Deployment Image",
            "DEV": "App Team",
            "PROD": "App Team",
            "QA": "App Team",
            "UAT": "App Team"
        },
        {
            "Component": "Application Logging",
            "DEV": "App Team",
            "PROD": "App Team",
            "QA": "App Team",
            "UAT": "App Team"
        }
    ]
},
"service": {
    "3.4.1 Service Level Indicators (SLI)": "An automated health check is performed to monitor service health.",
    "3.4.2 Service Level Objective (SLO)": "The service must maintain at least 99.5% availability."
},
"governance": {
    "3.4.3 Recovery Point Objective (RPO)": "The acceptable amount of data loss in a catastrophic failure must be specified (e.g., 1 minute, 1 hour, 1 day, etc.).",
    "3.4.4 Recovery Time Objective (RTO)": "The maximum acceptable downtime for the application following a catastrophic failure needs to be defined (e.g., 1 hour, 4 hours, 1 day, etc.).",
    "3.6 Governance": "Governance requirements (PCI, CMMC, SOX, etc.) and adherence processes or waivers need to be identified and documented."
}
},
        "risks_and_assumptions": {
"Design_Assumptions": {
    "4. Risks, Assumptions, and Decisions": {
        "4.1 Design Assumptions": [
            {
                "Assumption": "Connections from services in GCP to on-premises via interconnect using nginx, NAT'd IPs, and traceability are required.",
                "Assumption ID": "A1",
                "Validation Criteria": "Verify the interconnect is configured and tested, nginx is installed and configured, NAT'd IPs are configured, and traceability is implemented."
            },
            {
                "Assumption": "Dependencies are defined and documented.",
                "Assumption ID": "A2",
                "Validation Criteria": "Review the dependency table (Table 5) to ensure all dependencies are identified and documented."
            },
            {
                "Assumption": "Design risks are identified and mitigated.",
                "Assumption ID": "A3",
                "Validation Criteria": "Review the design risk table (Table 6) to ensure all risks are identified and mitigation strategies are in place."
            },
            {
                "Assumption": "Key decisions regarding interconnect setup and IP visibility are documented and implemented.",
                "Assumption ID": "A4",
                "Validation Criteria": "Review the key decisions table and verify that the interconnect setup and IP visibility are implemented as documented."
            }
        ]
    }
},
"Dependencies": {
    "4.2 Dependencies": [
        {
            "Date Required": "2025-05-27",
            "Dependency": "GKE",
            "Provider": "Google",
            "Reason": "Required for deploying containerized applications"
        },
        {
            "Date Required": "2025-05-27",
            "Dependency": "GCE",
            "Provider": "Google",
            "Reason": "Required for hosting virtual machines"
        },
        {
            "Date Required": "2025-05-27",
            "Dependency": "Vertex AI",
            "Provider": "Google",
            "Reason": "Required for building and deploying machine learning models"
        },
        {
            "Date Required": "2025-05-27",
            "Dependency": "Memorystore",
            "Provider": "Google",
            "Reason": "Required for caching data"
        },
        {
            "Date Required": "2025-05-27",
            "Dependency": "Google Load Balancer - External",
            "Provider": "Google",
            "Reason": "Required for load balancing traffic to services"
        },
        {
            "Date Required": "2025-05-27",
            "Dependency": "Cloud Run",
            "Provider": "Google",
            "Reason": "Required for running serverless applications"
        }
    ]
},
"Design_Risks": {
    "4.3 Design Risks": [
        {
            "Category": "Security",
            "Date Accepted/Removed": "2025-05-27",
            "ID": "DR-1",
            "Likelihood (Low/Med/High)": "Medium",
            "Risks Impacts and Actions": "Potential for unauthorized access to on-premises systems through the interconnect. Implement robust authentication and authorization mechanisms, including multi-factor authentication, to mitigate this risk."
        },
        {
            "Category": "Performance",
            "Date Accepted/Removed": "2025-05-27",
            "ID": "DR-2",
            "Likelihood (Low/Med/High)": "Medium",
            "Risks Impacts and Actions": "Latency issues due to network connectivity between GCP and on-premises systems. Utilize a high-speed interconnect with sufficient bandwidth and optimize network configurations to minimize latency."
        },
        {
            "Category": "Reliability",
            "Date Accepted/Removed": "2025-05-27",
            "ID": "DR-3",
            "Likelihood (Low/Med/High)": "Low",
            "Risks Impacts and Actions": "Interconnect failures may disrupt communication between GCP and on-premises systems. Implement redundancy and failover mechanisms, such as multiple interconnects, to ensure continued communication."
        },
        {
            "Category": "Cost",
            "Date Accepted/Removed": "2025-05-27",
            "ID": "DR-4",
            "Likelihood (Low/Med/High)": "Medium",
            "Risks Impacts and Actions": "High cost associated with using an interconnect and NAT services.  Evaluate cost-effective solutions and explore alternative connectivity options."
        },
        {
            "Category": "Complexity",
            "Date Accepted/Removed": "2025-05-27",
            "ID": "DR-5",
            "Likelihood (Low/Med/High)": "High",
            "Risks Impacts and Actions": "Managing the interconnect and associated security policies can be complex.  Provide clear documentation and training to ensure smooth operations and minimize complexity."
        }
    ]
},
"Key_Decisions": {
    "4.4 Key Decisions": [
        {
            "Category": "Connectivity",
            "Date Accepted/Removed": "2025-05-27",
            "Date Raised": "2025-05-13",
            "Decision Description": "Interconnect setup and IP visibility - How to ensure the on-premises IPs are visible within the GCP environment while maintaining security and traceability.",
            "ID": "D-001",
            "Likelihood": "High"
        },
        {
            "Category": "Security",
            "Date Accepted/Removed": "2025-05-27",
            "Date Raised": "2025-05-13",
            "Decision Description": "Implementation of security measures for the NATed IPs and the interconnect connection.",
            "ID": "D-002",
            "Likelihood": "High"
        },
        {
            "Category": "Performance",
            "Date Accepted/Removed": "2025-05-27",
            "Date Raised": "2025-05-13",
            "Decision Description": "Performance impact of NATing and the interconnect on overall application latency and response time.",
            "ID": "D-003",
            "Likelihood": "Medium"
        },
        {
            "Category": "Scalability",
            "Date Accepted/Removed": "2025-05-27",
            "Date Raised": "2025-05-13",
            "Decision Description": "Scalability of the interconnect and NAT solution to handle anticipated growth in data traffic.",
            "ID": "D-004",
            "Likelihood": "Medium"
        },
        {
            "Category": "Management",
            "Date Accepted/Removed": "2025-05-27",
            "Date Raised": "2025-05-13",
            "Decision Description": "Management and monitoring of the interconnect and NAT infrastructure within GCP.",
            "ID": "D-005",
            "Likelihood": "Medium"
        }
    ]
}
},
        "appendix": {
"Abbreviations": {
    "5. Appendix": {
        "5.1 Abbreviations and Glossary": {
            "5.1.1 Abbreviations": [
                {
                    "Abbreviation/Acronym": "GKE",
                    "Description": "Google Kubernetes Engine"
                },
                {
                    "Abbreviation/Acronym": "VERTEX AI",
                    "Description": "Vertex AI is a machine learning platform"
                }
            ]
        }
    }
},
"Glossary": {
    "5.1.2 Glossary": [
        {
            "Definition": "Relevant acronyms and terms for the project are defined in this section.",
            "Term": "Abbreviations and Glossary"
        },
        {
            "Definition": "Project-related abbreviations are defined here.",
            "Term": "Abbreviations"
        },
        {
            "Definition": "Project-related terms are defined here to aid in understanding the application.",
            "Term": "Glossary"
        },
        {
            "Definition": "External resources that the project interacts with to function properly. Explanations of these interactions and diagrams identifying the interaction points should be included.",
            "Term": "Required Project References"
        },
        {
            "Definition": "References to regulatory or standards required for this project, including versions adhered to, should be listed.",
            "Term": "Standards and other References"
        },
        {
            "Definition": "Cloud Center of Excellence",
            "Term": "Resource"
        },
        {
            "Definition": "Global Architecture Guiding Principles, Technology Architecture Working Group (TAWG), TAWG - Home",
            "Term": "Architecture"
        },
        {
            "Definition": "DevOps Transformation, DevOps Strategy, CI/CD Strategy, Orchestration and Workflow, Tool Selection and Considerations",
            "Term": "SP&T DevOps Transformation"
        },
        {
            "Definition": "Security Portal Home, Federal InfoSec, TMF Adherence, TM Forum",
            "Term": "Data Security"
        },
        {
            "Definition": "API Strategic Architecture, API Enablement",
            "Term": "API Enablement"
        },
        {
            "Definition": "App Modernization Team Room",
            "Term": "Application Modernization"
        },
        {
            "Definition": "DX Strategy",
            "Term": "Digital Transformation (DX)"
        },
        {
            "Definition": "Information Security Portal",
            "Term": "Information Security Policy"
        },
        {
            "Definition": "ARB Registration, SRB Registration",
            "Term": "ARB/SRB Review Process"
        },
        {
            "Definition": "VIA Project Initialization and GKE,VERTEX AI",
            "Term": "Value Identification Acceleration - VIA"
        }
    ]
},
"References": {
    "5.1.3 References": {
        "5.1.3.1 Required Project References": [],
        "5.1.3.2 Standards and other References": []
    }
},
"Resources_Guidance": {
    "5.2 Resources and Guidance": [
        {
            "Link": "CCoE Sharepoint, CCoE Team Room",
            "Resource": "Cloud Center of Excellence (CCOE)"
        },
        {
            "Link": "Global Architecture Guiding Principles, Technology Architecture Working Group (TAWG), TAWG - Home",
            "Resource": "Architecture"
        },
        {
            "Link": "DevOps Transformation, DevOps Strategy, CI/CD Strategy, Orchestration and Workflow, Tool Selection and Considerations",
            "Resource": "SP&T DevOps Transformation"
        },
        {
            "Link": "Security Portal Home, Federal InfoSec, TMF Adherence, TM Forum",
            "Resource": "Data Security"
        },
        {
            "Link": "API Strategic Architecture, API Enablement",
            "Resource": "API Enablement"
        },
        {
            "Link": "App Modernization Team Room",
            "Resource": "Application Modernization"
        },
        {
            "Link": "DX Strategy",
            "Resource": "Digital Transformation (DX)"
        },
        {
            "Link": "Information Security Portal",
            "Resource": "Information Security Policy"
        },
        {
            "Link": "ARB Registration, SRB Registration",
            "Resource": "ARB/SRB Review Process"
        },
        {
            "Link": "VIA Project Initialization and GKE,VERTEX AI",
            "Resource": "Value Identification Acceleration - VIA"
        }
    ],
    "5.3 Google APIs": [
        {
            "api": "secretmanager.googleapis.com, certificatemanager.googleapis.com, servicenetworking.googleapis.com, networkmanagement.googleapis.com, run.googleapis.com, sqladmin.googleapis.com, cloudfunctions.googleapis.com, vpcaccess.googleapis.com",
            "service": "DEFAULT"
        }
    ]
}
}
    }
,
    "PX": {
        "technical_architecture": {
"project_access": {
    "2.02 Technology Stack": "GKE",
    "2.04 Project Access": [
        {
            "Description": "admin group",
            "Environment": "dev, qa, prod",
            "Group": "admin",
            "Owners": "nash.vedire@lumen.com,eric.gates@lumen.com,tejinder.singh@lumen.com,richard.e.nelson@lumen.com,<otherowner>"
        },
        {
            "Description": "dev team group",
            "Environment": "dev, qa, prod",
            "Group": "dev-team",
            "Owners": "nash.vedire@lumen.com,eric.gates@lumen.com,tejinder.singh@lumen.com,richard.e.nelson@lumen.com,<otherowner>"
        },
        {
            "Description": "viewer group",
            "Environment": "dev, qa, prod",
            "Group": "viewer",
            "Owners": "nash.vedire@lumen.com,eric.gates@lumen.com,tejinder.singh@lumen.com,richard.e.nelson@lumen.com,<otherowner>"
        },
        {
            "Description": "ops team group",
            "Environment": "dev, qa, prod",
            "Group": "ops-team",
            "Owners": "nash.vedire@lumen.com,eric.gates@lumen.com,tejinder.singh@lumen.com,richard.e.nelson@lumen.com,<otherowner>"
        }
    ]
},
"key_components": {
    "2.05 Key Components": {
        "- **2.5.1 Components**": [
            {
                "Service": "GKE",
                "dev": "$Machine Type:eg.\"e2-standard-4\"$\n            $Disk Size:\"100\"$\n            $Disk Type:\"pd-standard\"$\n            Region: \"us-central1\"\n            $POD:18$\n            $CPU&MEMORY:12 CPU & 64 GB (@ Cluster level)$\n            $SVS:18$\n            $CPU&MEMORY:16 CPUs & 64 GB (@ Cluster level)$\n            $sgs_gke_cp_cidr:/28$\n            $sgs_gke_node_cidr:TBD$\n            $sgs_gke_pods_cidr,:TBD$\n            $sgs_gke_svs_cidr:TBD$",
                "prod": "$Machine Type:eg.\"e2-standard-4\"$\n            $Disk Size:\"100\"$\n            $Disk Type:\"pd-standard\"$\n            Region: \"us-central1\"\n            $POD:12(4 replicas for each service) 2GB/pod$\n            $CPU&MEMORY:12 CPU & 64 GB (@ Cluster level)$\n            $SVS:12(4 replicas for each service) +Appd- 2pods + Splunk-2pods + ingress controller$\n            $CPU&MEMORY: 16 CPUs & 64 GB (@ Cluster level)$ \n            $sgs_gke_cp_cidr:/28$\n            $sgs_gke_node_cidr:TBD$ \n            $sgs_gke_pods_cidr,:TBD$\n            $sgs_gke_svs_cidr:TBD$",
                "qa": "$Machine Type:eg.\"e2-standard-4\"$\n            $Disk Size:\"100\"$\n            $Disk Type:\"pd-standard\"$\n            Region: \"us-central1\"\n            $POD:18$\n            $CPU&MEMORY:12 CPU & 64 GB (@ Cluster level)$\n            $SVS:18$\n            $CPU&MEMORY:16 CPUs & 64 GB (@ Cluster level)$  \n            $sgs_gke_cp_cidr:/28$\n            $sgs_gke_node_cidr:TBD$ \n            $sgs_gke_pods_cidr,:TBD$\n            $sgs_gke_svs_cidr:TBD$"
            },
            {
                "Service": "INTERNAL-DNS",
                "dev": "*.sgs.mm.gcp.dev.intranet",
                "prod": "*.sgs.mm.gcp.corp.intranet",
                "qa": "*.sgs.mm.gcp.qa.test.intranet"
            }
        ]
    }
},
"service_accounts": {
    "2.09 Service Accounts": [
        {
            "Environment": "dev, qa, prod",
            "JSON Key": "NA",
            "Permission": "Compute Instance Admin (v1), Compute Network User, Kubernetes Engine Admin, Kubernetes Engine Host Service Agent User, Kubernetes Engine Node Service Account, Secret Manager Secret Accessor",
            "Service": "GKE",
            "Service Account": "sa-gke"
        },
        {
            "Environment": "dev, qa, prod",
            "JSON Key": "Yes",
            "Permission": "Kubernetes Engine Admin",
            "Service": "GKE",
            "Service Account": "sa-cicd"
        }
    ]
},
"firewall": {
    "2.12 Firewall Rules": [
        {
            "Actions": "Allow",
            "Destination": "sgs_gke_cp_cidr, sgs_gke_node_cidr, sgs_gke_pods_cidr, sgs_gke_svs_cidr",
            "Direction": "Egress",
            "Network": "PRJ",
            "Port": "All",
            "Protocol": "TCP",
            "Source IP": "sgs_gke_cp_cidr, sgs_gke_node_cidr, sgs_gke_pods_cidr, sgs_gke_svs_cidr"
        },
        {
            "Actions": "Allow",
            "Destination": "sgs_gke_cp_cidr, sgs_gke_node_cidr, sgs_gke_pods_cidr, sgs_gke_svs_cidr",
            "Direction": "Ingress",
            "Network": "PRJ",
            "Port": "All",
            "Protocol": "TCP",
            "Source IP": "sgs_gke_cp_cidr, sgs_gke_node_cidr, sgs_gke_pods_cidr, sgs_gke_svs_cidr"
        },
        {
            "Actions": "Deny",
            "Destination": "sgs_gke_node_cidr",
            "Direction": "Ingress",
            "Network": "PRJ",
            "Port": "22",
            "Protocol": "TCP",
            "Source IP": "0.0.0.0/0"
        },
        {
            "Actions": "Allow",
            "Destination": "sgs_gke_cp_cidr",
            "Direction": "Egress",
            "Network": "PRJ",
            "Port": "443",
            "Protocol": "TCP",
            "Source IP": "NON SOX JUMP HOST CIDR"
        },
        {
            "Actions": "Allow",
            "Destination": "sgs_gke_node_cidr",
            "Direction": "Egress",
            "Network": "PRJ",
            "Port": "443",
            "Protocol": "TCP",
            "Source IP": "jenkins_us_central1_cidrs"
        }
    ]
},
"iam": {
    "2.13 IAM": [
        {
            "Environment": "dev, qa, prod",
            "Permission": "Secret Manager Secret Accessor, Secret Manager Secret Version Manager, Tech Support Editor, Logs Configuration Writer, Logs Viewer, Monitoring Alert Policy Editor, Monitoring Editor, Monitoring Notification Channel Editor, viewer",
            "Principal": "dev-team, ops-team",
            "Service": "Default"
        },
        {
            "Environment": "dev, qa, prod",
            "Permission": "viewer",
            "Principal": "viewer",
            "Service": "Default"
        },
        {
            "Environment": "dev, qa, prod",
            "Permission": "Kubernetes Engine Developer",
            "Principal": "dev-team, ops-team",
            "Service": "GKE"
        }
    ]
}
},
        "devops_and_operations": {
"devops": {
    "3. Development and Operations": {
        "3.1 Development Environment": "Developers will utilize Cloud Code for VS Code to interact with the GKE cluster.  The development environment will include a local Kubernetes cluster for testing and debugging.  Version control will be managed using Git, and code will be stored in a centralized repository. Continuous Integration/Continuous Delivery (CI/CD) pipelines will be implemented using tools such as Jenkins or Google Cloud Build to automate testing and deployment.",
        "3.2 Deployment Process": "The deployment process will leverage GKE's built-in capabilities for automated deployments.  Container images will be built and pushed to Google Container Registry (GCR). Kubernetes manifests will define the application's deployment specifications.  Deployments will be rolled out using techniques like blue/green deployments or canary deployments to minimize disruption.  Automated rollback mechanisms will be implemented to handle deployment failures."
    }
},
"ops": {
    "3.3 Operational Support Model": [
        {
            "Component": "GKE",
            "DEV": "App Team",
            "PROD": "App Team",
            "QA": "App Team",
            "UAT": "App Team"
        },
        {
            "Component": "API Gateway",
            "DEV": "App Team",
            "PROD": "App Team",
            "QA": "App Team",
            "UAT": "App Team"
        },
        {
            "Component": "DNS Records",
            "DEV": "MM Cloud Team",
            "PROD": "MM Cloud Team",
            "QA": "MM Cloud Team",
            "UAT": "MM Cloud Team"
        },
        {
            "Component": "SSL Certificates",
            "DEV": "MM Cloud Team",
            "PROD": "MM Cloud Team",
            "QA": "MM Cloud Team",
            "UAT": "MM Cloud Team"
        },
        {
            "Component": "Firewall Rules",
            "DEV": "MM Cloud Team",
            "PROD": "MM Cloud Team",
            "QA": "MM Cloud Team",
            "UAT": "MM Cloud Team"
        },
        {
            "Component": "Application Deployment Image",
            "DEV": "App Team",
            "PROD": "App Team",
            "QA": "App Team",
            "UAT": "App Team"
        },
        {
            "Component": "Application Logging",
            "DEV": "App Team",
            "PROD": "App Team",
            "QA": "App Team",
            "UAT": "App Team"
        }
    ]
},
"service": {
    "3.4.1 Service Level Indicators (SLI)": "An automated health check is performed to monitor service health.",
    "3.4.2 Service Level Objective (SLO)": "The service must maintain at least 99.5% availability."
},
"governance": {
    "3.4.3 Recovery Point Objective (RPO)": "The acceptable amount of data loss in a catastrophic failure must be specified (e.g., 1 minute, 1 hour, 1 day, etc.).",
    "3.4.4 Recovery Time Objective (RTO)": "The maximum acceptable downtime for the application following a catastrophic failure needs to be defined (e.g., 1 hour, 4 hours, 1 day, etc.).",
    "3.6 Governance": "Governance requirements (PCI, CMMC, SOX, etc.) and adherence processes or waivers need to be identified and documented."
}
},
        "risks_and_assumptions": {
"Design_Assumptions": {
    "4. Risks, Assumptions, and Decisions": {
        "4.1 Design Assumptions": [
            {
                "Assumption": "Connections from services in GCP to on-premises via interconnect using nginx, NAT'd IPs, and traceability are required.",
                "Assumption ID": "A1",
                "Validation Criteria": "Verify the interconnect is configured and tested, nginx is installed and configured, NAT'd IPs are configured, and traceability is implemented."
            },
            {
                "Assumption": "Dependencies are defined and documented.",
                "Assumption ID": "A2",
                "Validation Criteria": "Review the dependency table (Table 5) to ensure all dependencies are identified and documented."
            },
            {
                "Assumption": "Design risks are identified and mitigated.",
                "Assumption ID": "A3",
                "Validation Criteria": "Review the design risk table (Table 6) to ensure all risks are identified and mitigation strategies are in place."
            },
            {
                "Assumption": "Key decisions regarding interconnect setup and IP visibility are documented and implemented.",
                "Assumption ID": "A4",
                "Validation Criteria": "Review the key decisions table and verify that the interconnect setup and IP visibility are implemented as documented."
            }
        ]
    }
},
"Dependencies": {
    "4.2 Dependencies": [
        {
            "Date Required": "2025-05-27",
            "Dependency": "GKE",
            "Provider": "Google",
            "Reason": "Required for deploying containerized applications"
        },
        {
            "Date Required": "2025-05-27",
            "Dependency": "GCE",
            "Provider": "Google",
            "Reason": "Required for hosting virtual machines"
        },
        {
            "Date Required": "2025-05-27",
            "Dependency": "Vertex AI",
            "Provider": "Google",
            "Reason": "Required for building and deploying machine learning models"
        },
        {
            "Date Required": "2025-05-27",
            "Dependency": "Memorystore",
            "Provider": "Google",
            "Reason": "Required for caching data"
        },
        {
            "Date Required": "2025-05-27",
            "Dependency": "Google Load Balancer - External",
            "Provider": "Google",
            "Reason": "Required for load balancing traffic to services"
        },
        {
            "Date Required": "2025-05-27",
            "Dependency": "Cloud Run",
            "Provider": "Google",
            "Reason": "Required for running serverless applications"
        }
    ]
},
"Design_Risks": {
    "4.3 Design Risks": [
        {
            "Category": "Security",
            "Date Accepted/Removed": "2025-05-27",
            "ID": "DR-1",
            "Likelihood (Low/Med/High)": "Medium",
            "Risks Impacts and Actions": "Potential for unauthorized access to on-premises systems through the interconnect. Implement robust authentication and authorization mechanisms, including multi-factor authentication, to mitigate this risk."
        },
        {
            "Category": "Performance",
            "Date Accepted/Removed": "2025-05-27",
            "ID": "DR-2",
            "Likelihood (Low/Med/High)": "Medium",
            "Risks Impacts and Actions": "Latency issues due to network connectivity between GCP and on-premises systems. Utilize a high-speed interconnect with sufficient bandwidth and optimize network configurations to minimize latency."
        },
        {
            "Category": "Reliability",
            "Date Accepted/Removed": "2025-05-27",
            "ID": "DR-3",
            "Likelihood (Low/Med/High)": "Low",
            "Risks Impacts and Actions": "Interconnect failures may disrupt communication between GCP and on-premises systems. Implement redundancy and failover mechanisms, such as multiple interconnects, to ensure continued communication."
        },
        {
            "Category": "Cost",
            "Date Accepted/Removed": "2025-05-27",
            "ID": "DR-4",
            "Likelihood (Low/Med/High)": "Medium",
            "Risks Impacts and Actions": "High cost associated with using an interconnect and NAT services.  Evaluate cost-effective solutions and explore alternative connectivity options."
        },
        {
            "Category": "Complexity",
            "Date Accepted/Removed": "2025-05-27",
            "ID": "DR-5",
            "Likelihood (Low/Med/High)": "High",
            "Risks Impacts and Actions": "Managing the interconnect and associated security policies can be complex.  Provide clear documentation and training to ensure smooth operations and minimize complexity."
        }
    ]
},
"Key_Decisions": {
    "4.4 Key Decisions": [
        {
            "Category": "Connectivity",
            "Date Accepted/Removed": "2025-05-27",
            "Date Raised": "2025-05-13",
            "Decision Description": "Interconnect setup and IP visibility - How to ensure the on-premises IPs are visible within the GCP environment while maintaining security and traceability.",
            "ID": "D-001",
            "Likelihood": "High"
        },
        {
            "Category": "Security",
            "Date Accepted/Removed": "2025-05-27",
            "Date Raised": "2025-05-13",
            "Decision Description": "Implementation of security measures for the NATed IPs and the interconnect connection.",
            "ID": "D-002",
            "Likelihood": "High"
        },
        {
            "Category": "Performance",
            "Date Accepted/Removed": "2025-05-27",
            "Date Raised": "2025-05-13",
            "Decision Description": "Performance impact of NATing and the interconnect on overall application latency and response time.",
            "ID": "D-003",
            "Likelihood": "Medium"
        },
        {
            "Category": "Scalability",
            "Date Accepted/Removed": "2025-05-27",
            "Date Raised": "2025-05-13",
            "Decision Description": "Scalability of the interconnect and NAT solution to handle anticipated growth in data traffic.",
            "ID": "D-004",
            "Likelihood": "Medium"
        },
        {
            "Category": "Management",
            "Date Accepted/Removed": "2025-05-27",
            "Date Raised": "2025-05-13",
            "Decision Description": "Management and monitoring of the interconnect and NAT infrastructure within GCP.",
            "ID": "D-005",
            "Likelihood": "Medium"
        }
    ]
}
},
        "appendix": {
"Abbreviations": {
    "5. Appendix": {
        "5.1 Abbreviations and Glossary": {
            "5.1.1 Abbreviations": [
                {
                    "Abbreviation/Acronym": "GKE",
                    "Description": "Google Kubernetes Engine"
                },
                {
                    "Abbreviation/Acronym": "VERTEX AI",
                    "Description": "Vertex AI is a machine learning platform"
                }
            ]
        }
    }
},
"Glossary": {
    "5.1.2 Glossary": [
        {
            "Definition": "Relevant acronyms and terms for the project are defined in this section.",
            "Term": "Abbreviations and Glossary"
        },
        {
            "Definition": "Project-related abbreviations are defined here.",
            "Term": "Abbreviations"
        },
        {
            "Definition": "Project-related terms are defined here to aid in understanding the application.",
            "Term": "Glossary"
        },
        {
            "Definition": "External resources that the project interacts with to function properly. Explanations of these interactions and diagrams identifying the interaction points should be included.",
            "Term": "Required Project References"
        },
        {
            "Definition": "References to regulatory or standards required for this project, including versions adhered to, should be listed.",
            "Term": "Standards and other References"
        },
        {
            "Definition": "Cloud Center of Excellence",
            "Term": "Resource"
        },
        {
            "Definition": "Global Architecture Guiding Principles, Technology Architecture Working Group (TAWG), TAWG - Home",
            "Term": "Architecture"
        },
        {
            "Definition": "DevOps Transformation, DevOps Strategy, CI/CD Strategy, Orchestration and Workflow, Tool Selection and Considerations",
            "Term": "SP&T DevOps Transformation"
        },
        {
            "Definition": "Security Portal Home, Federal InfoSec, TMF Adherence, TM Forum",
            "Term": "Data Security"
        },
        {
            "Definition": "API Strategic Architecture, API Enablement",
            "Term": "API Enablement"
        },
        {
            "Definition": "App Modernization Team Room",
            "Term": "Application Modernization"
        },
        {
            "Definition": "DX Strategy",
            "Term": "Digital Transformation (DX)"
        },
        {
            "Definition": "Information Security Portal",
            "Term": "Information Security Policy"
        },
        {
            "Definition": "ARB Registration, SRB Registration",
            "Term": "ARB/SRB Review Process"
        },
        {
            "Definition": "VIA Project Initialization and GKE,VERTEX AI",
            "Term": "Value Identification Acceleration - VIA"
        }
    ]
},
"References": {
    "5.1.3 References": {
        "5.1.3.1 Required Project References": [],
        "5.1.3.2 Standards and other References": []
    }
},
"Resources_Guidance": {
    "5.2 Resources and Guidance": [
        {
            "Link": "CCoE Sharepoint, CCoE Team Room",
            "Resource": "Cloud Center of Excellence (CCOE)"
        },
        {
            "Link": "Global Architecture Guiding Principles, Technology Architecture Working Group (TAWG), TAWG - Home",
            "Resource": "Architecture"
        },
        {
            "Link": "DevOps Transformation, DevOps Strategy, CI/CD Strategy, Orchestration and Workflow, Tool Selection and Considerations",
            "Resource": "SP&T DevOps Transformation"
        },
        {
            "Link": "Security Portal Home, Federal InfoSec, TMF Adherence, TM Forum",
            "Resource": "Data Security"
        },
        {
            "Link": "API Strategic Architecture, API Enablement",
            "Resource": "API Enablement"
        },
        {
            "Link": "App Modernization Team Room",
            "Resource": "Application Modernization"
        },
        {
            "Link": "DX Strategy",
            "Resource": "Digital Transformation (DX)"
        },
        {
            "Link": "Information Security Portal",
            "Resource": "Information Security Policy"
        },
        {
            "Link": "ARB Registration, SRB Registration",
            "Resource": "ARB/SRB Review Process"
        },
        {
            "Link": "VIA Project Initialization and GKE,VERTEX AI",
            "Resource": "Value Identification Acceleration - VIA"
        }
    ],
    "5.3 Google APIs": [
        {
            "api": "secretmanager.googleapis.com, certificatemanager.googleapis.com, servicenetworking.googleapis.com, networkmanagement.googleapis.com, run.googleapis.com, sqladmin.googleapis.com, cloudfunctions.googleapis.com, vpcaccess.googleapis.com",
            "service": "DEFAULT"
        }
    ]
}
}
    }
}
"""

TERRAFORM_INSTRUCTION_PROMPT = """
Your task is to generate the terraform code in JSON Format using the tools to provide the output everytime.

**Inputs**
{ValidatedInput} 

Provide the tool output response in the Expected Ouptut Format.
Example:
technology_stack in "NETQT"=["AD GROUP", "CLOUDSQL(POSTGRESQL)"] 
{
"tech_stack":["AD GROUP", "CLOUDSQL(POSTGRESQL)"],
    "NETQT":{
        "adgroup": {
            "script": {
                "gcp.project-mm-sgs-dev.tf": "\nlocals {\n    sgs_dev_owners = [\"richard.e.nelson@lumen.com\"]\n\n}\nmodule \"prj-sgs-dev-001-admin\"{\n    source       = \"../modules/create_and_link\"\n    project_id   = \"prj-mm-sgs-dev-001\"\n    group_suffix = \"admin\"\n    group_owners = concat(local.sgs_dev_owners, local.gcp_ccoe_owners)\n}\nmodule \"prj-sgs-dev-001-dev-team\"{\n    source       = \"../modules/create_and_link\"\n    project_id   = \"prj-mm-sgs-dev-001\"\n    group_suffix = \"dev-team\"\n    group_owners = concat(local.sgs_dev_owners, local.gcp_ccoe_owners)\n}\nmodule \"prj-sgs-dev-001-viewer\"{\n    source       = \"../modules/create_and_link\"\n    project_id   = \"prj-mm-sgs-dev-001\"\n    group_suffix = \"viewer\"\n    group_owners = concat(local.sgs_dev_owners, local.gcp_ccoe_owners)\n}\nmodule \"prj-sgs-dev-001-ops-team\"{\n    source       = \"../modules/create_and_link\"\n    project_id   = \"prj-mm-sgs-dev-001\"\n    group_suffix = \"ops-team\"\n    group_owners = concat(local.sgs_dev_owners, local.gcp_ccoe_owners)\n}"
            }
        },
        "postgresql": {
            "script": {
                "main.tf": "module \"sql\" {\n  source = \"github.com/CenturyLink/tf-modules--gcp-tf-modules//sql?ref=4.1.7\"\n\n  project_id = var.project_id\n  region     = var.region\n\n  network_id                                    = var.network_id\n  subnetwork_name                               = var.subnetwork_name\n  authorized_networks                           = var.authorized_networks\n  ssl_mode                                      = var.ssl_mode\n  enable_private_path_for_google_cloud_services = var.enable_private_path_for_google_cloud_services\n\n  name                = var.name\n  instance_name       = var.instance_name\n  db_name             = var.db_name\n  tier                = var.tier\n  edition             = var.edition\n  database_version    = var.database_version\n  database_charset    = var.database_charset\n  database_collation  = var.database_collation\n  disk_size           = var.disk_size\n  disk_autoresize     = var.disk_autoresize\n  disk_type           = var.disk_type\n  availability_type   = var.availability_type\n  backup_enabled      = var.backup_enabled\n  binary_log_enabled  = var.binary_log_enabled\n  day                 = var.day\n  start_time          = var.start_time\n  deletion_protection = var.deletion_protection\n  activation_policy   = var.activation_policy\n  database_flags      = var.database_flags\n}    \n",
                "provider.tf": "provider \"google\" {}\nterraform {\n  required_version = \">=1.4.6\"\n\n  backend \"gcs\" {\n    bucket = \"lumen-mm-cloud-eng-terraform\"\n    prefix = \"mass-markets-cloud/technology/sgs/prj-mm-sgs-dev-001/sql/postgres-001\"\n    }\n}\n",
                "terraform.tfvars": "name                                          = \"sgs-dev\"\ninstance_name                                 = \"sgs-dev\"\nproject_id                                    = \"prj-mm-sgs-dev-001\"\nregion                                        = \"postgres_15\"\ndatabase_version                              = \"postgres_15\"\ntier                                          = eg. \nactivation_policy                             = \"ALWAYS\"\ndisk_size                                     = 100 \ndisk_autoresize                               = true \nbackup_enabled                                = true \nbinary_log_enabled                            = false \nretained_backups                              = 7 \nretained_backup_size                          = 100 \npoint_in_time_recovery                        = true \nnetwork_id                                    = \"projects/prj-core-network-dev-001/global/networks/vpc-core-net-prj-dev-001\"\nrequire_ssl                                   = true \nenable_private_path_for_google_cloud_services = true \nday                                           = 1 \nstart_time                                    = 07 \ndeletion_protection                           = false  \navailability_type                             = \"ZONAL\" \nenvironment                                   = \"dev\"\ndb_name                                       = \"sgs_dev\"\nsubnetwork_name                               = \"net-psa-private-service-access-dev-001\"\nssl_mode                                      = \"ENCRYPTED_ONLY\"\nauthorized_networks                           = \"<tbd>\"\n",
                "varibales.tf": "variable \"name\" {\n  description = \"The default name of the database instance\"\n  type        = string\n  default     = \"\"\n\n  validation {\n    condition     = can(regex(\"^[a-z]([-a-z0-9]*[a-z0-9])?$\", var.name)) && length(var.name) <= 64 && length(var.name) > 0\n    error_message = \"Invalid name. The name must be less than 64 characters, at least one character, and match the required pattern.\"\n  }\n}\n\nvariable \"instance_name\" {\n  description = \"The name of the database instance\"\n  type        = string\n  default     = \"\"\n\n  validation {\n    condition     = can(regex(\"^[a-z]([-a-z0-9]*[a-z0-9])?$\", var.instance_name)) && length(var.instance_name) <= 64 && length(var.instance_name) > 0\n    error_message = \"Invalid instance name. The name must be less than 64 characters, at least one character, and match the required pattern.\"\n  }\n}\n\nlocals {\n  effective_instance_name = var.instance_name != \"\" ? var.instance_name : \"db-${var.name}-${var.environment}-${var.region}-001\"\n}\n\n\nvariable \"project_id\" {\n  description = \"Project ID\"\n  type        = string\n}\n\nvariable \"region\" {\n  description = \"Region where the database instance is located\"\n  type        = string\n  default     = \"us-central1\"\n}\n\nvariable \"database_version\" {\n  description = \"Version of the database\"\n  type        = string\n\n  validation {\n    condition     = can(regex(\"^MYSQL_5_6$|^MYSQL_5_7$|^MYSQL_8_0$|^_9_6$|^_10$|^_11$|^_12$|^_13$|^_14$|^_15$|^SQLSERVER_2017_STANDARD$|^SQLSERVER_2017_ENTERPRISE$|^SQLSERVER_2017_EXPRESS$|^SQLSERVER_2017_WEB$|^SQLSERVER_2019_STANDARD$|^SQLSERVER_2019_ENTERPRISE$|^SQLSERVER_2019_EXPRESS$|^SQLSERVER_2019_WEB$\", var.database_version))\n    error_message = \"Invalid database version. Only MySQL, QL, and SQL Server versions are supported.\"\n  }\n}\n\nvariable \"tier\" {\n  description = \"Machine tier for the database instance\"\n  type        = string\n\n  #  validation {\n  #    condition     = can(regex(\"^(db-f1-micro|db-custom|db-g1-small|db-n1-standard-[1-9][0-9]*)$\", var.tier))\n  #    error_message = \"Invalid tier. Only specific tiers are supported.\"\n  #  }\n}\n\n\nvariable \"activation_policy\" {\n  description = \"Activation policy for the database instance\"\n  type        = string\n}\n\nvariable \"disk_size\" {\n  description = \"Disk size in GB\"\n  type        = number\n}\n\nvariable \"disk_autoresize\" {\n  description = \"Whether disk auto-resize is enabled or not\"\n  type        = bool\n}\n\nvariable \"backup_enabled\" {\n  description = \"Whether backup is enabled or not\"\n  type        = bool\n}\n\nvariable \"binary_log_enabled\" {\n  description = \"Whether binary log is enabled or not\"\n  type        = bool\n}\n\nvariable \"retained_backups\" {\n  description = \"Number of retained backups\"\n  type        = number\n}\n\nvariable \"retained_backup_size\" {\n  description = \"Size of retained backups\"\n  type        = number\n}\n\nvariable \"point_in_time_recovery\" {\n  description = \"Whether point-in-time recovery is enabled or not\"\n  type        = bool\n}\n\nvariable \"network_id\" {\n  description = \"ID of the vpc. e.g. projects/prj-core-network-prod-001/global/networks/vpc-core-net-prj-prod-001\"\n  type        = string\n}\n\nvariable \"subnetwork_name\" {\n  description = \"name of the subnetwork to use for connectivity. e.g. net-psa-cloud-sql-prod-global-001\"\n  type        = string\n}\n\nvariable \"require_ssl\" {\n  description = \"Whether SSL is required or not\"\n  type        = bool\n  default     = true\n}\n\nvariable \"enable_private_path_for_google_cloud_services\" {\n  description = \"Whether to enable private path for Google Cloud services\"\n  type        = bool\n}\n\nvariable \"day\" {\n  description = \"Day of the week for the maintenance window\"\n  type        = number\n}\n\nvariable \"start_time\" {\n  description = \"Hour of the day for the maintenance window\"\n  type        = number\n  default     = 07\n}\n\nvariable \"deletion_protection\" {\n  description = \"Whether deletion protection is enabled or not\"\n  type        = bool\n}\n\nvariable \"db_name\" {\n  description = \"Name of the database\"\n  type        = string\n}\n\nvariable \"database_charset\" {\n  description = \"Character set for the database\"\n  type        = string\n  default     = \"UTF8\"\n}\n\nvariable \"database_collation\" {\n  description = \"Collation for the database\"\n  type        = string\n  default     = \"en_US.UTF8\"\n}\n\nvariable \"availability_type\" {\n  description = \"The availability type of the database instance\"\n  type        = string\n  default     = \"ZONAL\"\n  validation {\n    condition     = var.availability_type == \"ZONAL\" || var.availability_type == \"REGIONAL\"\n    error_message = \"Invalid availability type. Allowed values are ZONAL or REGIONAL.\"\n  }\n}\n\nvariable \"disk_type\" {\n  description = \"The type of disk for the database instance\"\n  type        = string\n  default     = \"PD_SSD\"\n}\n\nvariable \"environment\" {\n  description = \"The environment in which the instance is deployed\"\n  type        = string\n  default     = \"\"\n}\n\nvariable \"edition\" {\n  description = \"edition of database\"\n  type        = string\n  default     = \"ENTERPRISE\"\n}\n\n\nvariable \"ssl_mode\" {\n  description = \"SSL Connection to connect DB\"\n  type        = string\n  default     = \"\"\n}\n\nvariable \"authorized_networks\" {\n  description = \"list of authorized networks\"\n  type        = list(object({ name = string, cidr = string }))\n  default     = []\n}\n\nvariable \"database_flags\" {\n  description = \"list of database flags\"\n  type        = list(object({ name = string, value = string }))\n  default     = []\n}   \n"
            }
        },
    }
}
"""

REVIEW_TERRAFORM_INSTRUCTION_PROMPT = """
You are an expert GCP engineer with deep expertise in writing and reviewing Terraform code for Google Cloud Platform (GCP) only. Your task is to review the Terraform output ({TerraformGenerationOutput}) generated by a Terraform agent and verify that it correctly incorporates all values from the provided input ({ValidatedInput}).

Input Definitions:
{ValidatedInput} input for reviewing the terraform code.
{TerraformGenerationOutput} is a Terraform code.
Review Criteria:
Check that all {ValidatedInput} values (e.g., machine_type, region, instance_type) are present and correctly applied in the {TerraformGenerationOutput}, except for any values or resources related to ADgroup, Landing Zone IAM, or DNS.
Exclude from review any Terraform resources or configurations related to ADgroup (e.g., Active Directory group integrations), Landing Zone IAM (e.g., organization-level IAM policies), or DNS (e.g., google_dns_managed_zone) or value like <tbd> also.
Check that all {ValidatedInput} values are present and correctly applied in the {TerraformGenerationOutput}.
Verify that the Terraform code is syntactically correct and adheres to GCP best practices for the relevant services (e.g., Compute Engine, Cloud Storage, IAM).
Ensure resource configurations align with the specified {ValidatedInput} values (e.g., correct project ID, region, or resource settings).
Output Requirements:
If all {ValidatedInput} values exactly match the corresponding attributes in {TerraformGenerationOutput} and the code is valid, return: “No changes required.”
If discrepancies exist (e.g., missing values, incorrect values, or syntax errors), provide a bullet-point list of issues, including:
The specific {ValidatedInput} key and expected value.
The actual value (or absence) in {TerraformGenerationOutput}.
The line number (if applicable) in {TerraformGenerationOutput}.
A suggested correction or explanation.
Comments must only address issues related to {ValidatedInput}, {TerraformGenerationOutput}, and GCP best practices, avoiding unrelated suggestions.
Edge Cases:
If {TerraformGenerationOutput} is malformed or contains syntax errors, note these issues first and suggest fixes before checking {ValidatedInput}.
If {ValidatedInput} is missing or incomplete, return: “Error: {ValidatedInput} is missing or incomplete. Please provide valid input.”
Example:
{ValidatedInput}: {"project_id": "my-project", "region": "us-central1", "instance_type": "e2-medium"}
{TerraformGenerationOutput}:
resource "google_compute_instance" "vm" {
  project      = "my-project"
  zone         = "us-central1-a"
  machine_type = "e2-small"
}
Expected Output:
-status: invalid
- Discrepancy found:
  - Key: instance_type
  - Expected: e2-medium
  - Actual: e2-small
  - Line: 3
  - Suggestion: Update `machine_type` to `"e2-medium"` to match {ValidatedInput}.
"""

PR_RAISE_PROMPT = """
You are a Github pr raise agent. Your task is to raise the pr with the help of the tool.

Expected Output Format:**
    **Return a JSON object with:**
       - message: A string describing the outcome or error.
       - core_it_infra_pr_link: The PR URL for the core infrastructure module (if applicable, otherwise empty string).
       - landing_zone_pr_link: The PR URL for the landing zone module (if applicable, otherwise empty string).
"""

# PR_RAISE_PROMPT = """
# Your are a Github pr raise agent. Your task is to raise pr with respect to the inputs that is provided.
# **Input:**
#     {ValidatedInput} - Input values that are use to create the branch and commit messages for the pr.
#     {ReviewTerraformOutput} - Terraform validated response.
#     {TerraformGenerationOutput} - Terraform input to create a pr.
#
# **Task Requirements:**
#     **Input Validation:**
#        - Ensure ValidatedInput contains all required fields and valid values (e.g., repository_url is a valid GitHub URL, new_branch_name follows Git branch naming conventions).
#        - Verify ReviewTerraformOutput.status is one of "valid", "no_changes", or "invalid".
#        - Confirm TerraformGenerationOutput.files is a non-empty array with valid file paths and non-empty content.
#     **Conditional Logic:**
#        - Proceed with PR creation only if ReviewTerraformOutput.status is "valid" or "no_changes".
#        - If status is "invalid", return a JSON response with an error message including ReviewTerraformOutput.details.
#     **PR Creation Process:**
#        - Authenticate with the GitHub API using a provided access token (assume it’s available in the environment).
#        - Create a new branch named new_branch_name from base_branch in the specified repository_url.
#        - Commit the files from TerraformGenerationOutput.files to the new branch with the provided commit_message.
#        - Raise a PR from the new branch to base_branch with the specified pr_title and pr_description.
#        - If the repository has separate modules (e.g., core_it_infra and landing_zone), create separate PRs for each and return their respective links.
#     **Error Handling:**
#        - If any step fails (e.g., branch creation, commit, or PR creation), return a JSON response with an error message and relevant details.
#        - Handle edge cases like existing branches, invalid repository URLs, or API rate limits.
# **Output Format:**
#     **Return a JSON object with:**
#        - status: A string indicating the result ("success", "error", or "skipped").
#        - message: A string describing the outcome or error.
#        - core_it_infra_pr_link: The PR URL for the core infrastructure module (if applicable, otherwise empty string).
#        - landing_zone_pr_link: The PR URL for the landing zone module (if applicable, otherwise empty string).
# """

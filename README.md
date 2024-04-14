This repository contains the deployment setup for two .NET microservices on Azure Kubernetes Service (AKS) using GitHub Actions. The microservices are designed to print "hello" and "world" at specific endpoints /hello and /world, respectively. Additionally, both microservices incorporate feature toggling for controlled functionality activation.
Features

    Microservices: Two .NET microservices with distinct functionalities.
    Endpoints:

    /hello: Prints "hello".
    /world: Prints "world".

    Feature Toggling: Feature toggles allow for controlled activation of functionalities.
    Pipeline Steps:

    Sonar Scan: Static code analysis to ensure code quality.
    ZAP Tests: Security testing using OWASP ZAP to identify vulnerabilities.
    Unit Tests: Execution of unit tests to validate code functionality.
    Build Tests: Build process to ensure successful compilation.
    Image Push to ACR: Docker images are pushed to Azure Container Registry (ACR) for versioning and deployment.
    Deployment: Microservices are deployed to AKS for production use.

Pipeline Workflow

    Sonar Scan:

    Executes Sonar scan to analyze code quality and identify potential issues.

    ZAP Tests:

    Conducts security testing using OWASP ZAP to detect vulnerabilities and security flaws.

    Unit Tests:

    Executes unit tests to ensure individual components function correctly.

    Build Tests:

    Builds the microservices to ensure successful compilation without errors.

    Image Push to ACR:

    Docker images are built and pushed to Azure Container Registry (ACR) for versioning and management.

    Deployment:

    Deploy microservices to AKS for production use, ensuring availability and scalability.

Setup Instructions
To deploy the microservices on AKS using GitHub Actions, follow these steps:

    Clone Repository:

           git clone <repository-url>

# This is first yaml file that we will when we're performing the secrets relates tasks

apiVersion: secrets-store.csi.x-k8s.io/v1
kind: SecretProviderClass
metadata:
  name: azure-kvname-system-msi
spec:
  provider: azure
  parameters:
    usePodIdentity: "false"
    useVMManagedIdentity: "true" # Set to true for using managed identity
    userAssignedIdentityID: "" # If empty, then defaults to use the system>
    keyvaultName: akssecret-vault
    cloudName: "AzureCloud" # [OPTIONAL for Azure] if not pro>
    objects: |
      array:
        - |
          objectName: mysql-password
          objectType: secret        # object types: secret, key, or cert
          objectVersion: ""         # [OPTIONAL] object versions, default to la>
    tenantId:
 e316acc5-71c6-471e-ba1d-591dd32d8e91 
 
 # replace with the directory id of
 # key vault created mentioned in the overview.


Contributor

    Your Name - Sohail Khan

If you encounter any issues or have suggestions for improvements, please raise them through GitHub issues.

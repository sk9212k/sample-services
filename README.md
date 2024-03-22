**Title: Deploying a Service in a Kubernetes Cluster**

**Objective:** 
The objective of this document is to guide the process of deploying a service in a Kubernetes cluster.

**Pre-requisites:**

1. Access the Azure CLI.
2. Docker is installed on the local machine.
3. Kubernetes CLI (kubectl) is installed on the local machine.

**Deployment Steps:**

1. **Logging into Azure CLI:** 
   Execute the following command in the terminal to log in to the Azure CLI:
   ```
   az login
   ```

2. **Creating a Resource Group:** 
   Create a resource group with the following command: 
   ```
   az group create --name resourcegroupname --location eastus3
   ```

3. **Creating a Container Registry:** 
   Create a container registry in the specified resource group: 
   ```
   az acr create --resource-group resourcegroupname --name acrname --sku Basic
   ```

4. **Logging into the Container Registry:** 
   Log in to the created container registry: 
   ```
   az acr login --name acrname
   ```

5. **Tagging and pushing the image:** 
   Tag the Docker image and push it to the Azure Container Registry: 
   ```
   docker tag new-service:latest acrname.azurecr.io/new-service:latest 
   docker push acrname.azurecr.io/new-service:latest
   ```

6. **Verifying Image:** 
   List the images in the Azure Container Registry to ensure a successful push: 
   ```
   az acr repository list --name debugdemoimage --output table
   ```

7. **Creating an AKS Cluster:** 
   Create an AKS cluster and attach it to the container registry: 
   ```
   az aks create --resource-group resourcegroupname --name clustername --node-count 2 --generate-ssh-keys --attach-acr acrname
   ```

8. **Connecting to the AKS Cluster:** 
   Get credentials to connect to the AKS cluster: 
   ```
   az aks get-credentials --resource-group resourcegroupname --name clustername
   ```

9. **Checking Node Status:** 
   Verify the status of nodes in the AKS cluster: 
   ```
   kubectl get nodes
   ```

10. **Service Definition:** 

Deployment definitions are available in the Deployment-definitions folder
Update the name of the acr as required.


11. **Applying Service Definition:** 
    Apply the service definition to the Kubernetes cluster: 
    ```
    kubectl apply -f new-deployment.yaml
    ```

12. **Checking Events:** 
    Check for any events in the Kubernetes cluster: 
    ```
    kubectl get events
    ```

13. **Verifying External IP:** 
    Get services to check the external IP of the newly deployed service: 
    ```
    kubectl get services
    ```
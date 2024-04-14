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
# Introduction 
Sample application and deployment to AKS with ingress controller

# Versioning and AKS targetting
In order to set applicaion version and deployment destination, edit azure-pipelines.yml file :

stages:
- template: service-pipeline.yml@pipeline_templates
  parameters:
    serviceName: app
    version: '2.0.0'
    aksClusterName: msft-demo-aks
    aksResourceGroup: msft-demo-rg


# Build
Once any change is commited , the CI/CD pipeline triggered

# Application access

Once CI/CD pipeline is done, application accessible by:

USD BTC price:
http://<ingress external IP>/appusd

EUR BTC price:
http://<ingress external IP>/appeur
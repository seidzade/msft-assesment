provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "default" {
  name     = "msft-demo-rg"
  location = "West Europe"

  tags = {
    environment = "Demo"
  }
}

resource "azurerm_kubernetes_cluster" "default" {
  name                = "msft-demo-aks"
  location            = azurerm_resource_group.default.location
  resource_group_name = azurerm_resource_group.default.name
  dns_prefix          = "msft-demo-k8s"

  default_node_pool {
    name            = "default"
    node_count      = 1
    vm_size         = "Standard_B2s"
    os_disk_size_gb = 30
    enable_auto_scaling = false
  }

  service_principal {
    client_id     = var.appId
    client_secret = var.password
  }

  # identity{
  #   type = "SystemAssigned"
  # }

  role_based_access_control {
    enabled = true
  }

  tags = {
    environment = "Demo"
  }
}

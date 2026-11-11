provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "dev" {
  name     = "bhalladev"
  location = "East US"

  tags = {
    environment = "dev"
  }
}
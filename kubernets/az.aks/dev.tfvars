terraform plan `
-var="resource_group_name=demo" `
-var="location=eastus" `
-var="aks_cluster_name=aks-demo-cluster" `
-var="node_count=2" `
-var="vm_size=Standard_D2s_v3" `
-var="environment=dev"
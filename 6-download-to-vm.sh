#!/bin/bash

# Step 1: SSH into VM
ssh azureuser@52.233.131.60 # VM-Sreehari

# Step 2: Setup azure-cli
sudo apt-get update
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
az --version

# Step 3: Log in to Azure
az login

# Step 3: Get the access key for the storage account
#az storage account keys list --resource-group <your-resource-group> --account-name dataengineerv1butla --output table

# Step 4: Download the file from the Azure Storage Account
az storage blob download --account-name dataengineerv1 --account-key <your-access-key> --container-name sreehari-butla --name Sreehari-Butla.csv --file ~/result-Sreehari

# Step 5: Validate downloaded file
ls
cat result-Sreehari
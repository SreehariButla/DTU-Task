from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os

# Define the connection details
storage_account_name = "dataengineerv1"
container_name = "sreehari-butla"
blob_name = "Sreehari-Butla.csv"
local_file_path = "Sreehari-Butla.csv"  # Path to the CSV file you want to upload

# Replace with your actual connection string
connection_string = "<storage_account_connection_string"

# Create a BlobServiceClient using the connection string
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Get a reference to the container
container_client = blob_service_client.get_container_client(container_name)

# If the container doesn't exist, create it
try:
    container_client.create_container()
    print(f"Container '{container_name}' created successfully.")
except Exception as e:
    print(f"Container '{container_name}' already exists or encountered an error: {e}")

# Create a BlobClient for the file you want to upload
blob_client = container_client.get_blob_client(blob_name)

# Upload the CSV file to the blob
with open(local_file_path, "rb") as data:
    blob_client.upload_blob(data, overwrite=True)
    print(f"File '{local_file_path}' uploaded to container '{container_name}' as blob '{blob_name}'.")

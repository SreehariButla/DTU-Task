from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
import pandas as pd
from io import BytesIO

# Azure Storage account name and container
account_name = "dataengineerv1"
container_name = "raw"
blob_name = "tourism_dataset.csv"

# Construct the blob service URL (this is specific to Azure blob storage format)
blob_service_url = f"https://{account_name}.blob.core.windows.net"

# Initialize DefaultAzureCredential for authentication
credential = DefaultAzureCredential()


# Create BlobServiceClient to interact with the storage account
blob_service_client = BlobServiceClient(account_url=blob_service_url, credential=credential)

# Function to download the CSV file from blob storage and load it into a pandas DataFrame
def load_csv_from_blob(container_name, blob_name):
    # Get the BlobClient for the specific blob (CSV file)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

    # Download the blob content (file)
    blob_data = blob_client.download_blob()

    # Read the downloaded CSV content into a pandas DataFrame
    pandasdf = pd.read_csv(BytesIO(blob_data.readall()))

    return pandasdf

if __name__ == "__main__":
    # Load the CSV file into a DataFrame
    print(f"Loading data from {blob_name} in container {container_name}...")
    df = load_csv_from_blob(container_name, blob_name)

    # Display the first few rows of the DataFrame
    print(df.head())

# Save DataFrame to a CSV locally (for later use in analysis)
df.to_csv('tourism_dataset_local.csv', index=False)



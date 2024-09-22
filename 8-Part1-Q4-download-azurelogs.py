import os
from azure.identity import ClientSecretCredential
from azure.mgmt.monitor import MonitorManagementClient
from datetime import datetime, timedelta, timezone
import pandas as pd

# Azure Service Principal credentials 
TENANT_ID = "<your-tenant-id>"  # Replace with your Tenant ID
CLIENT_ID = "<your-client-id>"  # Replace with your Client ID
CLIENT_SECRET = "<your-client-secret>"  # Replace with your Client Secret
SUBSCRIPTION_ID = "<your-subscription-id>"  # Replace with your Azure Subscription ID

# Authenticate using the Service Principal
credential = ClientSecretCredential(tenant_id=TENANT_ID, client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

# Create a MonitorManagementClient
monitor_client = MonitorManagementClient(credential, SUBSCRIPTION_ID)

# Define the time range for logs (e.g., logs from the last 24 hours)
end_time = datetime.now(timezone.utc)  # Use timezone-aware datetime
start_time = end_time - timedelta(days=1)

# Fetch activity logs for the last 24 hours 
activity_logs = monitor_client.activity_logs.list(
    filter=f"eventTimestamp ge '{start_time}' and eventTimestamp le '{end_time}'"
)

# Process the logs
logs = []
for log in activity_logs:
    logs.append({
        "eventTimestamp": log.event_timestamp,
        "resourceGroupName": log.resource_group_name,
        "operationName": log.operation_name.localized_value,
        "status": log.status.localized_value,
        "caller": log.caller
    })

# Convert logs to pandas DataFrame for easier manipulation
df = pd.DataFrame(logs)

# Save logs to a CSV file
output_file = "azure_activity_logs.csv"
df.to_csv(output_file, index=False)
print(f"Logs saved to {output_file}")

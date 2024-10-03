import json
import time
import random
import requests

from azure.storage.blob import BlobServiceClient

# Sample log messages
sample_logs = [
    {"level": "INFO", "message": "User logged in", "user_id": 1},
    {"level": "DEBUG", "message": "Query executed", "user_id": 3},
]

error_logs = [
    {"level": "ERROR", "message": "Failed to connect to database", "user_id": 2},
    {"level": "ERROR", "message": "Permission denied", "user_id": 4},
]

# Azure Function endpoint (replace this with your function URL)
AZURE_FUNCTION_ENDPOINT = "YOUR_AZURE_FUNCTION_URL"

# Azure Blob Storage connection string (replace with your connection string)
AZURE_STORAGE_CONNECTION_STRING = "YOUR_AZURE_STORAGE_CONNECTION_STRING"

# Blob service client
blob_service_client = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)

# The container name where logs will be stored
CONTAINER_NAME = "logs-container"


def send_log_to_azure_function(log):
    """Send log to Azure Function."""
    response = requests.post(AZURE_FUNCTION_ENDPOINT, json=log)
    if response.status_code == 200:
        print(f"Sent log: {log}")
    else:
        print(f"Failed to send log: {log}. Status code: {response.status_code}")


def store_log_in_blob(log):
    """Store log in Azure Blob Storage."""
    blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=f"log-{log['user_id']}-{time.time()}.json")
    
    # Convert log to JSON and upload to blob storage
    blob_client.upload_blob(json.dumps(log))
    print(f"Stored log in blob storage: {log}")


def simulate_log_stream():
    """Simulate log stream sending logs to Azure."""
    while True:
        if random.random() < 0.1:
            log = random.choice(error_logs)
        else:
            log = random.choice(sample_logs)
        
        # Send the log to Azure Function
        send_log_to_azure_function(log)
        
        # Optionally store logs in Blob Storage as well
        store_log_in_blob(log)
        
        time.sleep(random.uniform(0.5, 3))


if __name__ == "__main__":
    simulate_log_stream()

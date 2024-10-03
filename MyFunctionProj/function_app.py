import json
import time
import os
import random
import requests
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient
import azure.functions as func
from azure.cosmos import CosmosClient, exceptions

load_dotenv()


AZURE_STORAGE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING") 
AZURE_FUNCTION_ENDPOINT = os.getenv("AZURE_FUNCTION_ENDPOINT")

COSMOS_ENDPOINT = os.getenv("COSMOS_ENDPOINT")
COSMOS_KEY = os.getenv("COSMOS_KEY")
client = CosmosClient(COSMOS_ENDPOINT, COSMOS_KEY)
database = client.get_database_client('UserDatabase')
users_container = database.get_container_client('users')

# Sample log messages
sample_logs = [
    {"level": "INFO", "message": "User logged in", "user_id": 1},
    {"level": "DEBUG", "message": "Query executed", "user_id": 3},
]

error_logs = [
    {"level": "ERROR", "message": "Failed to connect to database", "user_id": 2},
    {"level": "ERROR", "message": "Permission denied", "user_id": 4},
]

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


# Function to handle user creation (POST)
def create_user(request_json):
    try:
        user_data = request_json.get('data')
        users_container.create_item(user_data)
        return func.HttpResponse('User added!', status_code=201)
    except Exception as e:
        return func.HttpResponse(f'Error adding user: {str(e)}', status_code=400)


# Function to handle user retrieval (GET)
def read_user(req):
    user_id = req.params.get('id')
    if user_id:
        # Fetch a specific user by ID
        try:
            user = users_container.read_item(item=user_id, partition_key=user_id)
            return func.HttpResponse(json.dumps(user), mimetype="application/json", status_code=200)
        except exceptions.CosmosResourceNotFoundError:
            return func.HttpResponse(f"User with id {user_id} not found.", status_code=404)
        except Exception as e:
            return func.HttpResponse(f"Error retrieving user: {str(e)}", status_code=400)
    else:
        # Fetch all users if no ID is provided
        users = list(users_container.read_all_items())
        return func.HttpResponse(json.dumps(users), mimetype="application/json", status_code=200)


# Function to handle user update (PUT)
def update_user(request_json):
    try:
        user_id = request_json.get('id')
        user_data = request_json.get('data')
        user_data['id'] = user_id  # Ensure the 'id' is part of the document
        users_container.upsert_item(user_data)
        return func.HttpResponse('User updated!', status_code=200)
    except Exception as e:
        return func.HttpResponse(f'Error updating user: {str(e)}', status_code=400)


# Function to handle user deletion (DELETE)
def delete_user(request_json):
    try:
        user_id = request_json.get('id')
        users_container.delete_item(user_id, partition_key=user_id)
        return func.HttpResponse(f'User {user_id} deleted!', status_code=200)
    except exceptions.CosmosResourceNotFoundError:
        return func.HttpResponse(f'User with id {user_id} not found.', status_code=404)
    except Exception as e:
        return func.HttpResponse(f'Error deleting user: {str(e)}', status_code=400)


def main(req: func.HttpRequest) -> func.HttpResponse:
    # Parse the request body
    # simulate_log_stream()

    request_json = req.get_json(silent=True)

    # CRUD Operation Handlers
    if req.method == 'POST':
        return create_user(request_json)
    elif req.method == 'GET':
        return read_user(req)
    elif req.method == 'PUT':
        return update_user(request_json)
    elif req.method == 'DELETE':
        return delete_user(request_json)
    else:
        return func.HttpResponse('Method not supported!', status_code=400)

import json
from azure.storage.blob import BlobServiceClient
import azure.functions as func
from azure.cosmos import CosmosClient, exceptions


# Azure Function endpoint (replace this with your function URL)
AZURE_FUNCTION_ENDPOINT = "https://funcazuremoh.azurewebsites.net/"

AZURE_STORAGE_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=logsblomomo;AccountKey=riU3U4kQByJQVgV3t9yI9/6mWaghzI3WxGVESW9BCfkinF2fJCyiQPl+eART8As+f3gPr3LMRj7B+AStTOjHkA==;EndpointSuffix=core.windows.net"

COSMOS_ENDPOINT = "cosmosfuncazure.mongo.cosmos.azure.com"
COSMOS_KEY = "oP1CBBYfzMFijlg3f7m8kab4l1Ybxiyp151cF9KBoTEDpqkpjpP2AnzX34BpJEuumnhUHskVAHpwACDbyQrVkQ=="

client = CosmosClient(COSMOS_ENDPOINT, COSMOS_KEY)
database = client.get_database_client('UserDatabase')
users_container = database.get_container_client('users')


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
    
    return func.HttpResponse('Method not supported!', status_code=400)

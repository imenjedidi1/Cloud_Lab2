import azure.functions as func
from azure.storage.blob import BlobServiceClient
import logging

# Connection string to your Azure Blob Storage
CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=imenelab2;AccountKey=X8ubtXmqt8zRef7jFi+R6pKp6pFdCFEgCkWrp9mdOih++DtzDj6CO/7PrS/H8L0zzUnkop5Bhuf8+AStgBJmIw==;EndpointSuffix=core.windows.net"
CONTAINER_NAME = "mrinput"

async def main(name: str) -> list:
    input_data = []
    blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
    container_client = blob_service_client.get_container_client(CONTAINER_NAME)
    blobs = container_client.list_blobs()

    for blob in blobs:
        blob_client = container_client.get_blob_client(blob.name)
        blob_content = blob_client.download_blob().readall().decode('utf-8')
        lines = blob_content.splitlines()

        # Create tuples of (line_number, line_content)
        for i, line in enumerate(lines):
            input_data.append((i, line))

    return input_data

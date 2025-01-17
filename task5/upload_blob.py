from azure.storage.blob import BlobServiceClient

CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=imenelab2;AccountKey=X8ubtXmqt8zRef7jFi+R6pKp6pFdCFEgCkWrp9mdOih++DtzDj6CO/7PrS/H8L0zzUnkop5Bhuf8+AStgBJmIw==;EndpointSuffix=core.windows.net"
CONTAINER_NAME = "mrinput"

def list_and_download_blobs():
    # Initialize the BlobServiceClient
    blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
    
    # Get the container client
    container_client = blob_service_client.get_container_client(CONTAINER_NAME)
    
    # List all blobs in the container
    print(f"Listing blobs in container: {CONTAINER_NAME}")
    blob_names = []
    for blob in container_client.list_blobs():
        print(f"Found blob: {blob.name}")
        blob_names.append(blob.name)

    # Download each blob
    for blob_name in blob_names:
        print(f"Downloading blob: {blob_name}")
        blob_client = container_client.get_blob_client(blob_name)
        blob_data = blob_client.download_blob().readall()
        
        # Save blob data locally
        with open(blob_name, "wb") as file:
            file.write(blob_data)
        print(f"Blob {blob_name} downloaded successfully.")

if __name__ == "__main__":
    list_and_download_blobs()

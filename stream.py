import time
import random
import uuid
from azure.cosmos import CosmosClient, exceptions
import datetime

# Replace these with your Cosmos DB account details from the Keys blade.
COSMOS_URI = "Your data"
COSMOS_KEY = "Your data"
DATABASE_NAME = "SensorDataDB"
CONTAINER_NAME = "SensorReadings"

# Initialize the Cosmos client
client = CosmosClient(COSMOS_URI, credential=COSMOS_KEY)

# Get the database and container client
database = client.get_database_client(DATABASE_NAME)
container = database.get_container_client(CONTAINER_NAME)

def simulate_sensor_data():
    # Simulate data for an IoT sensor
    sensor_data = {
        "id": str(uuid.uuid4()),
        "deviceId": f"Device-{random.randint(1, 5)}",
        "temperature": round(random.uniform(20, 35), 2),
        "humidity": round(random.uniform(30, 70), 2),
        "timestamp": datetime.datetime.utcnow().isoformat()
    }
    return sensor_data

def insert_data():
    while True:
        data = simulate_sensor_data()
        try:
            container.create_item(body=data)
            print("Inserted data:", data)
        except exceptions.CosmosHttpResponseError as e:
            print("An error occurred:", e.message)
        time.sleep(3)  # Insert data every 3 seconds

if __name__ == "__main__":
    insert_data()

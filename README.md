# Azure-Cosmos-DB-Data-Management-and-Access

## **Project Description**  
This project demonstrates how to create, manage, and interact with an **Azure Cosmos DB** instance. It includes the following:  
- Setting up an **Azure Cosmos DB** account and database  
- Creating containers and adding sample data  
- Querying the database using Python  
- Connecting to Cosmos DB remotely from different environments  

This repository provides code and step-by-step instructions to help users replicate the setup and access the database from any location.  

---

## **Prerequisites**  
Before running this project, ensure you have:  
- An **Azure account** (You can create one at [Azure Portal](https://portal.azure.com/))  
- **Azure Cosmos DB** provisioned (SQL API used in this project)  
- **Python 3.x** installed  
- Necessary Python libraries installed (`pip install azure-cosmos`)  

---

## **Setup Guide**  

### **1. Create an Azure Cosmos DB Account**  
1. Go to the [Azure Portal](https://portal.azure.com/).  
2. Search for **Cosmos DB** and click **Create**.  
3. Choose the **NoSQL API (SQL API)** and configure the resource group, database name, and region.  
4. Click **Review + Create** → **Create**.  

### **2. Create a Database and Container**  
1. Open your newly created **Cosmos DB Account**.  
2. In the **Data Explorer**, click **New Container**.  
3. Set:  
   - **Database ID**: `myDatabase`  
   - **Container ID**: `myContainer`  
   - **Partition Key**: `/id`  
4. Click **OK** to create the container.  

---

## **Connecting to Cosmos DB with Python**  

### **3. Retrieve Connection Details**  
1. Navigate to **Keys** in the Cosmos DB menu.  
2. Copy the **Primary Connection String** or **URI & Primary Key**.  

### **4. Python Script to Connect and Query Cosmos DB**  

```python
from azure.cosmos import CosmosClient, PartitionKey

# Azure Cosmos DB credentials
ENDPOINT = "YOUR_COSMOS_DB_URI"
KEY = "YOUR_COSMOS_DB_PRIMARY_KEY"

# Initialize the Cosmos client
client = CosmosClient(ENDPOINT, KEY)

# Reference the database and container
database_name = "myDatabase"
container_name = "myContainer"

database = client.get_database_client(database_name)
container = database.get_container_client(container_name)

# Insert sample data
item = {
    "id": "1",
    "name": "Sample Item",
    "category": "Test",
    "price": 25.99
}
container.upsert_item(item)

# Query data
query = "SELECT * FROM c"
items = list(container.query_items(query, enable_cross_partition_query=True))

# Print retrieved items
for item in items:
    print(item)
```

---



## **Accessing Cosmos DB from Anywhere**  
You can use the **connection string** or **endpoint + key** to access this database from:  
- **Local scripts**  
- **Cloud applications**  
- **Other programming languages (Node.js, Java, etc.)**  





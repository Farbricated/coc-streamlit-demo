from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Your connection string
uri = os.getenv('MONGODB_URI')

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("✅ SUCCESS: Connected to MongoDB Atlas!")
    
    # Test database access
    db = client['evidence_blockchain']
    print(f"✅ Database access confirmed: {db.name}")
    
except Exception as e:
    print(f"❌ Connection failed: {e}")

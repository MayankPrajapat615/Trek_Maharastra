import os
import certifi
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

mongo_client = MongoClient(
    os.getenv("MONGO_URI"),
    serverSelectionTimeoutMS=3000,
    tz_aware=True,
    tls=True,
    tlsCAFile=certifi.where(),          # ← key fix
    tlsAllowInvalidCertificates=False,  # ← revert to False now that certifi handles it
)

mongo_db = mongo_client["trek_maharashtra"]

treks_collection     = mongo_db["treks"]
waterfalls_collection = mongo_db["waterfalls"]
users_collection     = mongo_db["users"]

# 🔒 INDEXES
treks_collection.create_index("slug", unique=True)
waterfalls_collection.create_index("slug", unique=True)
treks_collection.create_index("location.district")
treks_collection.create_index("difficulty")
users_collection.create_index("email", unique=True)

# ✅ TEST CONNECTION
try:
    mongo_client.admin.command('ping')
    print("✅ Connected to MongoDB Atlas successfully!")
    print(f"Collections: {mongo_db.list_collection_names()}")
except Exception as e:
    print(f"❌ Connection failed: {e}")
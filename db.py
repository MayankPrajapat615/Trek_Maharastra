#DB ONLY
from pymongo import MongoClient

mongo_client = MongoClient("mongodb://localhost:27017", serverSelectionTimeoutMS=3000)
mongo_db = mongo_client["trek_maharashtra"]

treks_collection = mongo_db["treks"]
waterfalls_collection = mongo_db["waterfalls"]
highlights_collection = mongo_db["highlights"]


# 🔒 INDEXES (RUNS SAFELY MULTIPLE TIMES)
treks_collection.create_index("slug", unique=True)
waterfalls_collection.create_index("slug", unique=True)

treks_collection.create_index("location.district")
treks_collection.create_index("difficulty")
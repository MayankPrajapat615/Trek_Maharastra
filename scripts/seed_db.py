from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

from validators.trek_validator import validate_trek
from validators.waterfall_validator import validate_waterfall

# ---------- DB CONNECTION ----------
client = MongoClient("mongodb://localhost:27017/")
db = client["trek_maharashtra"]

treks_collection = db["treks"]
waterfalls_collection = db["waterfalls"]

# ---------- DATA ----------
TREKS = [
    {
        "name": "Rajgad Fort",
        "slug": "rajgad-fort",
        "difficulty": "Medium",
        "height": 1376,
        "best_season": ["Monsoon", "Winter"],
        "is_active": True,
        "location": {
            "district": "Pune",
            "region": "Western Ghats",
            "state": "Maharashtra"
        }
    }
]

WATERFALLS = [
    {
        "name": "Kalmadvi Waterfall",
        "slug": "kalmadvi-waterfall",
        "description": "A seasonal waterfall near Bhira village.",
        "image_url": "static/images/waterfalls/kalmadvi.jpg",
        "difficulty": "Easy",
        "height": 120,
        "best_season": ["Monsoon", "Winter", "Summer"],
        "is_active": True,
        "location": {
            "district": "Raigad",
            "region": "Konkan",
            "state": "Maharashtra"
        }
    },
    {
        "name": "Dasoba Waterfall",
        "slug": "dasoba-waterfall",
        "description": "Hidden waterfall near Malshej Ghat.",
        "difficulty": "Medium",
        "height": 150,
        "best_season": ["Monsoon", "Winter"],
        "is_active": True,
        "location": {
            "district": "Thane",
            "region": "Western Ghats",
            "state": "Maharashtra"
        }
    }
]

# ---------- INSERT HELPERS ----------
def seed_treks():
    for trek in TREKS:
        try:
            validate_trek(trek)
            treks_collection.insert_one(trek)
            print(f"✅ Trek inserted: {trek['name']}")
        except DuplicateKeyError:
            print(f"⚠️ Trek already exists: {trek['slug']}")
        except Exception as e:
            print(f"❌ Trek failed: {e}")

def seed_waterfalls():
    for wf in WATERFALLS:
        try:
            validate_waterfall(wf)
            waterfalls_collection.insert_one(wf)
            print(f"✅ Waterfall inserted: {wf['name']}")
        except DuplicateKeyError:
            print(f"⚠️ Waterfall already exists: {wf['slug']}")
        except Exception as e:
            print(f"❌ Waterfall failed: {e}")

# ---------- RUN ----------
if __name__ == "__main__":
    print("🌱 Seeding database...")
    seed_treks()
    seed_waterfalls()
    print("✅ Seeding complete")

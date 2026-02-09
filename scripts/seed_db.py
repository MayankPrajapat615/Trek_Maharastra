from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from sqlalchemy import false, true

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
      "name": "Madan Fort",
      "slug": "madan-fort",
      "description": "Madan Fort is the central peak of the AMK trio and features a very narrow and exposed summit.\nThe climb involves a vertical rock patch that is considered quite challenging even for regular trekkers.\nThe top of the fort is small and rugged, providing a true sense of isolation and high-altitude thrill.\nIt offers the most unique perspective of the neighboring Alang and Kulang forts standing tall.\nThe historical steps were mostly destroyed, making modern climbing equipment a necessity for the ascent.",
      "difficulty": "Hard",
      "duration_hours": 9,
      "distance_km": 11.0,
      "height": 1470,
      "best_season": ["Winter"],
      "group_size": 10,
      "image": "images/treks/madan.webp",
      "location": {
        "district": "Nashik",
        "region": "Sahyadri (Western Ghats)",
        "state": "Maharashtra"
      },
      "created_at": { "$date": "2026-02-09T00:00:00Z" },
      "highlights": [
        {
          "name": "The Rock Patch",
          "type": "adventure",
          "description": "A 40-foot near-vertical climb that requires ropes and safety harnesses."
        },
        {
          "name": "Narrow Summit",
          "type": "viewpoint",
          "description": "A limited plateau space offering an intense 'top of the world' feeling."
        }
      ],
      "is_active": True,
      "is_featured": True,
      "featured_rank": 11
    }
]

WATERFALLS = [

    {
      "name": "Thoseghar Waterfall",
      "slug": "thoseghar-waterfall",
      "description": "Thoseghar is a series of waterfalls located near the city of Satara at the edge of Konkan.\nThe area features both a small waterfall and a much larger one with a thunderous drop.\nThere is a well-maintained viewing platform that allows visitors to see the falls safely.\nThe surrounding plateau is part of the Kas region and is known for its biodiversity.\nDuring heavy rains the sound of the falling water can be heard from several kilometers away.",
      "difficulty": "easy",
      "height": 1100,
      "best_season": ["monsoon"],
      "location": {
        "district": "Satara",
        "region": "Sahyadri (Western Ghats)",
        "state": "Maharashtra"
      },
      "type": "waterfall",
      "image": "images/waterfalls/thoseghar.webp",
      "is_featured": True,
      "is_active": True,
      "featured_rank": 2,
      "highlights": [
        {
          "name": "Main Waterfall Platform",
          "type": "viewpoint",
          "description": "A safe deck offering a direct view of the 500m drop."
        },
        {
          "name": "Small Waterfall Pool",
          "type": "scenic",
          "description": "A smaller, calmer cascade where visitors can get closer to the water."
        }
      ]
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

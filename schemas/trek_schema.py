TREK_SCHEMA = {
    "name": str,
    "slug": str,
    "description": str,

    "difficulty": str,          # Easy | Medium | Hard
    "duration_hours": int,
    "distance_km": float,
    "height": int,

    "best_season": list,        # list[str]
    "image_url": str,

    "group_size": int,

    "location": {
        "district": str,
        "region": str
    },

    "type": "trek"              # enforced internally
}


TREK_REQUIRED_FIELDS = [
    "name",
    "slug",
    "difficulty",
    "location"
]

DIFFICULTY_LEVELS = {"Easy", "Medium", "Hard"}
SEASONS = {"Summer", "Monsoon", "Winter"}


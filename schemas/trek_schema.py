TREK_SCHEMA = {
    "name": str,
    "slug": str,
    "description": str,

    "difficulty": str,          # Easy | Medium | Hard
    "duration_hours": int,
    "distance_km": float,
    "height": int,

    "best_season": list,        # list[str]
    "image": str,

    "group_size": int,

    "location": {
        "district": str,
        "region": str,
        "state":str
    },

    "highlights": [
      {
        "name": str,
        "type": str,
        "description": str
      }
    ],

    "type": "trek",             # enforced internally
    "is_active": bool,
    "is_featured": bool,
    "featured_rank": int
}


TREK_REQUIRED_FIELDS = {
    "name",
    "slug",
    "difficulty",
    "location",
    "image"
}

DIFFICULTY_LEVELS = {"Easy", "Moderate", "Hard"}
SEASONS = {"Summer", "Monsoon", "Winter"}


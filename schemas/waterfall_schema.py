WATERFALL_SCHEMA = {
    "name" : str,
    "slug" : str,
    "description" : str,

    "difficulty" : str,  # EASY \ MEDIUM \ HARD
    "height" : int,

    "best_season" : list,
    "image" : str,

    "location": {
        "district" : str,
        "region" : str,
        "state" : str
    },

    "highlights": [
      {
        "name": str,
        "type": str,
        "description": str
      }
    ],

    "type" : "waterfall",
    "is_active": bool,
    "is_featured": bool,
    "featured_rank": int 

}

WATERFALL_REQUIRED_FIELDS = {
    "name",
    "slug",
    "difficulty",
    "location",
    "image"
}

DIFFICULTY_LEVELS = {"Easy", "Moderate", "Hard"}
SEASONS = {"Summer", "Monsoon", "Winter"}

LOCATION_REQUIRED_FIELDS = [
    "district",
    "region",
    "state"
]
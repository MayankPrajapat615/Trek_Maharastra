WATERFALL_SCHEMA = {
    "name" : str,
    "slug" : str,
    "description" : str,

    "difficulty" : str,  # EASY \ MEDIUM \ HARD
    "height" : int,

    "best_season" : list,
    "image_url" : str,

    "is_active": bool,

    "location": {
        "district" : str,
        "region" : str,
        "state" : str
    },

    "type" : "waterfall" 

}

WATERFALL_REQUIRED_FIELDS = [
    "name",
    "slug",
    "difficulty",
    "location"
]

DIFFICULTY_LEVELS = {"easy", "medium", "hard"}
SEASONS = {"summer", "monsoon", "winter"}

LOCATION_REQUIRED_FIELDS = [
    "district",
    "region",
    "state"
]
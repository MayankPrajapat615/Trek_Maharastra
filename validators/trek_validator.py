# validators/trek_validator.py

from schemas.trek_schema import (
    TREK_SCHEMA,
    TREK_REQUIRED_FIELDS,
    DIFFICULTY_LEVELS,
    SEASONS
)

def validate_trek(data: dict):
    # Required fields
    for field in TREK_REQUIRED_FIELDS:
        if field not in data:
            raise ValueError(f"Missing required field: {field}")

    # Type enforcement
    for key, expected in TREK_SCHEMA.items():
        if key not in data:
            continue

        if isinstance(expected, dict):
            for subkey, subtype in expected.items():
                if subkey not in data[key]:
                    raise ValueError(f"Missing location field: {subkey}")
        elif isinstance(expected, type):
            if not isinstance(data[key], expected):
                raise ValueError(f"Invalid type for {key}")

    # Enums
    if "difficulty" in data and data["difficulty"] not in DIFFICULTY_LEVELS:
        raise ValueError("Invalid difficulty value")

    if "best_season" in data:
        if not isinstance(data["best_season"], list):
            raise ValueError("best_season must be a list")

    for season in data["best_season"]:
        if season not in SEASONS:
            raise ValueError(f"Invalid season: {season}")
        
    if "slug" in data:
        data["slug"] = data["slug"].strip().lower()


    # Enforce internal field
    data["type"] = "trek"

    return True

from schemas.waterfall_schema import (
    DIFFICULTY_LEVELS,
    SEASONS,
    WATERFALL_REQUIRED_FIELDS,
    LOCATION_REQUIRED_FIELDS
)


def validate_waterfall(data: dict) -> dict:
    if not isinstance(data, dict):
        raise ValueError("Payload must be an object")

    # ---------- REQUIRED FIELDS ----------
    missing = WATERFALL_REQUIRED_FIELDS - data.keys()
    if missing:
        raise ValueError(f"Missing required fields: {missing}")

    # ---------- BASIC NORMALIZATION ----------
    data["name"] = str(data["name"]).strip()
    data["slug"] = str(data["slug"]).strip().lower().replace(" ", "-")

    # ---------- DIFFICULTY (FORGIVING) ----------
    raw_difficulty = str(data.get("difficulty", "")).strip().lower()
    difficulty_map = {d.lower(): d for d in DIFFICULTY_LEVELS}
    data["difficulty"] = difficulty_map.get(raw_difficulty, "Easy")

    # ---------- LOCATION ----------
    location = data.get("location", {})
    if not isinstance(location, dict):
        raise ValueError("location must be an object")

    for field in LOCATION_REQUIRED_FIELDS:
        location[field] = str(location.get(field, "")).strip()

    data["location"] = location

    # ---------- OPTIONAL FIELDS ----------
    if "height" in data:
        try:
            data["height"] = int(data["height"])
            if data["height"] <= 0:
                del data["height"]
        except Exception:
            del data["height"]

    # ---------- SEASONS (NO CRASHING) ----------
    if "best_season" in data and isinstance(data["best_season"], list):
        data["best_season"] = [s.strip().lower() for s in data["best_season"]]
    else:
        data["best_season"] = []

    #highlights
    if "highlights" in data and not isinstance(data["highlights"], list):
        raise ValueError("highlights must be a list")

    # ---------- SAFE DEFAULTS ----------
    data["type"] = "waterfall"

    data["image"] = str(data.get("image", "")).strip()
    data["is_active"] = bool(data.get("is_active", True))
    data["is_featured"] = bool(data.get("is_featured", False))

    if data["is_featured"]:
        data["featured_rank"] = int(data.get("featured_rank", 0))
    else:
        data["featured_rank"] = None
        

    return data

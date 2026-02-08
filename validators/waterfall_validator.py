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
        normalized = []
        for season in data["best_season"]:
            season = str(season).strip().lower()
            if season in SEASONS:
                normalized.append(season)
        data["best_season"] = normalized
    else:
        data["best_season"] = []

    # ---------- SAFE DEFAULTS ----------
    data["image"] = str(data.get("image", "")).strip()
    data["is_active"] = bool(data.get("is_active", True))
    data["is_featured"] = bool(data.get("is_featured", True))
    data["featured_rank"] = int(data.get("featured_rank", 1))
    data["type"] = "waterfall"

    return data

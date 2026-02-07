from flask import Blueprint, request
from pymongo.errors import DuplicateKeyError
from validators.waterfall_validator import validate_waterfall
from db import waterfalls_collection

admin_waterfalls = Blueprint("admin_waterfalls", __name__)

@admin_waterfalls.route("/waterfalls", methods=["POST"])
def create_waterfall():
    if not request.is_json:
        return {"error": "JSON body required"}, 400

    data = request.get_json()
    validate_waterfall(data)

    try:
        waterfalls_collection.insert_one(data)
    except DuplicateKeyError:
        return {"error": "Slug already exists"}, 400

    return {"status": "created"}, 201

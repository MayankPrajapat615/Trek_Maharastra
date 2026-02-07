from flask import Blueprint, request
from pymongo.errors import DuplicateKeyError
from validators.trek_validator import validate_trek
from db import treks_collection

admin_treks = Blueprint("admin_treks", __name__)

@admin_treks.route("/treks", methods=["POST"])
def create_trek():
    if not request.is_json:
        return {"error": "JSON body required"}, 400

    data = request.get_json()
    validate_trek(data)

    try:
        treks_collection.insert_one(data)
    except DuplicateKeyError:
        return {"error": "Slug already exists"}, 400

    return {"status": "created"}, 201
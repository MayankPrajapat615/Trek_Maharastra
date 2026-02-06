from flask import app, jsonify
from flask import request
from app import create_app, insert_trek

@app.route("/admin/treks", methods=["POST"])
def create_trek():
    if not request.is_json:
        return {"error": "JSON body required"}, 400

    data = request.get_json()

    try:
        insert_trek(data)
    except ValueError as e:
        return {"error": str(e)}, 400
    except Exception as e:
        return {"error": "Internal server error"}, 500

    return {"status": "created"}, 201
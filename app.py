from flask import Flask, render_template, request, abort, jsonify
#DTABASE IMPORTS 
from pymongo import MongoClient
from xmlrpc import client
from pymongo.errors import DuplicateKeyError
from validators.trek_validator import validate_trek
from db import treks_collection, waterfalls_collection
from flask_cors import CORS


def create_app():

    app = Flask(__name__)

    def insert_trek(data):
        validate_trek(data)
        try:
            treks_collection.insert_one(data)
        except DuplicateKeyError:
            raise ValueError("Slug already exists")
    
    @app.route("/ping")
    def ping():
        return jsonify({'status': "ok"})
    
    @app.route('/test-db')
    def test_db():
        count = treks_collection.count_documents({})
        return jsonify({"Treks": count})
    
    @app.route("/__health")
    def health():
        try:
            treks_collection.find_one()
            return {"status": "ok", "db": "connected"}
        except Exception as e:
            return {"status": "fail", "error": str(e)}, 500

    
    @app.route('/')
    def home():
        return render_template('home.html')

    
    #SEARCH ROUTE
    @app.route('/search')
    def search():
        query = request.args.get("q", "").strip()

        if not query:
            return jsonify([])

        regex = {"$regex": query, "$options": "i"}

        treks = list(
            treks_collection.find(
                {
                    "$or": [
                        {"name": regex},
                        {"location.district": regex},
                        {"location.region": regex}
                    ]
                },
                {"_id":0}
            )
        )

        waterfalls = list(
            waterfalls_collection.find(
                {
                    "$or": [
                        {"name": {"$regex": query, "$options": "i"}},
                        {"location.district": {"$regex": query, "$options": "i"}},
                        {"location.region": {"$regex": query, "$options": "i"}},
                    ]
                },
                {"_id": 0}
            )
        )

        return jsonify({
            "treks": treks,
            "waterfalls": waterfalls
        })

        
    @app.route('/api/treks')
    def get_treks():
        treks = list(treks_collection.find({}, {"_id": 0}))
        return jsonify(treks)


    #TREK ROUTE 
    @app.route('/treks')
    def treks_page():
        treks = list(treks_collection.find( {}, {"_id": 0} ))
        return render_template('treks.html', treks=treks)

    #WATERFALLS ROUTE 
    @app.route('/waterfalls')
    def waterfalls_page():
        waterfalls = list(waterfalls_collection.find({}, {"_id": 0}))
        return render_template('waterfalls.html', waterfalls=waterfalls)

    #TREK SLUG ROUTE 
    @app.route('/treks/<slug>')
    def trek_details(slug):
        trek = treks_collection.find_one( {"slug": slug}, {"_id":0} )
        if not trek:
            abort(404)
        return render_template('trek_details.html', trek=trek)
    
    #ADMIN ROUTE TO ADD TREKS
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


    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
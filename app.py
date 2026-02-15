from flask import Flask, render_template, request, abort, jsonify
from  datetime import datetime, timedelta, timezone

#DTABASE IMPORTS 
from pymongo import MongoClient
from xmlrpc import client
from pymongo.errors import DuplicateKeyError
from validators.trek_validator import validate_trek
from validators.waterfall_validator import validate_waterfall
from db import treks_collection, waterfalls_collection
from flask_cors import CORS
from admin import admin_treks, admin_waterfalls


def create_app():

    app = Flask(__name__)

    app.register_blueprint(admin_waterfalls, url_prefix="/admin")
    app.register_blueprint(admin_treks, url_prefix="/admin")
    

    #<------------TEST ROUTES---------------->
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
        treks = list(
            treks_collection.find( 
                {"is_active":True, "is_featured":True}, 
                {"_id":0} ).sort("featured_rank", 1).limit(3)
        )
        treks = [add_new_flag(t) for t in treks]

        waterfalls = list(
            waterfalls_collection.find(
                {"is_active":True, "is_featured":True},
                {"_id":0}).sort("featured_rank", 1).limit(3)
        )
        waterfalls = [add_new_flag(w) for w in waterfalls]

        return render_template('home.html', treks=treks, waterfalls=waterfalls)
    


    #<-------------SEARCH ROUTE----------------->
    @app.route('/search')
    def search():
        # time.sleep(2)  // added just to check wheather the loading stats was working or not
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


    @app.route("/search-page")
    def search_page():
        query = request.args.get("q", "").strip()

        if not query:
            return render_template("search_results.html", treks=[], waterfalls=[], query=query)

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
                {"_id": 0}
            )
        )

        waterfalls = list(
            waterfalls_collection.find(
                {
                    "$or": [
                        {"name": regex},
                        {"location.district": regex},
                        {"location.region": regex}
                    ]
                },
                {"_id": 0}
            )
        )

        return render_template(
            "search_results.html",
            treks=treks,
            waterfalls=waterfalls,
            query=query
        )


    @app.route('/api/treks')
    def get_treks():
        treks = list(treks_collection.find({}, {"_id": 0}))
        return jsonify(treks)
    

    #<----------------ROUTES FOR THE TREKS AND WATERFALL PAGES----------------->
    @app.route('/treks' , methods=["GET"])
    def treks_page():
        difficulty = request.args.get("difficulty")
        
        query = {}

        if difficulty:
            query["difficulty"] = {
                "$regex": f"^{difficulty}$",
                "$options": "i"
            }

        treks = list(treks_collection.find(query, {"_id": 0}))
        treks = [add_new_flag(t) for t in treks]

        return render_template('treks.html', treks=treks, active_difficulty=difficulty)

    @app.route('/waterfalls')
    def waterfalls_page():
        difficulty = request.args.get("difficulty")

        query = {}

        if difficulty:
            query["difficulty"] = {
                "$regex" : f"^{difficulty}$",
                "$options" : "i"
            }

        waterfalls = list(waterfalls_collection.find(query, {"_id": 0}))
        waterfalls = [add_new_flag(w) for w in waterfalls]

        return render_template('waterfalls.html', waterfalls=waterfalls, active_difficulty=difficulty)
    

    #<-----------------SLUG ROUTES FOR TREKS AND WATERFALLS--------------------->
    @app.route('/treks/<slug>')
    def trek_details(slug):
        # time.sleep(4)
        trek = treks_collection.find_one( {"slug": slug}, {"_id":0} )
        if not trek:
            abort(404)
        return render_template('trek_details.html', trek=trek)
    
    @app.route('/waterfalls/<slug>')
    def waterfall_deatil(slug):
        waterfall = waterfalls_collection.find_one( {"slug":slug}, {"_id":0} )
        if not waterfall:
            abort(404)

        return render_template("waterfall_details.html", waterfall=waterfall)
    

    # <--------------------IS_FEATURED ROUTE FOR TREKS AND WATERFALLS-------------------->
    def add_new_flag(item):
        now = datetime.now(timezone.utc)
        threshold = now - timedelta(hours=48)

        created_at = item.get("created_at")


        if created_at:
            # Convert naive to UTC-aware
            if created_at.tzinfo is None:
                created_at = created_at.replace(tzinfo=timezone.utc)

            item["is_new"] = created_at >= threshold
        else:
            item["is_new"] = False

        return item


    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
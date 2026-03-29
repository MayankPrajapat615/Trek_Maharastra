from flask import Flask, render_template, request, abort, jsonify, session, redirect, url_for, flash
from datetime import datetime, timedelta, timezone
import bcrypt
import os
import uuid

# DATABASE IMPORTS
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from validators.trek_validator import validate_trek
from validators.waterfall_validator import validate_waterfall
from db import treks_collection, waterfalls_collection, users_collection, bookings_collection  # ← added users_collection
from flask_cors import CORS
from admin import admin_treks, admin_waterfalls


def create_app():

    app = Flask(__name__)
    app.secret_key = os.getenv("SECRET_KEY")

    app.register_blueprint(admin_waterfalls, url_prefix="/admin")
    app.register_blueprint(admin_treks, url_prefix="/admin")


    # ─────────────────────────────────────────
    # HELPER — get logged-in user from session
    # ─────────────────────────────────────────
    def get_current_user():
        user_id = session.get("user_id")
        print(">>> SESSION CONTENTS:", dict(session)) 
        print(">>> user_id from session:", user_id)      
        if not user_id:
            return None
        user = users_collection.find_one({"email": user_id}, {"_id": 0, "password": 0})
        print(">>> USER FOUND:", user)               
        return user
    
    
    # Inject current_user into ALL templates automatically
    @app.context_processor
    def inject_user():
        user = get_current_user()
        return {"current_user": user}


    # ─────────────────────────────────────────
    # TEST ROUTES
    # ─────────────────────────────────────────
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


    # ─────────────────────────────────────────
    # HOME
    # ─────────────────────────────────────────
    @app.route('/')
    def home():
        treks = list(
            treks_collection.find(
                {"is_active": True, "is_featured": True}, {"_id": 0}
            ).sort("featured_rank", 1).limit(3)
        )
        treks = [add_new_flag(t) for t in treks]

        waterfalls = list(
            waterfalls_collection.find(
                {"is_active": True, "is_featured": True}, {"_id": 0}
            ).sort("featured_rank", 1).limit(3)
        )
        waterfalls = [add_new_flag(w) for w in waterfalls]

        hero_items = []
        for trek in treks:
            hero_items.append({"type": "trek", "name": trek["name"], "image": trek["image"]})
        for waterfall in waterfalls:
            hero_items.append({"type": "waterfall", "name": waterfall["name"], "image": waterfall["image"]})

        return render_template("home.html", treks=treks, waterfalls=waterfalls, hero_items=hero_items)


    # ─────────────────────────────────────────
    # SEARCH
    # ─────────────────────────────────────────
    @app.route('/search')
    def search():
        query = request.args.get("q", "").strip()
        if not query:
            return jsonify([])

        regex = {"$regex": query, "$options": "i"}

        treks = list(treks_collection.find(
            {"$or": [{"name": regex}, {"location.district": regex}, {"location.region": regex}]},
            {"_id": 0}
        ))
        waterfalls = list(waterfalls_collection.find(
            {"$or": [{"name": regex}, {"location.district": regex}, {"location.region": regex}]},
            {"_id": 0}
        ))

        return jsonify({"treks": treks, "waterfalls": waterfalls})

    @app.route("/search-page")
    def search_page():
        query = request.args.get("q", "").strip()
        if not query:
            return render_template("search_results.html", treks=[], waterfalls=[], query=query)

        regex = {"$regex": query, "$options": "i"}

        treks = list(treks_collection.find(
            {"$or": [{"name": regex}, {"location.district": regex}, {"location.region": regex}]},
            {"_id": 0}
        ))
        waterfalls = list(waterfalls_collection.find(
            {"$or": [{"name": regex}, {"location.district": regex}, {"location.region": regex}]},
            {"_id": 0}
        ))

        return render_template("search_results.html", treks=treks, waterfalls=waterfalls, query=query)

    @app.route('/api/treks')
    def get_treks():
        treks = list(treks_collection.find({}, {"_id": 0}))
        return jsonify(treks)


    # ─────────────────────────────────────────
    # AUTH — Register / Login / Logout
    # ─────────────────────────────────────────

    @app.route('/auth', methods=["GET"])
    def auth():
        # If already logged in, redirect to home
        if session.get("user_id"):
            return redirect(url_for("profile"))
        return render_template('auth.html')


    @app.route('/register', methods=["POST"])
    def register():
        first_name  = request.form.get("first_name", "").strip()
        last_name   = request.form.get("last_name", "").strip()
        email       = request.form.get("email", "").strip().lower()
        password    = request.form.get("password", "")
        confirm     = request.form.get("confirm_password", "")

        # ── Basic server-side validation ──
        if not all([first_name, last_name, email, password, confirm]):
            flash("All fields are required.", "error")
            return redirect(url_for("auth") + "?tab=register")

        if len(password) < 8:
            flash("Password must be at least 8 characters.", "error")
            return redirect(url_for("auth") + "?tab=register")

        if password != confirm:
            flash("Passwords do not match.", "error")
            return redirect(url_for("auth") + "?tab=register")

        # ── Check if email already exists ──
        existing = users_collection.find_one({"email": email})
        if existing:
            flash("An account with this email already exists. Please log in.", "error")
            return redirect(url_for("auth"))

        # ── Hash password with bcrypt ──
        hashed_pw = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

        # ── Build user document ──
        new_user = {
            "first_name":  first_name,
            "last_name":   last_name,
            "email":       email,
            "password":    hashed_pw,        # stored as bytes (bcrypt)
            "created_at":  datetime.now(timezone.utc),
            "is_active":   True,
        }

        # ── Insert into MongoDB ──
        users_collection.insert_one(new_user)

        # ── Log the user in immediately after registration ──
        session["user_id"]    = email
        session["user_name"]  = first_name
        session.permanent     = True
        app.permanent_session_lifetime = timedelta(days=7)

        flash(f"Welcome to Trek Maharashtra, {first_name}! 🎉", "success")
        return redirect(url_for("profile"))
    
    @app.route('/profile')
    def profile():
        if not session.get("user_id"):
            flash("Please log in to view your profile.", "error")
            return redirect(url_for("auth"))

        # Fetch this user's bookings from MongoDB
        user_email = session.get("user_id")
        bookings = list(
            bookings_collection.find(
                {"booked_by": user_email},
                {"_id": 0}
            ).sort("created_at", -1)  # newest first
        )
        return render_template('auth.html', bookings=bookings)


    @app.route('/login', methods=["POST"])
    def login():
        email    = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        remember = request.form.get("remember")   # checkbox value

        # ── Basic validation ──
        if not email or not password:
            flash("Please enter your email and password.", "error")
            return redirect(url_for("auth"))

        # ── Look up user in MongoDB ──
        user = users_collection.find_one({"email": email})

        if not user:
            flash("No account found with that email.", "error")
            return redirect(url_for("auth"))

        # ── Check password with bcrypt ──
        password_matches = bcrypt.checkpw(password.encode("utf-8"), user["password"])

        if not password_matches:
            flash("Incorrect password. Please try again.", "error")
            return redirect(url_for("auth"))

        # ── Log in — save to session ──
        session["user_id"]   = email
        session["user_name"] = user["first_name"]

        if remember:
            session.permanent = True
            app.permanent_session_lifetime = timedelta(days=30)
        else:
            session.permanent = False   # session ends when browser closes

        flash(f"Welcome back, {user['first_name']}! 👋", "success")
        return redirect(url_for("profile"))


    @app.route('/logout')
    def logout():
        session.clear()
        flash("You've been logged out successfully.", "success")
        return redirect(url_for("home"))


    # ─────────────────────────────────────────
    # TREKS
    # ─────────────────────────────────────────
    @app.route('/treks', methods=["GET"])
    def treks_page():
        difficulty = request.args.get("difficulty")
        page       = request.args.get('page', 1, type=int)
        per_page   = 12

        query = {}
        if difficulty:
            query["difficulty"] = {"$regex": f"^{difficulty}$", "$options": "i"}

        total       = treks_collection.count_documents(query)
        total_pages = (total + per_page - 1) // per_page

        treks = list(
            treks_collection.find(query, {"_id": 0})
            .skip((page - 1) * per_page)
            .limit(per_page)
        )
        treks = [add_new_flag(t) for t in treks]

        class Pagination:
            def __init__(self):
                self.page     = page
                self.pages    = total_pages
                self.total    = total
                self.per_page = per_page
                self.has_prev = page > 1
                self.has_next = page < total_pages
                self.prev_num = page - 1
                self.next_num = page + 1

            def iter_pages(self, left_edge=1, right_edge=1, left_current=2, right_current=2):
                last = 0
                for num in range(1, self.pages + 1):
                    if (num <= left_edge or
                        (self.page - left_current <= num <= self.page + right_current) or
                            num > self.pages - right_edge):
                        if last + 1 != num:
                            yield None
                        yield num
                        last = num

        return render_template('treks.html', treks=treks, active_difficulty=difficulty, pagination=Pagination())


    # ─────────────────────────────────────────
    # WATERFALLS
    # ─────────────────────────────────────────
    @app.route('/waterfalls', methods=["GET"])
    def waterfalls_page():
        difficulty = request.args.get("difficulty")
        page       = request.args.get('page', 1, type=int)
        per_page   = 12

        query = {}
        if difficulty:
            query["difficulty"] = {"$regex": f"^{difficulty}$", "$options": "i"}

        total       = waterfalls_collection.count_documents(query)
        total_pages = (total + per_page - 1) // per_page

        waterfalls = list(
            waterfalls_collection.find(query, {"_id": 0})
            .skip((page - 1) * per_page)
            .limit(per_page)
        )
        waterfalls = [add_new_flag(w) for w in waterfalls]

        class Pagination:
            def __init__(self):
                self.page     = page
                self.pages    = total_pages
                self.total    = total
                self.per_page = per_page
                self.has_prev = page > 1
                self.has_next = page < total_pages
                self.prev_num = page - 1
                self.next_num = page + 1

            def iter_pages(self, left_edge=1, right_edge=1, left_current=2, right_current=2):
                last = 0
                for num in range(1, self.pages + 1):
                    if (num <= left_edge or
                        (self.page - left_current <= num <= self.page + right_current) or
                            num > self.pages - right_edge):
                        if last + 1 != num:
                            yield None
                        yield num
                        last = num

        return render_template('waterfalls.html', waterfalls=waterfalls, active_difficulty=difficulty, pagination=Pagination())


    # ─────────────────────────────────────────
    # OTHER PAGES
    # ─────────────────────────────────────────
    @app.route('/about-us')
    def about_us():
        return render_template('about-us.html')

    @app.route('/rentals')
    def rentals():
        return render_template('rentals.html')

    @app.route('/plan-your-trek')
    def plan_your_trek():
        return render_template('plan-your-trek.html')
    
    @app.route('/directions')
    def directions():
        trek_name = request.args.get('trek', '')
        return render_template('directions.html', trek_name=trek_name)
    
    # ─────────────────────────────────────────
    # BOOK AND CHECKOUTPAGE 
    # ─────────────────────────────────────────
    @app.route('/book')
    def book():
        if not session.get("user_id"):
            flash("Please log in first to book a trek.", "error")
            return redirect(url_for("auth"))
        return render_template('book.html')
    
    @app.route('/api/demo-payment', methods=["POST"])
    def demo_payment():
        if not session.get("user_id"):
            return jsonify({"success": False, "error": "Not logged in"}), 401
        try:
            data = request.get_json(force=True)

            if not data or "booking" not in data:
                return jsonify({"success": False, "error": "No booking data received"}), 400

            booking_data = data["booking"]
            booking_id   = "TM-" + uuid.uuid4().hex[:6].upper()

            booking = {
                "booking_id":     booking_id,
                "trek":           booking_data.get("trek", ""),
                "operator":       booking_data.get("operator", ""),
                "date":           booking_data.get("date", ""),
                "adults":         booking_data.get("adults", 1),
                "teens":          booking_data.get("teens", 0),
                "kids":           booking_data.get("kids", 0),
                "lead_name":      booking_data.get("lead_name", ""),
                "lead_email":     booking_data.get("lead_email", ""),
                "lead_phone":     booking_data.get("lead_phone", ""),
                "em_name":        booking_data.get("em_name", ""),
                "em_phone":       booking_data.get("em_phone", ""),
                "em_relation":    booking_data.get("em_relation", ""),
                "fitness":        booking_data.get("fitness", ""),
                "gear":           list(booking_data.get("gear", {}).keys()),  # store as list of keys
                "special":        booking_data.get("special", ""),
                "amount":         booking_data.get("amount", 0),
                "payment_status": "paid",
                "payment_method": "demo",
                "booked_by":      session.get("user_id"),
                "created_at":     datetime.now(timezone.utc),
            }

            bookings_collection.insert_one(booking)

            return jsonify({"success": True, "booking_id": booking_id})

        except Exception as e:
            print("❌ demo_payment error:", str(e))   # you'll see this in your terminal
            return jsonify({"success": False, "error": str(e)}), 500
        
    @app.route('/my-bookings')
    def my_bookings():
        if not session.get("user_id"):
            flash("Please log in to view your bookings.", "error")
            return redirect(url_for("auth"))

        user_email = session.get("user_id")
        bookings = list(
            bookings_collection.find(
                {"booked_by": user_email},
                {"_id": 0}
            ).sort("created_at", -1)  # newest first
        )
        return render_template('my-bookings.html', bookings=bookings)    
    

    # ─────────────────────────────────────────
    # SLUG ROUTES
    # ─────────────────────────────────────────
    @app.route('/treks/<slug>')
    def trek_details(slug):
        trek = treks_collection.find_one({"slug": slug}, {"_id": 0})
        if not trek:
            abort(404)
        return render_template('trek_details.html', trek=trek)

    @app.route('/waterfalls/<slug>')
    def waterfall_deatil(slug):
        waterfall = waterfalls_collection.find_one({"slug": slug}, {"_id": 0})
        if not waterfall:
            abort(404)
        return render_template("waterfall_details.html", waterfall=waterfall)


    # ─────────────────────────────────────────
    # UTILITY
    # ─────────────────────────────────────────
    def add_new_flag(item):
        now       = datetime.now(timezone.utc)
        threshold = now - timedelta(hours=48)
        created_at = item.get("created_at")

        if created_at:
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
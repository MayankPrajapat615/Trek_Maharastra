from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///locations.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from models.locations import Location
    from models.treks import Trek
    from models.waterfalls import Waterfall
    from models.highlights import Highlight

    @app.route('/')
    def home():
        return render_template('home.html')
    
    @app.route('/search')
    def search():
        query = request.args.get("q", "").strip()

        if not query:
            return render_template("treks.html", treks=[])
        
        treks = (
            db.session.query(Trek)
            .join(Location)
            .filter(
                db.or_(
                    Trek.name.ilike(f"%{query}%"),
                    Location.district.ilike(f"%{query}%"),
                    Location.region.ilike(f"%{query}%")
                )
            )
            .all()
        )
    
        return render_template("treks.html", treks=treks, query=query)

    @app.route('/treks')
    def treks_page():
        treks = Trek.query.all()
        return render_template('treks.html', treks=treks)

    @app.route('/waterfalls')
    def waterfalls_page():
        waterfalls = Waterfall.query.all()
        return render_template('waterfalls.html', waterfalls=waterfalls)

    @app.route('/treks/<slug>')
    def trek_details(slug):
        trek = Trek.query.filter_by(slug=slug).first_or_404()
        return render_template('trek_details.html', trek=trek)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
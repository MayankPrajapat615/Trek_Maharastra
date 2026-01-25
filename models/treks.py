from app import db

class Trek(db.Model):
    __tablename__ = "treks"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(150), nullable=False)
    slug = db.Column(db.String(150), nullable=False, unique=True)

    location_id = db.Column(db.Integer, db.ForeignKey("locations.id"), nullable=False)

    difficulty = db.Column(db.String(20),nullable=False)

    distance_km = db.Column(db.Float)
    elevation_m = db.Column(db.Integer)

    best_season = db.Column(db.String(100))
    description = db.Column(db.Text)

    created_at = db.Column(db.DateTime, server_default=db.func.current_timestamp())

    location = db.relationship("Location", backref="treks")
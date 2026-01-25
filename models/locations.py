from app import db

class Location(db.Model):
    __tablename__ = "locations"

    id = db.Column(db.Integer, primary_key=True)
    district = db.Column(db.String(100), nullable=False, index=True)
    region = db.Column(db.String(100))
    state = db.Column(db.String(50), default="Maharashtra")
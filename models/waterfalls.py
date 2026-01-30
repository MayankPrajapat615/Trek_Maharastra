from app import db 

class Waterfall(db.Model):
    __tablename__ = "waterfalls"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(150), nullable=False)
    slug = db.Column(db.String(150), unique=True, nullable=False)

    location_id = db.Column(db.Integer, db.ForeignKey("locations.id"), nullable=False)
    
    height_m = db.Column(db.Integer)
    is_seasonal = db.Column(db.Boolean, default=True)
    best_season = db.Column(db.String(100))
    description = db.Column(db.Text)

    created_at = db.Column(db.DateTime, server_default=db.func.current_timestamp())

    location = db.relationship("Location", backref="waterfalls")

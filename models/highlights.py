from app import db

class Highlight(db.Model):
    __tablename__ = "highlights"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    highlight_type = db.Column(db.Text)
    description = db.Column(db.Text)

    trek_id = db.Column(db.Integer, db.ForeignKey("treks.id"), nullable=False)
    trek = db.relationship("Trek", backref="highlights")
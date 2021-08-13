from .db import db


class Gym(db.Model):
    __tablename__ = "gyms"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.String(200), nullable=False, unique=True)
    latitude = db.Column(db.Numeric, nullable=False)
    longitude = db.Column(db.Numeric, nullable=False)
    location = db.Column(db.String(50), nullable=False)
    url_img = db.Column(db.String(200), unique=True)
    

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "location": self.location,
            "url_img": self.url_img,
        }

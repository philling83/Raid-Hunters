from .db import db


class Boss(db.Model):
    __tablename__ = "bosses"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    url_img = db.Column(db.String(200), unique=True)
    min_cp_range = db.Column(db.Integer, nullable=False)
    max_cp_range = db.Column(db.Integer, nullable=False)
    boosted_min_cp_range = db.Column(db.Integer, nullable=False)
    boosted_max_cp_range = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "url_img": self.url_img,
            "min_cp_range": self.min_cp_range,
            "max_cp_range": self.max_cp_range,
            "boosted_min_cp_range": self.boosted_min_cp_range,
            "boosted_max_cp_range": self.boosted_max_cp_range,
        }

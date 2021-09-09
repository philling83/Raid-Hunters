from .db import db
from .raid_pokemon_type import raid_pokemon_types


class Raid(db.Model):
    __tablename__ = "raids"

    id = db.Column(db.Integer, primary_key=True)
    pokemon = db.Column(db.String(50), nullable=False, unique=True)
    tier = db.Column(db.String(50), nullable=False)
    url_img = db.Column(db.String(200), unique=True)
    min_cp_range = db.Column(db.Integer, nullable=False)
    max_cp_range = db.Column(db.Integer, nullable=False)
    boosted_min_cp_range = db.Column(db.Integer, nullable=False)
    boosted_max_cp_range = db.Column(db.Integer, nullable=False)
    is_active = db.Column(db.Boolean, nullable=False)
    gym_id = db.Column(db.Integer, db.ForeignKey("gyms.id"))

    gym = db.relationship("Gym")
    types = db.relationship("Type", secondary=raid_pokemon_types, back_populates="raids")
    

    def to_dict(self):
        return {
            "id": self.id,
            "pokemon": self.pokemon,
            "tier": self.tier,
            "url_img": self.url_img,
            "min_cp_range": self.min_cp_range,
            "max_cp_range": self.max_cp_range,
            "boosted_min_cp_range": self.boosted_min_cp_range,
            "boosted_max_cp_range": self.boosted_max_cp_range,
            "gym_id": self.gym_id,
            "is_active": self.is_active,
            "types": [type.name for type in self.types],
        }
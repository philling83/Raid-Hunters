from .db import db
from .raid_pokemon_type import raid_pokemon_types


class Type(db.Model):
    __tablename__ = 'types'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

    raids = db.relationship("Raid", secondary=raid_pokemon_types, back_populates="types")


    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
        }

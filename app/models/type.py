from .db import db
from .boss_type import boss_types


class Type(db.Model):
    __tablename__ = 'types'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

    bosses = db.relationship("Boss", secondary=boss_types, back_populates="types")


    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
        }

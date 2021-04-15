from .db import db


raid_pokemon_types = db.Table(
    "raid_pokemon_types",
    db.Column("raid_id", db.Integer, db.ForeignKey("raids.id"), primary_key=True),
    db.Column("type_id", db.Integer, db.ForeignKey("types.id"), primary_key=True),
)
from .db import db


boss_types = db.Table(
    "boss_types",
    db.Column("boss_id", db.Integer, db.ForeignKey("bosses.id"), primary_key=True),
    db.Column("type_id", db.Integer, db.ForeignKey("types.id"), primary_key=True),
)
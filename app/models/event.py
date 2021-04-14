from .db import db
from sqlalchemy.dialects import postgresql


class Event(db.Model):
    __tablename__ = "events"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    participants = db.Column(postgresql.ARRAY(db.String))
    start_time = db.Column(db.DateTime, nullable=False)
    host_id =  db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    raid_id = db.Column(db.Integer, db.ForeignKey("raids.id"), nullable=False)
    
    host = db.relationship("User")
    raid = db.relationship("Raid")


    def to_dict(self):
        return {
            "id": self.id,
            "tier": self.tier,
            "gym_id": self.gym_id,
            "boss_id": self.boss_id
        }
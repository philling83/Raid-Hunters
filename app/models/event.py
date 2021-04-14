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
            "name": self.name,
            "participants": self.participants,
            "start_time": self.start_time,
            "host_id": self.host_id,
            "raid_id": self.raid_id,
        }
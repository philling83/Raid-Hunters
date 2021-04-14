from .db import db


class Event(db.Model):
    __tablename__ = "events"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    participants = 
    start_time = db.Column(db.DateTime, nullable=False)
    gym_id =  db.Column(db.Integer, db.ForeignKey("gyms.id"), nullable=False)
    boss_id = db.Column(db.Integer, db.ForeignKey("bosses.id"), nullable=False)
    

    def to_dict(self):
        return {
            "id": self.id,
            "tier": self.tier,
            "gym_id": self.gym_id,
            "boss_id": self.boss_id
        }
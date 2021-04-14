from .db import db


class Raid(db.Model):
    __tablename__ = "raids"

    id = db.Column(db.Integer, primary_key=True)
    tier = db.Column(db.Integer, nullable=False)
    gym_id =  db.Column(db.Integer, db.ForeignKey("gyms.id"))
    boss_id = db.Column(db.Integer, db.ForeignKey("bosses.id"), nullable=False)

    gym = db.relationship("Gym")
    boss = db.relationship("Boss")
    

    def to_dict(self):
        return {
            "id": self.id,
            "tier": self.tier,
            "gym_id": self.gym_id,
            "boss_id": self.boss_id
        }
from flask import Blueprint
from app.models import Raid

raid_routes = Blueprint('raids', __name__)


@raid_routes.route('/')
def raids():
    raids = Raid.query.filter_by(is_active=True)
    return {"raids": [raid.to_dict() for raid in raids]}
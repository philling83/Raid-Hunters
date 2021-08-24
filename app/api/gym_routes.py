from flask import Blueprint
from app.models import Gym

gym_routes = Blueprint('gyms', __name__)


@gym_routes.route('/')
def gyms():
    gyms = Gym.query.all()
    return {"gyms": [gym.to_dict() for gym in gyms]}

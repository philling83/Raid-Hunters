from flask import Blueprint
from app.models import Team

team_routes = Blueprint('teams', __name__)


@team_routes.route('/')
def teams():
    teams = Team.query.all()
    return {"teams": [team.to_dict() for team in teams]}

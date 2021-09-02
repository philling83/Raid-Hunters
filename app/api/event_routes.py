from flask import Blueprint
from app.models import Event

event_routes = Blueprint('events', __name__)


@event_routes.route('/')
def events():
    events = Event.query.all()
    return {"events": [event.to_dict() for event in events]}

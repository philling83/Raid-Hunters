# Raid-Hunters

# Introduction and Features

This project will allow users to find raids in their area and create events that allow users to team up to defeat raid bosses!


## Technologies Used
**Backend**
- Python (Flask)
- React/Redux
- PostgreSQL
- SQLAlchemy Object Relational Mapper
- Werkzeug
- pyjwt. Generates javascript web tokens for user sessions
- Alembic. Engine for database relational migrations

## Frontend Routes
**Splash**
- / -> Homepage welcomes new users/ existing users with auth modal

**Authentication**
- /sign-up -> signs up for an account
- /login -> Existing users sign-in

**Map View**
- / Displays map with pins of all the gyms in area

**User profile**
- /user displays events user created and events user has joined

**Gyms**
- /gyms -> displays a list of all gyms
- /gyms/id/events -> display info about single gym including events

**Raids**
- /raids -> display all possible raids

**Events**
- /events displays all events in the area

## API Documentation
## Endpoints
**Auth**
- Login POST /api/auth/login
- Sign Up POST /api/auth/signup
- Log out GET /api/auth/logout

**Users**
- Get all users GET /api/users
- Create user event POST /api/users/<id>/create-event
- Edit user event PUT /api/users/<id>/events/id
- Delete user event DELETE /api/users/<id>/events/id

**Gyms**
- Get all gyms GET -> /api/gyms
- Get single gym GET -> /api/gyms/id

**Raids**
- Get all raids GET -> /api/raids

**Events**
- Get all events GET -> /api/events
- Get single event GET -> /api/events/id
## Database and Schema
![DB Schema](db-schema.png)

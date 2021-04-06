# Raid-Hunters

# Introduction and Features

This project will allow users to find raids in their area and create events that allow users to team up to defeat raid bosses!


## Technologies Used
**Backend**
- Python (Flask)
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
**User**
- Login POST /api/auth/login
- Sign Up POST /api/auth/signup
- Log out GET /api/auth/logout

**Gym**
- Get all gyms GET -> /gyms
- 


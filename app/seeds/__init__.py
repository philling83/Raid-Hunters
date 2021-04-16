from flask.cli import AppGroup
from .users import seed_users, undo_users
from .teams import seed_teams, undo_teams
from .types import seed_types, undo_types
from .raids import seed_raids, undo_raids

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')

# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    # seed_teams()
    # seed_users()
    # seed_types()
    seed_raids()
    # Add other seed functions here

# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_raids()
    undo_types()
    undo_teams()
    undo_users()
    # Add other undo functions here

from app.models import db, Team

def seed_teams():

    team1 = Team(name='Valor')
    team2 = Team(name='Mystic')
    team3 = Team(name='Instinct')

    db.session.add(team1)
    db.session.add(team2)
    db.session.add(team3)

    db.session.commit()

def undo_teams():
    db.session.execute('TRUNCATE teams RESTART IDENTITY CASCADE;')
    db.session.commit()

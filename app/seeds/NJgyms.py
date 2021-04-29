from app.models import db, Gym


def seed_NJgyms():

    db.session.add()
    db.session.add()
    db.session.add()
    db.session.add()

    db.session.commit()


def undo_NJgyms():
    db.session.execute('TRUNCATE gyms RESTART IDENTITY CASCADE;')
    db.session.commit()

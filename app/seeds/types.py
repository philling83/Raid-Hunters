from app.models import db, Type


def seed_types():

    type1 = Type(name='Normal')
    type2 = Type(name='Fire')
    type3 = Type(name='Water')
    type4 = Type(name='Electric')
    type5 = Type(name='Grass')
    type6 = Type(name='Ice')
    type7 = Type(name='Fighting')
    type8 = Type(name='Poison')
    type9 = Type(name='Ground')
    type10 = Type(name='Flying')
    type11 = Type(name='Psychic')
    type12 = Type(name='Bug')
    type13 = Type(name='Rock')
    type14 = Type(name='Ghost')
    type15 = Type(name='Dragon')
    type16 = Type(name='Dark')
    type17 = Type(name='Steel')
    type18 = Type(name='Fairy')

    db.session.add(type1)
    db.session.add(type2)
    db.session.add(type3)
    db.session.add(type4)
    db.session.add(type5)
    db.session.add(type6)
    db.session.add(type7)
    db.session.add(type8)
    db.session.add(type9)
    db.session.add(type10)
    db.session.add(type11)
    db.session.add(type12)
    db.session.add(type13)
    db.session.add(type14)
    db.session.add(type15)
    db.session.add(type16)
    db.session.add(type17)
    db.session.add(type18)

    db.session.commit()


def undo_types():

    db.session.execute("TRUNCATE types RESTART IDENTITY CASCADE;")
    db.session.commit()

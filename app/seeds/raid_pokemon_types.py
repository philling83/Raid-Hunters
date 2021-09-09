from app.models import db, raid_pokemon_types


def seed_raid_pokemon_types():

    db.session.execute("INSERT INTO raid_pokemon_types (raid_id, type_id) \
                        VALUES (5, 3), (5, 11), (6, 11), (6, 10), (7, 4), \
                        (7, 11), (8, 11), (9, 7), (9, 11), (10, 17), (10,11), \
                        (11, 3), (12, 11), (13, 17), (13, 11), (14, 11), \
                        (15, 16), (15, 11)"
    )

    db.session.commit()

def undo_raid_pokemon_types():

    db.session.execute("TRUNCATE raid_pokemon_types RESTART IDENTITY CASCADE;")
    db.session.commit()

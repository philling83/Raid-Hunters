from app.models import db, Gym


def seed_NJgyms():

    gym1 = Gym(name="Patriots' Path Chester", description="Trailhead leading to Chubb Park and Chester Furnace Historical Site",
               latitude="40.781", longitude="-74.704", location="Chester, NJ", url_img="test.url")
    gym2 = Gym(name="Chester Library", description="",
               latitude="40.781", longitude="-74.706", location="Chester, NJ", url_img="test2.url")

    db.session.add(gym1)
    db.session.add(gym2)

    db.session.commit()


def undo_NJgyms():
    db.session.execute('TRUNCATE gyms RESTART IDENTITY CASCADE;')
    db.session.commit()

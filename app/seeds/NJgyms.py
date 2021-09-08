from app.models import db, Gym


def seed_NJgyms():

    gym1 = Gym(name="Patriots' Path Chester", description="Trailhead leading to Chubb Park and Chester Furnace Historical Site",
               latitude="40.781", longitude="-74.704", location="Chester, NJ", url_img="http://patriotspathtrailmaps.weebly.com/uploads/5/3/6/4/5364549/8913350_orig.jpg")
    gym2 = Gym(name="Chester Library", description="Chester Library is a member of M.A.I.N., Inc. a consortium of 49 public libraries located in Hunterdon, Morris, Somerset, and Warren counties",
               latitude="40.781", longitude="-74.706", location="Chester, NJ", url_img="https://chesterlib.org/wp-content/uploads/2019/08/479117_10150651359607191_1706882551_o-570x428.jpg")

    db.session.add(gym1)
    db.session.add(gym2)

    db.session.commit()


def undo_NJgyms():
    db.session.execute('TRUNCATE gyms RESTART IDENTITY CASCADE;')
    db.session.commit()

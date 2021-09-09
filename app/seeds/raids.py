from app.models import db, Raid


def seed_raids():

    raid1 = Raid(pokemon="Mankey", tier="1", url_img="https://play.pokemonshowdown.com/sprites/ani/mankey.gif",
                 min_cp_range=616, max_cp_range=665, boosted_min_cp_range=770, boosted_max_cp_range=832, is_active=False)
    raid2 = Raid(pokemon="Nidoking", tier="3", url_img="https://play.pokemonshowdown.com/sprites/ani/nidoking.gif",
                 min_cp_range=1395, max_cp_range=1466, boosted_min_cp_range=1743, boosted_max_cp_range=1833, is_active=False)
    raid3 = Raid(pokemon="Landorus (Therian Forme)", tier="5", url_img="https://play.pokemonshowdown.com/sprites/ani/landorus-therian.gif",
                 min_cp_range=2151, max_cp_range=2241, boosted_min_cp_range=2688, boosted_max_cp_range=2801, is_active=False)
    raid4 = Raid(pokemon="Mega Lopunny", tier="mega", url_img="https://play.pokemonshowdown.com/sprites/ani/lopunny-mega.gif",
                 min_cp_range=1112, max_cp_range=1177, boosted_min_cp_range=1391, boosted_max_cp_range=1471, is_active=False)

    db.session.add(raid1)
    db.session.add(raid2)
    db.session.add(raid3)
    db.session.add(raid4)

    db.session.commit()


def undo_raids():
    db.session.execute('TRUNCATE raids RESTART IDENTITY CASCADE;')
    db.session.commit()

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
    raid5 = Raid(pokemon="Mega Slowbro", tier="mega", url_img="https://play.pokemonshowdown.com/sprites/ani/slowbro-mega.gif",
                 min_cp_range=1382, max_cp_range=1454, boosted_min_cp_range=1728, boosted_max_cp_range=1817, is_active=True)
    raid6 = Raid(pokemon="Lugia", tier="5", url_img="https://play.pokemonshowdown.com/sprites/ani/lugia.gif",
                 min_cp_range=2028, max_cp_range=2115, boosted_min_cp_range=2535, boosted_max_cp_range=2645, is_active=True)
    raid7 = Raid(pokemon="Alolan Raichu", tier="3", url_img="https://play.pokemonshowdown.com/sprites/ani/raichu-alola.gif",
                 min_cp_range=1238, max_cp_range=1306, boosted_min_cp_range=1548, boosted_max_cp_range=1633, is_active=True)
    raid8 = Raid(pokemon="Wobbuffet", tier="3", url_img="https://play.pokemonshowdown.com/sprites/ani/wobbuffet.gif",
                 min_cp_range=532, max_cp_range=586, boosted_min_cp_range=665, boosted_max_cp_range=733, is_active=True)
    raid9 = Raid(pokemon="Medicham", tier="3", url_img="https://play.pokemonshowdown.com/sprites/ani/medicham.gif",
                 min_cp_range=764, max_cp_range=817, boosted_min_cp_range=955, boosted_max_cp_range=1022, is_active=True)
    raid10 = Raid(pokemon="Metagross", tier="3", url_img="https://play.pokemonshowdown.com/sprites/ani/metagross.gif",
                 min_cp_range=2078, max_cp_range=2166, boosted_min_cp_range=2598, boosted_max_cp_range=2708, is_active=True)
    raid11 = Raid(pokemon="Staryu", tier="1", url_img="https://play.pokemonshowdown.com/sprites/ani/staryu.gif",
                 min_cp_range=613, max_cp_range=661, boosted_min_cp_range=766, boosted_max_cp_range=826, is_active=True)
    raid12 = Raid(pokemon="Chimecho", tier="1", url_img="https://play.pokemonshowdown.com/sprites/ani/chimecho.gif",
                 min_cp_range=1224, max_cp_range=1291, boosted_min_cp_range=1530, boosted_max_cp_range=1614, is_active=True)
    raid13 = Raid(pokemon="Bronzor", tier="1", url_img="https://play.pokemonshowdown.com/sprites/ani/bronzor.gif",
                 min_cp_range=308, max_cp_range=344, boosted_min_cp_range=381, boosted_max_cp_range=430, is_active=True)
    raid14 = Raid(pokemon="Espurr", tier="1", url_img="https://play.pokemonshowdown.com/sprites/ani/espurr.gif",
                 min_cp_range=669, max_cp_range=719, boosted_min_cp_range=837, boosted_max_cp_range=899, is_active=True)
    raid15 = Raid(pokemon="Inkay", tier="1", url_img="https://play.pokemonshowdown.com/sprites/ani/inkay.gif",
                 min_cp_range=486, max_cp_range=529, boosted_min_cp_range=608, boosted_max_cp_range=662, is_active=True)

    db.session.add(raid1)
    db.session.add(raid2)
    db.session.add(raid3)
    db.session.add(raid4)
    db.session.add(raid5)
    db.session.add(raid6)
    db.session.add(raid7)
    db.session.add(raid8)
    db.session.add(raid9)
    db.session.add(raid10)
    db.session.add(raid11)
    db.session.add(raid12)
    db.session.add(raid13)
    db.session.add(raid14)
    db.session.add(raid15)

    db.session.commit()


def undo_raids():
    db.session.execute('TRUNCATE raids RESTART IDENTITY CASCADE;')
    db.session.commit()

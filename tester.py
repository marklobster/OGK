import items, characters, locations

missions = [True, True, True, False, False, False]
hero = characters.New_Hero("Victor", "To Victor go the Spoils!")
hero.inventory = [items.gold_ring, items.handmedowns, items.cheap_dagger,\
                  items.first_aid, items.wood_shield, items.first_aid, \
                  items.first_aid, items.sweet_armor, items.shiny_sword, \
                  items.sturdy_shield, items.btl, items.bear_trap, \
                  items.bear_trap, items.bear_trap, items.t_map]
hero.time = 6

village = locations.valley
village.hero = hero
village.departure = 0
village.resources = 50

village.boss1()

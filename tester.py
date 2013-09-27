import items, characters, locations

missions = [True, True, True, False, False, False]
hero = characters.New_Hero("Victor", "To Victor go the Spoils!")
hero.inventory = [items.gold_ring, items.handmedowns, items.cheap_dagger,\
                  items.first_aid, items.wood_shield, items.first_aid, \
                  items.first_aid, items.sweet_armor, items.shiny_sword, \
                  items.sturdy_shield, items.btl, items.bear_trap, \
                  items.bear_trap, items.bear_trap]

village = locations.shmucksburg
village.hero = hero

village.menu()

import items, characters, locations

missions = [False, False]
hero = characters.New_Hero("Victor", "To Victor go the Spoils!")
hero.inventory = [items.gold_ring, items.handmedowns, items.cheap_dagger,\
                  items.first_aid, items.wood_shield, items.first_aid, \
                  items.first_aid, items.sweet_armor, items.shiny_sword, \
                  items.sturdy_shield, items.btl, items.bear_trap, \
                  items.bear_trap, items.bear_trap]

village = locations.Shmucksburg()
village.hero = hero

if issubclass(locations.Cowhip, items.Item):
    print("yes")
else:
    print("no")

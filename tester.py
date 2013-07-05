import items, characters, converter, battle_system, random, monsters

hero = characters.Hero("Victor", 70, items.rusty_sword, items.wood_shield, items.handmedowns)

hero.display_inventory()
hero.inventory = [items.gold_ring, items.handmedowns, items.cheap_dagger,\
                  items.first_aid, items.wood_shield, items.first_aid, \
                  items.first_aid, items.sweet_armor, items.shiny_sword, \
                  items.sturdy_shield, items.btl, items.bear_trap, \
                  items.bear_trap, items.bear_trap]

# hero.display_inventory()
packet = [items.band_aid, items.battle_axe, items.herb]
claws = items.Weapon("claws", 0, "", 40, None)
#monster = characters.Easy_Monster("Evil Dragon", 350, claws, None, None, packet)

monsterz = (monsters.Sir_Rat(), monsters.Ancient_Technology())
monster1 = random.choice(monsterz)
monster2 = random.choice(monsterz)



fight1 = battle_system.Battle(hero, monster1)
fight2 = battle_system.Battle(hero, monster2)

# Packets for 'Oh Great Knight'
# Mark Lauber
# June 2013

import items, locations, characters, monsters

# Item packets for monsters
easy = (items.band_aid, items.wood_shield)
medium = (items.band_aid, items.rusty_sword, items.wood_shield, items.handmedowns)
hard = (items.herb, items.battle_axe, items.green_shield, items.leather)

# Destinations for location objects
#shmuck_data = (locations.cowdump, locations.fiddlestick, locations.valley, locations.wrathful)
#cow_data = (locations.shmucksburg,)
#fiddle_data = (

# Monster tuples for path objects
Shmu_Cowd = (monsters.Goblin(), monsters.Pretty_Blob(), monsters.Sir_Rat(), monsters.Gnasher())

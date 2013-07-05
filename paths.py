# Paths to be used for 'Oh Great Knight'
# path = A route between two villages containing n number of
    # opportunities for random battle encounters with a specific subset
    # of monsters.

import random, battle_system, monsters

# Monster tuples, specific to each path
north_monsters = (monsters.Pretty_Blob(),
                  monsters.Gnasher(),
                  monsters.Nacht_Musik(),
                  monsters.Sir_Rat())
east_monsters = (monsters.Goblin(),
                 monsters.Pretty_Blob(),
                 monsters.Sir_Rat(),
                 monsters.Gnasher(),
                 monsters.Nacht_Musik)
#south_monsters = (monsters.Hydra_Badger(), monsters.Orc(), monsters.Mega_Troll(), monsters.Ogre_Primo())
west_monsters = (monsters.Orc(), monsters.Ancient_Technology())
northeast_monsters = (monsters.Goblin(), monsters.Gnasher())
northwest_monsters = (monsters.Sir_Rat())

# Path parent class, followed by sub-classes for each village
class Path(object):
    """ Class for all paths, which are location connecting functions. """
    
    def __init__(self, distance, fight_chance, monster_pool):
        self.distance = distance
        self.fight_chance = fight_chance
        self.monster_pool = monster_pool
        
    def monster_pick(self):
        """ Randomly choose monster from self.monster_pool """
        random.choice(self.monster_pool)
    
    def go(self, hero, endpoint):
        print("Your journey beginneth.  Press 'I' at any time to use items.")
        for segment in range(self.distance):
            if hero.health:
                # Opportunity to use item
                entry = input("").upper()
                while entry == "I":
                    hero.display_inventory()
                    item = hero.item_pick()
                    if item != False:
                        hero.use_item(item)
                    entry = input("").upper()

                # Start message string, get occurence
                message = ""
                occurence = random.randint(1, 100)
                
                # Determine time and day, add to message
                if segment in range(0,20,3):
                    message += "On the morning of day " + str(int((segment+3)/3))
                elif segment in range(1,21,3):
                    message += "On the afternoon of day " + str(int((segment+2)/3))
                else:
                    message += "On the evening of day " + str(int((segment+1)/3))

                # If occurence == monster, update message, print message, start battle
                if occurence < self.fight_chance:
                    monster = self.monster_pick()
                    message += " a monster approaches!"
                    print(message)
                    battle = battle_system.Battle(hero, monster)
                    if hero.health:
                        print("Your journey continues.  Press 'I' at any time to use items.")

                # Or if occurence != monster, update message, print message
                else:
                    message += " nothing happens."
                    print(message)
                    
        # If hero is still alive, return the proper endpoint.
        if hero.health:
            return endpoint
        
        # Otherwise, return None
        else:
            return None

class North(Path):
    """ Connects Shmucksburg and Fiddlestick """
    def __init__(self):
        self.distance = 3
        self.fight_chance = 45
        self.monster_pool = north_monsters

class East(Path):
    """  """
    def __init__(self):
        self.distance = 3
        self.fight_chance = 50
        self.monster_pool = east_monsters


# Paths
north = North()
east = East()
test = Path(10, 20, None)

if __name__ == "__main__":
    print("This is a module for 'Oh Great Knight'.")
    input("Press enter to exit.")

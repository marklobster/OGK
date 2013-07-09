# Paths to be used for 'Oh Great Knight'
# path = A route between two villages containing n number of
    # opportunities for random battle encounters with a specific subset
    # of monsters.

import random, battle_system, monsters

# Monster tuples, specific to each path
#south_monsters = (monsters.Hydra_Badger(), monsters.Orc(), monsters.Mega_Troll(), monsters.Ogre_Primo())
#west_monsters = (monsters.Orc(), monsters.Ancient_Technology())
#northeast_monsters = (monsters.Goblin(), monsters.Gnasher())
#northwest_monsters = (monsters.Sir_Rat())

# Path parent class, followed by sub-classes for each village
class Path(object):
    """ Class for all paths, which are location connecting functions. """
    
    def __init__(self, distance, fight_chance):
        self.distance = distance
        self.fight_chance = fight_chance
    
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
                        hero.use_item(item, hero)
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

        def run(self, hero, endpoint):
            """ This is called by the Location when the user enters a path.
By default, this method calls self.go().  But some locations may over-ride
the default method in order to run other functions or checks before allowing
the user to begin the path."""
            next_location = self.go(hero, endpoint)
            return next_location

class North(Path):
    """ Connects Shmucksburg and Fiddlestick """
    def __init__(self):
        self.distance = 3
        self.fight_chance = 45

    def monster_pick(self):
        """ Creates monster_pool (specific to each Path).  Randomly
picks a monster and returns it before a battle begins. """
        monster_pool = (monsters.Pretty_Blob(),
                        monsters.Gnasher(),
                        monsters.Nacht_Musik(),
                        monsters.Sir_Rat())
        return random.choice(monster_pool)

class East(Path):
    """ Connects Shmucksburg and Cowdump """
    def __init__(self):
        self.distance = 3
        self.fight_chance = 50

    def monster_pick(self):
        monster_pool = (monsters.Goblin(),
                 monsters.Pretty_Blob(),
                 monsters.Sir_Rat(),
                 monsters.Gnasher(),
                 monsters.Nacht_Musik())
        return random.choice(monster_pool)



# Paths
north = North()
east = East()


if __name__ == "__main__":
    print("This is a module for 'Oh Great Knight'.")
    input("Press enter to exit.")

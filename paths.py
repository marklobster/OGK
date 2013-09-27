# Paths to be used for 'Oh Great Knight'
# path = A route between two villages containing n number of
    # opportunities for random battle encounters with a specific subset
    # of monsters.

import random, battle_system, monsters

from user_input import prompt

# Path parent class, followed by sub-classes for each village
class Path(object):
    """ Class for all paths, which are location connecting functions. """
    
    def __init__(self, distance, fight_chance, hero):
        self.distance = distance
        self.fight_chance = fight_chance
        self.hero = hero
    
    def go(self, endpoint):
        print("Your journey beginneth.  Press 'I' at any time to use items.")
        for segment in range(self.distance):
            if self.hero.health:
                # Opportunity to use item
                entry = prompt("").upper()
                while entry == "I":
                    self.hero.inventory_menu()
                    item = self.hero.item_pick()
                    if item != False:
                        self.hero.use_item(item, self.hero)
                    if entry == "I":
                        print("\nPress 'I' to use another item.")
                    entry = prompt("").upper()

                # Start message string, get occurence
                message = ""
                occurence = random.randint(1, 100)
                
                # Determine time and day, add to message
                if self.hero.time %3 == 0:
                    message += "On the morning of day " + str(int((self.hero.time+3)/3))
                elif (self.hero.time + 2)%3 == 0:
                    message += "On the afternoon of day " + str(int((self.hero.time+2)/3))
                else:
                    message += "On the evening of day " + str(int((self.hero.time+1)/3))

                # If occurence == monster, update message, print message, start battle
                if occurence < self.fight_chance:
                    monster = self.monster_pick()
                    message += " a monster approaches!"
                    print(message)
                    battle = battle_system.Battle(self.hero, monster)
                    if self.hero.health:
                        print("Your journey continues.  Press 'I' at any \
time to use an item.")

                # Or if occurence != monster, update message, print message
                else:
                    message += " nothing happens."
                    print(message)

                # Increment hero's time attribute
                self.hero.time += 1
                    
        # If hero is still alive, return the proper endpoint.
        if self.hero.health:
            return endpoint
        
        # Otherwise, return None
        else:
            return None

    def run(self, endpoint):
        """ This is called by the Location when the user enters a path.
By default, this method calls self.go().  But some locations may over-ride
the default method in order to run other functions or checks before allowing
the user to begin the path."""
        next_location = self.go(endpoint)
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
                        monsters.Sir_Rat(),
                        monsters.Goblin())
        return random.choice(monster_pool)

class East(Path):
    """ Connects Shmucksburg and Cow-Hip """
    def __init__(self):
        self.distance = 3
        self.fight_chance = 50

    def monster_pick(self):
        monster_pool = (monsters.Pretty_Blob(),
                 monsters.Sir_Rat(),
                 monsters.Gnasher(),
                 monsters.Nacht_Musik())
        return random.choice(monster_pool)

class South(Path):
    """ Connects Shmucksburg to Wrathful Pass """
    def __init__(self):
        self.distance = 5
        self.fight_chance = 65

    def monster_pick(self):
        monster_pool = (monsters.Ogre_Primo(),
                        monsters.Mega_Troll(),
                        monsters.Hydra_Badger(),
                        monsters.Orcupine())
        return random.choice(monster_pool)


class West(Path):
    """ Connects Shmucksburg to Valley of Forbidden Objects """
    def __init__(self):
        self.distance = 3
        self.fight_chance = 70

    def monster_pick(self):
        monster_pool = (monsters.Ancient_Technology(),
                        monsters.Goblin(),
                        monsters.Hungry_Spider())
        return random.choice(monster_pool)

class Northwest(Path):
    """  """
    def __init__(self):
        self.distance = 2
        self.fight_chance = 70
    
    def monster_pick(self):
        monster_pool = (monsters.Goblin(),
                        monsters.Orc(),
                        monsters.Hungry_Spider())
        return random.choice(monster_pool)

class Northeast(Path):
    """ Connects Fiddlestick to Castle Oldendrab """
    def __init__(self):
        self.distance = 1
        self.fight_chance = 45
        
    def monster_pick(self):
        monster_pool = (monsters.Sir_Rat(),
                        monsters.Gnasher(),
                        monsters.Nacht_Musik())
        return random.choice(monster_pool)

class Mountain_Road(Path):
    """  """
    def __init__(self):
        self.distance = 3
        self.fight_chance = 45
        
    def monster_pick(self):
        monster_pool = (monsters.Ninja_Bear(),
                        monsters.Hungry_Spider())
        return random.choice(monster_pool)

# Initialize paths
north = North()
east = East()
south = South()
west = West()
northeast = Northeast()
northwest = Northwest()
mountain_road = Mountain_Road()

all_paths = (north, east, south, west, northeast, northwest, mountain_road)


if __name__ == "__main__":
    print("This is a module for 'Oh Great Knight'.")
    prompt("Press enter to exit.")

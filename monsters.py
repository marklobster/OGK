# Monsters for 'Oh Great Knight'
# Mark Lauber
# June 2013

import characters, packets, random, items

# Parent Classes
class Monster(characters.Character):
    """ Parent class for Easy_Monster, Medium_Monster and Hard_Monster """
    
    def __init__(self):
        #Every monster will build an inventory and start with health equal to health_max
        self.inventory = []
        self.create_inventory(self.item_pool)
        self.health = self.health_max

    def create_inventory(self, pool):
        # For each item in item_pool there is a 1/3 chance it will be added to inventory.
        if pool != None:
            for item in pool:
                number = random.randint(1, 3)
                if number == 1:
                    self.inventory.append(item)

    def deactivate(self):
        self.health = 0

    def die(self):
        self.dead = True
        print("\nYou hath vanquished the " + self.name + ".")

    def gets_plundered(self, opponent):
        print("You gain: ")
        for item in self.inventory:
            print("\t" + item.name)
            opponent.inventory.append(item)
        print("\t" + str(self.coins) + " coins")
        opponent.coins += self.coins

class Easy_Monster(Monster):
    # Inherits tactic() from grandparent class characters.Character
    item_pool = packets.easy
    def __init__(self):
        self.coins = random.randint(3, 8)
        super(Easy_Monster, self).__init__()

class Medium_Monster(Monster):
    def __init__(self):
        self.item_pool = packets.medium
        self.coins = random.randint(13, 18)
        super(Medium_Monster, self).__init__()

    def tactic(self, opponent):
        if self.health < (self.health_max * 0.18) and items.band_aid in self.inventory:
            number = random.randint(1, 3)
            if number == 1:
                self.use_item(items.band_aid, self)
            else: self.attack(opponent)
        else:
            self.attack(opponent)

class Hard_Monster(Monster):
    def __init__(self):
        self.item_pool = packets.hard
        self.coins = random.randint(22, 28)
        super(Hard_Monster, self).__init__()

    def tactic(self, opponent):
        if self.health < (self.health_max * 0.18) and items.first_aid in self.inventory:
            self.use_item(items.first_aid, self)
        else:
            self.attack(opponent)

        
# Easy Monsters
class Goblin(Easy_Monster):
    def __init__(self):
        self.name = "Goblin"
        self.health_max =35
        self.weapon = items.cheap_dagger
        self.shield = items.wood_shield
        self.armor = None
        super(Goblin, self).__init__()
        self.inventory.append(items.cheap_dagger)

class Pretty_Blob(Easy_Monster):
    def __init__(self):
        self.name = "Pretty Blob"
        self.health_max =30
        self.weapon = items.pseudopod
        self.shield = None
        self.armor = items.leather
        super(Pretty_Blob, self).__init__()

    def win(self):
        input("Pretty Blob gives you a big kiss.")

class Sir_Rat(Easy_Monster):
    def __init__(self):
        self.name = "Sir Rat"
        self.health_max = 30
        self.weapon = items.cheap_dagger
        self.shield = items.wood_shield
        self.armor = items.handmedowns
        super(Sir_Rat, self).__init__()
        self.inventory.append(items.cheap_dagger)

    def die(self):
        self.dead = True
        print("You hath vanquished Sir Rat.")

class Gnasher(Easy_Monster):
    def __init__(self):
        self.name = "Gnasher"
        self.health_max = 18
        self.weapon = items.fangs
        self.shield = None
        self.armor = None
        super(Gnasher, self).__init__()

# Medium Monsters
class Orc(Medium_Monster):
    def __init__(self):
        self.name = "Orc"
        self.health_max = 65
        self.weapon = items.blunt_object
        self.shield = items.wood_shield
        self.armor = items.handmedowns
        super(Orc, self).__init__()
        if items.rusty_sword in self.inventory:
            self.weapon = items.rusty_sword

class Hydra_Badger(Medium_Monster):
    def __init__(self):
        self.name = "Hydra Badger"
        self.health_max = 55
        self.weapon = items.fangs
        self.shield = None
        self.armor = items.handmedowns
        super(Hydra_Badger, self).__init__()

class Nacht_Musik(Medium_Monster):
    def __init__(self):
        self.name = "Nacht Musik"
        self.health_max = 35
        self.weapon = items.talons
        self.shield = None
        self.armor = items.handmedowns
        super(Nacht_Musik, self).__init__()
        
    def shriek(self, target):
        number = random.randint(15, 18)
        print(self.name + " shrieks!\n" + str(number) + " damage!")
        target.lose_health(number)
    
    def tactic(self, opponent):
        number = random.randint(1,3)
        if number < 3:
            self.attack(opponent)
        else:
            self.shriek(opponent)


if __name__ == "__main__":
    print("This is a module for 'Oh Great Knight'.")
    input("Press enter to exit.")

# Monsters for 'Oh Great Knight'
# Mark Lauber
# June 2013

import characters, random, items

from user_input import prompt

# Item packets for monsters
easy_monsters = (items.bandage, items.wood_shield)
medium_monsters = (items.bandage, items.rusty_sword, items.wood_shield, items.handmedowns)
hard_monsters = (items.herbenol, items.green_shield, items.leather, items.wood_shield)

# Parent Classes
class Monster(characters.Character):
    """ Parent class for Easy_Monster, Medium_Monster and Hard_Monster """
    
    def __init__(self):
        #Every monster will build an inventory and start with health equal to health_max
        self.inventory = []
        self.create_inventory(self.item_pool)
        self.health = self.health_max
        self.dead = False

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

    def run_away(self):
        number = random.randint(1, 6)
        if number == 1:
            self.deactivate()
        else:
            print("You fail to escape")
        

class Easy_Monster(Monster):
    # Inherits tactic() from grandparent class characters.Character
    def __init__(self):
        self.item_pool = easy_monsters
        self.coins = random.randint(3, 8)
        super(Easy_Monster, self).__init__()

class Medium_Monster(Monster):
    def __init__(self):
        self.item_pool = medium_monsters
        self.coins = random.randint(13, 18)
        super(Medium_Monster, self).__init__()

    def tactic(self, opponent):
        if self.health < (self.health_max * 0.18) and items.bandage in self.inventory:
            number = random.randint(1, 4)
            if number == 1:
                self.use_item(items.bandage, self)
            else: self.attack(opponent)
        else:
            self.attack(opponent)

class Hard_Monster(Monster):
    def __init__(self):
        self.item_pool = hard_monsters
        self.coins = random.randint(22, 28)
        super(Hard_Monster, self).__init__()

    def tactic(self, opponent):
        if self.health < (self.health_max * 0.18) and items.herbenol in self.inventory:
            number = random.randint(1, 3)
            if number == 1:
                self.use_item(items.herbenol, self)
            else: self.attack(opponent)
        else:
            self.attack(opponent)

class Boss(Monster):
    def run_away(self):
        print("You can't run from " + self.name + "!")
        
        
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
        prompt("Pretty Blob gives you a big kiss.")

class Sir_Rat(Easy_Monster):
    def __init__(self):
        self.name = "Sir Rat"
        self.health_max = 28
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

    def tactic(self, opponent):
        """ One-in-four chance of a double-attack. """
        number = random.randint(1, 4)
        if number == 4:
            self.attack(opponent)
            if opponent.health:
                self.attack(opponent)
        else:
            self.attack(opponent)

class Nacht_Musik(Medium_Monster):
    def __init__(self):
        self.name = "Nacht Musik"
        self.health_max = 35
        self.weapon = items.talons
        self.shield = None
        self.armor = items.handmedowns
        super(Nacht_Musik, self).__init__()
        
    def shriek(self, target):
        number = random.randint(17, 20)
        print(self.name + " shrieks!\n" + str(number) + " damage!")
        target.lose_health(number)
    
    def tactic(self, opponent):
        """ A 1\3 chance it will shriek(), otherwise it attacks. """
        number = random.randint(1,3)
        if number < 3:
            self.attack(opponent)
        else:
            self.shriek(opponent)

class Ancient_Technology(Medium_Monster):
    def __init__(self):
        self.name = "Ancient Technology"
        self.health_max = 60
        self.weapon = items.flashing_ob
        self.shield = None
        self.armor = items.leather
        super(Ancient_Technology, self).__init__()

class Hungry_Spider(Medium_Monster):
    def __init__(self):
        self.name = "Hungry Spider"
        self.health_max = 45
        self.weapon = items.mandible
        self.shield = None
        self.armor = items.leather
        super(Hungry_Spider, self).__init__()

    def win(self):
        prompt(self.name + " decides she wasn't hungry after all!")


# Hard Monsters
class Mega_Troll(Hard_Monster):
    def __init__(self):
        self.name = "Mega Troll"
        self.health_max = 80
        self.weapon = items.battle_axe
        self.shield = items.wood_shield
        self.armor = items.handmedowns
        super(Mega_Troll, self).__init__()
        self.coins -= 15
        self.inventory.append(items.battle_axe)

class Ogre_Primo(Hard_Monster):
    def __init__(self):
        self.name = "Ogre Primo"
        self.health_max = 90
        self.weapon = items.ugly_stick
        self.shield = None
        self.armor = items.leather
        super(Ogre_Primo, self).__init__()

    def win(self):
        prompt(self.name + " was having so much fun he tries to put you back together.")

    def die(self):
        self.dead = True
        print("You hath vanquished Ogre Primo.")

class Orcupine(Hard_Monster):
    def __init__(self):
        self.name = "Orcupine"
        self.health_max = 60
        self.weapon = items.spikes
        self.shield = items.green_shield
        self.armor = items.leather
        super(Orcupine, self).__init__()

class Ninja_Bear(Hard_Monster):
    def __init__(self):
        self.name = "Ninja Bear"
        self.health_max = 75
        self.weapon = items.nunchucks
        self.shield = items.green_shield
        self.armor = items.handmedowns
        super(Ninja_Bear, self).__init__()

    def tactic(self, opponent):
        number = random.randint(1, 4)
        if number == 4:
            self.paws(opponent)
        else:
            self.attack(opponent)

    def paws(self, opponent):
        the_hurt = random.randint(37, 42)
        print(self.name + " attacks with Paws of Fury.")
        opponent.damage(the_hurt)

# Bosses

class Simon_Slick(Boss):
    def __init__(self):
        self.name = "Simon the Slick"
        self.health_max = 70
        self.health = 70
        self.dead = False
        self.weapon = items.battle_axe
        self.shield = items.wood_shield
        self.armor = items.handmedowns
        self.coins = 20
        self.inventory = [items.battle_axe, items.wood_shield,
                          items.handmedowns, items.bandage,
                          items.herbenol]

    def tactic(self, opponent):
        if self.health < (self.health_max * 0.18) and items.bandage in self.inventory:
            number = random.randint(1, 4)
            if number == 1:
                self.use_item(items.bandage, self)
            else:
                self.attack(opponent)
        else:
            self.attack(opponent)

    def die(self):
        self.dead = True
        print("You have captured Simon the Slick, a wanted man!")

class Guillek(Boss):
    def __init__(self):
        self.name = "Guillek the Mighty"
        self.health_max = 80
        self.health = 80
        self.dead = False
        self.weapon = items.rusty_sword
        self.shield = items.sturdy_shield
        self.armor = items.handmedowns
        self.coins = 22
        self.inventory = [items.rusty_sword, items.rusty_sword,
                          items.wood_shield, items.wood_shield,
                          items.handmedowns, items.first_aid]

    def tactic(self, opponent):
        self.attack(opponent)
        if opponent.health:
            self.attack(opponent)

    def die(self):
        self.dead = True
        print("Guillek the Mighty falls to the ground.")

if __name__ == "__main__":
    print("This is a module for 'Oh Great Knight'.")
    prompt("Press enter to exit.")

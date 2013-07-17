# Items to be imported for Oh Great Knight
# Mark Lauber
# April 2013

import random

# Item classes
class Item(object):
    """ Any purchasable item """
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description
        
    item_class = "N/A"
    personal_use = True

    def use(self, target):
        print("Nothing happens.")

class Weapon(Item):
    """ Items that can be equipped as weapons """
    def __init__(self, name, price, description, power, item_class):
        super(Weapon, self).__init__(name, price, description)
        self.power = power
        self.item_class = item_class

    def use(self, target):
        target.weapon = self
        print(self.name + " equipped!")
        

class Shield(Item):
    """ Items that can be equipped as shields """
    def __init__(self, name, price, description, deflection, item_class):
        super(Shield, self).__init__(name, price, description)
        self.deflection = deflection
        self.item_class = item_class

    def use(self, target):
        target.shield = self
        print(self.name + " equipped!")

class Armor(Item):
    """ Items that can be equipped as armor """
    def __init__(self, name, price, description, thickness, item_class):
        super(Armor, self).__init__(name, price, description)
        self.thickness = thickness
        self.item_class = item_class

    def use(self, target):
        target.armor = self
        print(self.name + " equipped!")

class Bandage(Item):
    def __init__(self):
        self.name = "Bandage"
        self.price = 18
        self.description = "Recover 25 HP"

    def use(self, target):
        print(target.name + " gains 25 HP.")
        target.gain_health(25)
        target.inventory.remove(self)

class Herbenol(Item):
    def __init__(self):
        self.name = "Herbenol"
        self.price = 45
        self.description = "A medicine made from herbs.  Recover 55 HP"

    def use(self, target):
        print(target.name + " gains 55 HP.")
        target.gain_health(55)
        target.inventory.remove(self)


class First_aid(Item):
    def __init__(self):
        self.name = "First-aid"
        self.price = 60
        self.description = "A complete kit!  Recover 70 HP."
        self.item_class = "N/A"

    def use(self, target):
        print(target.name + " gains 70 HP.")
        target.gain_health(70)
        target.inventory.remove(self)

class Beartraplauncher(Item):
    def __init__(self):
        self.name = "B.T.L."
        self.price = 130
        self.description = "NOT LOADED"
        self.personal_use = False

    def use(self, target):
        if self.description == "LOADED":
            number = random.randint(1, 10)
            if number < 8:
                target.damage(65)
                self.description = "NOT LOADED"
            else:
                print("Miss!")
        else:
            print("It's not loaded!")

    def load(self):
        print("Bear trap launcher loaded.")
        self.description = "LOADED"

class Bear_trap(Item):
    def __init__(self):
        self.name = "Bear trap"
        self.price = 60
        self.description = "Ammo for B.T.L."

    def use(self, target):
        if btl in target.inventory:
            if btl.description == "LOADED":
                print("Bear-trap launcher is already loaded!")
            else:
                btl.load()
                target.inventory.remove(self)
        else:
            ("You don't have a Bear-trap launcher!")

            
# Initialize objects

#Items, non-equippable, non-usable
# Parameters: name, price, description
gold_ring = Item("Gold Ring", 180, "The wedding ring you \"lost\".")


#Equippable Items
# Weapons
# Parameters: name, price, description, power, item_class
# Monster-only weapons
pseudopod = Weapon("Pseudopod", 0, "Pretty Blob's Weapon", 7, None)
blunt_object = Weapon("Blunt Object", 0, "Orc's Weapon", 17, None)
fangs = Weapon("Fangs", 0, "Gnasher's/Hydra Badger's Weapon", 18, None)
talons = Weapon("Talons", 0, "Nacht Musik's Weapon", 14, None)
flashing_ob = Weapon("Flashing Obelisk", 0, "Ancient Technology's Weapon", 15, None)
mandible = Weapon("Mandible", 0, "Hungry Spider's Weapon", 19, None)
spikes = Weapon("Spikes", 0, "Orcupine's Weapon", 24, None)
ugly_stick = Weapon("Ugly Stick", 0, "Ogre Primo's Weapon", 30, None)
nunchuck = Weapon("Nunchuck", 0, "Ninja Bear's Weapon", 21, None)
# Player-use weapons
cheap_dagger = Weapon("Cheap Dagger", 30, "Pointy", 12, "W-0")
rusty_sword = Weapon("Rusty Sword", 50, "A bargain sword for a bargain price.", 20, "W-1")
battle_axe = Weapon("Battle Axe", 70, "A skillfully made, mortally wounding axe.", 35, "W-2")
shiny_sword = Weapon("Shiny Sword", 90, "A sword fit for a knight.", 47, "W-3")

# Shields
# Parameters: name, price, description, deflection, item_class
wood_shield = Shield("Wood Shield", 30, "A well-used shield.", 20, "S-1")
green_shield = Shield("Green Shield", 70, "Made from recycled shields", 45, "S-2")
sturdy_shield = Shield("Sturdy Shield", 120, "A sturdy iron shield", 70, "S-3")

# Armor
# Parameters: name, price, description, thickness, item_class
handmedowns = Armor("Hand-me-downs", 30, "Hand-me-down armor", 20, "A-1")
leather = Armor("Leather Armor", 65, "Sleek leather with a helmet that totally doesn't match", 40, "A-2")
sweet_armor = Armor("Sweet Get-up", 100, "Chain-mail armor with a life-time warranty", 60, "A-3")


#Usable Items:
# Healing Items:
bandage = Bandage()
herbenol = Herbenol()
first_aid = First_aid()

# Special Items For Attacking
btl = Beartraplauncher()

# Other Usable Items
bear_trap = Bear_trap()

if __name__ == "__main__":
    print("This is a module for 'Oh Great Knight'")
    input("Press enter to exit.")

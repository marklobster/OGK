# Characters, Heroes and Monsters to be imported for 'Oh Great Knight'
# Mark Lauber
# April 2013

import items, random, converter
class Character(object):
    """ The super class for Hero and for Monster """
    def __init__(self, name, health_max, weapon, shield, armor):
        self.name = name
        self.health_max = health_max
        self.weapon = weapon
        self.shield = shield
        self.armor = armor
        self.health = self.health_max
        self.dead = False

    def gain_health(self, amount):
        """ Invoked by anything to cause a Character to gain health """
        self.health += amount
        if self.health > self.health_max:
            self.health = self.health_max

    def lose_health(self, amount):
        """ Invoke this only when an enemy causes damage which bypasses shield and armor. """
        self.health -= amount
        if self.health < 0:
            self.health = 0
        if self.health == 0:
            self.die()

    def display_inventory(self):
        print("ITEM\t\tCLASS\tDESCRIPTION")
        for item in self.inventory:
            if item == items.btl:
                print(self.name + "\t\t" + item.item_class + "\t" + item.description)
            else:
                print(item.name + "\t" + item.item_class + "\t" + item.description)

# Battle Functions
    def die(self):
        """ To be used when self.health == 0 """
        self.dead = True
        print("\n" + self.name + " is dead.")

    def deflect(self):
        """ Determine if enemy hit will be deflected by shield. """
        if self.shield:
            deflect_factor = int(self.shield.deflection * 0.5)
            number = random.randint(1, 100)
            if number in range(1, deflect_factor):
                return True
        return False

    def absorb_hit(self, the_hurt):
        """ Determine amount of damage reduction due to armor. """
        if self.armor:
            absorb_factor = int(self.armor.thickness * 0.2)
            the_hurt -= absorb_factor
        return the_hurt

    def damage(self, the_hurt):
        """ Receives 'the_hurt' from an enemy attack and calculates 'the_pain', which is subtracted from self.health """
        deflect_hit = self.deflect()
        if deflect_hit == True:
            print("Deflected!")
        else:
            the_pain = self.absorb_hit(the_hurt)
            if the_pain < 0:
                the_pain = 0
            print(str(the_pain) + " damage!")
            self.health -= the_pain
        if self.health < 0:
            self.health = 0
        if self.health == 0:
            self.die()

    def attack(self, enemy):
        """ Calculates 'the_hurt' caused to the enemy by an attack. """
        base = random.randint(0, 7)
        # Attacking with a weapon
        if self.weapon:
            the_hurt = self.weapon.power + base
            print(self.name + " attacks with " + self.weapon.name + ".")

        # Attacking without a weapon
        else:
            the_hurt = base
            print(self.name + " throws a punch.")

        # If attack not successful, print 'miss'.  Otherwise, invoke enemy's damage() method.
        if base == 0:
            print("Miss!")
        else:
            enemy.damage(the_hurt)

    def win(self):
        input("Tis a bad day to be a hero....\n")

    def tactic(self, opponent):
        """ The default battle tactic executed within the battle loop. """
        self.attack(opponent)        

# Using an item
    def use_item(self, item, target):
        """ Employ the 'use()' method of an item. """
        if item in self.inventory:
            print(self.name + " uses " + item.name + ".")
            item.use(target)
        else:
            print("You do not have one!\a")

    
class Hero(Character):
    """ Your hero character """
    def __init__(self, name, health_max, weapon, shield, armor):
        super(Hero, self).__init__(name, health_max, weapon, shield, armor)
        self.health_max = 70
        self.inventory = [items.gold_ring]
        self.coins = 0

    def item_pick(self):
        item = input("Select an item to use or equip or press 'enter' to \
exit.\n").lower()
        item = converter.convert(item)
        return item

    def display_inventory(self):
        print("\nITEM\t\tCLASS\tDESCRIPTION")
        for item in self.inventory:
            print(item.name + "\t" + item.item_class + "\t" + item.description)
        print("")
        try:
            print("Weapon: " + self.weapon.name)
        except AttributeError:
            print("Weapon: None")
        try:
            print("Shield: " + self.shield.name)
        except AttributeError:
            print("Shield: None")
        try:
            print("Armor: " + self.armor.name)
        except AttributeError:
            print("Armor: None")
        print("Coins: " + str(self.coins))
        print("Health: " + str(self.health) + " / " + str(self.health_max))
        print("")
        

    def tactic(self, opponent):
        """ The hero's tactic method consists of the battle menu. """
        end_turn = False
        while end_turn == False:
            print(self.name + " has " + str(self.health) + \
                  " / " + str(self.health_max) +" health.")
            print("""
A - Attack
I - Item
R - Run Away""")
            choice = input("").upper()
            if choice == "A":
                self.attack(opponent)
                end_turn = True
            elif choice == "I":
                self.display_inventory()
                item = self.item_pick()
                if item != False:
                    if item.personal_use == True:
                        self.use_item(item, self)
                    else:
                        self.use_item(item, opponent)
                    end_turn = True
            elif choice == "R":
                number = random.randint(1, 4)
                if number == 4:
                    opponent.deactivate()
                else:
                    print("You fail to escape.")
                end_turn = True

    def win(self):
        input(self.catchphrase)

class New_Hero(Hero):
    def __init__(self, name, catchphrase):
        self.name = name
        self.catchphrase = catchphrase
        self.dead = False
        self.weapon = None
        self.shield = None
        self.armor = None
        self.health_max = 70
        self.health = 70
        self.inventory = [items.gold_ring]
        self.coins = 0


        
if __name__ == "__main__":
    print("This is a module for 'Oh Great Knight'")
    input("Press enter to exit.")


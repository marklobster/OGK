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
            if len(item.name) < 8:
                print(item.name + "\t\t" + item.item_class + "\t" + item.description)
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
    def __init__(self, personal, inventory, missions):
        self.health_max = 70
        self.dead = False
        self.name = personal[0]
        self.cathchphrase = personal[1]
        self.health = personal[2]
        self.coins = personal[3]
        self.weapon = personal[4]
        self.shield = personal[5]
        self.armor = personal[6]
        self.time = personal[7]
        self.inventory = inventory
        self.missions = missions

    # FOR DEBUGGING PURPOSES:
    def show_missions(self):
        counter = 0
        for i in self.missions:
            print(str(counter) + str(i))
            counter += 1
    # ~~~ !!! ~~~ !!! 

    def item_pick(self):
        item = input("Select an item to use or equip or press 'enter' to \
exit.\n").lower()
        item = converter.convert(item)
        return item

    def inventory_menu(self):
        # FOR DEBUGGING PURPOSES:
        self.show_missions()
        # ~~~ !!! ~~~ !!!

        # Show inventory
        self.display_inventory()
        print("")

        # Show what is equipped
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

        # Show other data
        print("Coins: " + str(self.coins))
        print("Health: " + str(self.health) + " / " + str(self.health_max))
        print("")

    def drop(self, item):
        """ Use when hero removes an item from inventory. """
        # Remove item from inventory
        if item in self.inventory:
            self.inventory.remove(item)

        # If item is no longer in inventory, but is equipped, then unequip it.
        if item not in self.inventory:
            if self.weapon == item:
                self.weapon = None
            elif self.shield == item:
                self.shield = None
            elif self.armor == item:
                self.armor = None
        

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
                self.inventory_menu()
                item = self.item_pick()
                if item != False:
                    if item.personal_use == True:
                        self.use_item(item, self)
                    else:
                        self.use_item(item, opponent)
                    end_turn = True
            elif choice == "R":
                opponent.run_away()
                end_turn = True

    def win(self):
        input("\"" + self.catchphrase + "\"")

class New_Hero(Hero):
    def __init__(self, name, catchphrase):
        # Assign name and catchphrase to hero.  Then assign default settings.
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
        self.time = 0

        # Create list of missions where all are set to False
        self.missions = []
        for i in range(0, 9):
            self.missions.append(False)

class Besieger(Character):
    """ Class for imaginary object that beseiges Shmucksburg while hero is away """
    def __init__(self, hero, power, deflection, thickness):
        self.hero = hero

    def besiege(self, opponent):
        self.health = 0
        opponent.health = 0
        for i in range(0, 2):
            self.attack(opponent)
            opponent.attack(self)
        winner = max(self.health, opponent.health)

class Soldier(Character):
    """ Either a Defender or an Attacker of Shmucksburg """
    def __init__(self):
        self.weapon = None
        self.shield = None
        self.armor = None

class Militia(object):
    def __init__(self, armory, persons):
        import items
        self.armory = armory

        # Instantiate warriors
        self.warriors = []
        for i in range(1, 8):
            defender = Soldier()
            self.warriors.append(defender)

        # Equip warriors
        for i in warriors:
            
            # Assign weapons
            if items.shiny_sword in self.armory:
                self.assign(i.weapon, items.shiny_sword)
            elif items.battle_axe in self.armory:
                self.assign(i.weapon, items.battle_axe)
            elif items.rusty_sword in self.armory:
                self.assign(i.weapon, items.rusty_sword)
            elif items.cheap_dagger in self.armory:
                self.assign(i.weapon, items.cheap_dagger)

            # Assign shields
            if items.sturdy_shield in self.armory:
                self.assign(i.shield, items.sturdy_shield)
            elif items.green_shield in self.armory:
                self.assign(i.shield, items.green_shield)
            elif items.wood_shield in self.armory:
                self.assign(i.shield, items.wood_shield)

            # Assign armor
            if items.sweet_armor in self.armory:
                self.assign(i.armor, items.sweet_armor)
            elif items.leather in self.armory:
                self.assign(i.armor, items.leather)
            elif items.handmedowns in self.armory:
                self.assign(i.armor, items.handmedowns)

    def assign(self, equip_as, item):
        """ Quickly equip weapon to person and remove from armory """
        equip_as = item
        self.armory.remove(item)
        
if __name__ == "__main__":
    print("This is a module for 'Oh Great Knight'")
    input("Press enter to exit.")


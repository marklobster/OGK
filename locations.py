# Locations to be imported to 'Oh Great Knight'
# Mark Lauber
# June 2013

import location_parent, paths, items, messages

from user_input import prompt

class Shmucksburg(location_parent.Location):
    def __init__(self):
        self.name = "Shmucksburg"
        self.inventory = [items.cheap_dagger, items.handmedowns, items.bandage, items.wood_shield]
        self.messages = messages.shmucksburg[0:4]
        self.gain = 0
        self.departure = 0
        self.donations = [items.cheap_dagger, items.cheap_dagger, items.handmedowns]
        self.sort_donations()

    def get_destination(self):
        response = prompt("""
Where shall you journey?
N) Fiddlestick
E) Cow-Hip
S) Wrathful Pass
W) Valley of Forbidden Objects
\nEnter the direction or location.  Or press enter to exit.
""").lower()
        if response == "n" or response == "fiddlestick":
            destination = (paths.north, fiddlestick)
        elif response == "e" or response == "cow-hip":
            if self.hero.missions[0] == False:
                # Missions 0 and 1: Helping a travelor.
                self.travelor()
            destination = (paths.east, cowhip)
        elif response == "s" or response == "wrathful pass":
            destination = self.south_path()
        elif response == "w" or response == "valley of forbidden objects":
            destination = (paths.west, valley)
        elif response == "":
            destination = None
        else:
            print("\a")
            destination = None

        return destination

    def south_path(self):
        """ Make sure the user really wants to travel this path. """
        answer = prompt("That is a very dangerous path.  Are you sure \
you want to proceed? (y/n) ").lower()
        if answer == "y":
            return (paths.south, wrathful)
        elif answer == "n":
            return None
        else:
            return None

    def travelor(self):
        """ Missions 0 and 1:  Helping a travelor. """
        print("\"Hi, stranger.  Going to Cow-Hip?  Do you mind if I \
come along?  I could certainly use the protection since I'll be \
transporting these goods.\"")
        answer = ""
        while answer != "y" and answer != "n":
            answer = prompt("\nWhat do you say? (y/n) ").lower()
            if answer == "y":
                self.hero.missions[1] = True
                prompt("\"Many thanks!  I will repay you when we arrive.\"")
            elif answer == "n":
                prompt("\"Okay.  Well I guess I'll just hire someone else.\"")
            self.hero.missions[0] = True
    
    def menu(self):
        response = ""
        while self.hero.health:
            print("\nYOU ARE IN " + self.name.upper() + ".")
            print("""
J - JOURNEY
T - TALK TO VILLAGERS
S - SHOP
I - INVENTORY
D - DONATE
R - REST
G - GAME SAVE
Q - QUIT

Village Resources: """ + str(self.resources) + "\n")
            response = prompt("").upper()
            if response == "J":
                destination = self.get_destination()
                if destination:
                    next_location = self.journey(destination[0], destination[1])
                    return next_location
            elif response == "T":
                self.talk()
            elif response == "S":
                self.shop_menu()
            elif response == "I":
                self.inv_function()
            elif response == "D":
                self.donation_menu()
            elif response == "R":
                self.rest()
            elif response == "G":
                print("save")
            elif response == "Q":
                return None
            else:
                print("\a")
        return None

    def update(self):
        # Update village messages
        if self.hero.missions[0] == True and self.hero.missions[3] == False:
            self.messages = messages.shmucksburg[1:2] + messages.shmucksburg[4:5]
        elif self.hero.missions[3] == True and self.hero.missions[4] == False:
            self.messages = messages.shmucksburg[5:9]
        elif self.hero.missions[4] == True:
            self.messages = messages.shmucksburg[9:11]

        # Mission 6: Reward hero if he brings home Simon the Slick
        if self.hero.missions[4] == True and self.hero.missions[6] == False:
            prompt(messages.arrival2 + "\n")
            gifts = (items.first_aid, items.green_shield)
            self.hero.get_stuff(gifts)
            self.hero.missions[6] = True
            
        # Check if Shmucksburg was invaded in your absence
        if self.departure != self.hero.time:
            self.invasion_check()


    def rest(self):
        print("You go home to rest.")
        self.hero.gain_health(70)
        prompt(self.hero.name + " gains 70 HP.")

    def donation_menu(self):
        response = ""
        print("\t\t\tYou have entered the Armory.\n")
        print("\"Welcome, patron!\"")
        while response != "X":
            print("""
ARMORY
V - View Contents
D - Donate
X - Exit
""")
            response = prompt("\"Are we feeling philanthropic today?\" ").upper()
            if response == "V":
                print("ITEM\t\tCLASS")
                for item in self.donations:
                    print(item.name + "\t" + item.item_class)
            elif response == "D":
                self.donate()
            elif response == "X":
                prompt("\"Have a grand day!\"\n")
            else:
                print("\"Could you repeat that?\"\a")

    def donate(self):
        """ For hero donating items to the armory. """

        # Get item
        import converter
        self.hero.display_inventory()
        item = prompt("Select a weapon, shield or armor to donate.  Or \
press enter to exit. ").lower()
        item = converter.convert(item)

        # If item is a weapon, shield or armor, accept the donation
        if isinstance(item, items.Weapon) or isinstance(item, items.Shield) or isinstance(item, items.Armor):
            if item in self.hero.inventory:
                self.donations.append(item)
                self.hero.drop(item)
                self.sort_donations()
                prompt("\"Thank you for your donation.\"")
            else:
                prompt("You don't have one!")

        # If item is a real item but is not in the above classes, do not accept.
        elif item != False:
            prompt("That type of item is not needed.")

    def sort_donations(self):
        """ Sort armory by each item's item_class attribute """
        intermed_list = []
        for item in self.donations:
            intermed_list.append((item.item_class, item))
        intermed_list.sort()
        self.donations = []
        for item in intermed_list:
            self.donations.append(item[1])

    # Functions related to battles at Shmucksburg while the hero was away.
    def invasion_check(self):
        
        # Get time gone, set up variables, import random
        import random
        chances = self.hero.time - self.departure
        self.gain = 0
        invasions = 0
        self.wins = 0
        counter = 0
        
        # For each chance:
        for i in range(0, chances):
            counter += 1
            # Determine if battle occurs
            number = random.randint(1, 8)

            # If number == 8, run a battle simulation, return win or loss,
            # determine gain or loss
            if number == 8:
                import battle_system
                invasions += 1
                # Battle decides gain
                battle = battle_system.Invasion(shmucksburg)

            # Otherwise, gain 10 resources
            else:
                self.gain += 10
        print("While you were away Shmucksburg was invaded " + str(invasions) + " times.")
        print("\nThe village successfully defended itself " + str(self.wins) \
              + " out of " + str(invasions) + " time(s).")
        print(str(self.gain) + " resources gained.\n")
        self.resources += self.gain
        print("chances: ", str(counter))

        # Reset departure data for next invasion_check()
        self.departure = self.hero.time


class Fiddlestick(location_parent.Location):
    def __init__(self):
        self.name = "Fiddlestick"
        self.inventory = [items.rusty_sword, items.wood_shield, items.bandage, items.handmedowns]
        self.messages = messages.fiddlestick[0:3]

    def update(self):
        if self.hero.missions[5] == True:
            self.messages = messages.fiddlestick[3:5]

    def get_destination(self):
        response = prompt("""
Where shall you journey?
NW) Silverrock
NE) Oldendrab Castle
S) Shmucksburg
\nEnter the direction or location.  Or press enter to exit.
""").lower()
        if response == "nw" or response == "silverrock":
            destination = (paths.northwest, silverrock)
        elif response == "ne" or response == "oldendrab castle":
            destination = (paths.northeast, oldendrab)
        elif response == "s" or response == "shmucksburg":
            destination = (paths.north, shmucksburg)
        elif response == "":
            destination = None
        else:
            print("\a")
            destination = None
        return destination


class Cowhip(location_parent.Location):
    def __init__(self):
        self.name = "Cow-Hip"
        self.inventory = [items.cheap_dagger, items.wood_shield, items.bandage]
        self.messages = messages.cow_hip[:1]

    def get_destination(self):
        response = prompt("""
Where shall you journey?
W) Shmucksburg
\nEnter the direction or location.  Or press enter to exit.
""").lower()
        if response == "w" or response == "shmucksburg":
            destination = (paths.east, shmucksburg)
        elif response == "":
            destination = None
        else:
            print("\a")
            destination = None
        return destination

    def update(self):
        if self.hero.missions[1] == True:
            self.messages = messages.cow_hip[0:2]
        # Mission 2: If hero arrives safely with travelor, reward hero.
        # Also add leather armor to shop inventory.
        if self.hero.missions[2] == False:
            self.hero.missions[2] = True
            if self.hero.missions[1] == True:
                reward = 18
                prompt("\n\"Thank you for your protection!  Here is your reward.\"")
                item = (items.wood_shield,)
                self.hero.get_stuff(item)
                if items.leather not in self.inventory:
                    self.inventory.append(items.leather)


class Valley_End(location_parent.Location):
    def __init__(self):
        self.name = "Valley's End"
        self.inventory = [items.green_shield, items.wood_shield,
                          items.rusty_sword, items.cheap_dagger,
                          items.rare_coin]

    def get_destination(self):
        response = prompt("""
Where shall you journey?
E) Shmucksburg
""").lower()
        if response == "e" or response == "shmucksburg":
            destination = (paths.west, shmucksburg)
        elif response == "":
            destination = None
        else:
            print("\a")
            destination = None
        return destination

    def menu(self):
        """ Run the menu and return the next_location """
        response = ""
        while self.hero.health:
            print("\nYOU ARE IN " + self.name.upper() + ".")
            print("""
D - DIG
J - JOURNEY
I - INVENTORY
R - REST
G - GAME SAVE
Q - QUIT""")
            response = prompt("").upper()
            if response == "J":
                destination = self.get_destination()
                if destination:
                    next_location = self.journey(destination[0], destination[1])
                    return next_location
            elif response == "D":
                if self.hero.missions[3] == True and self.hero.missions[4] == False:
                    # Mission 4: Defeat Simon the Slick
                    self.boss1()
                else:
                    self.dig()
            elif response == "I":
                self.inv_function()
            elif response == "R":
                self.rest()
            elif response == "G":
                print("save")
            elif response == "Q":
                return None
            else:
                print("\a")
        
        return None

    def dig(self):
        import random
        number = random.randint(1, 5)
        if number == 1 or number == 2:
            print("You find nothing.")
        elif number == 3 or number == 4:
            print("A monster approaches!")
            import monsters, battle_system
            monster_pool = (monsters.Ancient_Technology(),
                                    monsters.Goblin(),
                                    monsters.Hungry_Spider())
            monster = random.choice(monster_pool)
            battle = battle_system.Battle(self.hero, monster)
        elif number == 5:
            item = (random.choice(self.inventory),)
            self.hero.get_stuff(item)
        self.hero.time += 1

    def rest(self):
        prompt("You can't rest here.  It's too dangerous!")

    def arrival1(self):
        prompt("King's Servant: " + self.hero.name + ", the journey has \
been dangerous thus far.  Please take this.  You may need it.")
        gift = (items.first_aid,)
        self.hero.get_stuff(gift)

    def boss1(self):
        print(messages.boss1[0])
        item = (items.kings_loot,)
        self.hero.get_stuff(item)
        self.hero.inventory.remove(items.t_map)
        prompt("")
        for i in range(1, 5):
            prompt(messages.boss1[i] + ("\n"))
        import battle_system, monsters
        boss = monsters.Simon_Slick()
        battle = battle_system.Battle(self.hero, boss)
        if self.hero.health:
            self.hero.missions[4] = True

    def update(self):
        if self.hero.missions[3] == True and self.hero.missions[4] == False:
            self.arrival1()

class Wrathful(location_parent.Location):
    def __init__(self):
        self.name = "Wrathful Pass"

    def get_destination(self):
        response = prompt("""
Where shall you journey?
N) Shmucksburg
""").lower()
        if response == "n" or response == "shmucksburg":
            destination = (paths.south, shmucksburg)
        elif response == "":
            destination = None
        else:
            print("\a")
            destination = None
        return destination


class Silverrock(location_parent.Location):
    def __init__(self):
        self.name = "Silverrock"
        self.inventory = [items.battle_axe, items.green_shield, items.leather,
                          items.btl, items.bear_trap, items.bandage,
                          items.herbenol]
        self.messages = messages.silverrock

    def update(self):
        if self.hero.missions[4] == False and self.hero.missions[5] == False:
            self.shortcut()
        elif self.hero.missions[5] == False:
            # Mission 5: Defeat Guillek the Mighty
            self.boss2()
        if items.t_map in self.hero.inventory:
            self.hero.inventory.remove(items.t_map)
        if items.kings_loot in self.hero.inventory:
            self.hero.inventory.remove(items.kings_loot)

    def get_destination(self):
        response = prompt("""
Where shall you journey?
N) Upheaval Mountain
SE) Fiddlestick
""").lower()
        if response == "se" or response == "fiddlestick":
            destination = (paths.northwest, fiddlestick)
        elif response == "n" or response == "unheaval mountain":
            destination = (paths.mountain_road, hall)
        elif response == "":
            destination = None
        else:
            print("\a")
            destination = None
        return destination

    def boss2(self):
        for i in range(0, 8):
            prompt(messages.boss2[i] + "\n")
        import battle_system, monsters
        boss = monsters.Guillek()
        battle_system.Battle(self.hero, boss)
        if self.hero.health:
            for i in range(8, 10):
                prompt(messages.boss2[i] + "\n")
            self.hero.missions[5] = True

    def shortcut(self):
        """This function is used when user goes to Silverrock without seeing King first"""
        for i in range(0, 2):
            prompt(messages.shortcut[i] + "\n")
        import battle_system, monsters
        boss = monsters.Guillek()
        battle_system.Battle(self.hero, boss)
        if self.hero.health:
            prompt(messages.shortcut[2] + "\n")
            self.hero.health = 0
    

class Oldendrab(location_parent.Location):
    def __init__(self):
        self.name = "Castle Oldendrab"

    def get_destination(self):
        response = prompt("""
Where shall you journey?
SW) Fiddlestick
""").lower()
        if response == "sw" or response == "fiddlestick":
            destination = (paths.northeast, fiddlestick)
        elif response == "":
            destination = None
        else:
            print("\a")
            destination = None
        return destination

    def menu(self):
        """ Run the menu and return the next_location """
        response = ""
        while self.hero.health:
            print("\nYOU ARE IN " + self.name.upper() + ".")
            print("""
J - JOURNEY
T - TALK TO KING
I - INVENTORY
R - REST
G - GAME SAVE
Q - QUIT""")
            response = prompt("").upper()
            if response == "J":
                destination = self.get_destination()
                if destination:
                    next_location = self.journey(destination[0], destination[1])
                    return next_location
            elif response == "T":
                if self.hero.missions[3] == False:
                    # Mission 3: King gives you treasure map.
                    self.meeting1()
                elif self.hero.missions[5] == True and self.hero.missions[7] == False:
                    # Mission 7: King asks you to go to Upheaval Mountain
                    self.meeting2()
                else:
                    print("\"The King cannot be seen right now.\"")
            elif response == "I":
                self.inv_function()
            elif response == "R":
                self.rest()
            elif response == "G":
                print("save")
            elif response == "Q":
                return None
            else:
                print("\a")

        return None

    def rest(self):
        print("\"You can't rest here.  This is the King's Court!\"")

    def meeting1(self):
        """ King gives you Treasure Map """
        # Mission 3: Get a treasure map.
        for message in messages.oldendrab1:
            paragraph = message.replace("Hero", self.hero.name)
            prompt(paragraph + "\n")
        item = (items.t_map,)
        self.hero.get_stuff(item)
        self.hero.missions[3] = True

    def meeting2(self):
        """ King asks you to go to Upheaval Mountain """
        for message in range(0, 2):
            prompt(messages.oldendrab2[message].replace("hero", self.hero.name) + "\n")
        donations = [items.rusty_sword, items.wood_shield,
                     items.wood_shield, items.leather]
        self.hero.get_stuff(donations)
        for message in range(2, 6):
            prompt(messages.oldendrab2[message].replace("hero", self.hero.name) + "\n")
        gift = (items.sweet_armor,)
        self.hero.get_stuff(gift)
        self.hero.missions[7] = True

class Hall(location_parent.Location):
    def __init__(self):
        self.name = "The Hall of the Mountain King"

    def menu(self):
        response = ""
        while self.hero.health:
            print("\nYOU ARE IN " + self.name.upper() + ".")
            print("""
J - JOURNEY
F - MOVE FORWARD
I - INVENTORY
R - REST
G - GAME SAVE
Q - QUIT""")
            response = prompt("").upper()
            if response == "J":
                destination = self.get_destination()
                if destination:
                    next_location = self.journey(destination[0], destination[1])
                    return next_location
            elif response == "F":
                self.boss3()
            elif response == "I":
                self.inv_function()
            elif response == "R":
                self.rest()
            elif response == "G":
                print("save!")
            elif response == "Q":
                return None
        return None

    def get_destination(self):
        response = prompt("""
Where shall you journey?
S) Silverrock
""").lower()
        if response == "s" or response == "silverrock":
            destination = (paths.mountain_road, silverrock)
        elif response == "":
            destination = None
        else:
            print("\a")
            destination = None
        return destination

    def boss3(self):
        pass

    def rest(self):
        prompt("You can't rest here, it's too dangerous!")

# Initialize locations
shmucksburg = Shmucksburg()
fiddlestick = Fiddlestick()
cowhip = Cowhip()
valley = Valley_End()
wrathful = Wrathful()
oldendrab = Oldendrab()
silverrock = Silverrock()
hall = Hall()

all_locations = (shmucksburg, fiddlestick, cowhip, valley, wrathful, oldendrab,
                 silverrock, hall)


if __name__ == "__main__":
    print("This is a module for 'Oh Great Knight'.")
    prompt("Press enter to exit.")

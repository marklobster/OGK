# Locations to be imported to 'Oh Great Knight'
# Mark Lauber
# June 2013

import location_parent, paths, items, messages


class Shmucksburg(location_parent.Location):
    def __init__(self):
        self.name = "Shmucksburg"
        self.inventory = [items.cheap_dagger, items.handmedowns, items.bandage, items.wood_shield]
        self.messages = messages.shmucksburg[0:4]
        self.donations = [items.cheap_dagger, items.cheap_dagger, items.handmedowns]
        self.sort_donations()

    def get_destination(self):
        response = input("""
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
        answer = input("That is a very dangerous path.  Are you sure \
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
            answer = input("\nWhat do you say? (y/n) ").lower()
            if answer == "y":
                self.hero.missions[1] = True
                input("\"Many thanks!  I will repay you when we arrive.\"")
            elif answer == "n":
                input("\"Okay.  Well I guess I'll just hire someone else.\"")
            self.hero.missions[0] = True
    
    def menu(self):
        response = ""
        while response != "Q":
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
""")
            response = input("").upper()
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
                print("Inn")
            elif response == "G":
                print("save")
            elif response == "Q":
                next_location = None
            else:
                print("\a")
        return next_location

    def update(self):
        if self.hero.missions[0] == True:
            self.messages = messages.shmucksburg[1:2] + messages.shmucksburg[4:5]

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
            response = input("\"Are we feeling philanthropic today?\" ").upper()
            if response == "V":
                print("ITEM\t\tCLASS")
                for item in self.donations:
                    print(item.name + "\t" + item.item_class)
            elif response == "D":
                self.donate()
            elif response == "X":
                input("\"Have a grand day!\"\n")
            else:
                print("\"Could you repeat that?\"\a")

    def donate(self):
        """ For hero donating items to the armory. """

        # Get item
        import converter
        self.hero.inventory_menu()
        item = input("Select a weapon, shield or armor to donate.  Or \
press enter to exit. ").lower()
        item = converter.convert(item)

        # If item is a weapon, shield or armor, accept the donation
        if isinstance(item, items.Weapon) or isinstance(item, items.Shield) or isinstance(item, items.Armor):
            if item in self.hero.inventory:
                self.donations.append(item)
                self.hero.drop(item)
                self.sort_donations()
                input("\"Thank you for your donation.\"")
            else:
                input("You don't have one!")

        # If item is a real item but is not in the above classes, do not accept.
        elif item != False:
            input("That type of item is not needed.")

    def sort_donations(self):
        """ Sort armory by each item's item_class attribute """
        intermed_list = []
        for item in self.donations:
            intermed_list.append((item.item_class, item))
        intermed_list.sort()
        self.donations = []
        for item in intermed_list:
            self.donations.append(item[1])

    
class Fiddlestick(location_parent.Location):
    def __init__(self):
        self.name = "Fiddlestick"
        self.inventory = [items.rusty_sword, items.wood_shield, items.bandage, items.handmedowns]
        self.messages = messages.fiddlestick[0:3]

    def get_destination(self):
        response = input("""
Where shall you journey?
NW) Gadgetsburg
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
        response = input("""
Where shall you journey?
W) Shmucksburg
\nEnter the direction or location.  Or press enter to exit.
""").lower()
        if response == "w" or response == "shmuckburg":
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
                input("\n\"Thank you for your protection!  Here is your reward.\"")
                print("You gain: ")
                input("\t" + str(reward) + " coins")
                self.hero.coins += reward
                if items.leather not in self.inventory:
                    self.inventory.append(items.leather)


class Valley_End(location_parent.Location):
    def __init__(self):
        self.name = "Valley's End"
        self.inventory = [items.green_shield, items.wood_shield,
                          items.rusty_sword, items.cheap_dagger,
                          items.rare_coin]

    def get_destination(self):
        response = input("""
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
        while response != "Q":
            print("\nYOU ARE IN " + self.name.upper() + ".")
            print("""
D - DIG
J - JOURNEY
I - INVENTORY
R - REST
G - GAME SAVE
Q - QUIT""")
            response = input("").upper()
            if response == "J":
                destination = self.get_destination()
                if destination:
                    next_location = self.journey(destination[0], destination[1])
                    return next_location
            elif response == "D":
                if self.hero.missions[3] == True and self.hero.missions[4] == False:
                    self.boss1()
                else:
                    self.dig()
                # If hero dies in battle, return None
                if self.hero.health == 0:
                    return None
            elif response == "I":
                self.inv_function()
            elif response == "R":
                print("Inn")
            elif response == "G":
                print("save")
            elif response == "Q":
                next_location = None
            else:
                print("\a")

        return next_location

    def dig(self):
        import random
        number = random.randint(1, 5)
        if number == 1 or number == 2:
            print("You find nothing.")
        elif number == 3 or number == 4:
            print("A monster approaches!")
            import monsters, battle_system
            monster_pool = (monsters.Ancient_Technology(),
                                    monsters.Orc(),
                                    monsters.Goblin(),
                                    monsters.Hungry_Spider())
            monster = random.choice(monster_pool)
            battle = battle_system.Battle(self.hero, monster)
        elif number == 5:
            item = random.choice(self.inventory)
            print("You find:\n\t" + item.name)
            self.hero.inventory.append(item)
        # self.hero.time += 1

    def boss1(self):
        print("You dig where the map directs you to dig.")
        input("And you find:\n\t" + items.kings_loot.name)
        self.hero.inventory.append(items.kings_loot)
        self.hero.inventory.remove(items.t_map)
        input("\nYou turn around to find that a stranger has snuck up on you!")
        input("Prepare for battle!\n")
        import battle_system, monsters
        boss = monsters.Simon_Slick()
        battle = battle_system.Battle(self.hero, boss)
        if self.hero.health:
            self.hero.missions[4] = True

class Wrathful(location_parent.Location):
    def __init__(self):
        self.name = "Wrathful Pass"

    def get_destination(self):
        response = input("""
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


class Oldendrab(location_parent.Location):
    def __init__(self):
        self.name = "Castle Oldendrab"

    def get_destination(self):
        response = input("""
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
        while response != "Q" and response != "J":
            print("\nYOU ARE IN " + self.name.upper() + ".")
            print("""
J - JOURNEY
T - TALK TO KING
I - INVENTORY
R - REST
G - GAME SAVE
Q - QUIT""")
            response = input("").upper()
            if response == "J":
                destination = self.get_destination()
                if destination:
                    next_location = self.journey(destination[0], destination[1])
                    return next_location
            elif response == "T":
                self.meeting1()
            elif response == "I":
                self.inv_function()
            elif response == "R":
                print("\"You can't rest here.  This is the King's Court!\"")
            elif response == "G":
                print("save")
            elif response == "Q":
                next_location = None
            else:
                print("\a")

        return next_location

    def meeting1(self):
        """ King gives you Treasure Map """
        # Mission 3: Get a treasure map.
        input("You introduce yourself as an ambassador in order to \
gain audience with the King.")
        print("King: Good morrow, young man.  What is it you seek?")
        input(self.hero.name + ": Good King Vinny, I come on behalf of \
 Shmucksburg.  We are robbed incessantly.  And since our armory was \
 ransacked last year, we are utterly unable to defend ourselves.  I \
 request guards or perhaps armaments with which to defend our poor village.")
        input("King: My good man, this entire kingdom is poor!  At \
least it will be if we cannot regain Silverrock....  As of now, \
nearly all of my guards are preparing to march west to rid Silverrock of its\
 orcish pests.  How, then, could I supply your village with guards\
 or armaments?  I am sorry good sir, but I must send you away empty-\
 handed.")
        input(self.hero.name + ": I will fight with your men if you promise to help me.")
        input("King: Are you offering me an ultimatem?!  If you are indeed \
a warrior, then I order you to fight for me!  In fact, I have a specific \
task for you:")
        input("Go to the Valley of Forbidden Objects.  There is treasure \
there with which we could bribe the orcs.  I'm afraid \
they have grown dangerously armed and organized.  I would rather give \
them buried treasure than waste my men on them.  Here is a map.  Dig \
up the chest at the end of the valley.  Give it to the orcs as payment.\
  Since you fancy yourself an ambassador, I'll leave convincing them to \
take it up to you.")
        input("I am sending trusted servants with you.  They will watch \
and make sure you do not steal the treasure.  If you accomplish \
what I ask, I will see what I can do for Shmucksburg.  Now make haste.")
        self.hero.inventory.append(items.t_map)
        self.hero.missions[3] = True
        input("You get:\n\tTreasure Map")

# Initialize locations
shmucksburg = Shmucksburg()
fiddlestick = Fiddlestick()
cowhip = Cowhip()
valley = Valley_End()
wrathful = Wrathful()
oldendrab = Oldendrab()

all_locations = (shmucksburg, fiddlestick, cowhip, valley, wrathful, oldendrab)


if __name__ == "__main__":
    print("This is a module for 'Oh Great Knight'.")
    input("Press enter to exit.")

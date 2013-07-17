# Locations to be imported to 'Oh Great Knight'

import paths, items, converter

class Location(object):
    """ Super class for village objects. """

    # Main Functions
    def run(self):
        next_location = self.menu()
        return next_location

    def menu(self):
        """ Run the menu and return the next_location """
        response = ""
        while response != "Q" and response != "J":
            print("\nYOU ARE IN " + self.name.upper() + ".")
            print("""
J - JOURNEY
T - TALK TO VILLAGERS
S - SHOP
I - INVENTORY
R - REST
G - GAME SAVE
Q - QUIT""")
            response = input("").upper()
            if response == "J":
                # Ask for next location via get_destination() method
                destination = self.get_destination()

                # If a destination was selected, call the journey function.
                # If the hero survives the journey, the desired endpoint will
                # be returned and fed back into the next_location of game.main_loop.
                # But an unsuccessful journey returns None, which is fed back to
                # the main_loop, and ends the game.main_loop.
                if destination:
                    next_location = self.journey(destination[0], destination[1])
                # Otherwise, just return to the location's main menu by
                # changing response from 'J' to the empty string.
                else:
                    response = ""
            elif response == "T":
                self.talk()
            elif response == "S":
                self.shop_menu()
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

        # next_location is returned to the game.main_loop
        return next_location

    # Menu functions
    def get_destination(self):
        """ This function is unique to each Location, so it is not in
the parent class.  This function gives a menu of destinations.  The user
selects one.  Then the journey() function is run with the appropriate path
and endpoint."""
        print("Where shall you journey?")
        
    def journey(self, path, endpoint):
        """ Run the selected path.  Return the appropriate new location. """
        next_location = path.run(endpoint)
        return next_location

    def talk(self):
        print(self.message1)
        print(self.message2)
        print(self.message3)
        print(self.message4)

    def inv_function(self):
        """ Allows hero to use item on himself while at a location's menu. """
        self.hero.display_inventory()
        item = self.hero.item_pick()
        if item != False:
            if item.personal_use == True:
                self.hero.use_item(item, self.hero)
            else:
                input("You cannot use this here.")

# Shop functions
    def shop_menu(self):
        print("You have entered Ye Olde Item Shoppe.")
        print("\"Greetings, stranger!\"")
        option = ""
        while option != "X":
            print("""
P - Purchase Item
S - Sell Item
I - View Inventory
X - Exit
""")
            print("Silver: " + str(self.hero.coins))
            option = input("What can I do for ye?\n").upper()
            if option == "X":
                input("\"Good day to you sir!\"")
            elif option == "P":
                self.hero_purchase()
            elif option == "S":
                self.hero_sell()
            elif option == "I":
                self.hero.display_inventory()
            else:
                print("\a\"What jibberish thou art speaketh?!\"")

    def show_inventory(self):
        print("ITEM\t\tPRICE\tCLASS\tDESCRIPTION")
        for item in self.inventory:
            if item == items.btl:
                print(item.name + "\t\t" + str(item.price) + "\t" + item.item_class + "\t" + item.description)
            else:
                print(item.name + "\t" + str(item.price) + "\t" + item.item_class + "\t" + item.description)

    def hero_purchase(self):
        self.show_inventory()
        print("\"Which would ye like to purchase?\"")
        item = input("")
        item = converter.convert(item)

        # Check if item is a real item.
        if item != False:
            
            # If item is in stock and hero can afford it:
            if item in self.inventory and item.price <= self.hero.coins:
                self.hero.inventory.append(item)
                self.hero.coins -= item.price

            # If item is in stock and hero cannot afford it:
            elif item in self.inventory and item.price > self.hero.coins:
                print("\a\"You can't afford that!\"")

            # If item is not in stock:
            else:
                print("\a\"Sorry I haven't got that in stock.\"")

    def hero_sell(self):
        print("Sell")


class Shmucksburg(Location):
    def __init__(self):
        self.name = "Shmucksburg"
        self.inventory = [items.cheap_dagger, items.handmedowns, items.bandage]
        self.message1 = "Aye!  The brigands robbed me again!  What this \
village needs is a guardian!\n"
        self.message2 = "Our armory is pitiful.  Donations of weapons, shields\
 and armor would help us defend ourselves.\n"
        self.message3 = "What I need is a guardian for my caravan!  Without \
that I can't deliver my goods to Cow-Hip.  You wouldn't happen to be travelin'\
 to Cow-Hip, would you sir?\n"
        self.message4 = "Nice mask fella!  You're not a robber are you?  \
Well I guess you'd have robbed me by now!\n"

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
            destination = (paths.east, cowhip)
        elif response == "s" or response == "wrathful pass":
            destination = (paths.south, wrathful)
        elif response == "w" or response == "valley of forbidden objects":
            destination = (paths.west, valley)
        elif response == "":
            destination = None
        else:
            print("\a")
            destination = None
        return destination
    
    def menu(self):
        response = ""
        while response != "Q" and response != "J":
            print("YOU ARE IN " + self.name.upper() + ".")
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
                else:
                    response = ""
            elif response == "T":
                self.talk()
            elif response == "S":
                self.shop_menu()
            elif response == "I":
                self.inv_function()
            elif response == "D":
                print("donate")
            elif response == "R":
                print("Inn")
            elif response == "G":
                print("save")
            elif response == "Q":
                next_location = None
            else:
                print("\a")
        return next_location
    
class Fiddlestick(Location):
    def __init__(self):
        self.name = "Fiddlestick"
        self.inventory = [items.rusty_sword, items.wood_shield, items.bandage]

    def get_destination(self):
        response = input("""
Where shall you journey?
NW) Gadgetsburg
NE) Oldendrab Castle
S) Shmucksburg
\nEnter the direction or location.  Or press enter to exit.
""").lower()
        if response == "nw" or response == "gadgetsburg":
            destination = (paths.northwest, gadgetsburg)
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


class Cowhip(Location):
    def __init__(self):
        self.name = "Cow-Hip"
        self.inventory = [items.wood_shield, items.bandage]

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

class Valley_End(Location):
    def __init__(self):
        self.name = "Valley's End"

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

class Wrathful(Location):
    def __init__(self):
        self.name = "Wrathful Pass"

    def get_destination(self):
        response = input("""
Where shall you journey?
N) Shmucksburg
""").lower()
        if response == "e" or response == "shmucksburg":
            destination = (paths.south, shmucksburg)
        elif response == "":
            destination = None
        else:
            print("\a")
            destination = None
        return destination



# Initialize locations
shmucksburg = Shmucksburg()
fiddlestick = Fiddlestick()
cowhip = Cowhip()
valley = Valley_End()
wrathful = Wrathful()

all_locations = (shmucksburg, fiddlestick, cowhip, valley, wrathful)


if __name__ == "__main__":
    print("This is a module for 'Oh Great Knight'.")
    input("Press enter to exit.")

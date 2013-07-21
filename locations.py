# Locations to be imported to 'Oh Great Knight'

import paths, items, converter, messages

class Location(object):
    """ Super class for village objects. """

    # Main Functions
    def run(self):
        """ Run appropriate updates for the location.  Then run the menu. """
        self.update()
        next_location = self.menu()
        return next_location

    def update(self):
        """ Update location attributes based on hero's data. """
        # By default, this method does nothing.
        pass

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
        """ This function is unique to each Location.  This function gives a
menu of destinations.  The user selects one.  Then the journey() function is
run with the appropriate path and endpoint."""
        pass
        
    def journey(self, path, endpoint):
        """ Run the selected path.  Return the appropriate new location. """
        next_location = path.run(endpoint)
        return next_location

    def talk(self):
        """ Read what the villagers have to say """
        for message in self.messages:
            print("\"" + message + "\"\n")

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
        print("\n\t\t\tYou have entered Ye Olde Item Shoppe.\n")
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
                input("\"Good day to you sir!\"\n")
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
            print(item.name + "\t\t" + str(item.price) + "\t" + item.item_class + "\t" + item.description)
            
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
                print("\"Nice doing business with you, sir!\"")

            # If item is in stock and hero cannot afford it:
            elif item in self.inventory and item.price > self.hero.coins:
                print("\a\"You can't afford that!\"")

            # If item is not in stock:
            else:
                print("\a\"Sorry I haven't got that in stock.\"")

    def hero_sell(self):
        # Show inventory, input item to sell
        self.hero.display_inventory()
        item = input("\"What would ye like to sell?\" ").lower()

        # If item does not exist, converter will print appropriate message
        # and neither if nor elif part of branch are executed.
        item = converter.convert(item)

        # If hero has the item, calculate sale price
        if item in self.hero.inventory:
            sale_price = int(item.price * 0.8)
            print("\"I'll offer you " + str(sale_price) + " silver.\"")
            response = input("Is that agreeable to you?\" (y/n) ").upper()

            # If sale price is acceptable, commence sale
            if response == "Y":
                self.hero.inventory.remove(item)

                # If item is equipped, unequip it
                if item == self.hero.weapon:
                    self.hero.weapon = None
                elif item == self.hero.shield:
                    self.hero.shield = None
                elif item == self.hero.armor:
                    self.hero.armor = None
                    
                self.hero.coins += sale_price
                print("\"Nice doing business with you, sir!\"")

            # If sale price is not acceptable end function
            elif response == "N":
                print("\"Tis the best I can do!\"")

            # If response is invalid, end function
            else:
                print("\a\"What?\"")

        # If item does exist but is not in inventory, end function
        elif item != False:
            print("\"You don't have one!\a\"")


class Shmucksburg(Location):
    def __init__(self):
        self.name = "Shmucksburg"
        self.inventory = [items.cheap_dagger, items.handmedowns, items.bandage, items.wood_shield]
        self.messages = messages.shmucksburg[0:4]

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
transporting these goods.")
        answer = ""
        while answer != "y" and answer != "n":
            answer = input("\nWhat do ya say?\" (y/n) ").lower()
            if answer == "y":
                self.hero.missions[1] = True
                input("\"Many thanks!  I will repay you when we arrive.\"")
            elif answer == "n":
                input("\"Okay.  Well I guess I'll just hire someone else.\"")
            self.hero.missions[0] = True
    
    def menu(self):
        response = ""
        while response != "Q" and response != "J":
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

    def update(self):
        if self.hero.missions[0] == True:
            self.messages = self.messages[1:2] + messages.shmucksburg[4:5]
            
    
class Fiddlestick(Location):
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
                reward = 15
                input("\"Thank you for your protection!  Here is your reward.\"")
                print("You gain: ")
                input("\t" + str(reward) + " coins")
                self.hero.coins += reward
                self.inventory.append(items.leather)

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

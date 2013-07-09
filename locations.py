# Locations to be imported to 'Oh Great Knight'

import paths

class Location(object):
    """ Super class for village objects. """

    def run(self, hero):
        next_location = self.menu(hero)
        return next_location

    def journey(self, hero, path, endpoint):
        """ Run the selected path.  Return the appropriate new location. """
        next_location = path.go(hero, endpoint)
        return next_location

    def menu(self, hero):
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
                    next_location = self.journey(hero, destination[0], destination[1])
                # Otherwise, just return to the location's main menu by
                # changing response from 'J' to the empty string.
                else:
                    response = ""
            elif response == "T":
                print("messages")
            elif response == "S":
                print("shop")
            elif response == "I":
                hero.inventory()
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


class Shmucksburg(Location):
    def __init__(self):
        self.name = "Shmucksburg"

    def get_destination(self):
        """ This function is unique to each Location, so it is not in
the parent class.  This function gives a menu of destinations.  The user
selects one.  Then the journey() function is run with the appropriate path
and endpoint."""
        response = input("""
Where shall you journey?
N) Fiddlestick
E) Cowdump
S) Wrathful Pass
W) Valley of Forbidden Objects
\nEnter the direction or location.  Or press enter to exit.
""").lower()
        if response == "n" or response == "fiddlestick":
            destination = (paths.north, fiddlestick)
        elif response == "e" or response == "cowdump":
            destination = (paths.east, cowdump)
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
    
    def menu(self, hero):
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
                    next_location = self.journey(hero, destination[0], destination[1])
                else:
                    response = ""
            elif response == "T":
                print("messages")
            elif response == "S":
                print("shop")
            elif response == "I":
                print("inventory")
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


class Cowdump(Location):
    def __init__(self):
        self.name = "Cowdump"

    def get_destination(self):
        response = input("""
Where shall you journey?
N) Fiddlestick
E) Cowdump
S) Wrathful Pass
W) Valley of Forbidden Objects
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

    
shmucksburg = Shmucksburg()
fiddlestick = Fiddlestick()
cowdump = Cowdump()

if __name__ == "__main__":
    print("This is a module for 'Oh Great Knight'.")
    input("Press enter to exit.")

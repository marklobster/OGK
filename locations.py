# Locations to be imported to 'Oh Great Knight'

import paths

class Location(object):
    """ Super class for village objects. """
    #def __init__(self):


    def get_destination(self):
        """ Select a destination from this location's menu. """
        print("Where shall you journey?  (Press enter to cancel.)")

    def journey(self, hero, path, endpoint):
        """ Run the selected path.  Return the appropriate new location. """
        finality = path.go(hero, endpoint)
        return finality

    def run(self, hero):
        """ Run the menu and return the next_location """
        response = ""
        while response != "Q" and response != "J":
            print("YOU ARE IN " + self.name.upper() + ".")
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
                    next_location = self.journey(self.hero, destination[0], destination[1])
                # Otherwise, just return to the location's main menu by
                # changing resonse from 'J' to the empty string.
                else:
                    response = ""
            elif response == "T":
                print("messages")
            elif response == "S":
                print("shop")
            elif response == "I":
                self.hero.inventory()
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
        response = input("""
Where shall you journey?
N) Fiddlestick
E) Cowdump
S) Wrathful Pass
W) Valley of Forbidden Objects\n
Enter the direction or location.  Or press enter to exit.
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
    
    def run(self, hero):
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
    
shmucksburg = Shmucksburg()
fiddlestick = Fiddlestick()

if __name__ == "__main__":
    print("This is a module for 'Oh Great Knight'.")
    input("Press enter to exit.")

# Locations to be imported to 'Oh Great Knight'

import paths

class Location(object):
    """ Super class for village objects. """
    def __init__(self, name, packet):
        self.name = name
        self.destinations = packet


    def get_destination():
        print("Where shall you journey?  Or press enter to cancel.")
        for destination in self.destinations:
            print(self.name)

    def journey(self, path, endpoint):
        next_location = self.destinations.path.go(endpoint)
        return next_location

    def menu(self):
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
                destination = self.get_destination()
                if destination == "":
                    continue
                if destination not in self.destinations:
                    print("That is not an option.\a")
                    continue
                next_location = self.journey(destination[1], destination[2])
            elif response == "T":
                print("messages")
            elif response == "S":
                print("shop")
            elif response == "I":
                game.hero.inventory()
            elif response == "R":
                print("Inn")
            elif response == "G":
                print("save")
            elif response == "Q":
                next_location = None
            else:
                print("\a")
        return next_location


class Shmucksburg(Location):
    name = "Shmucksburg"
    destinations = []
    armory = []
    def main(self):
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
Q - QUIT""")
            response = input("").upper()
            if response == "J":
                destination = self.get_destination()
                if destination == "":
                    continue
                if destination not in self.destinations:
                    print("That is not an option.\a")
                    continue
                next_location = self.journey(destination[1], destination[2])
            elif response == "T":
                print("messages")
            elif response == "S":
                print("shop")
            elif response == "I":
                game.hero.inventory()
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


if __name__ == "__main__":
    print("This is a module for 'Oh Great Knight'.")
    input("Press enter to exit.")

# Parent location class to be imported to locations folder in 'Oh Great Knight'
# Mark Lauber
# June 2013

import converter

from user_input import prompt

class Location(object):
    """ Super class for location objects in 'locations' file """

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
        while self.hero.health:
            print("\nYOU ARE IN " + self.name.upper() + ".")
            print("""
J - JOURNEY
T - TALK TO VILLAGERS
S - SHOP
I - INVENTORY
R - REST
G - GAME SAVE
Q - QUIT""")
            response = prompt("").upper()
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
                    return next_location
            elif response == "T":
                self.talk()
            elif response == "S":
                self.shop_menu()
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

        # If hero dies during self.menu(), return None to end game.main_loop() 
        return None

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
        self.hero.inventory_menu()
        item = self.hero.item_pick()
        if item != False:
            if item.personal_use == True:
                self.hero.use_item(item, self.hero)
            else:
                prompt("You cannot use this here.")

    def rest(self):
        """ Allows hero to rest at an inn. """
        price = 20
        answer = prompt("\"Welcome to the " + self.name + " inn!  \
A room costs " + str(price) + " silver.  Care to rest a while?\" (y/n) ").lower()
        if answer == "y":
            if self.hero.coins >= price:
                print("\"Have a nice stay\"!")
                self.hero.coins -= price
                self.hero.gain_health(50)
                print(self.hero.name + " gains 50 health!")
            else:
                print("\"I'm sorry sir, but you haven't enough silver.\"")

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
            option = prompt("What can I do for ye?\n").upper()
            if option == "X":
                prompt("\"Good day to you sir!\"\n")
            elif option == "P":
                self.hero_purchase()
            elif option == "S":
                self.hero_sell()
            elif option == "I":
                self.hero.inventory_menu()
            else:
                print("\a\"What jibberish thou art speaketh?!\"")

    def show_inventory(self):
        print("ITEM\t\tPRICE\tCLASS\tDESCRIPTION")
        for item in self.inventory:
            if len(item.name) < 8:
                print(item.name + "\t\t" + str(item.price) + "\t" + item.item_class + "\t" + item.description)
            else:
                print(item.name + "\t" + str(item.price) + "\t" + item.item_class + "\t" + item.description)
            
    def hero_purchase(self):
        self.show_inventory()
        print("\"Which would ye like to purchase?\"")
        item = prompt("")
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
        self.hero.inventory_menu()
        item = prompt("\"What would ye like to sell?\" ").lower()

        # If item does not exist, converter will print appropriate message
        # and hero_sell() function will end.
        item = converter.convert(item)

        # If hero has the item and the item does not belong to the King, commence sale.
        if item in self.hero.inventory and item.name != "Treasure Map" and item.name != "King's Loot":
            sale_price = int(item.price * 0.8)
            print("\"I'll offer you " + str(sale_price) + " silver.\"")
            response = prompt("Is that agreeable to you?\" (y/n) ").upper()

            # If sale price is accepted, commence sale
            if response == "Y":
                self.hero.drop(item)
                self.hero.coins += sale_price
                print("\"Nice doing business with you, sir!\"")

            # If sale price is not accepted, end function
            elif response == "N":
                print("\"Tis the best I can do!\"")

            # If response is invalid, end function
            else:
                print("\a\"What?\"")

        # If the item is in hero's inventory, but does not belong to him, reject sale.
        elif item in self.hero.inventory:
            print("You can't sell that -- it belongs to the King!")

        # If item does exist but is not in inventory, end function
        elif item != False:
            print("\"You don't have one!\a\"")


if __name__ == "__main__":
    print("This is a module for 'Oh Great Knight'.")
    prompt("Press enter to exit.")

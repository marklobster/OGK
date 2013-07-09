# 'Oh Great Knight'
# Main Program
# Mark Lauber

# Run title sequence.
# Run opening menu.
    # If 'New Game':
        # Create New Game
    # Or if 'Resume':
        # Load old file
    # Or if 'Exit':
        # End program
# Main Loop:
    # Run 'run()' program for current location
    # If user does not quit:
        # Run 'journey()' function for current location
        # Run program for selected path
        # Return next_location
    # Or if user quits:
        # End program

import characters, locations, introduction


class New_game(object):
    def __init__(self, hero):
        self.hero = hero
        self.current_local = locations.shmucksburg
        self.main_loop()

    def main_loop(self):
        while self.current_local != None:
            next_location = self.current_local.run(self.hero)
            self.current_local = next_location
    

# Functions for 'main' file
def title():
    print("\t\t\t****************")
    print("\t\t\tOh Great Knight!")
    print("\t\t\t****************")
    print("\nby Mark Lauber\n\n")
    input("Press enter to begin.\n\n")

def opening_menu():
    choice = ""
    while choice != "R" and choice != "N" and choice != "X" and choice != "T":
        print("R - Resume Game")
        print("N - New Game")
        print("X - Exit")
        print("T FOR TESTING!!!!")
        choice = input("").upper()
    if choice == "R":
        print("LOAD")
    elif choice == "N":
        import items
        data = introduction.intro()
        hero = characters.New_Hero(data[0], data[1])
        hero.weapon = items.rusty_sword
        game = New_game(hero)

    # For testing only!!!!!!!!
    elif choice == "T":
        import items
        hero = characters.New_Hero("Bob", "Hooray!")
        hero.weapon = items.cheap_dagger
        hero.shield = items.wood_shield
        hero.armor = items.handmedowns
        game = New_game(hero)

def main():
    title()
    opening_menu()

# Execute main()
main()
input("Thanks for playing!")

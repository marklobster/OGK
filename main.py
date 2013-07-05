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

class Test(object):        
    def __init__(self, message):
        self.message = message
    
    def give_message(self):
        print(self.message)

    def run(self):
        self.give_message()
        next_locale = input("Where to next?")
        if next_locale == "test1":
            return test1
        elif next_locale == "test2":
            return test2
        elif next_locale == "test3":
            return test3
        elif next_locale == "none":
            return None

class New_game(object):
    def __init__(self, hero):
        self.hero = hero
        self.current_local = locations.shmucksburg
        self.main_loop(self.hero)

    def main_loop(self, hero):
        while self.current_local != None:
            next_location = self.current_local.run(self.hero)
            self.current_local = next_location
        
test1 = Test("This is test1.")
test2 = Test("This is test2.")
test3 = Test("This is test3.")


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
        data = introduction.intro()
        hero = characters.New_Hero(data[0], data[1])
        game = New_game(hero)

    # For testing only!!!!!!!!
    elif choice == "T":
        import items
        hero = characters.New_Hero("Bob", "Hooray!")
        hero.weapon = items.battle_axe
        hero.shield = items.sturdy_shield
        hero.armor = items.leather
        game = New_game(hero)

def main():
    title()
    opening_menu()

main()
input("Thanks for playing!")

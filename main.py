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
        # Reset current location
    # Or if user quits:
        # End program

import items, characters, battle_system

class Test(object):        
    def __init__(self, message):
        self.message = message
    
    def run(self):
        print(self.message)

    def next(self):
        next_locale = input("Where to next?")
        if next_locale == "test1":
            return test1
        elif next_locale == "test2":
            return test2
        elif next_locale == "test3":
            return test3
        elif next_locale == "none":
            return None
        return next_locale

class New_game(object):
    def __init__(self, current_local):
        self.current_local = current_local
        self.main_loop()

    def main_loop(self):
        while self.current_local != None:
            next_location = self.current_local.menu()
            self.current_local = next_location
        
test1 = Test("This is test1.")
test2 = Test("This is test2.")
test3 = Test("This is test3.")


def title():
    print("\t\t\t****************")
    print("\t\t\tOh Great Knight!")
    print("\t\t\t****************")
    print("\nby Mark Lauber\n\n")
    input("Press enter to begin.")

def opening_menu():
    choice = ""
    while choice != "R" and choice != "N" and choice != "X":
        print("R - Resume Game")
        print("N - New Game")
        print("X - Exit")
        choice = input("").upper()
    if choice == "R":
        print("LOAD")
    elif choice == "N":
        print("SETTING VARIABLES TO DEFAULT SETTINGS.")
        game = New_game(test1)
    elif choice == "X":
        input("Quitting so soon?")


def main():
    title()
    opening_menu()

main()
input("Thanks for playing!")

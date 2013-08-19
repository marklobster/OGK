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

import characters, locations, paths, introduction

from user_input import prompt

class New_game(object):
    def __init__(self, hero, location):
        self.hero = hero
        
        # Feed hero into each location as an attribute
        for i in locations.all_locations:
            i.hero = self.hero
        
        # Feed hero into each path as an attribute
        for i in paths.all_paths:
            i.hero = self.hero

        # Set current_local and begin main_loop()
        self.current_local = location
        self.main_loop()

    def main_loop(self):
        while self.current_local != None:
            next_location = self.current_local.run()
            self.current_local = next_location
    

# Functions for 'main' file
def title():
    print("\t\t\t****************")
    print("\t\t\tOh Great Knight!")
    print("\t\t\t****************")
    print("\nby Mark Lauber\n\n")
    prompt("Press enter to begin.\n\n")

def opening_menu():
    choice = ""
    while choice != "Q":
        print("\nMAIN MENU")
        print("R - Resume Game")
        print("N - New Game")
        print("Q - Quit")
        print("T FOR TESTING!!!!")
        choice = prompt("").upper()
        if choice == "R":
            print("LOAD")
        elif choice == "N":
            import items
            data = introduction.intro()
            hero = characters.New_Hero(data[0], data[1])
            game = New_game(hero, locations.shmucksburg)

        # For testing only!!!!!!!!
        elif choice == "T":
            import items
            hero = characters.New_Hero("Bob", "Hooray!")
            hero.missions = [True, True, True, True, False, False]
            hero.weapon = items.shiny_sword
            hero.shield = items.sturdy_shield
            hero.armor = items.sweet_armor
            hero.coins = 100
            hero.inventory = [items.herbenol,
                              items.shiny_sword,
                              items.sturdy_shield,
                              items.sweet_armor,
                              items.kings_loot,
                              items.t_map
                              ]
            for i in range(1, 7):
                hero.inventory.append(items.bandage)
            game = New_game(hero, locations.silverrock)

def main():
    title()
    opening_menu()

# Execute main()
main()
prompt("Thanks for playing!")

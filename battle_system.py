# Battle System

# Randomly select a monster
# Import monster's statistics
# Determine 1st strike
# Player: choose from attack, item, run
# Computer: attacks
# Switch turns until 1) HP depleted or 2) run away successfully
# Outcome: Victory (gain assets), loss (death), or run away

import random

class Battle(object):
    def __init__(self, hero, monster):
        """ Constructor function initiates battle sequence. """
        self.hero = hero
        self.monster = monster
        self.first_strike = self.get_first_strike()
        self.battle_loop()

    def get_first_strike(self):
        """ First strike chosen at random """
        opponents = (self.hero, self.monster)
        first_strike = random.choice(opponents)
        input(first_strike.name + " strikes first!\n")
        return first_strike
           
          
    def battle_loop(self):
        """ The battle loop """
        # Whoever has first_strike will strike first.
        # Then battle loop continues until someone's health becomes zero.
        if self.first_strike == self.hero:
            while self.hero.health and self.monster.health:
                self.hero.tactic(self.monster)
                if self.monster.health:
                    self.monster.tactic(self.hero)
        else:
            while self.hero.health and self.monster.health:
                self.monster.tactic(self.hero)
                if self.hero.health:
                    self.hero.tactic(self.monster)
                    
        # One way the battle ends is that someone dies via the die() method,
            # setting their self.dead attribute to True.
        if self.monster.dead:
            self.hero.win()
            self.monster.gets_plundered(self.hero)
        elif self.hero.dead:
            self.monster.win()
            
        # The other possibility is that the hero escapes, which calls the
            # monster's deactivate() method.  This sets the monster's health
            # to zero, but monster.dead is NOT set to True. 
        else:
            print("You escape with your life.\n")

if __name__ == "__main__":
    print("This is a module for 'Oh Great Knight'.")
    input("Press enter to exit.")

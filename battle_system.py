# Battle System

# Randomly select a monster
# Import monster's statistics
# Determine 1st strike
# Player: choose from attack, item, run
# Computer: attacks
# Switch turns until 1) HP depleted or 2) run away successfully
# Outcome: Victory (gain assets), loss (death), or run away

import random
from user_input import prompt

class Battle(object):
    def __init__(self, hero, monster):
        """ Constructor function initiates battle sequence. """
        self.hero = hero
        self.monster = monster
        prompt("\n\n\t\t\t" + self.hero.name + " vs. " + self.monster.name + "\n")
        self.first_strike = self.get_first_strike()
        self.battle_loop()

    def get_first_strike(self):
        """ First strike chosen at random """
        opponents = (self.hero, self.monster)
        first_strike = random.choice(opponents)
        prompt(first_strike.name + " strikes first!\n")
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

class War(object):
    def __init__(self, good_guys, mission_data):
        self.good_guys = good_guys
        self.mission_data = mission_data
        self.goods_health = 0
        self.bads_health = 0
        self.battle()

    def battle(self):
        # Each army attacks each other.  Then the remaining health is totaled.
        for i in range(0, 7):
            good_guys[i].attack(bad_guys[i])
            bad_guys[i].attack(good_guys[i])
            
            self.goods_health += good_guys[i].health
            self.bads_health += bad_guys[i].health
            
        both = (self.goods_health, self.bads_health)

        # If there is a tie, winner chosen randomly
        if self.goods_health == self.bads_health:
            winner = random.choice(both)
        # Otherwise, winner is whoever has more health left
        else:
            winner = max(both)

        return winner

if __name__ == "__main__":
    print("This is a module for 'Oh Great Knight'.")
    prompt("Press enter to exit.")

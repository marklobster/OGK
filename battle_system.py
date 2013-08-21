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

class Invasion(object):
    def __init__(self, location):
        """Create teams, do battle, return winner"""
        self.good_guys = self.make_good_guys(location.donations)
        self.bad_guys = self.make_bad_guys(location.hero.time)
        print("goods:")
        for num in self.good_guys:
            print(str(num))
        print("bads:")
        for num in self.bad_guys:
            print(str(num))
        outcome = self.battle()
        if outcome == "win":
            location.gain += 10
            location.wins += 1
        else:
            location.gain -= 100

    def make_good_guys(self, inventory):
        """Create tuple of stats for good_guys, based on donations inventory"""
        import items
        thickness = 0
        deflection = 0
        power = 0
        for item in inventory:
            if isinstance(item, items.Armor):
                thickness += item.thickness
            elif isinstance(item, items.Shield):
                deflection += item.deflection
            elif isinstance(item, items.Weapon):
                power += item.power
        stats = (thickness, deflection, power)
        return stats

    def make_bad_guys(self, time):
        """Create tuple of stats for bad_guys based on hero.time number"""
        thickness = 12 + time
        deflection = 12 + time
        power = 12 + time
        stats = (thickness, deflection, power)
        return stats

    def battle(self):
        # Set variables
        damage_to_good = 0
        damage_to_bad = 0

        # Each team attacks the other 3 times
        for i in range(0, 3):
            damage_to_bad += self.attack(self.good_guys, self.bad_guys)
            damage_to_good += self.attack(self.bad_guys, self.good_guys)
        print("damage to goods: " + str(damage_to_good))
        print("damage to bads: " + str(damage_to_bad))
        if damage_to_good <= damage_to_bad:
            return "win"
        else:
            return "lose"

    def attack(self, attacker, defender):
        # Set variables and battle ratings
        variation = random.randint(0, 7)
        chance = random.randint(1, 100)
        attack_rating = attacker[2] + variation
        deflection_rating = defender[1] / attacker[2] * 9
        armor_rating = defender[0]

        # If chance <= deflection_rating, attack is deflected
        if chance <= deflection_rating:
            print("deflected")
            return 0

        # Otherwise, damage is returned
        else:
            damage = attack_rating * 10 / armor_rating
            print(str(damage))
            return damage

if __name__ == "__main__":
    print("This is a module for 'Oh Great Knight'.")
    prompt("Press enter to exit.")

# characters old version
class Easy_Monster(Character):
    
    def __init__(self, name, health_max, weapon, shield, armor, item_pool):
        super(Easy_Monster, self).__init__(name, health_max, weapon, shield, armor)
        self.item_pool = item_pool
        self.coins = random.randint(3, 8)
        self.create_inventory()
        if self.weapon == items.cheap_dagger and items.cheap_dagger not in self.inventory:
            self.inventory.append(items.cheap_dagger)

    def create_inventory(self):
        if self.item_pool:
            for item in self.item_pool:
                number = random.randint(1,3)
                if number == 3:
                    self.inventory.append(item)

    def deactivate(self):
        self.health = 0

    def die(self):
        self.dead = True
        print("\nYou hath vanquished the " + self.name + ".")

    def gets_plundered(self, opponent):
        print("You gain: ")
        for item in self.inventory:
            print("\t" + item.name)
            opponent.inventory.append(item)
        print("\t" + str(self.coins) + " coins")
        opponent.coins += self.coins

class Medium_Monster(Easy_Monster):
    def __init__(self):
        
        self.coins = random.randint(14, 19)

    def tactic(self, opponent):
        if self.health < (self.health_max * 0.18) and items.band_aid in self.inventory:
            self.use_item(items.band_aid, self)
        else:
            self.attack(opponent)

class Hard_Monster(Easy_Monster):
    def __init__(self, name, health_max, weapon, shield, armor, item_pool):
        super(Hard_Monster, self).__init__(name, health_max, weapon, shield, armor, item_pool)
        self.coins = random.randint(22, 28)
        #self.create_inventory() is run via the super class __init__() function
        #if items.battle_axe in self.inventory:
            #self.use_item(items.battle_axe, self)
            
    def tactic(self, opponent):
        if self.health < (self.health_max * 0.18) and items.first_aid in self.inventory:
            self.use_item(items.first_aid, self)
        else:
            self.attack(opponent)

class Sir_Rat(Easy_Monster):
    def __init__(self):
        self.name = "Sir Rat"
        self.health_max = 35
        self.health = self.health_max
        self.weapon = items.cheap_dagger
        self.shield = items.wood_shield
        self.armor = None
        self.inventory = packets.easy
    
    def die(self):
        self.dead = True
        print("\nYou hath vanquished Sir Rat.")

class Nacht_Musik(Medium_Monster):
    def __init__(self):
        self.name = "Nacht Musik"
        self.health_max = 35
        self.health = self.health_max
        self.weapon = items.talons
        self.shield = None
        self.armor = items.handmedowns
        self.inventory = packets.medium
        
    def shriek(self, target):
        number = random.randint(15, 18)
        print(self.name + " shrieks!\n" + str(number) + " damage!")
        target.lose_health(number)
    
    def tactic(self, opponent):
        number = random.randint(1,3)
        if number < 3:
            self.attack(opponent)
        else:
            self.shriek(opponent)

goblin = Easy_Monster("Goblin", 35, items.cheap_dagger, items.wood_shield, None, packets.easy)
pretty_blob = Easy_Monster("Pretty Blob", 30, items.pseudopod, None, items.leather, packets.easy)
sir_rat = Easy_Monster("Sir Rat", 25, items.cheap_dagger, items.wood_shield, items.handmedowns, packets.easy)
nasher = Easy_Monster("Nasher", 18, items.fangs, None, None, packets.easy)

orc = Medium_Monster("Orc", 65, items.blunt_object, items.wood_shield, items.handmedowns, packets.medium)
hydra_badger = Medium_Monster("Hydra Badger", 55, items.fangs, None, items.handmedowns, packets.medium)
nacht_musik = Nacht_Musik("Nacht Musik", 35, items.talons, None, items.handmedowns, packets.medium)
#ancient_technology = Medium_Monster("Ancient Technology", 

orcupine = Hard_Monster("Orcupine", 75, items.spikes, items.green_shield, items.leather, packets.hard)
#ninja_bear = Hard_Monster("Ninja Bear", 75, items.nunchucks, items.wood_shield, items.handmedowns, packets.hard)
mega_troll = Hard_Monster("Mega Troll", 80, items.battle_axe, items.wood_shield, items.leather, packets.hard)
#ogre_primo = Hard_Monster("Ogre Primo", 85, items.ugly_stick, None, items.handmedowns, packets.hard)
        
if __name__ == "__main__":
    print("This is a module for 'Oh Great Knight'")
    input("Press enter to exit.")


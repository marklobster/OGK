# Ye Olde Item Shop
# This will be changed around a bit now that I am learning about classes and\
# am getting more comfortable creating functions.

# Here are the items.
# They contain values (name with abbreviation, cost, description)
# Abbreviations ('sh1', 'sh2') are used to reference the item during gameplay.
wood_shield = ("Wood Shield (sh1)", 30, "A well-used shield.")
sturdy_shield = ("Sturdy Shield (sh2)", 90, "A sturdy iron shield.")
rusty_sword = ("Rusty Sword (sw1)", 50, "A bargain sword for a bargain price.")
battle_axe = ("Battle Axe (sw2)", 70, "A skillfully made, mortally wounding axe.")
shiny_sword = ("Shiny Sword (sw3)", 90, "A sword fit for a knight, and shiny too!")
heal_potion = ("Healing Potion (p1)", 60, "Drinking this potion will recover 30 HP")
cow_potion = ("Cowards Potion (p2)", 100, "Briefly turn invisible for a quick escape.")
gold_ring = ("Pretty Gold Ring (gr)", 180, "The wedding ring you \"lost\".")
bear_trap = ("Rusty Bear Trap (bt)", 45, "Try hurling it at your enemy.  OUCH!!!")

# For now all items are in shop[].  Later, I will create a new list that
# includes every item in the game, some of which will be in shop[].
shop = [wood_shield, sturdy_shield, rusty_sword, battle_axe, shiny_sword,
             heal_potion, cow_potion, bear_trap]

# Convertor dictionary contains commonly used string abbreviations for items
# and the constant (item) the string refers to.
convertor = {"sh1": wood_shield, "sh2": sturdy_shield, "sw1": rusty_sword,
             "sw2": battle_axe, "sw3": shiny_sword, "p1": heal_potion,
             "p2": cow_potion, "gr": gold_ring, "bt": bear_trap}

# Variables:
# gold_ring must be sold before you have any money.
inventory = [gold_ring]
coins = 0


# Functions:
def convert(term):
    """converts item abbreviation to item variable using convertor dictionary"""
    if term in convertor:
        return convertor[term]
    else:
        print("That item does not exist.\a")
    
def inv_display():
    """Displays items in inventroy along with a description."""
    print("You are carrying:")
    for item in inventory:
        print(item[0], " - ", item[2])
    print("You have ", coins, " silver pieces.")

# Program begins
print("You have entered Ye Olde Item Shop")
print("\"Greetings stranger!\"\n")
option = ""
while option != "X":
    print("X - Exit")
    print("P - Purchase Item")
    print("S - Sell Item")
    print("I - View Inventory")
    print("\nSilver ", coins)
    option = input("\n\"What can I do for ye?\"").upper()
    if option == "X":
        print("\"Good day to you sir!\"\n")
    elif option == "P":
        print("Item\t\t\tCost\tDescription")
        for item in shop:
            print(item[0], "\t", item[1], "\t", item[2])
        term = input("\"Which would ye like to purchase?\"")
        item = convert(term)
        if item in shop:
            if item[1] <= coins:
                inventory.append(item)
                shop.remove(item)
                coins -= item[1]
            else:
                input("\"You can't afford that!\"\a\n")
        elif item in inventory:
            input("\"Sorry I haven't got that in stock.\"")
    elif option == "S":
        inv_display()
        sell = input("\"What would ye like to sell?\"")
        item = convert(sell)
        if item in inventory:
            response = input("\"I'll offer you " + str(int((item[1] * 0.8))) +\
                             " silver.  Is that agreeable to you? (y/n)\"").upper()
            if response == "Y":
                inventory.remove(item)
                shop.append(item)
                coins += int(item[1] * 0.8)
            elif response == "N":
                input("\"Tis the best I can do!\"")
            else:
                input("\"What?\"\a\n")
        else:
            if item in shop:
                input("You don't have one!\a\n")
    elif option == "I":
        inv_display()
    else:
        input("\"What jibberish thou art speaketh!?\"\a")

inv_display()
            
input("Thanks for playing!")


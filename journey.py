# Journey
# This will be turned into an importable function, journey().
# The rest of the program is a demonstration of it.
# Each landmark has its own distance from the town.
# The distance is either brief, or in days.
# (brief = distance of 1; each day is distance of 2)
# For each distance covered away or toward town:
# An event (monster appears or nothing happens) occurs at random.

import random

def journey(distance):
    for segment in range(distance):
        occurence = random.randint(0, 15)
        if occurence < 10:
            if segment in range(0,20,2):
                input("On the morning of day " + str(int((segment+2) / 2)) + \
                      " nothing happens.")
            elif segment in range(1,19,2):
                input("On the evening of day " + str(int((segment + 1) /2)) \
                      + " nothing happens.")
        else:
            if segment in range(0,20,2):
                input("On the morning of day " + str(int((segment+2)/2)) \
                      + " a monster appears!")
            else:
                input("On the evening of day " + str(int((segment+1)/2))\
                      + " a monster appears!")

distance = int(input("How long is the journey?" ))
if distance != 1:
    input("Your journey will be " + str(int(((distance + 1) / 2))) + " days.")
else:
    input("Your journey will be brief.")
journey(distance)
input("fin")

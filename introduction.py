# "Oh Great Knight!" Introduction

print("\t\t\t****************")
print("\t\t\tOh Great Knight!")
print("\t\t\t****************")
print("\nby Mark Lauber\n\n")
input("Press enter to begin.")

# The beginning part is made to sound like the Greek tragedy chorus.  The\
# Greek chorus consisted of dozen(s) of actors who commented on the play \
# in unison, sort of like a group of narrators.
# Everything in the intro is done inside of quotes, even when no one is \
# speaking.  I don't know why I did this, it was just a random idea that I \
# kept going.  I thought it made it sound like someone was telling you a story.
print("\t\t\tThe Village of Schumcksburg\n")
input("\"Oh, that the town would be safe!\
  Oh, that our goods would be returned!  \
Oh, that the robbers would be put to justice!  \
Oh, that we would be granted federal funding for our municipal improvements!\
  Oh, that there would be peace!\"")
input("\n\"But who?  Who will be our knight?  Who will fight for us?\"\n")

# Get your regular name (not your hero name).
# Some users may want to skip the intro, so they may hold down the enter\
# key.  In order to stop them from skipping the name entry, name1 cannot\
# equal the empty string.
name1 = ""
while name1 == "":
    name1 = input("What do you call yourself?\n")
    name1 = name1.title()

input("\"Alas, a poor farmer approacheth.  His wife chaseth him, calling out '"\
      + name1 + "!!!!!!!  Get on home and make me some dinna!!!!'\"\n")
input("\"" + name1 + " returns home to his shack, his three goats, and \
his loving wife.  'Where you been at all day?  My stomach is empty and me \
bottle's half gone!  And ye better bring in the rest of the harvest before \
them brigands take it all!'\"\n")
input("\"After making a small dinner, " + name1 + " works in the field til the sun goes down.\
  Then, he and Helga go to bed. But " + name1 + " does not sleep well.  He worries about \
his home, his fellow Shmucksburgians and the enemies who ceaselessly plunder the village.\"\n")
input("\"The next morning, " + name1 + " rises to milk the goats.\
  As he reaches under the bed for his boots, he finds a box from his childhood.\
  Inside the box is a mask.\"\n")
input("\"'Wow!  This makes me look twice as valiant and three times as dapper!'\"\
\n")

# Get hero name.
# Again, name2 cannot equal empty string.
name2 = ""
while name2 == "":
    name2 = input("What is your hero-name?\n")
    name2 = name2.title()
    
input("\n\"'This mask will strike fear into the hearts of the brigands.  For I, "\
      + name2 + ", will protect this town and bring our enemies to justice!'\"\n")

input("\n\n\t\t\tYour journey begins.\n\n".upper())

if __name__ == "__main__":
    print("This is a module for 'Oh Great Knight'")
    input("Press enter to exit.")

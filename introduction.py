from user_input import prompt


def intro():
    print("Welcome to Shmucksburg: A knightless town in a dangerous world.")
    prompt("")
    print("Your name is Cecil.  Cecil Farmer.\n")
    prompt("You're a farmer.\n")
    prompt("You leave your cabin one morning and walk to the townsquare.  \
You can hear the beautiful sound of birds chirping.\n")
    prompt("\ttweet!\a")
    prompt("\ttweet tweet!\a\a")
    prompt("\ttweet tweet tweet!\a\a\a\n")
    print("You see your fellow villagers standing in the townsquare, \
mourning, as they've grown accustom to doing:\n")
    prompt("\"Oh, that the town would be safe!  \
Oh, that our goods would be returned!  Oh, that the robbers would be put to \
justice!  Oh, that we would be granted federal funding for our municipal \
improvements!\n \
\"But who?  Who will be our knight!?\"\n")
    prompt("You silently agree.  A hero is needed!  In the past, Shmucksburg \
has been able to defend itself because of its armory.  But since that was \
robbed last year, they've had little luck defending the village.  If only \
someone could find and retake the contents of your armory....\n")
    prompt("You return home.  You go into your barn to begin your work.  \
As you reach for a shovel, you find an old mask from your childhood.\n")
    prompt("\"Why this makes me look twice as dapper and three times as \
valiant!\"\n")
    prompt("'Tis fate, perhaps, but the mask inspires you.\n")
    prompt("\"A hero needs two things: heart, and a sweet mask!  \
Now that I have the latter, I can be our village knight!\"\n")
    
    name = ""
    while name == "":
        name = prompt("\tWhat shall you call yourself, sir knight?\n").title()

    catchphrase = ""
    while catchphrase == "":
        catchphrase = prompt("\tWhat shall your battle cry be?\n")
        
    prompt("\"When I wear this mask, I shall be known as " + name + "!  \
And when I march into battle, I will shout, '" + catchphrase + "!'\"\n")

    prompt("After some thought, you decide a hero may need some other things \
as well, such as weapons and armor and perhaps a shield.  You head to \
the townsquare to pawn your gold ring and buy some supplies.")
    
    prompt("\n\n\t\t\tYOUR JOURNEY BEGINS.\n\n")

    intro_data = (name, catchphrase)
    return intro_data
    

if __name__ == "__main__":
    print("This is a module for 'Oh Great Knight'")
    prompt("Press enter to exit.")

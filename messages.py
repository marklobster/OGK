from user_input import prompt

# Messages to be imported for 'Oh Great Knight' locations

shmucksburg = ("Aye!  The brigands robbed me again!  What this village needs is a guardian!",
               "Our armory is pitiful.  Donations of weapons, shields and armor would help us defend ourselves.",
               "What I need is a guardian for my caravan!  Without that I can't deliver my goods to Cow-Hip.  You wouldn't happen to be travelin' to Cow-Hip, would you sir?",
               "Nice mask fella!  You're not a robber are you?  Well I guess you'd have robbed me by now!",
               "Someone should go to King Vinny up north at Oldendrab Castle to request donations for our armory.",
               "Mommy, can I go to the Valley of Ferdidden Objects?",
               "No, dear!  That place is dangerous!",
               "But they say that there's treasure there!",
               "Yes.  And treasure attracts robbers.  Besides, one would only bury something there if they thought it were cursed!",
               "You captured Simon the Slick!  You truly are a hero!",
               "But there are more wanted men out there.  May they be brought to \
to justice!",
               )

cow_hip = ("Welcome to Cow-Hip!  Sure, we seem to be the butt of every joke.  But in my opinion we have the best fresh dairy air!",
           "It sure is great to have commerce back in Cow-Hip.  In fact, I heard there's a new item at the shop."
           )

fiddlestick = ("Are you heading northeast to Castle Oldendrab?  Do you have an audience with the King?",
               "There is much wealth up north.  Both in Silverrock and at Oldendrab.",
               "Have you heard the terrible news?  Silverrock has been invaded by an army of orcs!",
               "Hooray!  Silverrock is free!  Hooray!  We surely would have been taken next!",
               "There he is!  That guy with the mask saved Silverrock!"
               )

silverrock = ("We are saved!  Long live King Vinny!",
              "We're safe once again!  At least until Monster Season :( "
              )

oldendrab1 = ("You introduce yourself as an ambassador in order to gain audience with the King.",
             "King: Good morrow, young man.  What is it you seek?",
             "Hero: Good King Vinny, I come on behalf of Shmucksburg.  We are \
robbed incessantly.  And since our armory was ransacked last year, we are \
utterly unable to defend ourselves.  I request guards or perhaps armaments \
with which to defend our poor village.",
             "King: My good man, this entire kingdom is poor!  At least it \
will be if we cannot regain Silverrock....  As of now, nearly all of my \
guards are preparing to march west to rid Silverrock of its orcish pests.  \
How, then, could I supply your village with guards or armaments?  I am \
sorry good sir, but I must send you away empty-handed.",
             "Hero: I will fight along side your men if you promise to help me.",
             "King: Are you offering me an ultimatem?!  If you are indeed \
a warrior, then I order you to fight for me!  In fact, I have a specific \
task for you:",
             "Go to the Valley of Forbidden Objects.  There is treasure \
there with which we could bribe the orcs.  I'm afraid \
they have grown dangerously armed and organized.  I would rather give \
them buried treasure than waste my men on them.  Here is a map.  Dig \
up the chest at the end of the valley.  Give it to the orcs as payment.\
  Since you fancy yourself an ambassador, I'll leave convincing them to \
take it up to you.",
             "I am sending trusted servants with you.  They will watch \
and make sure you do not steal the treasure.  If you accomplish \
what I ask, I will see what I can do for Shmucksburg.  Now make haste."
             )

oldendrab2 = ("The guards recognize you and let you in right away.",
              "King: Good day to you, hero.  I understand that you were a \
great help to my men.  As I promised, here is a gift for your fellow \
villagers:",
              "hero: Thank you sir for your aid.  I would gratefully offer you \
my service if you ever require it again.",
              "King: In fact I do have another request!  As we all know, when \
the icy grip of winter thaws and before the blossoms of Spring can bloom, \
Monster Season rears its ugly head.  I need someone to \
explore where the monsters come from: Upheaval Mountain, just north of Silverrock.  \
My hope is that you can thin out the monsters somewhat before they \
come down here to forage.  I know this is a dangerous mission, so I understand \
if you do not wish to accept it.",
              "hero: I accept your mission.  I will explore the origin of the \
frost monsters!  I will --",
              "King: Excellent!  Unfortunately I cannot send help with you, because I \
promised my guards three weeks paid vacation if they freed Silverrock.  But \
since you don't technically work for me, we don't have to worry about that.  \
So anyway, please take this.  You may need it!"
              )

shortcut = ("You approach Silverrock.  You see that an army of orcs has \
encamped just outside the village.  Before you can make it to the gate, \
a very tall orc makes a move to intercept you.",
            "\nPrepare for battle!\n",
            "Dear user,\nYou were not supposed to be able to win this battle \
yet, but you somehow managed to win out of pure luck.  Let's just say you beat \
the game.  Good job.")

boss1 = ("You dig where the map directs you.",
         "King's Servant 1: I see that much of this treasure was made by \
orcs.  Perhaps Good King Vinny is trying to make amends by returning goods \
taken during one of the old wars.",
         "King's Servant 2: I don't believe the orcs would even \
realize....  What ho!  Who goes there!?",
         "\nYou turn around to find that a stranger has snuck up on you!",
         "Prepare for battle!\n")

boss2 = ("\nAs you approach Silverrock, you see two encampments facing each other \
with the helpless village close by.  One of the King's servants hoists a \
negotiator's flag as you approach the orc general's tent.  As you draw near, \
you see a half-dozen nasty orcs surrounding one who is nearly a foot taller \
than the rest.  He is known as Guillek the Mighty, for he has never been \
harmed in combat.  He is the legend who has four arms, the upper of \
which each holds a sword and the lower of which hold shields.  He looks toward the box of \
treasure you had set down ten yards from the tent.  The King's servants \
explain to him King Vinny's offer.  Guillek and two servants come out to examine \
the box.",
         "Orc 1: Is it a bait-switch?",
         "Orc 2: What's a bait-switch?",
         "Guillek: (Sigh)  We won't know if it's a bait-and-switch unless they try \
to switch it....  Knuckleheads.",
         "King's Servant: As you can see, the King wishes to return these \
orc-made treasures to you in order to make peace....",
         "Orc 1: What's that smell....  It smells like Valley of Cursed Objects!",
         "Guillek: You try to bring us cursed treasure?  This is King Vinny's \
offer?!  Cursed treasure!?",
         "\nPrepare for battle!\n",
         "The orcs were definately not expecting that!  With there general \
and greatest warrior dead and having all of King Vinny's army to deal with, \
the orcs take to flight, pursued by the King's men.",
         "King's Servant: I will tell the King what you have done!  Please rest \
here in Silverrock and let the King's men handle the rest of the orcs.  When \
you have regained your strength, come see King Vinny!"
         )

boss3 = ()

if __name__ == "__main__":
    print("This is a module for 'Oh Great Knight'.")
    prompt("Press enter to exit.")

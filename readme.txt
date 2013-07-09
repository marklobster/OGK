'Oh Great Knight'
by Mark Lauber

About:
This is a text adventure game built using Python 3.3.  I did it to learn more about object-oriented programming.  It's been a lot of fun.

In this text adventure, your hero, Cecil Farmer, appoints himself to be the knight for the troubled town of Shmucksburg.  The user assigns him a 'hero name' and battle-cry, selects destinations to journey to, fights monsters and completes missions.  The user must build up his own character, as well as Shmucksburg's armory so that your fellow villagers can defend the town when you're not around.

Programming:
The main loop of the program begins with a specific current location (current_local).  The current_local refers to one of many Location objects, which represent villages you travel to.  Each Location has a run() method, which is invoked by the game's main_loop.  When current_local.run(), the user is presented with a menu of options to buy weapons, talk to villagers, travel to a different location, etc.  When the user selects a new location (next_local) to journey to, the run() method of one of many Path objects is invoked.  This is where you fight monsters.  If the user completes the Path without dying, the desired endpoint, next_local, is returned to the main_loop.  The loop restarts with next_local as the new current_local.  But if the hero does not complete the Path, None is returned as the next_local.  Then the  main_loop ends when its current_local is set to None.

Special Thanks:
Brian Lauber
Matt Lauber
LJ Hill
Thanks for your many words of wisdom and encouragement!!!
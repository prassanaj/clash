# clash

* One can get the player details organized across 15 different sports being played
* One can get the player details for a given list of players through -p <player>
* One can get to see the Team budget details and player count details etc.,

This works on a excel file which has certain worksheets organized w/ soem formulas.  **Just don't alter it, you will be fine.**

```
>>> python model.py --help
Usage: model.py [options]

Options:
  -h, --help            show this help message and exit
  -t TEAM, --team=TEAM  Specify the team name.  Ninja, Samurai, Spartans,
                        Knights
  -p PLAYER, --player=PLAYER
                        Specify a player

```

```
>>> python model.py -p janarthp

```

# Clash

NOTE: You need an excel file titled `Clash.xlsx` in the checkout location that has couple of sheets setup in certain way.
So, before you start running ask me (Prassana) to send you that file.

* One can get the player details organized across 15 different sports being played in a matrix form
* One can get the player details for a given list of players through -p <player> arguments in the command line
* One can get to see the team budget details and player count details etc., to aid during the auction process

This works on a excel file which has certain worksheets organized w/ soem formulas.  **Just don't alter it, you will be fine.**

```
>>> python model.py --help
Usage: model.py [options]

Options:
  -h, --help            show this help message and exit
  -t TEAM, --team=TEAM  Specify the team name.  Ninja, Samurai, Spartans,
                        Knights
  -p PLAYER, --player=PLAYER
                        Specify a player. Defaults to yourself.

```

```
>>> python model.py -p janarthp

```

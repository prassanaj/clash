#!/usr/local/bin/python

"""
Simple script to help read the Clash player details and assemble the information
in a single view that helps me during the auction.

Anyone can use this. Just

python model.py -p <player1> -p <player2> -t <team1> -t <team2> etc.,

player -- userlogin
team -- Ninja, Samurai, Spartans, Knights

"""
import getpass
from pandas import pandas
from tabulate import tabulate
from optparse import OptionParser


def team_matrix(player_df, details, team, sports):
    players = player_df.loc[:, ['Team', 'Login', 'Gender', 'Game', 'Ranks', 'Price', 'Sold For']].drop_duplicates()
    players['Login - R'] = players.Login.str.cat(players.Ranks.astype(str), sep=' ').str.cat(players.Gender, sep='-')

    clash_teams = team if (type(team) is list) else [team]

    col_name = ['Spent', 'Remaining', 'Male', 'Female', 'Total']
    for team in clash_teams:
        print team.upper() + " -",
        for d in details[team]:
            print col_name[details[team].index(d)] + ":" + d.astype(str) + "  ",
        print
        print '~~~~~~~~' * 10
        t = players[players.Team == team]
        player_details = {}
        for s in sports:
            player_details[s.replace('~', ' ')] = list(t[t.Game == s.split(' ')[0].replace('~', ' ')]['Login - R'])
        print tabulate(player_details, headers='keys', tablefmt='simple')
        print

    return;


def get_player_details(player_df, name):

    player = player_df.loc[:, ['Login', 'Gender', 'Ranks', 'Game', 'Price']].drop_duplicates()

    p_names = [name] if (type(name) is not list) else name

    for p in p_names:
        person = player[player.Login == p]
        person_dict = {'Name': [p], 'Gender': [person.iloc[1, 1]], 'Base Price': [person.iloc[1, 4]],
                       'Max Price': [person.iloc[1, 4] * 4]}

        print '- - - - - ' * 10
        print tabulate(person_dict, headers='keys', tablefmt='simple')
        print
        print tabulate(person.loc[:, ['Game', 'Ranks']].sort_values(by='Ranks'), headers='keys', tablefmt='simple')

    print '- - - - - ' * 10

    return;


def load_excel_into_pandas(file, sheet):
    df = pandas.read_excel(file, sheet)
    sdf = df.sort_values(by=['Team', 'Game', 'Ranks'])
    return sdf;


def get_team_details(file, sheet):
    df = pandas.read_excel(file, sheet)
    return df.set_index('Team').T.to_dict('list')


parser = OptionParser()

parser.add_option('-t', '--team', dest='team', action='append',
                  help='Specify the team name. Considers all otherwise.')
parser.add_option('-p', '--player', dest='player', action='append', help='Specify a player. Defaults to you')

(options, args) = parser.parse_args()

# This excel file is pre-arranged w/ few sheets, Ask me for the file.
Excel = 'Clash.xlsx'
Sheet = 'Sport n Player List'

# Sports list w/ male+female minimum requirement.
Sports = ['Athletics 4+2', 'Badminton 4+1', 'Basketball 4', 'Carrom 3+1', 'Chess 4+1', 'Cricket 5', 'Foosball 5+2',
          'Football 5', 'Snooker 4+1', 'Squash 3+1', 'Swimming 3+1', 'Table~Tennis 5+1', 'Tennis 6+1', 'Throwball 5',
          'Volleyball 5+1']

Teams = ['Knights', 'Spartans', 'Samurai', 'Ninja'] if (options.team is None) else options.team
Player = getpass.getuser() if(options.player is None) else options.player

team_details = get_team_details(Excel, 'Summary')
pd = load_excel_into_pandas(Excel, Sheet)
team_matrix(pd, team_details, Teams, Sports)
get_player_details(pd, Player)


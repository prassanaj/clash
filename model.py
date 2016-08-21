#!/usr/local/bin/python

"""
This is an attempt to build a model that predicts the best price for the payer based on the current situation in the
auction. Its best part is that, it will be try to find based on the inputs as of THIS moment.  All that we need to tell
him is the current payer list, probable price which is base_price * 4, sold_price which is the actual price he was
bought for, team which bought the player.

# Player    base_price  max_price   sold_price  team

Algorithm

Identify the given and calculatable inputs
    total_budget            Max budget = Rs 19,75,000 for 2016
    male_count_required     Number of male players to buy
    female_count_required   Number of Female players to buy
    budget_remaining        Budget Left with each team
    male_count              Number of male players bought
    female_count            Number of female players bought

Identify the player inputs
    gender          male or female
    base_price
    list_of_sports  tuple - List of sports he/she plays along with the rank.

Identify the team details as inputs
    team            name of the team
    sport           List of players in set of sports along with their rank.
    high_sports     List of sports to strengthen 100%
    medium_sports   List of sports to strengthen 75%
    low_sports      List of sports to strengthen 50%
    super_low_sports

"""
from pandas import pandas
from tabulate import tabulate
from optparse import OptionParser


def team_matrix(player_df, team):
    players = player_df.loc[:, ['Team', 'Login', 'Gender', 'Game', 'Ranks', 'Price', 'Sold For']].drop_duplicates()
    players['Login - R'] = players.Login.str.cat(players.Ranks.astype(str), sep='-').str.cat(players.Gender, sep='-')

    clash_teams = team if (type(team) is list) else [team]

    for team in clash_teams:
        print team.upper()
        print '~~~~~~~~'
        t = players[players.Team == team]
        player_details = {}
        for s in Sports:
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


parser = OptionParser()

parser.add_option('-t', '--team', dest='team', action='append',
                  help='Specify the team name.  Ninja, Samurai, Spartans, '
                       'Knights')
parser.add_option('-p', '--player', dest='player', action='append', help='Specify a player')

(options, args) = parser.parse_args()

file = 'Clash.xlsx'
sheet = 'Sport n Player List'

Sports = ['Athletics 4+2', 'Badminton 3+1', 'Basketball 4', 'Carrom 2+1', 'Chess 4+1', 'Cricket 5', 'Foosball 5+2',
          'Football 5', 'Snooker 4+1', 'Squash 3+1', 'Swimming 3+1', 'Tables~Tennis 5+1', 'Tennis 6+1', 'Throwball 5',
          'Volleyball 5+1']

Teams = ['Ninja', 'Spartans', 'Samurai', 'Knights'] if (options.team is None) else options.team

pd = load_excel_into_pandas(file, sheet)
team_matrix(pd, Teams)
get_player_details(pd, options.player)

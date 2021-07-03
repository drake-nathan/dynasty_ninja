import requests
import json
from collections import Counter
import datetime

date = datetime.date.today()

#gets user id from username
def get_user_id(username):
    user_id_request = requests.get(f'https://api.sleeper.app/v1/user/{username}')
    username_json = user_id_request.json()
    user_id = username_json['user_id']
    return user_id

#gets league ids from user id. 
def get_league_ids(user_id):
    leagues_url = f'https://api.sleeper.app/v1/user/{user_id}/leagues/nfl/{date.year}'
    leagues_request = requests.get(leagues_url)
    leagues_json = leagues_request.json()
    league_ids = []
    league_names = []
    for league in leagues_json:
        #'type' 2 is dynasty leagues.
        if league['settings']['type'] == 2:
            league_ids.append(league['league_id'])
            league_names.append(league['name'])
    return league_ids, league_names

#takes a user id and a league id and pulls all the players on that roster
def get_rosters(user_id, league_id):
    roster_url = f'https://api.sleeper.app/v1/league/{league_id}/rosters'
    roster_request = requests.get(roster_url)
    roster_json = roster_request.json()
    roster = []
    for team in roster_json:
        if team['owner_id'] == user_id:
            if team['players'] is None:
                pass
            else:
                roster.extend(team['players'])
    return roster

def get_names(player_id):
    with open('portfolio/simple_players.json') as players_file:
        players_json = json.load(players_file)
    return players_json[player_id]

def portfolio_function(username):
    user_id = get_user_id(username)
    # print(f"{username}'s user id is {user_id}")
    
    league_ids, league_names = get_league_ids(user_id)
    league_count = len(league_ids)
    # print(f"{username}'s dynasty leagues are {league_names}")
    
    rosters = []
    for league in league_ids:
        rosters.append(get_rosters(user_id, league))
    # print(rosters)

    roster_names = []
    for roster in rosters:
        for player in roster:
            roster_names.append(get_names(player))
    # print(roster_names)
    
    number_of_players = dict(Counter(roster_names))
    num_players_sorted = sorted(number_of_players.items(), key=lambda item: item[1])
    names = []
    numbers = []
    for tupl in num_players_sorted:
        names.append(tupl[0])
        numbers.append(tupl[1])
    new_dict = {"Name": names, "Count": numbers}
    total_num_of_players = len(names)
    highest_count = numbers[0]
    
    return new_dict, league_count, league_names, total_num_of_players, highest_count
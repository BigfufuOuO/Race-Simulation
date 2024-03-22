import random

# define team number and simulation times
nums_team = 17
nums_simulation = 10000
# set race format (default 3 games with 2 wins)
format = 2


# load race standings and race schedule here
def load_standings(filename):
    standings = {}
    winrate = []
    with open(filename, 'r') as file:
        for line in file:
            team_data = line.strip.split()
            team = team_data[0]
            win_race, loss_race = map(int, team_data[1].split('/'))
            win_match, loss_match = map(int, team_data[2].split('-'))
            standings[team] = {"win_race": win_race, 
                               "loss_race": loss_race,
                               "win_match": win_match,
                               "loss_match": loss_match}
            winrate[team] = win_match / loss_match
    return standings, winrate

def load_schedule(filename):
    schedule = []
    with open(filename, 'r') as file:
        for line in file:
            race = line.strip.split()
            schedule.append(race)
    return schedule
    

# define simulation function
def simulation_simple_match(team1_winrate, team2_winrate):
    team1_win_prob = team1_winrate / (team1_winrate + team2_winrate)
    return random.random() < team1_win_prob

def simulation_simple_race(race, winrate, standings):
    team1 = race[0]
    team2 = race[1]
    team1_win_simple_race = 0
    team2_win_simple_race = 0
    while team1_win_simple_race < format or team2_win_simple_race < format:
        if simulation_simple_match(winrate[team1], winrate[team2]):
            team1_win_simple_race += 1
        else:
            team2_win_simple_race += 1
    
    # update standings and winrate after each race
    standings[team1]['win_race'] += (team1_win_simple_race > team2_win_simple_race)
    standings[team1]['loss_race'] += (team1_win_simple_race < team2_win_simple_race)
    standings[team1]['win_match'] += team1_win_simple_race
    standings[team1]['loss_match'] += team2_win_simple_race

    standings[team2]['win_race'] += (team1_win_simple_race < team2_win_simple_race)
    standings[team2]['loss_race'] += (team1_win_simple_race > team2_win_simple_race)
    standings[team2]['win_match'] += team2_win_simple_race
    standings[team2]['loss_match'] += team1_win_simple_race

    winrate[team1] = standings[team1]['win_match'] / standings[team1]['loss_match']
    winrate[team2] = standings[team2]['win_match'] / standings[team2]['loss_match']

# simulation
def simulation_season(schedule, standings):
    
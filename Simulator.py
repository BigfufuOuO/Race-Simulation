import random

# define cace format (default = 3g2w)
format = 2

class LeagueSimulation:
    def __init__(self, team_standings_filename, race_schedule_filename):
        self.teams = set()
        self.standings = {}
        self.schedule = []
        self.winrate = {}
        self.standings_filename = team_standings_filename
        self.schedule_filename = race_schedule_filename
         
    # load race standings and race schedule here
    def load_standings(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                team_data = line.strip().split()
                team = team_data[0]
                self.teams.add(team)
                win_race, loss_race = map(int, team_data[1].split('/'))
                win_match, loss_match = map(int, team_data[2].split('-'))
                self.standings[team] = {"win_race": win_race, 
                                "loss_race": loss_race,
                                "win_match": win_match,
                                "loss_match": loss_match}
                self.winrate[team] = win_match / (loss_match + win_match)

    def load_schedule(self, filename):
        with open(filename, 'r') as file:
            for line in file:
            #     match_data = line.strip().split()
            #     if len(match_data) > 2:
            #         team1 = match_data[0]
            #         team2 = match_data[1]
            #         team1_score, team2_score = map(int, match_data[2].split(':'))
            #         self.standings[team1]['win_race'] = (team1_score > team2_score)
            #         self.standings[team1]['lose_race'] = (team1_score < team2_score)
            #         self.standings[team1]['win_match'] =  
                race = line.strip().split()
                self.schedule.append(race)
        

    # define simulation function
    def simulation_simple_match(self, team1_winrate, team2_winrate):
        team1_win_prob = team1_winrate / (team1_winrate + team2_winrate)
        return random.random() < team1_win_prob

    def simulation_simple_race(self, race):
        team1 = race[0]
        team2 = race[1]
        team1_win_simple_race = 0
        team2_win_simple_race = 0
        while team1_win_simple_race < format and team2_win_simple_race < format:
            if self.simulation_simple_match(self.winrate[team1], self.winrate[team2]):
                team1_win_simple_race += 1
            else:
                team2_win_simple_race += 1
        
        # update standings and winrate after each race
        self.standings[team1]['win_race'] += (team1_win_simple_race > team2_win_simple_race)
        self.standings[team1]['loss_race'] += (team1_win_simple_race < team2_win_simple_race)
        self.standings[team1]['win_match'] += team1_win_simple_race
        self.standings[team1]['loss_match'] += team2_win_simple_race

        self.standings[team2]['win_race'] += (team1_win_simple_race < team2_win_simple_race)
        self.standings[team2]['loss_race'] += (team1_win_simple_race > team2_win_simple_race)
        self.standings[team2]['win_match'] += team2_win_simple_race
        self.standings[team2]['loss_match'] += team1_win_simple_race

        self.winrate[team1] = self.standings[team1]['win_match'] / (self.standings[team1]['win_match'] + self.standings[team1]['loss_match'])
        self.winrate[team2] = self.standings[team2]['win_match'] / (self.standings[team2]['win_match'] + self.standings[team2]['loss_match'])

    # sort all teams and select those ranked in top 10 under following rules:
        # 1.Priority to win_race
        # 2.if win_race are the same, then comprare the difference between win_match and loss_match
        # [--------NOT REALIZED YET---------]3.if rule 1 and 2 are not applicable, then comprapre the win-loss relation between two teams.
    def get_top_10(self):
        sorted_standings = sorted(self.standings.items(), 
                                  key=lambda x: (x[1]['win_race'], x[1]['win_match'] - x[1]['loss_match']),
                                  reverse=True)
        return [team for team, _ in sorted_standings[:10]]
    
    # simulation of the whole season
    def simulation_season(self, nums_simulation, output_standings=False):
        top_10_scenarios = {} 
        for _ in range(nums_simulation):
            self.teams = set()
            self.standings = {}
            self.schedule = []
            self.winrate = {}
            self.load_standings(self.standings_filename)
            self.load_schedule(self.schedule_filename)
            for race in self.schedule:
                self.simulation_simple_race(race)
            top_10 = tuple(self.get_top_10())

            if top_10 in top_10_scenarios:
                top_10_scenarios[top_10] += 1
            else:
                top_10_scenarios[top_10] = 1
        return top_10_scenarios
       
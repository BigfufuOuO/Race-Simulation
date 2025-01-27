from Simulator import LeagueSimulation 

nums_simulation = 100000

if __name__ == "__main__":

    league_sim = LeagueSimulation("https://lol.fandom.com/wiki/LPL/2024_Season/Spring_Season",
                                  "https://lol.fandom.com/wiki/LPL/2024_Season/Spring_Season")
    top_10_scenarios = league_sim.simulation_season(nums_simulation, True)

    ranking_counts = {i: {} for i in range(1, 11)} 
    for scenario, count in top_10_scenarios.items():
        for i, team in enumerate(scenario, start=1):
            if team in ranking_counts[i]:
                ranking_counts[i][team] += count
            else:
                ranking_counts[i][team] = count

    with open(r'total_result.txt', 'w') as file:
        for scenario, count in sorted(top_10_scenarios.items(), key=lambda x: x[1], reverse=True):
                file.write(f"{', '.join(scenario)}: {count}\n")
    
    with open(r'team_result.txt', 'w') as file:
        for position, teams in ranking_counts.items():
            file.write(f"Position {position}: \n")
            for team, count in teams.items():
                ratio = count / nums_simulation * 100
                file.write(f"\t {team}: {ratio:.2f}%\n")


    

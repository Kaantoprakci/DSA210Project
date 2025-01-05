import json
import pandas as pd
from espn_api.basketball import League

def fetch_all_player(league):
    # Fetch all players (team rosters + free agents)
    all_players = []
    for team in league.teams:
        all_players.extend(team.roster)
    all_players.extend(league.free_agents(size=500))

    # Extract relevant data
    player_data = [
        {
            "name": player.name,
            "position": player.position,
            "team": player.proTeam,
            "total_points": player.total_points
        }
        for player in all_players
    ]

    # Save data to a JSON file
    with open("all_players.json", "w") as file:
        json.dump(player_data, file, indent=4)

    print("All player data has been saved to 'all_players.json'.")

    # New Feature: Save Historical Player Data as CSV
    def save_historical_data(league, total_weeks=10):
        historical_data = []
        for week in range(1, total_weeks + 1):
            box_scores = league.box_scores(matchup_period=week)
            for box in box_scores:
                for player in box.home_lineup + box.away_lineup:
                    historical_data.append({
                        "Player": player.name,
                        "Position": player.position,
                        "Team": player.proTeam,
                        "Rebounds": player.stats.get('rebounds', 0),
                        "Assists": player.stats.get('assists', 0),
                        "Steals": player.stats.get('steals', 0),
                        "Blocks": player.stats.get('blocks', 0),
                        "Turnovers": player.stats.get('turnovers', 0),
                        "Fantasy_Points": player.points  # Fantasy points in the matchup
                    })

        # Convert to DataFrame and save as CSV
        historical_df = pd.DataFrame(historical_data)
        historical_df.to_csv('historical_player_data.csv', index=False)
        print("Historical data saved to 'historical_player_data.csv'.")

    # Call the function to save historical data
    save_historical_data(league)
import json
from espn_api.basketball import League

# Replace with your details
league_id = 1937531242  # Your league ID
season_year = 2025  # Current season year
swid = "{4A2E222B-5E0A-49A5-9140-95B49F24DE78}"
espn_s2 = ("AEB2Uek%2Bx6CDTjgULvGa%2BcklRISl%2BVN0YAI4jWV0gl9KOoy"
           "JSjixHEoz6tzWSBeePg8xAdWwRahoGRD3oTnRiMI8Y%2BN3jSR3eu%2"
           "FnpZVHrXiv0TkrvJKpTGbtbgRojDkeVZ0tXf2EUxrdm7Lu5BVaRp6fm"
           "5n8cfPzISPtS7SCKGYWrild0PmL5ctwHOrpMx4M0PKRGzGrRsh546QUh"
           "GvXhALng6X5tKSPj82lvc4AJc6LnVl35mcB54ooRFbI1SJTIoX2hbW23f"
           "EYaQ2Yv93fr59b0xEvJwtCz6Pj%2BMlRPEH7Jw%3D%3D")  # Your ESPN_S2 token

# Connect to your league
league = League(league_id=league_id, year=season_year, swid=swid, espn_s2=espn_s2)

# Fetch and print team rosters
# for team in league.teams:
#     print(f"\nTeam Name: {team.team_name}")
#     for player in team.roster:
#         print(f"{player.name} - {player.position} - {player.total_points} points")


# Replace with your team name
team_name = "SHILE RHINO'S"

# Find your team
my_team = next(team for team in league.teams if team.team_name == team_name)

# print(f"My Team: {my_team.team_name}")
# for player in my_team.roster:
#     print(f"{player.name} - {player.position} - {player.total_points} points")

# Load player data from the JSON file
with open("all_players.json", "r") as file:
    all_players = json.load(file)

added_players = {"Alex Caruso", "Terry Rozier"}  # Manually identified added players
# Example: Fetch contributions of added players during Week 9
added_player_stats = []

for player in all_players:
    if player["name"] in added_players:
        # Fetch player data dynamically using the API
        # Find the corresponding player object in the league
        api_player = next(
            (p for team in league.teams for p in team.roster if p.name == player["name"]), None
        )

        if api_player:
            # Fetch weekly stats (e.g., Week 9)
            weekly_stats = api_player.stats.get(7)  # Replace 9 with the desired week
            print(weekly_stats)
            added_player_stats.append({
                "Player": player["name"],
                "Position": player["position"],
                "NBA_Team": player["team"],
                "Fantasy_Points_Week_9": weekly_stats.get("points", 0) if weekly_stats else 0,
            })

# # Display the contributions of added players
import pandas as pd
df_added_stats = pd.DataFrame(added_player_stats)
print("Added Player Contributions:")
print(df_added_stats)
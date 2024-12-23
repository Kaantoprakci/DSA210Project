import json
from espn_api.basketball import League

# Replace with your ESPN credentials
league_id = 1937531242
season_year = 2025
swid = "{4A2E222B-5E0A-49A5-9140-95B49F24DE78}"
espn_s2 = ("AEB2Uek%2Bx6CDTjgULvGa%2BcklRISl%2BVN0YAI4jWV0gl9KOoy"
           "JSjixHEoz6tzWSBeePg8xAdWwRahoGRD3oTnRiMI8Y%2BN3jSR3eu%2"
           "FnpZVHrXiv0TkrvJKpTGbtbgRojDkeVZ0tXf2EUxrdm7Lu5BVaRp6fm"
           "5n8cfPzISPtS7SCKGYWrild0PmL5ctwHOrpMx4M0PKRGzGrRsh546QUh"
           "GvXhALng6X5tKSPj82lvc4AJc6LnVl35mcB54ooRFbI1SJTIoX2hbW23f"
           "EYaQ2Yv93fr59b0xEvJwtCz6Pj%2BMlRPEH7Jw%3D%3D")

# Connect to the league
league = League(league_id=league_id, year=season_year, swid=swid, espn_s2=espn_s2)

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
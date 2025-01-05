from collections import Counter
from espn_api.basketball import League
import compare_weeks
import predict_player
import fetch_all_player

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

fetch_all_player.fetch_all_player(league)

# Initiate the weeks to analyze
total_weeks = 10
position_frequencies = Counter()

# Loop through all weeks to analyze position contributions
for week in range(2, total_weeks + 1):  # Start from week 2 (compare weeks 1 and 2, 2 and 3, etc.)
    print(f"\nAnalyzing contributions between Week {week - 1} and Week {week}...")
    highest_positions = compare_weeks.compare_weeks(league, current_week=week)
    print(f"Week {week}: Highest-Contributing Position(s): {highest_positions}")

    # Update the frequency counter for highest-contributing positions
    position_frequencies.update(highest_positions)

# Determine the most frequent highest-contributing position(s)
most_frequent_positions = position_frequencies.most_common()

print("\nFinal Analysis:")
print("Position Frequencies Across Weeks:", dict(position_frequencies))
print("Most Frequent Highest-Contributing Position(s):",
      [pos for pos, freq in most_frequent_positions if freq == most_frequent_positions[0][1]])

predict_player.predict_player(league, most_frequent_positions)
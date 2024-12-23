import pandas as pd
import matplotlib.pyplot as plt

def get_lineup(box_scores, name):
    for box in box_scores:
        if box.home_team.team_name == name or box.away_team.team_name == name:
            if box.home_team.team_name == name:
                return box.home_lineup
            else:
                return box.away_lineup
    return []

def compare_weeks(league, current_week):
    # Init. the previous week
    previous_week = current_week - 1

    # Fetch box scores for both weeks
    box_scores_current = league.box_scores(matchup_period=current_week)
    box_scores_previous = league.box_scores(matchup_period=previous_week)

    # Replace with your team name
    team_name = "SHILE RHINO'S"

    # Find your team
    my_team = next(team for team in league.teams if team.team_name == team_name)

    # Get lineups for both weeks
    lineup_current = get_lineup(box_scores_current, team_name)
    lineup_previous = get_lineup(box_scores_previous, team_name)

    # Extract player names for comparison
    current_players = {player.name: player for player in lineup_current}
    previous_players = {player.name: player for player in lineup_previous}

    # Identify added and dropped players
    added_players = set(current_players.keys()) - set(previous_players.keys())

    print("Added Players:", added_players)

    # Analyze contributions of added players with eligible positions
    position_contributions = {}

    # Define primary positions to keep
    primary_positions = {"PG", "SG", "SF", "PF", "C"}

    for player_name in added_players:
        player = current_players[player_name]
        points = player.points
        eligible_positions = player.eligibleSlots

        filtered_positions = []
        for position in eligible_positions:
            if position in primary_positions:
                filtered_positions.append(position)

        # Distribute points across eligible positions
        for position in filtered_positions:
            if position not in position_contributions:
                position_contributions[position] = 0
            position_contributions[position] += points

    # Display contributions by eligible positions
    print("\nContributions by Eligible Positions:")
    for position, total_points in position_contributions.items():
        print(f"{position}: {total_points} points")

        # Visualize contributions
        df_filtered_positions = pd.DataFrame(position_contributions.items(), columns=["Position", "Points"])
        df_filtered_positions.sort_values(by="Points", ascending=False, inplace=True)

        # Plot the graph
        plt.figure(figsize=(8, 5))
        df_filtered_positions.plot(kind="bar", x="Position", y="Points",
                                   title=f"Impact of Added Players (Week {previous_week} -> Week {current_week})",
                                   legend=False)
        plt.xlabel("Position")
        plt.ylabel("Total Points")
        plt.tight_layout()

        # Save the graph to 'figures' directory
        filename = f"figures/week_{previous_week}_to_week_{current_week}.png"
        plt.savefig(filename)
        plt.close()  # Close the plot to free memory
        print(f"Graph saved to {filename}")

        # Find the position(s) with the highest contribution
        max_points = max(position_contributions.values())
        highest_contributing_positions = [position for position, points in position_contributions.items() if
                                          points == max_points]

        return highest_contributing_positions

import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

def predict_player(league, most_frequent_positions):
    # Fetch free agents
    free_agents = league.free_agents(size=500)

    # Convert free agents to a DataFrame
    free_agents_data = [
        {
            "Player": player.name,
            "Position": player.position,
            "Team": player.proTeam,
            "Rebounds": player.stats.get('rebounds', 0),
            "Assists": player.stats.get('assists', 0),
            "Steals": player.stats.get('steals', 0),
            "Blocks": player.stats.get('blocks', 0),
            "Turnovers": player.stats.get('turnovers', 0)
        }
        for player in free_agents
    ]
    free_agents_df = pd.DataFrame(free_agents_data)

    # Step 1: Add Positional Relevance
    # Normalize positional relevance
    relevant_positions = {pos: i + 1 for i, (pos, _) in enumerate(most_frequent_positions)}
    max_relevance = max(relevant_positions.values(), default=1)
    normalized_relevance = {pos: rel / max_relevance for pos, rel in relevant_positions.items()}

    # Assign relevance to free agents
    free_agents_df['Positional_Relevance'] = free_agents_df['Position'].map(normalized_relevance).fillna(0)

    # Step 2: Preprocess Data
    # Load historical data for training
    historical_data = pd.read_csv('historical_player_data.csv')

    # Add positional relevance to historical data
    historical_data['Positional_Relevance'] = historical_data['Position'].map(normalized_relevance).fillna(0)

    # Preprocessing pipeline
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), ['Rebounds', 'Assists', 'Steals', 'Blocks', 'Turnovers', 'Positional_Relevance']),
            ('cat', OneHotEncoder(handle_unknown='ignore'), ['Position', 'Team'])
        ]
    )

    # Split historical data into X (features) and y (target)
    X = historical_data.drop(columns=['Player', 'Fantasy_Points'])
    y = historical_data['Fantasy_Points']

    # Step 3: Train the Decision Tree Model
    pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('model', DecisionTreeRegressor(max_depth=5, random_state=42))
    ])
    pipeline.fit(X, y)

    # Step 4: Predict Free Agent Contributions
    X_free_agents = free_agents_df.drop(columns=['Player'])
    predictions = pipeline.predict(X_free_agents)

    # Add predictions to free agent DataFrame
    free_agents_df['Predicted_Fantasy_Points'] = predictions

    # Step 5: Recommend the Best Players
    best_players = free_agents_df.sort_values(by='Predicted_Fantasy_Points', ascending=False).head(5)
    print("Top Free Agents to Add:")
    print(best_players[['Player', 'Position', 'Predicted_Fantasy_Points']])

    return best_players
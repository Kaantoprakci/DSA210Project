# NBA Fantasy Team Optimization Project

## Project Objective
This project, developed for the **DSA210 course during the Fall 2024 semester**, aims to optimize my NBA Fantasy team's performance by leveraging data-driven insights. Using personalized data from my ESPN Fantasy account, the project focuses on understanding the impact of weekly player additions, retention patterns, and timing of decisions on overall team performance. The ultimate goal is to develop strategies that maximize weekly fantasy points and improve decision-making.

---

## Hypothesis
Strategically adding players to my NBA Fantasy team by analyzing data-driven factors such as timing of additions, matchup advantages, player roles, and retention patterns will significantly improve my team’s weekly performance. By understanding how different variables—such as the day of the week players are added, their contributions relative to league averages, and their impact on specific matchups—affect overall team performance, I hypothesize that I can develop an optimal decision-making framework. This framework will maximize fantasy points, reduce reliance on guesswork, and provide actionable strategies for long-term success in the league.
---

## Dataset

The dataset is derived from my ESPN Fantasy account and personalized through additional tracking. Key components include:

1. **Weekly Player Additions:**
   - Names of players added to my team each week.
   - **Date and time** of each addition.
   - **Reason for addition** (e.g., injury replacement, matchup advantage).

2. **Player Performance on My Team:**
   - Fantasy points contributed during their tenure.
   - Game-specific statistics (points, rebounds, assists, steals, etc.).
   - Comparison of their performance to season averages.

3. **Retention and Impact Data:**
   - **Duration** each player stayed on my team.
   - Their contribution to my team’s weekly total score.
   - Timing and reasoning for player drops.

4. **Timing Insights:**
   - Performance based on **days of the week** (e.g., does adding players on certain days yield better results?).
   - Optimal times for adding players to maximize contributions.

5. **Player Position and NBA Team Analysis:**
   - **Player Position:** Positions (e.g., PG, SG, SF, PF, C) for each player and their average contributions.
   - **NBA Team:** The NBA team each player belongs to and their impact on fantasy points.
   - **Analysis Goals:**
     - Identify which positions provide the highest fantasy points.
     - Determine which NBA teams' players contribute the most to fantasy success.

---

## Motivation
Managing an NBA Fantasy team is an engaging yet challenging task, especially with limited weekly player addition slots. This project aims to analyze the timing and impact of my decisions to uncover patterns that can optimize my team's performance. Combining my passion for basketball with data science, this project not only helps in improving my fantasy league strategy but also provides practical experience in data analysis and modeling.

---

## Project Plan

1. **Data Collection and Personalization:**
   - Export player performance and weekly team data from ESPN using the API.
   - Manually log the **date, time, and reason** for each player addition.
   - Enrich the dataset with opponent statistics and player matchups.

2. **Exploratory Data Analysis (EDA):**
   - Analyze weekly player additions and their impact on team performance.
   - Identify trends in retention duration and player contributions.

3. **Predictive Modeling:**
   - Use regression models to predict player impact based on timing and matchups.
   - Apply clustering to categorize players by retention value and performance.

4. **Optimization:**
   - Develop strategies for maximizing weekly points through better timing and player selection.

5. **Visualization:**
   - Create charts to illustrate key findings, such as:
     - Weekly fantasy points from added players.
     - Retention duration vs. contribution trends.






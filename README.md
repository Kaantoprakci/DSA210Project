# NBA Fantasy Team Optimization Project

## Project Objective
This project, developed for the DSA210 course during the Fall 2024 semester, aims to optimize my NBA Fantasy team's performance by analyzing the impact of player additions which are made manually by me  each week on team success. Using weekly matchup data from my ESPN Fantasy account, the project identifies added players, evaluates their contributions based on their eligible positions (PG, SG, SF, PF, C), and visualizes position-specific trends. By iterating through weekly matchups and storing insights in a dedicated repository, the project provides actionable strategies to maximize fantasy points and improve decision-making.






---

## Hypothesis


Strategically adding players to my NBA Fantasy team by analyzing their contributions based on eligible positions (PG, SG, SF, PF, C) and weekly performance trends will significantly improve my team’s success. By identifying which positions consistently contribute the most fantasy points and understanding how added players impact my team's weekly matchups, I hypothesize that I can develop an optimal strategy for roster management. This strategy will enable me to make data-driven decisions that maximize fantasy points, reduce reliance on guesswork, and ensure long-term success in the league.---

## **Dataset**

The dataset is derived from my ESPN Fantasy account and enhanced through weekly matchup analysis. It provides a detailed view of the impact of added players on my team’s performance. Key components include:

### **1. Weekly Player Additions**
- Names of players added to my team each week.
- Their **eligible positions** (PG, SG, SF, PF, C).
- Fantasy points contributed by these players during the matchup week they were added.

### **2. Player Performance on My Team**
- Total fantasy points contributed by added players in the week they were on my team.
- Distribution of points across their eligible positions (e.g., PG, SG).

### **3. Position-Specific Analysis**
- Contributions of added players categorized by their eligible positions (PG, SG, SF, PF, C).
- Identification of positions that consistently contribute the most points.

### **4. Weekly Visualizations**
- Bar graphs illustrating the contributions of added players by position for each week.
- Stored visualizations in a `figures` directory for detailed review.

### **5. Trends and Insights**
- Cumulative analysis of position-specific contributions over multiple weeks.
- Identification of positions (e.g., SG, PF) that are most impactful for maximizing fantasy points.
- Insights into the consistency of performance across weeks.

This dataset provides a comprehensive foundation for understanding how roster changes affect my team’s success and helps refine strategies for future weeks.

---

## Motivation
 Managing an NBA Fantasy team is both exciting and challenging, particularly when working within the constraints of limited weekly player addition slots. This project focuses on analyzing the impact of my roster decisions, specifically the players I add each week, to uncover patterns that enhance my team's performance. By leveraging data-driven insights, the project combines my enthusiasm for basketball with a structured approach to data analysis. Beyond improving my fantasy league strategy, this project offers valuable hands-on experience in data analysis, visualization, and decision-making, bridging my passion for sports with practical data science applications.

---

### **Project Plan**

### **1. Data Collection and Personalization**
- Retrieve weekly matchup and player performance data using the ESPN API.
- Automatically identify added players and their eligible positions (PG, SG, SF, PF, C).
- Enrich the dataset with weekly points contributed by added players and categorize them by position.

---

### **2. Exploratory Data Analysis (EDA)**
- Compare weekly rosters to analyze the impact of player additions on team performance.
- Identify trends in player contributions by position and retention duration.
- Evaluate which positions consistently yield the highest fantasy points.

---

### **3. Position-Based Analysis**
- Categorize added players by their eligible positions.
- Analyze the cumulative contribution of positions (PG, SG, SF, PF, C) over multiple weeks.
- Identify the positions with the greatest impact on overall team success.

---

### **4. Visualization**
- Generate and save bar charts for each week, illustrating the contributions of added players by position.
- Store all visualizations in a `figures` directory for easy reference.
- Create cumulative visualizations to show trends across weeks.

---

### **5. Insights and Strategy Development**
- Summarize findings to determine which positions are most impactful.
- Develop actionable strategies for optimizing weekly roster changes based on position-specific contributions.
- Use insights to refine future decision-making and maximize fantasy points.



## **What Could Be Done Better?**
1. **Enhanced Data Accuracy**:
   - Incorporate mid-week transaction logs to capture precise timestamps for player additions and drops, providing a more detailed analysis of timing and its impact on performance.
   - Map composite positions (e.g., `G/F`, `F/C`) more accurately to avoid potential misclassification in position-based contributions.

2. **Larger Dataset**:
   - Analyze data from multiple seasons to identify long-term trends and patterns in position-based contributions and player performance.


---

## **Future Plans**

1. **Automated Updates**:
   - Automate the data collection process at the end of each week, including visualizations and analysis summaries, to reduce manual work.

2. **Interactive Tool Development**:
   - Build an interactive tool or web application that allows users to input their team data and receive position-based recommendations for player additions.


-- Goal: Find the top 10 goal contributors
SELECT 
    name, 
    position, 
    goals, 
    assists, 
    goal_contributions
FROM ac_milan_players
ORDER BY goals DESC
LIMIT 10;
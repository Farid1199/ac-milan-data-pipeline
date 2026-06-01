-- Goal: Analyze efficiency for players with at least 1 appearance
SELECT 
    name, 
    position, 
    appearances, 
    goals, 
    assists,
    ROUND(goals * 1.0 / appearances, 2) as goals_per_game
FROM ac_milan_players
WHERE appearances > 0
ORDER BY goal_contributions DESC;
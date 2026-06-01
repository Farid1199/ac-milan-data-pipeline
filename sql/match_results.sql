-- Goal: Count the frequency of each result type
SELECT 
    result,
    COUNT(*) as total_matches
FROM ac_milan_matches
GROUP BY result
ORDER BY total_matches DESC;
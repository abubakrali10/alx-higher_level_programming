-- This script lists records of a table
-- displays records of scores and names with score >= 10
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC

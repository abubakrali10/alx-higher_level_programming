-- This script lists all records of a table
-- lists records with a value in the name column
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;

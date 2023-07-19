-- This script lists all cities in hbtn_0d_usa Database
-- lists cities by id, name and state id in asc order
SELECT cities.id, cities.name, states.name
FROM cities INNER JOIN states
ON cities.state_id = cities.id
ORDER BY cities.id

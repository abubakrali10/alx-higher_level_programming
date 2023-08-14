-- This script lists all shows in hbtn_0d_tvshows Database
-- lists shows by title and genre_id in asc order
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
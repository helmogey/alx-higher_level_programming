-- script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.
-- Each record should display: tv_genres.name - rating sum
-- Results must be sorted in descending order by their rating
-- You can use only one SELECT statement
SELECT tv_genres.name, SUM(hbtn_0d_tvshows_rate.rating) AS rating_sum
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN hbtn_0d_tvshows_rate ON tv_show_genres.show_id = hbtn_0d_tvshows_rate.show_id
GROUP BY tv_genres.name
ORDER BY rating_sum DESC;

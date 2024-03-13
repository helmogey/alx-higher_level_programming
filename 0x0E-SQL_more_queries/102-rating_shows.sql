-- script that lists all shows from hbtn_0d_tvshows_rate by their rating.
-- Each record should display: tv_shows.title - rating sum
-- Results must be sorted in descending order by the rating
-- You can use only one SELECT statement
SELECT tv_shows.title, SUM(hbtn_0d_tvshows_rate.rating) AS rating_sum
FROM tv_shows
JOIN hbtn_0d_tvshows_rate ON tv_shows.id = hbtn_0d_tvshows_rate.show_id
GROUP BY tv_shows.title
ORDER BY rating_sum DESC;

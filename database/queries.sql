-- Netflix Movies and TV Shows ETL Project
-- SQL reporting queries

-- 1. Count movies and TV shows
SELECT type, COUNT(*) AS total_titles
FROM titles
GROUP BY type
ORDER BY total_titles DESC;


-- 2. Find the top 10 release years
SELECT release_year, COUNT(*) AS total_titles
FROM titles
WHERE release_year IS NOT NULL
GROUP BY release_year
ORDER BY total_titles DESC
LIMIT 10;


-- 3. Show the distribution of content ratings
SELECT rating, COUNT(*) AS total_titles
FROM titles
WHERE rating IS NOT NULL
GROUP BY rating
ORDER BY total_titles DESC;


-- 4. Find the 10 longest movies
SELECT
    title,
    CAST(REPLACE(duration, ' min', '') AS INTEGER) AS duration_minutes
FROM titles
WHERE type = 'Movie'
  AND duration LIKE '%min%'
ORDER BY duration_minutes DESC
LIMIT 10;


-- 5. Count titles added to Netflix each year
SELECT
    CAST(strftime('%Y', date_added) AS INTEGER) AS date_added_year,
    COUNT(*) AS total_titles
FROM titles
WHERE date_added IS NOT NULL
GROUP BY date_added_year
ORDER BY date_added_year;


-- 6. Find countries with more than 20 titles
SELECT
    c.country_name,
    COUNT(DISTINCT tc.show_id) AS total_titles
FROM countries AS c
JOIN title_countries AS tc
    ON c.country_id = tc.country_id
GROUP BY c.country_name
HAVING COUNT(DISTINCT tc.show_id) > 20
ORDER BY total_titles DESC
LIMIT 10;


-- 7. Categorize content using CASE
SELECT
    CASE
        WHEN type = 'Movie' THEN 'Movies'
        WHEN type = 'TV Show' THEN 'TV Shows'
        ELSE 'Other'
    END AS content_category,
    COUNT(*) AS total_titles
FROM titles
GROUP BY content_category
ORDER BY total_titles DESC;


-- 8. Find the 10 most common genres
SELECT
    g.genre_name,
    COUNT(DISTINCT tg.show_id) AS total_titles
FROM genres AS g
JOIN title_genres AS tg
    ON g.genre_id = tg.genre_id
GROUP BY g.genre_name
ORDER BY total_titles DESC
LIMIT 10;


-- 9. Subquery: Find release years with at least 100 titles
SELECT
    release_year,
    COUNT(*) AS total_titles
FROM titles
WHERE release_year IN (
    SELECT release_year
    FROM titles
    WHERE release_year IS NOT NULL
    GROUP BY release_year
    HAVING COUNT(*) >= 100
)
GROUP BY release_year
ORDER BY total_titles DESC;
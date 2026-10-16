
import sqlite3
from pathlib import Path
import pandas as pd

# Connect to the Netflix database
db_path = Path(__file__).resolve().parent / "database" / "netflix.db"
conn = sqlite3.connect(db_path)

try:
    # 1. Count movies and TV shows
    query = """
    SELECT type, COUNT(*) AS total
    FROM netflix_titles
    GROUP BY type
    ORDER BY total DESC;
    """
    print("\n1. Movies and TV Shows")
    print(pd.read_sql_query(query, conn))

    # 2. Find the years with the most releases
    query = """
    SELECT release_year, COUNT(*) AS total
    FROM netflix_titles
    GROUP BY release_year
    ORDER BY total DESC
    LIMIT 10;
    """
    print("\n2. Top 10 Release Years")
    print(pd.read_sql_query(query, conn))

    # 3. Check the distribution of content ratings
    query = """
    SELECT rating, COUNT(*) AS total
    FROM netflix_titles
    GROUP BY rating
    ORDER BY total DESC;
    """
    print("\n3. Content Ratings")
    print(pd.read_sql_query(query, conn))

    # 4. Find the 10 longest movies
    query = """
    SELECT title, duration
    FROM netflix_titles
    WHERE type = 'Movie'
      AND duration LIKE '%min%'
    ORDER BY CAST(REPLACE(duration, ' min', '') AS INTEGER) DESC
    LIMIT 10;
    """
    print("\n4. Top 10 Longest Movies")
    print(pd.read_sql_query(query, conn))

    # 5. Count titles added to Netflix each year
    query = """
    SELECT
        CAST(strftime('%Y', date_added) AS INTEGER) AS date_added_year,
        COUNT(*) AS total
    FROM netflix_titles
    WHERE date_added IS NOT NULL
    GROUP BY date_added_year
    ORDER BY date_added_year;
    """
    print("\n5. Titles Added Each Year")
    print(pd.read_sql_query(query, conn))

    # 6. Find countries with more than 20 titles
    query = """
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
    """
    print("\n6. Top Countries by Number of Titles")
    print(pd.read_sql_query(query, conn))

    # 7. Group the content into movies and TV shows
    query = """
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
    """
    print("\n7. Content Type Summary")
    print(pd.read_sql_query(query, conn))

    # 8. Find the most common genres
    query = """
    SELECT
        g.genre_name,
        COUNT(DISTINCT tg.show_id) AS total_titles
    FROM genres AS g
    JOIN title_genres AS tg
        ON g.genre_id = tg.genre_id
    GROUP BY g.genre_name
    ORDER BY total_titles DESC
    LIMIT 10;
    """
    print("\n8. Top 10 Genres")
    print(pd.read_sql_query(query, conn))

    print("\nSQL analysis completed successfully.")

finally:
    conn.close()

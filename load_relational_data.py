
from pathlib import Path
import sqlite3
import pandas as pd

# 1. Set project paths
BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "data" / "netflix_cleaned.csv"
DB_PATH = BASE_DIR / "database" / "netflix.db"
SCHEMA_PATH = BASE_DIR / "database" / "schema.sql"

# 2. Read the cleaned dataset
df = pd.read_csv(CSV_PATH, dtype=str).fillna("")

print("Dataset loaded:", len(df), "records")

# 3. Connect to the database
conn = sqlite3.connect(DB_PATH)

try:
    # Enable foreign key checks
    conn.execute("PRAGMA foreign_keys = ON")

    # 4. Create the relational tables
    with open(SCHEMA_PATH, "r", encoding="utf-8") as file:
        conn.executescript(file.read())

    # 5. Clear existing relational data to avoid duplicates
    conn.execute("DELETE FROM title_countries")
    conn.execute("DELETE FROM title_genres")
    conn.execute("DELETE FROM title_directors")
    conn.execute("DELETE FROM titles")
    conn.execute("DELETE FROM countries")
    conn.execute("DELETE FROM genres")
    conn.execute("DELETE FROM directors")

    # 6. Insert main title details
    for _, row in df.iterrows():
        conn.execute(
            """
            INSERT INTO titles
            (show_id, type, title, date_added, release_year,
             rating, duration, description)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                row["show_id"],
                row["type"],
                row["title"],
                row["date_added"] or None,
                int(row["release_year"]) if row["release_year"] else None,
                row["rating"] or None,
                row["duration"] or None,
                row["description"] or None,
            ),
        )

    # 7. Insert countries and title-country relationships
    for _, row in df.iterrows():
        show_id = row["show_id"]
        for country in row["country"].split(","):
            country = country.strip()
            if country and country != "Unknown":
                conn.execute(
                    "INSERT OR IGNORE INTO countries (country_name) VALUES (?)",
                    (country,),
                )
                country_id = conn.execute(
                    "SELECT country_id FROM countries WHERE country_name = ?",
                    (country,),
                ).fetchone()[0]
                conn.execute(
                    """
                    INSERT OR IGNORE INTO title_countries
                    (show_id, country_id) VALUES (?, ?)
                    """,
                    (show_id, country_id),
                )

    # 8. Insert genres and title-genre relationships
    for _, row in df.iterrows():
        show_id = row["show_id"]
        for genre in row["listed_in"].split(","):
            genre = genre.strip()
            if genre:
                conn.execute(
                    "INSERT OR IGNORE INTO genres (genre_name) VALUES (?)",
                    (genre,),
                )
                genre_id = conn.execute(
                    "SELECT genre_id FROM genres WHERE genre_name = ?",
                    (genre,),
                ).fetchone()[0]
                conn.execute(
                    """
                    INSERT OR IGNORE INTO title_genres
                    (show_id, genre_id) VALUES (?, ?)
                    """,
                    (show_id, genre_id),
                )

    # 9. Insert directors and title-director relationships
    for _, row in df.iterrows():
        show_id = row["show_id"]
        for director in row["director"].split(","):
            director = director.strip()
            if director and director != "Unknown":
                conn.execute(
                    "INSERT OR IGNORE INTO directors (director_name) VALUES (?)",
                    (director,),
                )
                director_id = conn.execute(
                    "SELECT director_id FROM directors WHERE director_name = ?",
                    (director,),
                ).fetchone()[0]
                conn.execute(
                    """
                    INSERT OR IGNORE INTO title_directors
                    (show_id, director_id) VALUES (?, ?)
                    """,
                    (show_id, director_id),
                )

    # 10. Save all changes
    conn.commit()

    # 11. Verify row counts
    print("\nRelational data loaded successfully!")
    for table in [
        "titles",
        "countries",
        "title_countries",
        "genres",
        "title_genres",
        "directors",
        "title_directors",
    ]:
        count = conn.execute(
            f"SELECT COUNT(*) FROM {table}"
        ).fetchone()[0]
        print(f"{table}: {count} rows")

    
    # 12. Check foreign key relationships
    violations = conn.execute(
        "PRAGMA foreign_key_check"
    ).fetchall()

    print("\nForeign key check:")
    if violations:
        print("Problems found:", violations)
    else:
        print("All foreign key relationships are valid!")


except Exception:
    conn.rollback()
    raise

finally:
    conn.close()


import pandas as pd
import sqlite3
from pathlib import Path

# Read the transformed dataset
df = pd.read_csv("data/netflix_transformed.csv")

print("Records to load:", len(df))

# Create a folder for the database
Path("database").mkdir(exist_ok=True)

# Connect to the SQLite database
connection = sqlite3.connect("database/netflix.db")

# Load the data into a table
df.to_sql(
    "netflix_titles",
    connection,
    if_exists="replace",
    index=False
)

# Check the number of records loaded
cursor = connection.cursor()
cursor.execute("SELECT COUNT(*) FROM netflix_titles")
total_records = cursor.fetchone()[0]

print("Records loaded into database:", total_records)

# Display the first five records
print("\nFirst five records:")
result = pd.read_sql_query(
    "SELECT show_id, title, type, release_year FROM netflix_titles LIMIT 5",
    connection
)
print(result)

connection.close()

print("\nData loading completed successfully.")

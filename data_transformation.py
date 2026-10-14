
import pandas as pd

# Read the cleaned dataset
df = pd.read_csv("data/netflix_cleaned.csv")

print("Dataset before transformation:", df.shape)

# Convert date_added to datetime
df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")

# Extract year and month when the content was added
df["date_added_year"] = df["date_added"].dt.year
df["date_added_month"] = df["date_added"].dt.month_name()

# Create a column for content age
df["content_age"] = 2026 - df["release_year"]

# Create separate datasets for movies and TV shows
movies = df[df["type"] == "Movie"].copy()
tv_shows = df[df["type"] == "TV Show"].copy()

# Display transformation results
print("\nDataset after transformation:", df.shape)

print("\nMovies:", len(movies))
print("TV Shows:", len(tv_shows))

print("\nNew columns:")
print(df[["title", "date_added_year", "date_added_month", "content_age"]].head())

# Save transformed datasets
df.to_csv("data/netflix_transformed.csv", index=False)
movies.to_csv("data/netflix_movies.csv", index=False)
tv_shows.to_csv("data/netflix_tv_shows.csv", index=False)

print("\nTransformed datasets saved successfully.")


import pandas as pd
from pathlib import Path

Path("data").mkdir(exist_ok=True)

# Read the Netflix dataset
original_df = pd.read_csv("netflix_titles.csv")

# Use 2000 records for the project
df = original_df.head(2000).copy()

df.to_csv("data/netflix_sample.csv", index=False)

print("Original records:", len(original_df))
print("Records used in project:", len(df))
print("Number of columns:", len(df.columns))

print("\nFirst five records:")
print(df.head())

print("\nColumn names:")
print(df.columns.tolist())

print("\nMissing values:")
print(df.isnull().sum())

print("\nMissing values percentage:")
print(((df.isnull().sum() / len(df)) * 100).round(2))

print("\nDuplicate rows:", df.duplicated().sum())
print("Duplicate show IDs:", df["show_id"].duplicated().sum())

print("\nRecords with missing directors:")
missing_directors = df[df["director"].isnull()]
print(missing_directors[["title", "type", "director"]].head(10))

print("\nData types:")
print(df.dtypes)

print("\nContent types:")
print(df["type"].unique())

print("\nContent ratings:")
print(df["rating"].unique())

print("\nSample durations:")
print(df["duration"].dropna().unique()[:20])

print("\nBlank text values:")
for column in df.select_dtypes(include=["object", "string"]).columns:
    blank_count = df[column].str.strip().eq("").sum()
    print(column, ":", blank_count)

print("\nEarliest release year:", df["release_year"].min())
print("Latest release year:", df["release_year"].max())

print("\nMissing durations:", df["duration"].isnull().sum())

df["date_added"] = pd.to_datetime(
    df["date_added"].str.strip(),
    format="%B %d, %Y",
    errors="coerce"
)

print("\nDates after conversion:")
print(df["date_added"].head(10))

print("\nMissing dates after conversion:")
print(df["date_added"].isnull().sum())

print("\nMovies and TV shows:")
print(df["type"].value_counts())

df.to_csv("data/netflix_processed.csv", index=False)

print("\nProcessed data saved successfully.")


import pandas as pd

# Load the original dataset
df = pd.read_csv("netflix_titles.csv")

# Select the first 2,000 rows
df = df.head(2000)

# Save the sample dataset
df.to_csv("data/netflix_sample.csv", index=False)

print(df.head())
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])
print("Column names:", df.columns.tolist())

# Check the number of missing values in each column
print(df.isnull().sum())

# Check the number of duplicate rows
print("Number of duplicate rows:", df.duplicated().sum())


# Display rows where the director is missing
missing_directors = df[df["director"].isnull()]
print(missing_directors[["title", "type", "director"]].head(10))


# Calculate missing values as percentages
missing_percentage = (df.isnull().sum() / len(df)) * 100

print("\nMissing values percentage:")
print(missing_percentage.round(2))


# Check data types of each column
print("\nData types:")
print(df.dtypes)

# Check for duplicate show IDs
print("\nDuplicate show IDs:", df["show_id"].duplicated().sum())


# Check the unique values in the type column
print("\nUnique content types:")
print(df["type"].unique())


# Check unique content ratings
print("\nUnique content ratings:")
print(df["rating"].unique())


# Check unique duration values
print("\nSample duration values:")
print(df["duration"].unique()[:20])

# Check sample date values
print("\nSample date_added values:")
print(df["date_added"].head(10))

# Check blank or whitespace-only values in text columns
print("\nBlank text values:")
for column in df.select_dtypes(include=["str"]).columns:
    blank_count = df[column].str.strip().eq("").sum()
    print(column, ":", blank_count)

# Check release year range
print("\nEarliest release year:", df["release_year"].min())
print("Latest release year:", df["release_year"].max())

# Check missing durations
print("\nMissing duration values:", df["duration"].isnull().sum())
# Convert date_added from text to datetime format
df["date_added"] = pd.to_datetime(
    df["date_added"].str.strip(),
    format="%B %d, %Y",
    errors="coerce"
)

print("\nDate column after conversion:")
print(df["date_added"].head(10))

print("\nInvalid or missing dates after conversion:")
print(df["date_added"].isnull().sum())

# Save the cleaned dataset
df.to_csv("data/netflix_cleaned.csv", index=False)

print("\nCleaned dataset saved successfully.")
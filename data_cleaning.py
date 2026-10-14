
import pandas as pd

# Read the selected 2000 records
df = pd.read_csv("data/netflix_sample.csv")

print("Dataset before cleaning:", df.shape)

# Check missing values before cleaning
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Remove extra spaces from text columns
for column in df.select_dtypes(include=["object", "str"]).columns:
    df[column] = df[column].str.strip()

# Fill missing values
df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")

# Convert date_added into a date format
df["date_added"] = pd.to_datetime(
    df["date_added"],
    format="%B %d, %Y",
    errors="coerce"
)

# Display cleaning results
print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nDataset after cleaning:", df.shape)

# Save the cleaned dataset
df.to_csv("data/netflix_cleaned.csv", index=False)

print("\nCleaned dataset saved successfully.")

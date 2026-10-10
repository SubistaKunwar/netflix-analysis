
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

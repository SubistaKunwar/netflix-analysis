# Netflix Movies and TV Shows Analysis

## About the Project

This is my ETL project using the Netflix Movies and TV Shows dataset from Kaggle. I chose this dataset because it contains information about movies and TV shows, such as their titles, directors, countries, release years, ratings, and genres.

The main purpose of this project is to learn how to work with real-world data using Python, Pandas, and SQL. I am following the ETL process, which involves extracting, cleaning, transforming, and loading data into a database before analyzing it.

## Dataset

- **Dataset:** Netflix Movies and TV Shows
- **Source:** [Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows)
- **Original dataset:** 8,807 rows and 12 columns
- **Working dataset:** 2,000 rows

I selected 2,000 records from the original dataset for this project. I have kept the original dataset unchanged and used the sample for my analysis.

## Tools Used

- Python
- Pandas
- SQLite
- SQL
- Jupyter Notebook
- Git and GitHub

## What I Have Done

### 1. Data Exploration

I started by checking the dataset's size, columns, data types, and missing values. I also explored the distribution of movies and TV shows and checked for duplicate records.

### 2. Data Cleaning

I cleaned the sample dataset using Python and Pandas. I removed duplicate records, trimmed extra spaces from text fields, and filled missing director, cast, and country values with `Unknown`.

### 3. Data Transformation

I added new columns for the year and month when a title was added to Netflix, along with a column showing the difference between the current year used in the analysis and the title's release year. I also separated the movies and TV shows into different CSV files.

### 4. Database Loading

I used SQLite to store the data. I also created relational tables for titles, countries, genres, and directors, with primary keys and foreign keys to connect related records.

### 5. SQL Analysis

I wrote and ran eight SQL reports to explore the dataset. These queries look at content types, release years, ratings, movie durations, the years titles were added, countries, and genres.

## Some Findings

From my sample of 2,000 records, I found that:

- There are 1,305 movies and 695 TV shows.
- TV-MA is the most common rating in the sample.
- 2021 and 2020 are the most frequent release years in the sample.
- The United States has the highest number of titles in the country analysis.
- International Movies is the most common genre category in the genre analysis.

These findings are based on my selected sample, not the entire Netflix dataset.

## Project Files

- `netflix_titles.csv` — Original dataset
- `data/netflix_sample.csv` — Sample of 2,000 records
- `data/netflix_cleaned.csv` — Cleaned dataset
- `data/netflix_transformed.csv` — Transformed dataset
- `data/netflix_movies.csv` — Movies data
- `data/netflix_tv_shows.csv` — TV shows data
- `etl_pipeline.ipynb` — Notebook for exploring and analyzing the data
- `data_cleaning.py` — Data cleaning script
- `data_transformation.py` — Data transformation script
- `data_loading.py` — Loads the transformed data into SQLite
- `load_relational_data.py` — Loads the relational tables
- `sql_analysis.py` — SQL analysis and reports
- `database/netflix.db` — SQLite database
- `database/schema.sql` — Database schema
- `database/queries.sql` — Nine SQL reporting queries
- `database/ERD.md` — ER diagram documentation
- `reports/erd_diagram.png` — ER diagram image

## How to Run the Project

First, activate the virtual environment and install the required packages if they are not already installed.

```bash
source .venv/bin/activate
python -m pip install pandas jupyter
```

Then run the scripts in this order:

```bash
python data_cleaning.py
python data_transformation.py
python data_loading.py
python load_relational_data.py
python sql_analysis.py
```

Both database-loading scripts are included because they load
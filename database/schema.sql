
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS titles (
    show_id TEXT PRIMARY KEY,
    type TEXT NOT NULL,
    title TEXT NOT NULL,
    date_added TEXT,
    release_year INTEGER,
    rating TEXT,
    duration TEXT,
    description TEXT
);

CREATE TABLE IF NOT EXISTS countries (
    country_id INTEGER PRIMARY KEY AUTOINCREMENT,
    country_name TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS title_countries (
    show_id TEXT NOT NULL,
    country_id INTEGER NOT NULL,
    PRIMARY KEY (show_id, country_id),
    FOREIGN KEY (show_id) REFERENCES titles(show_id),
    FOREIGN KEY (country_id) REFERENCES countries(country_id)
);

CREATE TABLE IF NOT EXISTS genres (
    genre_id INTEGER PRIMARY KEY AUTOINCREMENT,
    genre_name TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS title_genres (
    show_id TEXT NOT NULL,
    genre_id INTEGER NOT NULL,
    PRIMARY KEY (show_id, genre_id),
    FOREIGN KEY (show_id) REFERENCES titles(show_id),
    FOREIGN KEY (genre_id) REFERENCES genres(genre_id)
);

CREATE TABLE IF NOT EXISTS directors (
    director_id INTEGER PRIMARY KEY AUTOINCREMENT,
    director_name TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS title_directors (
    show_id TEXT NOT NULL,
    director_id INTEGER NOT NULL,
    PRIMARY KEY (show_id, director_id),
    FOREIGN KEY (show_id) REFERENCES titles(show_id),
    FOREIGN KEY (director_id) REFERENCES directors(director_id)
);

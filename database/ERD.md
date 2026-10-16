
# Netflix ETL Project — Entity Relationship Diagram

This diagram shows how Netflix titles are connected to countries, genres, and directors in the relational database.

```mermaid
erDiagram
    TITLES {
        string show_id PK
        string type
        string title
        string date_added
        int release_year
        string rating
        string duration
        string description
    }

    COUNTRIES {
        int country_id PK
        string country_name
    }

    TITLE_COUNTRIES {
        string show_id PK, FK
        int country_id PK, FK
    }

    GENRES {
        int genre_id PK
        string genre_name
    }

    TITLE_GENRES {
        string show_id PK, FK
        int genre_id PK, FK
    }

    DIRECTORS {
        int director_id PK
        string director_name
    }

    TITLE_DIRECTORS {
        string show_id PK, FK
        int director_id PK, FK
    }

    TITLES ||--o{ TITLE_COUNTRIES : has
    COUNTRIES ||--o{ TITLE_COUNTRIES : includes

    TITLES ||--o{ TITLE_GENRES : has
    GENRES ||--o{ TITLE_GENRES : categorizes

    TITLES ||--o{ TITLE_DIRECTORS : has
    DIRECTORS ||--o{ TITLE_DIRECTORS : directs
```

## Relationships

- **Titles and Countries:** A title can be associated with multiple countries.
- **Titles and Genres:** A title can belong to multiple genres.
- **Titles and Directors:** A title can have multiple directors.
- **Junction tables:** These connect titles with countries, genres, and directors.
- **Primary keys (PK):** Uniquely identify records.
- **Foreign keys (FK):** Connect related records between tables.

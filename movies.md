# FastAPI Movie Filter API 🎥

FastAPI Movie Filter API is a simple API that allows you to retrieve movie data with optional filters. 🍿

## Features 🌟

- 🎞️ Get a list of movies with optional filters like title, release year, and rating.
- 📡 Built with FastAPI and PostgreSQL.

## Getting Started 🚀

1. **Installation**: To get started, install the required Python packages using `pip`.

    ```bash
    pip install fastapi psycopg2-binary
    ```

2. **Database Setup**: Make sure you have a PostgreSQL database set up. Modify the `db_params` dictionary in the code to match your database configuration.

3. **Run the API**: Run the FastAPI application.

    ```bash
    uvicorn your_app_name:app --reload
    ```

4. **Use the API**: Access the API documentation at `http://localhost:8000/docs` and start filtering movies!

## Usage 📝

### Endpoint

- **GET /movies/**: Get a list of movies with optional filters.

#### Query Parameters

- `title` (optional): Filter by movie title.
- `release_year` (optional): Filter by release year.
- `rating` (optional): Filter by rating.

#### Example Request

```http
GET /movies/?title=Avengers&rating=8.0

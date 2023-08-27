from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import List
import psycopg2

# Initialize FastAPI app
app = FastAPI(
    title="ovies API",
    description="An API for retrieving movie data with optional filters.",
    version="1.0",
    openapi_url="/swagger.json",  # Specify the OpenAPI JSON endpoint
    redoc_url="/redoc",  # Endpoint for ReDoc documentation
    docs_url="/swagger",  # Endpoint for Swagger UI
)

# PostgreSQL connection parameters
db_params = {
    "host": "localhost",
    "database": "movies",
    "user": "postgres",
    "password": "5432",
}

# Model to define request parameters for filtering
class MovieFilterParams(BaseModel):
    title: str = None
    release_year: str = None
    rating: str = None

# Function to connect to the PostgreSQL database
def connect_to_db():
    return psycopg2.connect(**db_params)

# Endpoint to get a list of movies with optional filters
@app.get("/movies/", response_model=List[dict], tags=["Movies"])
async def get_movies(
    title: str = Query(None, description="Filter by movie title"),
    release_year: str = Query(None, description="Filter by release year"),
    rating: str = Query(None, description="Filter by rating"),
):
    conn = connect_to_db()
    cur = conn.cursor()

    # Construct the SQL query based on filters
    query = "SELECT * FROM movies WHERE true"
    params = []

    if title:
        query += " AND title ILIKE %s"
        params.append(f"%{title}%")

    if release_year:
        query += " AND release_year = %s"
        params.append(release_year)

    if rating:
        query += " AND rating = %s"
        params.append(rating)

    cur.execute(query, params)
    movies = [
        {"title": row[0], "release_year": row[1], "rating": row[2]}
        for row in cur.fetchall()
    ]

    cur.close()
    conn.close()

    return movies

# Example endpoint for testing purposes
@app.get("/ping", tags=["Health"])
async def ping():
    return {"message": "pong"}

# Run the FastAPI application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

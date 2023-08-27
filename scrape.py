import requests
from bs4 import BeautifulSoup
import psycopg2  # Import psycopg2 library for PostgreSQL database interaction


# Function to scrape movie details from IMDb using BeautifulSoup
def scrape_imdb_movies_by_genre(genre, top_n=10):
    url = f"https://www.imdb.com/search/title/?genres={genre}&sort=year,desc&title_type=feature&num_votes=5000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=04a08fbc-fa0e-4e80-a01f-b6b3b135ecc3&pf_rd_r=58H8ENHTT3B4DXMXNKMT&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_1"

    # Send an HTTP GET request to IMDb
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, "html.parser")
        movie_cards = soup.find_all("div", class_="lister-item")

        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            host="localhost",
            database="movies",
            user="postgres",
            password="5432",
        )

        # Create a cursor
        cur = conn.cursor()

        # Insert scraped data into the database
        for i, movie_card in enumerate(movie_cards[:top_n], start=1):
            title = movie_card.h3.a.text
            year = movie_card.find("span", class_="lister-item-year").text

            # Use error handling to check if rating information exists
            rating_element = movie_card.find("span", class_="ipl-rating-star__rating")
            rating = rating_element.text if rating_element else "N/A"

            # Insert movie data into the database
            cur.execute(
                "INSERT INTO movies (title, release_year, rating) VALUES (%s, %s, %s)",
                (title, year.strip("()"), rating),
            )

        # Commit the changes and close the database connection
        conn.commit()
        conn.close()

    else:
        print("Failed to retrieve data from IMDb")


if __name__ == "__main__":
    print("Scraping IMDb Top 10 Action Movies:")
    scrape_imdb_movies_by_genre("action", 10)

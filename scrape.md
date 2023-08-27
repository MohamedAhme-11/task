# IMDb Movie Scraper 🎬

IMDb Movie Scraper is a Python script that scrapes movie details from IMDb based on genre and stores them in a PostgreSQL database. 🍿

## Features 🌟

- 🎞️ Scrape top-rated movies from IMDb based on genre.
- 📦 Store movie data in a PostgreSQL database.
- 🧐 Use BeautifulSoup for web scraping.

## Getting Started 🚀

1. **Dependencies**: Make sure you have the required Python libraries installed. You can install them using `pip`.

    ```bash
    pip install requests beautifulsoup4 psycopg2-binary
    ```

2. **Database Setup**: Create a PostgreSQL database named "movies" and modify the database connection parameters in the script.

3. **Run the Script**: Execute the script to scrape and store movie data.

    ```bash
    python your_script_name.py
    ```

## Usage 📝

- The script scrapes IMDb's top-rated movies for a specified genre and stores them in the PostgreSQL database.
- You can change the genre and the number of movies to scrape by modifying the function call in the script.

## Database Schema 📊

- The script assumes a PostgreSQL database with a table named "movies" with columns: "title," "release_year," and "rating."

## Contributions and Issues 🤝

Contributions and bug reports are welcome! Feel free to open an issue or submit a pull request on our [GitHub repository](https://github.com/your_repo_url).

## License 📜

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments 🙌

Thanks to IMDb for providing a wealth of movie data! 🙏

Happy movie scraping! 🌟

# MyAnimeList & Quotes Scraper

A collection of Python web scraping tools. 

## Projects Included
1. **Quotes Scraper:** A beginner script that extracts quotes and authors from quotes.toscrape.com.
2. **Anime Finder:** A dynamic CLI tool that scrapes anime from MyAnimeList based on genre and page number.

## Anime Finder Features
- Dynamic genre searching (Action, Comedy, Romance, etc.)
- Pagination support (scrape page 1, 2, or 15 to find hidden gems)
- Extracts Title, Score, Image URL, and Synopsis
- Saves output to beautifully formatted JSON files
- Includes polite delay (`time.sleep`) to respect server limits

## How to Use
1. Install requirements: `pip install requests beautifulsoup4`
2. Run the script: `python anime_scraper.py`
3. Enter a genre (e.g., `romance`) and a page number (e.g., `5`).
import requests
import time
import json
import os
from bs4 import BeautifulSoup

genre_dict = {
    "action": 1,
    "adventure": 2,
    "comedy": 4,
    "drama": 8,
    "fantasy": 10,
    "romance": 22,
    "sci-fi": 24,
    "slice of life": 36,
    "sports": 30,
    "supernatural": 37
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

while True:
    user_genre = input("What genre do you want to scrape? ('quit' to exit): ").lower().strip()

    if user_genre == "quit":
        print("Goodbye!")
        break

    if user_genre in genre_dict:
        genre_id = genre_dict[user_genre]

        page_input = input("Which page? (Press enter for page 1. or type 2, 3, etc.): ")
        page_num = page_input if page_input.isdigit() else "1"
        search_url = f"https://myanimelist.net/anime/genre/{genre_id}/{user_genre.title()}?page={page_num}"

        file_name = f"{user_genre.replace(' ', '_')}_page_{page_num}_anime.json"
        file_path = os.path.join(os.path.dirname(__file__), file_name)

    else:
        print("Genre not found.")
        continue

    response = requests.get(search_url, headers=headers)

    print(f"Status code: {response.status_code}")

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        titles = soup.select("h2.h2_anime_title > a")

        final_anime_list = []

        for link_tag in titles[:5]:
            name = link_tag.text.strip()
            link = link_tag['href']

            if name:
                print(f"Scraping details for {name}...")

                anime_response = requests.get(link, headers=headers)

                if anime_response.status_code == 200:
                    anime_soup = BeautifulSoup(anime_response.text, "html.parser")

                    score_div = anime_soup.find("div", class_="score-label")
                    score = score_div.text.strip() if score_div else "N/A"

                    synopsis_p = anime_soup.find("p", itemprop="description")
                    synopsis = synopsis_p.text.strip() if synopsis_p else "No synopsis available."

                    image_tag = anime_soup.find("img", itemprop="image")
                    image_url = image_tag['data-src'] if image_tag else "No image found."
                    anime_data = {
                        "name": name,
                        "image": image_url,
                        "score": score,
                        "synopsis": synopsis,
                        "link": link
                    }

                    final_anime_list.append(anime_data)
                    print(f"  -> Score: {score}")
                    if image_url != "No image found.":
                        print("  -> Image: Found")
                    else:
                        print("  -> Image: Missing")

                time.sleep(1)
                print("-" * 30)

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(final_anime_list, f, indent=2, ensure_ascii=False)

        print(f"\nSuccessfully saved {len(final_anime_list)} {user_genre} animes with full detail!")
    else:
        print("Failed to connect.")
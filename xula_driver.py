from urllib import response
from imdbData2 import IMDB
import re
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from requests import get
import lxml
import requests
from Movie import Movie

def main():
    #ascii art added by @cwhitexula29
    print(r"""
 __     __    __     _____     ______        ______   ______     ______      __    __     ______     __   __   __     ______     ______    
/\ \   /\ "-./  \   /\  __-.  /\  == \      /\__  _\ /\  __ \   /\  == \    /\ "-./  \   /\  __ \   /\ \ / /  /\ \   /\  ___\   /\  ___\   
\ \ \  \ \ \-./\ \  \ \ \/\ \ \ \  __<      \/_/\ \/ \ \ \/\ \  \ \  _-/    \ \ \-./\ \  \ \ \/\ \  \ \ \'/   \ \ \  \ \  __\   \ \___  \  
 \ \_\  \ \_\ \ \_\  \ \____-  \ \_____\       \ \_\  \ \_____\  \ \_\       \ \_\ \ \_\  \ \_____\  \ \_/     \ \_\  \ \_____\  \/\_____\ 
  \/_/   \/_/  \/_/   \/____/   \/_____/        \/_/   \/_____/   \/_/        \/_/  \/_/   \/_____/   \/_       \/_/   \/_____/   \/_____/ 
                                                                                                                                           
          """)
    print("Welcome to the IMDB Top Movies Data Driver!")
    print()
    
    def get_centennial_campaign_impact(url):
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/118.0.5993.90 Safari/537.36"
            ),
            "Referer": "https://www.google.com/",
            "Accept-Language": "en-US,en;q=0.9",
        }

        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        campaign_header = soup.find(
            lambda tag: tag.get_text(strip=True).upper() == "CAMPAIGN IMPACT"
        )

        impact_paragraphs = []
        if campaign_header:
            for sibling in campaign_header.find_all_next():
                if sibling.name in ["h2", "h3"]:
                    break

                if sibling.name in ["p", "span", "div"]:
                    text = sibling.get_text(strip=True)
                    if text and len(text.split()) > 5:  
                        impact_paragraphs.append(text)
                        break  
        if not impact_paragraphs:
            impact_paragraphs = ["Campaign impact text not found."]

        title_tag = soup.find("h1")
        title_text = title_tag.get_text(strip=True) if title_tag else "No title found"

        return {
            "title": title_text,
            "impact_text": impact_paragraphs,
            "source_url": url,
        }












    campaign_data = get_centennial_campaign_impact("https://www.xula.edu/about/centennial.html")

    print(f"{campaign_data['title']}: {campaign_data['impact_text']}\n")

    
    csv_path = "Movie_Data.csv"
    df = pd.read_csv(csv_path)

    print("Welcome to the IMDB Top Movies Data Display!")
    print()
    user_input = input('What would you like see?(Type "Title", "Date", "Runtime", "Genre", "Rating", "Metascore", "Description", "Director", "Stars", "Votes", "Gross"): ')
    print("You selected:", user_input)

    all_movies = []


    for html_content in df['html']:
        imdb_page = IMDB(html_content)
        movie_df = imdb_page.movieData()
        all_movies.append(movie_df)
    

    full_df = pd.concat(all_movies, ignore_index=True)
    print("Here is our movie data for ", user_input + ":")
    print(full_df[user_input].to_string(index=False))

    specific_input = input('Would you like to see a specific movie's data? (yes/no): ').strip().lower()
    if specific_input == 'yes':
        movie_title = input('Enter the movie title: ').strip()
        specific_movie = full_df[full_df['Title'].str.lower() == movie_title.lower()]
        if not specific_movie.empty:
            print(specific_movie.to_string(index=False))
        else:
            print("Movie not found.")

    #random movie feature added by @cwhitexula29
    from random_movie import RandomMovie

    random_movie = RandomMovie(full_df)
    suggestion = random_movie.get_random_movie()

    print("\n🎬 Random Movie Suggestion 🎬")
    print(f"{suggestion['Title']} ({suggestion['Date']}) - {suggestion['Genre']} | Rating: {suggestion['Rating']}")

    
if __name__ == "__main__":
    main()

    
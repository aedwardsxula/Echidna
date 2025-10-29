from imdbData2 import IMDB
import re
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from requests import get
import lxml

def main():

    #TODO: The Tester must create and call a function that scrapes the Centennial 
    # Campaign Impact from XULA's website.
    
    def get_centennial_campaign_impact(url):

        url="https://www.xula.edu/centennial/campaign-impact"
        response = get(url, timeout=10)
        response.raise_for_status()  

        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.find("h1")
        title_text = title.get_text(strip=True) if title else "No title found"

        paragraphs = [p.get_text(strip=True) for p in soup.find_all("p")]
        impact_paragraphs = [p for p in paragraphs if "impact" in p.lower() or "campaign" in p.lower()]

        if not impact_paragraphs:
            impact_paragraphs = paragraphs[:3]  
        return {
            "title": title_text,
            "impact_text": impact_paragraphs,
            "source_url": url
        }

    
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
    
if __name__ == "__main__":
    main()
from imdbData2 import IMDB
import re
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from requests import get
import lxml
from Movie import Movie

def main():

    #TODO: The Tester must create and call a function that scrapes the Centennial 
    # Campaign Impact from XULA's website.
    
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

    
if __name__ == "__main__":
    main()
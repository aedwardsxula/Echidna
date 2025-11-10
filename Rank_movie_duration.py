import pandas as pd
from imdbData2 import IMDB 

class RankMovieDuration:
    def __init__(self, csv_file):
        self.df_raw = pd.read_csv(csv_file)
        self.movies_df = self._extract_movie_data()

    def _extract_movie_data(self):
        all_movies = []

        for html_content in self.df_raw["html"]:
            imdb_page = IMDB(html_content)
            df_movie = imdb_page.movieData()  
            all_movies.append(df_movie)

        return pd.concat(all_movies, ignore_index=True)

    def rank_by_duration(self, top_n=10):
        df = self.movies_df.copy()

        df["Runtime"] = pd.to_numeric(df["Runtime"], errors="coerce")
        df = df.dropna(subset=["Runtime"])

        ranked_movies = df.sort_values(by="Runtime", ascending=False)

        return ranked_movies[["Title", "Date", "Runtime", "Genre", "Rating"]].head(top_n)

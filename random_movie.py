import random


class RandomMovie:
    def __init__(self, movies_df):
        self.movies_df = movies_df

    def get_random_movie(self):
        if self.movies_df.empty:
            return ValueError("The movies DataFrame is empty.")
            
        random_index = random.randint(0, len(self.movies_df) - 1)
        movie_info = self.movies_df.iloc[random_index]

        return{
            "Title": movie_info.get("Title", "N/A"),
            "Date": movie_info.get("Date", "N/A"),
            "Genre": movie_info.get("Genre", "N/A"),
            "Director": movie_info.get("Director", "N/A"),
            "Rating": movie_info.get("Rating", "N/A"),
        }
   
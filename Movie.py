
class Movie:
    def __init__(self, title, year, rating, genre, metascore, director):
        self.title = title
        self.year = year
        self.rating = rating
        self.genre = genre
        self.metascore = metascore
        self.director = director
    def __str__(self):
        return f"{self.title} ({self.year}) - Rating: {self.rating}, Genre: {self.genre}, Metascore: {self.metascore}, Director: {self.director}"

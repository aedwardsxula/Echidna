
class Movie:
    def __init__(self, title, year, rating, genre, metascore, director):
        self.title = title
        if year < 0:
            raise ValueError("Year cannot be negative")
        self.year = year
        if not 0 <= rating <= 10:
            raise ValueError("Rating must be between 0 and 10")
        self.rating = rating
        self.genre = genre
        if not 0 <= metascore <= 100:
            raise ValueError("Metascore must be between 0 and 100")
        self.metascore = metascore
        self.director = director
    def __str__(self):
        return f"{self.title} ({self.year}) - Rating: {self.rating}, Genre: {self.genre}, Metascore: {self.metascore}, Director: {self.director}"

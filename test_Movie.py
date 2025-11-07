import unittest
import requests
from Movie import Movie

class TestMovie(unittest.TestCase):

    def test_movie_initialization(self):
        """Test 1: Verify that a Movie object is initialized correctly."""
        movie = Movie("Inception", 2010, 8.8, "Sci-Fi", 74, "Christopher Nolan")
        
        self.assertEqual(movie.title, "Inception")
        self.assertEqual(movie.year, 2010)
        self.assertEqual(movie.rating, 8.8)
        self.assertEqual(movie.genre, "Sci-Fi")
        self.assertEqual(movie.metascore, 74)
        self.assertEqual(movie.director, "Christopher Nolan")

    def test_movie_str_representation(self):
        """Test 2: Verify the string representation of a Movie object."""
        movie = Movie("The Matrix", 1999, 8.7, "Action", 73, "The Wachowskis")
        expected_str = "The Matrix (1999) - Rating: 8.7, Genre: Action, Metascore: 73, Director: The Wachowskis"
        
        self.assertEqual(str(movie), expected_str)

    def test_movie_year_validation(self):
        """Test 3: Verify that movie year cannot be negative."""
        with self.assertRaises(ValueError):
            movie = Movie("Test Movie", -2000, 7.0, "Drama", 70, "Test Director")
    
    def test_movie_rating_range(self):
        """Test 4: Verify that movie rating must be between 0 and 10."""
        with self.assertRaises(ValueError):
            movie = Movie("Test Movie", 2023, 11.5, "Drama", 70, "Test Director")
        with self.assertRaises(ValueError):
            movie = Movie("Test Movie", 2023, -1.0, "Drama", 70, "Test Director")
    
    def test_movie_multiple_genres(self):
        """Test 5: Verify that movie can handle multiple genres."""
        movie = Movie("Inception", 2010, 8.8, "Sci-Fi, Action, Thriller", 74, "Christopher Nolan")
        self.assertIn("Sci-Fi", movie.genre)
        self.assertIn("Action", movie.genre)
        self.assertIn("Thriller", movie.genre)
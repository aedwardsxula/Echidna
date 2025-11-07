import unittest
from suggest_movie import SuggestMovie

class TestSuggestMovie(unittest.TestCase):

    def setUp(self):
        self.movie_list = ["Inception", "Avatar", "Titanic"]
        self.suggester = SuggestMovie(self.movie_list.copy())
    
    def test_suggest_random_movie(self):
        result = self.suggester.suggest_random()
        self.assertIn(result, self.movie_list, "Suggested movie should be from the list")

    def test_add_movie(self):
        self.suggester.add_movie("Interstellar")
        self.assertIn("Interstellar", self.suggester.get_all_movies(), "New movie should be added")

    
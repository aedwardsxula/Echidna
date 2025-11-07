import unittest
from unittest import result
import pandas as pd
from director_file import DirectorFilter

class TestDirectorFilter(unittest.TestCase):

    def setUp(self):
        self.data = pd.DataFrame({
        "Title": ["Inception", "Interstellar", "Tenet", "Dunkirk", "Pulp Fiction", "Jackie Brown"],
        "Director": ["Christopher Nolan", "Christopher Nolan","Christopher Nolan","Christopher Nolan","Quentin Tarantino","Quentin Tarantino"],
        "Genre": ["Action", "Sci-Fi", "Thriller", "War", "Crime", "Drama"],
        "Rating": [8.8, 8.6, 7.4, 7.9, 8.9, 7.5]
    })
        self.filter = DirectorFilter(self.data)


    def test_filter_valid_director(self):
        data = {
            "Title": ["Inception", "Interstellar", "Dunkirk"],
            "Director": ["Christopher Nolan", "Christopher Nolan", "Someone Else"]
        }
    
        df = pd.DataFrame(data)
        filter_obj = DirectorFilter(df)
        result = filter_obj.filter_by_director("Christopher Nolan")
        self.assertEqual(len(result), 2)
        self.assertTrue(all(result["Director"] == "Christopher Nolan"))

    def test_filter_director_not_found(self):
        df = pd.DataFrame({
            "Title": ["Titanic", "Avatar"],
            "Director": ["James Cameron", "James Cameron"]
        })
        filter_obj = DirectorFilter(df)

        result = filter_obj.filter_by_director("Steven Spielberg")

        self.assertIsInstance(result, str)
        self.assertIn("No movies found", result)

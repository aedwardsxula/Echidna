import unittest
import pandas as pd
from unittest.mock import patch
from Rank_movie_duration import RankMovieDuration

class MockIMDB:
    def __init__(self, html):
        self.html = html

    def movieData(self):
        return pd.DataFrame([{
            "Title": "Mock Movie",
            "Date": "2025",
            "Runtime": "120",
            "Genre": "Drama",
            "Rating": "8.2"
        }])

class TestRankMovieDuration(unittest.TestCase):

    @patch("Rank_movie_duration.IMDB", MockIMDB)
    def setUp(self):
        self.mock_df = pd.DataFrame({
            "html": ["<html></html>", "<html></html>", "<html></html>"]
        })
        self.mock_df.to_csv("test_movies.csv", index=False)

    @patch("Rank_movie_duration.IMDB", MockIMDB)
    def test_initialization_creates_dataframe(self):
        """Test that the class initializes and extracts a non-empty DataFrame."""
        ranker = RankMovieDuration("test_movies.csv")
        self.assertFalse(ranker.movies_df.empty)
        self.assertIn("Runtime", ranker.movies_df.columns)

    @patch("Rank_movie_duration.IMDB", MockIMDB)
    def test_rank_by_duration_returns_sorted_movies(self):
        """Test that movies are sorted by runtime descending."""
        ranker = RankMovieDuration("test_movies.csv")
        result = ranker.rank_by_duration(top_n=1)
        self.assertEqual(len(result), 1)
        self.assertEqual(result.iloc[0]["Title"], "Mock Movie")

    @patch("Rank_movie_duration.IMDB", MockIMDB)
    def test_handles_missing_runtime(self):
        """Test that missing or invalid runtimes are dropped."""
        ranker = RankMovieDuration("test_movies.csv")
        ranker.movies_df.loc[0, "Runtime"] = None
        result = ranker.rank_by_duration()
        self.assertTrue(result["Runtime"].notna().all())

    @patch("Rank_movie_duration.IMDB", MockIMDB)
    def test_top_n_limit(self):
        """Test that top_n parameter limits results."""
        ranker = RankMovieDuration("test_movies.csv")
        result = ranker.rank_by_duration(top_n=2)
        self.assertEqual(len(result), min(2, len(ranker.movies_df)))

    @patch("Rank_movie_duration.IMDB", MockIMDB)
    def test_raises_error_if_runtime_column_missing(self):
        """Test that KeyError is raised if Runtime column is missing."""
        ranker = RankMovieDuration("test_movies.csv")
        del ranker.movies_df["Runtime"]
        with self.assertRaises(KeyError):
            ranker.rank_by_duration()



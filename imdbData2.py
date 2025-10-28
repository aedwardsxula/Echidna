#please run this file 
import re
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from requests import get
import lxml


class IMDB:
    """Scrape IMDb movie and TV series data using BeautifulSoup."""

    def __init__(self, html_content):
        """Initialize with raw HTML (from file or web)."""
        self.soup = BeautifulSoup(html_content, 'lxml')

    def bodyContent(self):
        """Return all movie/series containers."""
        content = self.soup.find(id="main")
        if content:
            return content.find_all("div", class_="lister-item mode-advanced")
        return []

    def movieData(self):
        """Extract and return movie/series data from the page."""
        movieFrame = self.bodyContent()

        movieTitle = []
        movieDate = []
        movieRunTime = []
        movieGenre = []
        movieRating = []
        movieScore = []
        movieDescription = []
        movieDirector = []
        movieStars = []
        movieVotes = []
        movieGross = []

        for movie in movieFrame:
            movieFirstLine = movie.find("h3", class_="lister-item-header")
            movieTitle.append(movieFirstLine.find("a").text)
            movieDate.append(re.sub(r"[()]", "", movieFirstLine.find_all("span")[-1].text))

            # Runtime
            try:
                movieRunTime.append(movie.find("span", class_="runtime").text[:-4])
            except Exception:
                movieRunTime.append(np.nan)

            # Genre
            try:
                genre_text = movie.find("span", class_="genre").text.rstrip().replace("\n", "")
                movieGenre.append(genre_text.split(","))
            except Exception:
                movieGenre.append(np.nan)

            # Rating
            try:
                movieRating.append(movie.find("strong").text)
            except Exception:
                movieRating.append(np.nan)

            # Metascore
            try:
                movieScore.append(movie.find("span", class_="metascore unfavorable").text.rstrip())
            except Exception:
                movieScore.append(np.nan)

            # Description
            try:
                movieDescription.append(movie.find_all("p", class_="text-muted")[-1].text.lstrip())
            except Exception:
                movieDescription.append(np.nan)

            # Cast
            movieCast = movie.find("p", class_="")
            try:
                casts = movieCast.text.replace("\n", "").split('|')
                casts = [x.strip() for x in casts]
                casts = [casts[i].replace(j, "") for i, j in enumerate(["Director:", "Stars:"])]
                movieDirector.append(casts[0])
                movieStars.append([x.strip() for x in casts[1].split(",")])
            except Exception:
                movieDirector.append(np.nan)
                movieStars.append(np.nan)

            # Votes & Gross
            movieNumbers = movie.find_all("span", attrs={"name": "nv"})
            if len(movieNumbers) == 2:
                movieVotes.append(movieNumbers[0].text)
                movieGross.append(movieNumbers[1].text)
            elif len(movieNumbers) == 1:
                movieVotes.append(movieNumbers[0].text)
                movieGross.append(np.nan)
            else:
                movieVotes.append(np.nan)
                movieGross.append(np.nan)

        movieData = {
            "Title": movieTitle,
            "Date": movieDate,
            "Runtime": movieRunTime,
            "Genre": movieGenre,
            "Rating": movieRating,
            "Metascore": movieScore,
            "Description": movieDescription,
            "Director": movieDirector,
            "Stars": movieStars,
            "Votes": movieVotes,
            "Gross": movieGross,
        }

        return pd.DataFrame(movieData)



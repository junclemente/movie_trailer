class Movie():
    """Create a class Movie

    Attributes:
        title (str): title of the movie
        year (str): release year of movie
        poster (str):  URL to the movie poster image
        trailer (str): URL to the movie trailer which must be found on YouTube
    """
    def __init__(self, title, year, poster, trailer):
        """Initiates an instance and sends a message to console"""
        print("Create instance of class Movie for: " + title)
        self.title = title
        self.year = year
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer

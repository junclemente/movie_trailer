class Movie():
    """Create a class Movie

    Keyword arguments:
    title -- title of the movie
    year -- release year of movie
    poster -- URL to the movie poster
    trailer -- URL to the movie trailer from YouTube
    """
    def __init__(self, title, year, poster, trailer):
        print("Create instance of class Movie for: " + title)
        self.title = title
        self.year = year
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer

    def show_doc(self):
        print(self.__doc__)

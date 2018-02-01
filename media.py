import webbrowser


class movie():
    """
    This class stores the information about the trailers.
    """
    def __init__(
                self, movie_title, movie_storyline,
                poster_image, youtube_trailer):
        """This function contains an instances of the class movie.
        All arguments are related to instance variables.
        The function takes the following arguments:
            movie_title
            movie_storyline
            poster_image
            youtube_trailer
        And returns:
            an instance of choosen movie."""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_trailer

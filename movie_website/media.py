import webbrowser


# the Movie object
class Movie():
    valid_ratings = ['G', 'PG', 'PG-13', 'R']

    def __init__(self, movie_title, movie_description, movie_poster_url, movie_youtube_url):
        self.title = movie_title
        self.description = movie_description
        self.poster_image_url = movie_poster_url
        self.trailer_youtube_url = movie_youtube_url

# the function to call to visualize the trailers in the webpage
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

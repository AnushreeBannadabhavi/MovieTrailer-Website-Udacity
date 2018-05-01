import webbrowser


class Movie():
    def __init__(self,
                 title=None,
                 poster_image=None,
                 youtube_url=None):
        self.title = title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_url

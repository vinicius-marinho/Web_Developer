import webbrowser

class Movie():

    VALID_RATINGS = ["G", "PG", "PG-13", "R"] #Esta variavel esta declarada assim por se tratar de uma constante Ela e uma variavel de classe e nao e inicializada com nenhum objeto



    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube


    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


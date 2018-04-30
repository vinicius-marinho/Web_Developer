import webbrowser


class Movie(object):

    """
       Atributos:
        title = titulo do filme
        storyline = sinopse do filme, um breve resumo
        poster_image_url = link para a imagem de um poster do filme
        trailer_youtube_url = link para o trailer no youtube
       Funcao show_trailer:
         mostra o trailer do objeto especificado.
        """

    def __init__(self, movie_title, movie_storyline, poster_image, trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

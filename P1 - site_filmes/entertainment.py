# importando os modulos que contem a classe(media) e o arquivo fresh_tomatoes
import media
import fresh_tomatoes

# Criando os objetos da classe media. Aqui crio os objetos dos meus filmes favoritos
Toy_story = media.Movie("Toy Story 3",
                        "Os brinquedos tentam escapar de uma enrascada",
                        "https://images-na.ssl-images-amazon.com/images/I/519fFTj6QnL._SY450_.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

Wick = media.Movie("John Wick",
                   "Mataram seu cachorro, agora ele vai se vingar",
                   "https://images-na.ssl-images-amazon.com/images/I/41i2SoUoRjL.jpg",
                   "https://www.youtube.com/watch?v=C0BMx-qxsP4")

King_lion = media.Movie("Rei Leao",
                        "Historia de Simba, e de como ele se tornou rei",
                        "https://img.elo7.com.br/product/original/146CF3B/o-rei-leao-poster-arte.jpg",
                        "https://www.youtube.com/watch?v=pY9P04JhdFk")

Cap_2 = media.Movie("Capitao America 2 - O Soldado Invernal",
                    "Capitao America enfrenta a Hydra e descobre o Soldado Invernal",
                    "http://br.web.img3.acsta.net/r_1280_720/pictures/14/01/31/18/27/343470.jpg",
                    "https://www.youtube.com/watch?v=rik1VguOKf4")

Superman = media.Movie("Homem de Aco",
                       "Clark Kent se tranforma no superman",
                       "https://i1.wp.com/heroisx.com/wp-content/uploads/2013/07/manofsteel-novoposter07.jpg?ssl=1",
                       "https://www.youtube.com/watch?v=Bgi8Ud7IJJ4")

Up = media.Movie("Up Altas Aventuras",
                 "Uma historia de amizade e uma casa voadora",
                 "https://http2.mlstatic.com/poster-up-altas-aventuras-5-D_NQ_NP_13929-MLB140510878_1195-O.jpg",
                 "https://www.youtube.com/watch?v=yADAYe9efE0")

# Crio uma lista onde coloco todos os meus objetos
movies = [Toy_story, Wick, King_lion, Cap_2, Superman, Up]

# Chamo a funcao open_movie_page passando como argumento a minha lista. Essa funcao gera a pagina html.
fresh_tomatoes.open_movies_page(movies)





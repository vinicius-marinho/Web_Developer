import media
import fresh_tomatoes

# Nas linhas abaixos, objetos contendo as informacoes dos filmes sao criados
Toy_story = media.Movie("Toy Story 3",
                        "Os brinquedos tentam escapar de uma enrascada",
                        "https://images-na.ssl-images-amazon" +
                        ".com/images/I/519fFTj6QnL._SY450_.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

Wick = media.Movie("John Wick",
                   "Mataram seu cachorro, agora ele vai se vingar",
                   "https://images-na.ssl-images-amazon." +
                   "com/images/I/41i2SoUoRjL.jpg",
                   "https://www.youtube.com/watch?v=C0BMx-qxsP4")

King_lion = media.Movie("Rei Leao",
                        "Historia de Simba, e de como ele se tornou rei",
                        "https://img.elo7.com.br/product/original/" +
                        "146CF3B/o-rei-leao-poster-arte.jpg",
                        "https://www.youtube.com/watch?v=OH_9AdaxtfE")

Cap_2 = media.Movie("Capitao America 2 - O Soldado Invernal",
                    "Capitao America enfrenta segredos do passado",
                    "http://br.web.img3.acsta.net/r_1280_720" +
                    "/pictures/14/01/31/18/27/343470.jpg",
                    "https://www.youtube.com/watch?v=rik1VguOKf4")

Superman = media.Movie("Homem de Aco",
                       "Clark Kent se tranforma no superman",
                       "https://i1.wp.com/heroisx.com/wp-content/uploads/" +
                       "2013/07/manofsteel-novoposter07.jpg?ssl=1",
                       "https://www.youtube.com/watch?v=Bgi8Ud7IJJ4")

Up = media.Movie("Up Altas Aventuras",
                 "Uma historia de amizade e uma casa voadora",
                 "https://http2.mlstatic.com/poster-up-altas-aventuras" +
                 "-5-D_NQ_NP_13929-MLB140510878_1195-O.jpg",
                 "https://www.youtube.com/watch?v=yADAYe9efE0")

# Os objetos criados sao em uma lista para que possam popular a pagina web.
movies = [Toy_story, Wick, King_lion, Cap_2, Superman, Up]

# A funcao abaixo gera a pagina html, tendo como argumento a lista criada acima
fresh_tomatoes.open_movies_page(movies)

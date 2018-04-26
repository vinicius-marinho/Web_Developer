import media
import fresh_tomatoes



Toy_story = media.Movie("Toy Story", "Uma historia de amizade", "https://i0.wp.com/www.cinemadebuteco.com.br/wp-content/uploads/2015/08/Poster-Toy-Story-1995.jpg?fit=1373%2C2048&ssl=1",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

Wick = media.Movie("John Wick", "Mataram seu cachorro, agora ele vai se vingar", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQAYFFy0iJITORmZ8XChPrbGrZcgrNoJe5K0zQSHy-gH_1F2Em6dA",
                   "https://www.youtube.com/watch?v=C0BMx-qxsP4")

King_lion = media.Movie("Rei leao", "Historia de Simba, e de como ele se tornou rei",
                        "https://img.elo7.com.br/product/original/146CF3B/o-rei-leao-poster-arte.jpg",
                        "https://www.youtube.com/watch?v=pY9P04JhdFk")

Cap_2 = media.Movie("Capitao America 2 - O Soldado Invernal", "Capitao America enfrenta a Hydra e descobre o Soldado Invernal",
                    "data:image/jpeg;base64,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",
                    "https://www.youtube.com/watch?v=rik1VguOKf4")

Superman = media.Movie("Homem de Aco", "Clark Kent se tranforma no superman",
                       "https://http2.mlstatic.com/poster-cinema-decoraco-superman-o-homem-de-aco-cartaz-porta-D_NQ_NP_621382-MLB25714646580_062017-F.jpg",
                       "https://www.youtube.com/watch?v=Bgi8Ud7IJJ4")
movies = [Toy_story, Wick, King_lion, Cap_2, Superman]

# fresh_tomatoes.open_movies_page(movies)
# print(media.Movie.VALID_RATINGS)

print(media.Movie.__module__)
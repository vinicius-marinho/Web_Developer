import media
import webbrowser


Toy_story = media.Movie("Toy Story", "Uma historia de amizade", "https://i0.wp.com/www.cinemadebuteco.com.br/wp-content/uploads/2015/08/Poster-Toy-Story-1995.jpg?fit=1373%2C2048&ssl=1",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

print(Toy_story.story)
webbrowser.open(Toy_story.trailer)
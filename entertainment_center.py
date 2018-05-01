import media
import fresh_tomatoes

# Creating instances of Class movie to represent few favorite movies
toy_story = media.Movie("ToyStory",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

inside_out = media.Movie("Inside Out",
                         "https://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_%282015_film%29_poster.jpg",  # NOQA
                         "https://www.youtube.com/watch?v=1HFv47QHWJU")

shaw_redem = media.Movie("The Shawshank Redemption",
                         "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",  # NOQA
                         "https://www.youtube.com/watch?v=NmzuHjWmXOc")  # NOQA

avengers_in = media.Movie("Avengers: Infinity War",
                          "https://upload.wikimedia.org/wikipedia/en/4/4d/Avengers_Infinity_War_poster.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=6ZfuNTqbHE8&t=52s")  # NOQA

inception = media.Movie("Inception",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=YoHD9XEInc0")

coco_anim = media.Movie("Coco",
                        "https://upload.wikimedia.org/wikipedia/en/9/98/Coco_%282017_film%29_poster.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=bvomHFZO0mk")

# Store the above Movie objects in a list.
movies = [coco_anim, avengers_in, shaw_redem, inception, inside_out, toy_story]

# Open the movie website in the user's browser featuring the movies above.
fresh_tomatoes.open_movies_page(movies)

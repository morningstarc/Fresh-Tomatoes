import fresh_tomatoes
import movie

# instantiate movie objects
titanic = movie.Movie("Titanic",
                      "A seventeen-year-old aristocrat falls in love with a kind"
                      ", but poor artist aboard the luxurious, ill-fated R.M.S."
                      " Titanic.",
                      "titanic.jpg",
                      "https://youtu.be/kVrqfYjkTdQ")

inception = movie.Movie("Inception",
                        "A thief, who steals corporate secrets through use of "
                        "dream-sharing technology, is given the inverse task of "
                        "planting an idea into the mind of a CEO.",
                        "inception.jpg",
                        "https://youtu.be/8hP9D6kZseM")

departed = movie.Movie("The Departed",
                       "An undercover cop and a mole in the police attempt to "
                       "identify each other while infiltrating an Irish gang in "
                       "South Boston.",
                       "departed.jpg",
                       "https://youtu.be/auYbpnEwBBg")

shutter_island = movie.Movie("Shutter Island",
                             "A U.S Marshal investigates the disappearance of a "
                             "murderess who escaped from a hospital for the "
                             "criminally insane.",
                             "shutter_island.jpg",
                             "https://youtu.be/qdPw9x9h5CY")

gatsby = movie.Movie("The Great Gatsby",
                     "A writer and wall street trader, Nick, finds himself drawn"
                     " to the past and lifestyle of his millionaire neighbor, "
                     "Jay Gatsby.",
                     "great_gatsby.jpg",
                     "https://youtu.be/sN183rJltNM")

body_of_lies = movie.Movie("Body of Lies",
                           "A CIA agent on the ground in Jordan hunts down a "
                           "powerful terrorist leader while being caught between"
                           " the unclear intentions of his American supervisors "
                           "and Jordan Intelligence.",
                           "body_of_lies.jpg",
                           "https://youtu.be/A4noCwwEUBA")

# create a list of movie objects for the fresh_tomatoes file to import
movies = [inception, departed, shutter_island, gatsby, titanic, body_of_lies]
# open the file to create the web page passing the movies list
fresh_tomatoes.open_movies_page(movies)

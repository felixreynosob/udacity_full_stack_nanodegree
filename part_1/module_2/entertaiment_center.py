import media 
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A Story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Toy_Story.svg/1920px-Toy_Story.svg.png",
                        "https://www.youtube.com/watch?v=f33yJZ5uOpU")


avatar = media.Movie("Avatar",
                    "A marine on an alien planet",
                    "https://i.pinimg.com/originals/17/aa/71/17aa718c1ab15b482505b8431cf596fc.jpg",
                    "https://www.youtube.com/watch?v=6ziBFh3V1aM")

avengers = media.Movie("Avengers",
                    "The best superheroes movie ever. From marvel studios",
                    "https://i.pinimg.com/originals/17/aa/71/17aa718c1ab15b482505b8431cf596fc.jpg",
                    "https://www.youtube.com/watch?v=6ziBFh3V1aM")             

hunger_games = media.Movie("Toy Story",
                        "A Story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Toy_Story.svg/1920px-Toy_Story.svg.png",
                        "https://www.youtube.com/watch?v=f33yJZ5uOpU")


pokemon = media.Movie("Avatar",
                    "A marine on an alien planet",
                    "https://i.pinimg.com/originals/17/aa/71/17aa718c1ab15b482505b8431cf596fc.jpg",
                    "https://www.youtube.com/watch?v=6ziBFh3V1aM")

earth = media.Movie("Avengers",
                    "The best superheroes movie ever. From marvel studios",
                    "https://i.pinimg.com/originals/17/aa/71/17aa718c1ab15b482505b8431cf596fc.jpg",
                    "https://www.youtube.com/watch?v=6ziBFh3V1aM")

movies = [toy_story,
          avatar,
          avengers,
          hunger_games,
          pokemon, earth]

fresh_tomatoes.open_movies_page(movies)
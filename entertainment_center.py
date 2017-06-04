import fresh_tomatoes
import media

# 3 Movie objects
toy_story = media.Movie("Toy Story", "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar", "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

bahubali = media.Movie("Bahubali", "https://upload.wikimedia.org/wikipedia/en/7/7e/Baahubali_poster.jpg",
                       "https://www.youtube.com/watch?v=sOEg_YZQsTI")

# created a list of Movie objects
movies = [toy_story, avatar, bahubali]

fresh_tomatoes.open_movies_page(movies)

import fresh_tomatoes
import media

toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his boys that come to life",
    "http://cdn.collider.com/wp-content/uploads/toy-story-poster1.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie(
    "Avatar",
    "A marine on an alien Planet",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

the_dark_knight = media.Movie(
    "The Dark Knight",
    "This is the Joker's court, and he's not looking for a laugh",
    "http://www.gstatic.com/tv/thumb/movieposters/173378/p173378_p_v8_aa.jpg",
    "https://www.youtube.com/watch?v=EXeTwQWrcwY")

avengers = media.Movie(
    "The Avengers",
    ("Earth's mightiest heroes must come together and learn to fight as a"
     "team if they are to stop the mischievous Loki and his alien army"),
    ("http://t1.gstatic.com/images?q=tbn:ANd9GcTp0qlAoWcOOswIkL"
     "_qpjYzJqCCDmWXiBzCXiqbE43Obo8c0Z-s"),
    "https://www.youtube.com/watch?v=eOrNdBpGMv8")

ratatouille = media.Movie(
    "Ratatouille",
    ("a rat named Remy dreams of becoming a great chef despite his family's"
     " wishes and the obvious problem of being a rat in a decidedly"
     " rodent-phobic profession."),
    "http://www.gstatic.com/tv/thumb/dvdboxart/165058/p165058_d_v8_aa.jpg",
    "https://www.youtube.com/watch?v=md_eEM9BWd8")

fantastic_beasts = media.Movie(
    "Fantastic Beasts",
    "The adventures of writer Newt Scamander in New York",
    ("http://t3.gstatic.com/images?q=tbn:ANd9GcTjr1HJSeba_"
     "PuPr9f8eWrr6ldbqSP22tGjGQ5tvfwH6B02jIon"),
    "https://www.youtube.com/watch?v=Vso5o11LuGU")

movies = [
    toy_story,
    avatar,
    the_dark_knight,
    avengers,
    ratatouille,
    fantastic_beasts]

fresh_tomatoes.open_movies_page(movies)

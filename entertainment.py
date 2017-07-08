import fresh_tomatoes
import media

# List of movie titles with poster image and trailer

the_other_guys = media.Movie("The Other Guys", "http://img.moviepostershop.com/the-other-guys-movie-poster-2010-1020545762.jpg", "https://www.youtube.com/watch?v=D6WOoUG1eNo")

star_wars_ep3 = media.Movie("Star Wars Episode 3", "http://t0.gstatic.com/images?q=tbn:ANd9GcT7TlfhiJ93841oYulGpyJZ3YULcgzah1CGumaVQuZ3-zXarfai", "https://www.youtube.com/watch?v=MR1xo1tLyBk")

step_brothers = media.Movie("Step Brothers", "http://www.gstatic.com/tv/thumb/movieposters/175884/p175884_p_v8_ag.jpg", "https://www.youtube.com/watch?v=ANjenc4W1_Q")

american_psycho = media.Movie("American Psycho", "http://t1.gstatic.com/images?q=tbn:ANd9GcR42NIX4d1J7ehsoZ9jAQoI04YS9Cz0cohVJvKkKLo7PVz7jj1B", "https://www.youtube.com/watch?v=5YnGhW4UEhc")

office_space = media.Movie("Office Space", "http://www.gstatic.com/tv/thumb/movieposters/22554/p22554_p_v8_aa.jpg", "https://www.youtube.com/watch?v=dMIrlP61Z9s")

die_hard = media.Movie("Die Hard", "http://www.gstatic.com/tv/thumb/movieposters/10255/p10255_p_v8_ar.jpg", "https://www.youtube.com/watch?v=2TQ-pOvI6Xo")


movies = [the_other_guys, star_wars_ep3, step_brothers, american_psycho, office_space, die_hard]

fresh_tomatoes.open_movies_page(movies)
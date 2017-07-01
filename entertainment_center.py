import fresh_tomatoes
import media

'''
This file contains all the information that will be displayed on the
"Movie Trailer Website" in the file fresh_tomatoes.html.

To add your own movies, or edit the movies shown, you must create (or edit) an
instance of the class Movie which takes four inputs:
movie_name = media.Movie("movie title", "movie release year",
                         "URL to movie poster image",
                         "URL to movie trailer on YouTube")
'''
hackers = media.Movie("Hackers",
                      "1995",
                      "http://www.impawards.com/1995/posters/hackers_ver1.jpg",
                      "https://youtu.be/c32Vt8IDf5s")

glory = media.Movie("Glory",
                    "1989",
                    "http://www.impawards.com/1989/posters/glory_ver1.jpg",
                    "https://youtu.be/5aEMfD36V_Q")

star_wars_iv = media.Movie("Star Wars: Episode IV - A New Hope",
                           "1997",
                           "http://www.impawards.com/1977/posters/star_wars_ver8.jpg",  # NOQA
                           "https://youtu.be/1g3_CFmnU7k")

outbreak = media.Movie("Outbreak",
                       "1995",
                       "http://www.impawards.com/1995/posters/outbreak.jpg",
                       "https://youtu.be/Y5povsMKfT4")

twenty_eight_days_later = media.Movie("28 Days Later...",
                                      "2002",
                                      "http://www.impawards.com/2003/posters/twenty_eight_days_later.jpg",  # NOQA
                                      "https://youtu.be/c7ynwAgQlDQ")

harry_potter_i = media.Movie("Harry Potter and the Sorcerer's Stone",
                             "2001",
                             "http://www.impawards.com/2001/posters/harry_potter_and_the_sorcerers_stone_ver4.jpg",  # NOQA
                             "https://youtu.be/PbdM1db3JbY")

wonder_woman = media.Movie("Wonder Woman",
                           "2017",
                           "http://www.impawards.com/2017/posters/wonder_woman.jpg",  # NOQA
                           "https://youtu.be/VSB4wGIdDwo")

power_rangers = media.Movie("Power Rangers",
                            "2017",
                            "http://www.impawards.com/2017/posters/power_rangers_ver22.jpg",  # NOQA
                            "https://youtu.be/5kIe6UZHSXw")

pirates_of_the_carribean = media.Movie("Pirates of the Caribbean:"
                                       " The Curse of the Black Pearl",
                                       "2003",
                                       "http://www.impawards.com/2003/posters/pirates_of_the_caribbean_ver3.jpg",  # NOQA
                                       "https://youtu.be/naQr0uTrH_s")

transformers = media.Movie("Transformers",
                           "2007",
                           "http://www.impawards.com/2007/posters/transformers.jpg",  # NOQA
                           "https://youtu.be/dxQxgAfNzyE")

independence_day = media.Movie("ID4: Independence Day",
                               "1996",
                               "http://www.impawards.com/1996/posters/independence_day_ver1.jpg",  # NOQA
                               "https://youtu.be/B1E7h3SeMDk")

straight_outta_compton = media.Movie("Straight Outta Compton",
                                     "2015",
                                     "http://www.impawards.com/2015/posters/straight_outta_compton.jpg",  # NOQA
                                     "https://youtu.be/OrlLcb7zYmw")

top_gun = media.Movie("Top Gun",
                      "1986",
                      "http://www.impawards.com/1986/posters/top_gun.jpg",
                      "https://youtu.be/qAfbp3YX9F0")

fast_and_the_furious = media.Movie("The Fast and the Furious",
                                   "2001",
                                   "http://www.impawards.com/2001/posters/fast_and_the_furious.jpg",  # NOQA
                                   "https://youtu.be/ZsJz2TJAPjw")

tokyo_drift = media.Movie("The Fast and the Furious: Tokyo Drive",
                          "2006",
                          "http://www.impawards.com/2006/posters/fast_and_the_furious_tokyo_drift.jpg",  # NOQA
                          "https://youtu.be/p8HQ2JLlc4E")

fools_rush_in = media.Movie("Fools Rush In",
                            "1997",
                            "http://www.impawards.com/1997/posters/fools_rush_in_ver2.jpg",  # NOQA
                            "https://youtu.be/Yquko-yY55E")

resident_evil = media.Movie("Resident Evil",
                            "2002",
                            "http://www.impawards.com/2002/posters/resident_evil_ver4.jpg",  # NOQA
                            "https://youtu.be/PWUT4CXWcwQ")

stick_it = media.Movie("Stick It",
                       "2006",
                       "http://www.impawards.com/2006/posters/stick_it.jpg",
                       "https://youtu.be/Ib48djESKGU")

the_descent = media.Movie("The Descent",
                          "2005",
                          "http://www.impawards.com/2006/posters/descent_ver3.jpg",  # NOQA
                          "https://youtu.be/WhZj0Q9rq9E")

moana = media.Movie("Moana",
                    "2016",
                    "http://www.impawards.com/2016/posters/moana.jpg",
                    "https://youtu.be/LKFuXETZUsI")

little_mermaid = media.Movie("The Little Mermaid",
                             "1989",
                             "http://www.impawards.com/1989/posters/little_mermaid_ver2.jpg",  # NOQA
                             "https://youtu.be/ZGZX5-PAwR8")

movie_list = [hackers, glory, star_wars_iv, outbreak, twenty_eight_days_later,
              harry_potter_i, wonder_woman, power_rangers,
              pirates_of_the_carribean, transformers, independence_day,
              straight_outta_compton, top_gun, fast_and_the_furious,
              tokyo_drift, fools_rush_in, resident_evil, stick_it, the_descent,
              moana, little_mermaid]

fresh_tomatoes.open_movies_page(movie_list)

import fresh_tomatoes
import media
toy_story = media.Movie("toy Story",
                        "A story of a boy and his toy that come in his life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https:www.youtube.com/watch?v=vwyZH85NQC4")
#print(toy_story.storyline)
avatar = media.Movie("Avatar",
                     "A marine on a alien planet",
                     "https://upload.wikimedia.org/wikipedia/sco/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")
#print(avatar.storyline)
#avatar.show_trailer()
school_of_rock = media.Movie("School of Rock", "Using rock to learn",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "http://www.youtube.com/watch?v=3PsUJFEBC74")
ratatouille = media.Movie("Ratatouille", "A rat is a chef in Paris",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "http://www.youtube.com/watch?v=c3sBBRxDAqk")
midnight_in_paris = media.Movie("Midnight in Paris", "Going back in time to meet authors",
                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "http://www.youtube.com/watch?v=atLg2wQQxvU")
hunger_games = media.Movie("Hunger Games", "A really real reality show",
                         "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                         "http://www.youtube.com/watch?v=PbA63a7H0bo")
gangs_of_wasseypur = media.Movie("Gangs of Wasseypur","A gangster (Manoj Bajpayee) clashes with the ruthless,coal-mining kingpin (Tigmanshu Dhulia) who killed his father (Jaideep Ahlawat)",
                                 "https://upload.wikimedia.org/wikipedia/en/6/6a/Gangs_of_Wasseypur_poster.jpg",
                                 "https://www.youtube.com/watch?v=j-AkWDkXcMY")
Manjhi_The_Mountain_Man = media.Movie("Manjhi: The Mountain Man","After his wife passes away trying to cross a mountain, Manjhi, out of sheer rage, sets out on a quest to carve a road through the mammoth peak.",
                                      "https://upload.wikimedia.org/wikipedia/en/4/4f/Manjhi_The_Mountain_Man_-_Poster.jpg",
                                      "https://www.youtube.com/watch?v=I9KAoTQlEWs")
titanic = media.Movie("Titanic","Seventeen-year-old Rose hails from an aristocratic family and is set to be married. When she boards the Titanic, she meets Jack Dawson, an artist, and falls in love with him.",
                      "https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg",
                      "https://www.youtube.com/watch?v=zCy5WQ9S4c0")
movies = {toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games,gangs_of_wasseypur,Manjhi_The_Mountain_Man,titanic}
fresh_tomatoes.open_movies_page(movies)
                          

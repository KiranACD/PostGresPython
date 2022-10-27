class Movie:
    def __init__(self, title, release_date, watched):
        self.title = title
        self.release_date = release_date

class User:
    def __init__(self, user, watched_movies):
        self.user = user
        self.watched_movies = watched_movies
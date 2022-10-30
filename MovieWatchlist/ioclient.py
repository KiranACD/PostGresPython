import datetime
from moviedatamodel import Movie

class IOClient:

    @staticmethod
    def get_movie_input():
        title = input('Movie title: ')
        release_date = input('Release date (dd-mm-yyyy): ')
        print()
        release_date = datetime.datetime.strptime(release_date, '%d-%m-%Y').timestamp()
        movie = Movie(title, release_date, 0)
        return movie
    
    @staticmethod
    def get_watched_movie():
        movie_id = input('Enter the id of the movie you have watched: ')
        return movie_id
    
    @staticmethod
    def get_username():
        username = input('Username: ')
        return username
    
    @staticmethod
    def get_search_term():
        search_term = input('Enter the search term: ')
        return search_term

    @staticmethod
    def show_movies(heading, movies):
        print(f'-- {heading} movies --')
        for movie in movies:
            date = datetime.datetime.fromtimestamp(movie["release_timestamp"]).strftime('%b %d %Y')
            print(f'{movie["id"]}: {movie["title"]} (on {date})\n')
    
    @staticmethod
    def show_watched_movies(username, movies):
        print(f"-- {username}'s watched movies --")
        for movie in movies:
            print(f'{movie}')
    

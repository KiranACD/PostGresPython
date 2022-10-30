from dbclient import DBClient
from ioclient import IOClient
import datetime

menu = '''Welcome to the watchlist app!

Please select one of the following options:

1. Add new movie
2. View upcoming movies
3. View all movies
4. Add watched movie
5. View watched movies
6. Register in the app
7. Search for a movie
8. Exit

Your selection: '''

welcome = 'Welcome to the movie watchlist app!'

# ioclient = IOClient()
filename = 'MovieWatchlist.db'
# #dbclient = DbClient('list')
dbclient = DBClient('sqlite', filename=filename)

print(welcome)
print()

while True:
    user_input = input(menu)
    print()
    if user_input == '8':
        exit()
    elif user_input == '1':
        movie = IOClient.get_movie_input()
        dbclient.insert_movie(movie)
    elif user_input == '2':
        today_timestamp = datetime.datetime.today().timestamp()
        query = 'upcoming_movies'
        movies = dbclient.fetch_movies(query=query)
        IOClient.show_movies('upcoming', movies)
    elif user_input == '3':
        query = 'movies'
        movies = dbclient.fetch_movies(query=query)
        IOClient.show_movies('all', movies)
    elif user_input == '4':
        username = IOClient.get_username()
        movie_title = IOClient.get_watched_movie()
        movie = dbclient.fetch_movies(query='movie_id', movie_name=movie_title)
        try:
            movie_id = movie[0]['id']
        except Exception as e:
            print(e)
            print(f'Movie {movie_title} not in database!')
            print()
            continue
        release_date = movie[0]['release_timestamp']
        if release_date > datetime.datetime.today().timestamp():
            print(f'Movie {movie_title} not yet released!')
            print()
            continue
        dbclient.watch_movie(username, movie_id)
    elif user_input == '5':
        sql_query = 'watched_movies'
        username = IOClient.get_username()
        movies = dbclient.fetch_movies(query=sql_query, username=username)
        IOClient.show_movies(username, movies)
    elif user_input == '6':
        username = IOClient.get_username()
        dbclient.insert_user(username)
    elif user_input == '7':
        search_term = IOClient.get_search_term()
        movies = dbclient.search_movies(search_term)
        if movies:
            IOClient.show_movies('Matching', movies)
        else:
            print(f'Found no movies for search term: {search_term}')
    else:
        print(f'Invalid option! {user_input}')
        print()
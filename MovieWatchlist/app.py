from dbclient import DBClient
import datetime

menu = '''Welcome to the watchlist app!

Please select one of the following options:

1. Add new movie
2. View upcoming movies
3. View all movies
4. Add watched movie
5. View watched movies
6. Register in the app
7. Exit

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
    if user_input == 6:
        exit()
    elif user_input == 1:
        pass
    elif user_input == 2:
        today_timestamp = datetime.datetime.today().timestamp()
        condition = 'release_timestamp > ?'
        dbclient.fetch_movies(where=condition)
    elif user_input == 3:
        pass
    elif user_input == 4:
        pass
    elif user_input == 5:
        pass
    else:
        print(f'Invalid option! {user_input}')
        print()
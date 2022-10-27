import sqlite3
import datetime

class SQLite:
    queries = {'create_movies_table':'CREATE TABLE IF NOT EXISTS movies (id INTEGER PRIMARY KEY, title TEXT, release_timestamp REAL);',
               'movies':'SELECT * FROM movies;',
               'insert_movies':'INSERT INTO movies (title, release_timestamp) VALUES(?, ?);',
               'upcoming_movies':'SELECT * FROM movies WHERE release_timestamp > ?;',
               'watched_movies':'SELECT * FROM watched WHERE watcher_name = ?;',
               'delete_movie':'DELETE FROM movies WHERE title = ?;',
               'create_users_table': 'CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY;',
               'create_watched_table':'CREATE TABLE IF NOT EXISTS watched (user_username TEXT, movie_id INTEGER, FOREIGN KEY(user_username) REFERENCES users(username), FOREIGN KEY(movie_id) REFERENCES movies(id));',
               'insert_watched_movie':'INSERT INTO watched (user_username, movie_id INTEGER) VALUES(?, ?);'}

    def __init__(self, filename):
        self.filename = filename
        self.connect()
        self.create_movies_table()
        self.create_watched_table()
        
    def connect(self):
        self.connection = sqlite3.connect(self.filename)
    
    def create_movies_table(self):
        sql_query = SQLite.queries['create_movies_table']
        with self.connection:
            self.connection.execute(sql_query)

    def create_watched_table(self):
        sql_query = SQLite.queries['create_watched_table']
        with self.connection:
            self.connection.execute(sql_query)

    def insert_movie(self, movie):
        sql_query = SQLite.queries['insert_movies']
        with self.connection:
            self.connection.execute(sql_query, (movie.title, movie.release_date))
    
    def fetch_movies(self, query=None, username=None):
        if query == 'movies':
            sql_query = SQLite.queries['movies']
            cursor = self.connection.execute(sql_query)
            data = self.convert_movies_data_to_output_format(cursor)
        elif query == 'upcoming_movies':
            sql_query = SQLite.queries[query]
            cursor = self.connection.execute(sql_query, (datetime.datetime.today().timestamp(),))
            data = self.convert_movies_data_to_output_format(cursor)
        elif query == 'watched_movies':
            sql_query = SQLite.queries[query]
            cursor = self.connection.execute(sql_query, (username,))
            data = self.convert_user_data_to_output_format(cursor)
        return data
    
    def watch_movie(self, username, title):
        delete_sql_query = SQLite.queries['delete_movie']
        insert_sql_query = SQLite.queries['insert_watched_movie']
        with self.connection:
            self.connection.execute(delete_sql_query, (title,))
            self.connection.execute(insert_sql_query, (username, title))
    
    def convert_movies_data_to_output_format(self, data):
        return_data = []
        for d in data:
            data_dict = {}
            data_dict['title'] = d[0]
            data_dict['release_timestamp'] = d[1]
            return_data.append(data_dict)
        return return_data
    
    def convert_user_data_to_output_format(self, data):
        return_movies_data = []
        for d in data:
            print(d)
            return_movies_data.append(d[1])
        return return_movies_data
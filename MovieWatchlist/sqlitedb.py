import sqlite3

class SQLite:
    def __init__(self, filename):
        self.filename = filename
        self.connect()
        self.create_movies_table()
        
    def connect(self):
        self.connection = sqlite3(self.filename)
    
    def create_movies_table(self):
        with self.connection:
            self.connection.execute('CREATE TABLE IF NOT EXISTS movies (title TEXT, release_timestamp REAL, watched INTEGER);')

    def insert_movie(self, movie):
        with self.connection:
            self.connection.execute('INSERT INTO movies (title, release_timestamp, watched) VALUES(?, ?, 0);', (movie.title, movie.release_date))
    
    def fetch_movies(self, where=[]):
        query = f'SELECT * FROM movies'
        if where:
            condition = ' '.join(where)
            query += f' WHERE {condition};'
        cursor = self.connection.execute(query)
        data = self.convert_data_to_output_format(cursor)
        return data
    
    def convert_data_to_output_format(self, data):
        return_data = []
        for d in data:
            data_dict = {}
            data_dict['title'] = d[0]
            data_dict['release_timestamp'] = d[1]
            data_dict['watched'] = d[2]
            return_data.append(data_dict)
        return return_data
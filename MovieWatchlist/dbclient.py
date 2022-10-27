from dbfactory import DBFactory

class DBClient:
    def __init__(self, db_type, filename=None):
        self.db_instance = DBFactory.get_db_instance(db_type, filename=filename)
    
    def insert_movie(self, movie):
        self.db_instance.insert_movie(movie)
    
    def fetch_movies(self, query=None, username=None):
        data = self.db_instance.fetch_movies(query=query, username=username)
        return data
    
    def watch_movie(self, username, title):
        self.db_instance.watch_movie(username, title)
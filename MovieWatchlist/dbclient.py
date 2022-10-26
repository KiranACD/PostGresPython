from dbfactory import DBFactory

class DBClient:
    def __init__(self, db_type, filename=None):
        self.db_instance = DBFactory.get_db_instance(db_type, filename=filename)
    
    def insert_movie(self, movie):
        self.db_instance.insert_movie(movie)
    
    def fetch_movies(self, where=[]):
        data = self.db_instance.fetch_movies(where=where)
        return data
    
    def watch_movie(self, title):
        pass
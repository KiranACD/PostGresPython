from dbfactory import DBFactory

class DBClient:
    def __init__(self, db_type, filename=None):
        self.db_instance = DBFactory.get_db_instance(db_type, filename=filename)
    
    def insert_movie(self, movie):
        self.db_instance.insert_movie(movie)
    
    def fetch_movies(self, query=None, username=None, movie_name=None):
        data = self.db_instance.fetch_movies(query=query, username=username, movie_name=movie_name)
        return data
    
    def watch_movie(self, username, title):
        self.db_instance.watch_movie(username, title)
    
    def insert_user(self, username):
        self.db_instance.insert_user(username)
    
    def search_movies(self, search_term):
        data = self.db_instance.search_movies(search_term)
        return data
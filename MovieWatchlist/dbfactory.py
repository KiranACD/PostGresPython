from sqlitedb import SQLite
class DBFactory:
    @staticmethod
    def get_db_instance(db_type, filename=None):
        if db_type == 'sqlite':
            return SQLite(filename)

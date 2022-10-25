from sqlitedb import SqliteDb
from listdb import ListDb

class DbFactory:
    @staticmethod
    def get_db_instance(db_name, filename=None):
        if db_name == 'sqlite':
            return SqliteDb(filename)
        elif db_name == 'list':
            return ListDb()
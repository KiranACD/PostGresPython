from listdb import ListDb
from sqlitedb import SqliteDb

class DbFactory:
    @staticmethod
    def get_db_instance(db_name):
        if db_name == 'list':
            return ListDb()
        elif db_name == 'sqlite':
            return SqliteDb()
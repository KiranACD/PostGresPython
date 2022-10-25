from dbfactory import DbFactory

class DbClient:
    def __init__(self, db_type, filename=None):
        self.db_instance = DbFactory.get_db_instance(db_type, filename=filename)
        self.db_instance.connect()

    def add_entry(self, entry):
        self.db_instance.insert(entry)

    def fetch_entries(self):
        dbdata = self.db_instance.fetch()
        return dbdata

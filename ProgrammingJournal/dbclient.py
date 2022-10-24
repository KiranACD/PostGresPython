from dbfactory import DbFactory

class DbClient:
    def __init__(self, db_type):
        self.db_instance = DbFactory.get_db_instance(db_type)
    

    def add_entry(self, entry):
        self.db_instance.insert(entry)

    def fetch_entries(self):
        dbdata = self.db_instance.fetch()
        return dbdata

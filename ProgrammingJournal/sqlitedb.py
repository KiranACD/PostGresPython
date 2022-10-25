import sqlite3
from entrymodel import EntryModel

class SqliteDb:
    def __init__(self, filename):
        self.filename = filename
        self.connect()
        self.create_table()
    
    def connect(self):
        self.connection = sqlite3.connect(self.filename)
    
    def create_table(self):
        with self.connection:
            self.connection.execute(f'CREATE TABLE IF NOT EXISTS entries (content TEXT, date TEXT);')

    def insert(self, entry):
        with self.connection:
            # self.connection.execute(f"INSERT INTO {self.entries_table} VALUES ('{entry.content}', '{entry.date}');")
            self.connection.execute("INSERT INTO entries VALUES (?, ?);", (entry.content, entry.date))

    def fetch(self):
        cursor = self.connection.execute("SELECT * FROM entries;")
        data = self.convert_data_to_output_format(cursor)
        return data
    
    def convert_data_to_output_format(self, data):
        return_data = []
        for d in data:
            data_dict = {}
            data_dict['content'] = d[0]
            data_dict['date'] = d[1]
            return_data.append(data_dict)
        return return_data
 

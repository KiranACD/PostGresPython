from entrymodel import EntryModel

class IOClient:
    @staticmethod
    def get_entry():
        entry_content = input('Make your entry: ')
        entry_date = input('Enter the date: ')
        print()
        entry = EntryModel(entry_content, entry_date)
        return entry
    
    @staticmethod
    def show_data(data):
        for entry in data:
            print(f'{entry["date"]}\n{entry["content"]}\n\n')
    

from ioclient import IOClient
from dbclient import DbClient
from listdb import ListDb

menu = '''Please select one of the following options:
1. Add new entry
2. View entries
3. Exit

Your selection: '''
welcome = 'Welcome to the programming diary'
ioclient = IOClient()
filename = 'JournalEntry.db'
#dbclient = DbClient('list')
dbclient = DbClient('sqlite', filename=filename)
print(welcome)
print()
while True:
    user_input = input(menu)
    print()
    if user_input == '3':
        exit()
    elif user_input == '1':
        entry = ioclient.get_entry()
        dbclient.add_entry(entry)
    elif user_input == '2':
        entries = dbclient.fetch_entries()
        ioclient.show_data(entries)
    else:
        print(f'Invalid option {user_input}')
        print()


    
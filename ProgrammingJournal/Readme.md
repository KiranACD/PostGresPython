# Programming Journal App using SQLlite as Database

## Features

1. Add new entries 
2. view existing entries

## Workflow

When users run the app, they will see a quick welcome. Then the three options in the menu.
```
Welcome to the programming diary

Please select one of the following options:
1. Add new entry
2. View entries
3. Exit

Your selection:
```

If user presses 1, we ask them for the date and contents of the entry. These are two seperate entries.
```
What have you learned today?:

Enter the date:
```

If the user presses 2, we will show them the entry. We will show them the date and content of the entry.

After the user performs the acton after making a selection, the whole process will be repeated till the user selects 3 to exit the app.

## SQL

SQL stands for Structured Query Language. It is used to interact with relational database management systems (RDBMS). SQL is meant to be similar to English. An example of an SQL query used to find some data in a table.
```
SELECT first_name, surname FROM users;
```
This query finds data pertaining to users as the query contains 'FROM users' and we are selecting the first name and surname of each user.

To insert data into a table, we run the following query
```
INSERT INTO users (first_name, surname) VALUES ('John', 'Smith');
```
We specified the table that we want put the data in, then the columns that we want to insert into and the values that we are inserting.

## Relational Databases

They are large, complex and powerful. Databases are constructed primarily from tables. Tables have columns and zero or more rows. 
Its called relational database because multiple tables are used together. For example
```
first_name  |   surname                  holder       |   number
   John          Smith                  Anne Pun          8375841
   Rolf          Smith               Robert Baratheon     1343545
   Anne          Pun                    John Smith        9586859
   Robert        Baratheon              Rolf Smith        1234567
```

The two tables are related to each other.

```
id  |   first_name  |   surname                  id     |   holder_id   |   holder      |   number
1          John          Smith                    1            3            Anne Pun      8375841
2          Rolf          Smith                    2            4         Robert Baratheon  1343545
3          Anne          Pun                      3            1            John Smith    9586859 
4          Robert        Baratheon                4            2            Rolf Smith     1234567
```

In both tables we have id. In the second table, we have the id from the users table too as given in the users column. This allows us to get rid of the holder column.
```
id  |   first_name  |   surname                  id     |   holder_id   |   number
1          John          Smith                    1            3            8375841
2          Rolf          Smith                    2            4            1343545
3          Anne          Pun                      3            1            9586859 
4          Robert        Baratheon                4            2            1234567
```

We design tables by deciding the pieces of data that can be stored in a table with its own meaning and then reference those tables from other places.

## Python Lists as a Database Table

Lists and database tables are similar. Both are used to store individual items. Inside a database table, we store rows of data. Each row can have multiple pieces of data, one per column. Inside a list, we can store dictionaries. Each dictionary can have multiple pieces of data as well.

A sample dictionary that we might store.
```
entries = [
    {'content': 'Today I started learning programming.', 'date':'01-01-2020'},
    {'content': 'I created my first SQLite database.', 'date':'02-01-2020'},
    {'content': 'I finished writing my programming diary application', 'date':'03-01-2020'},
    {'content': 'I started learning Postgres database.', 'date':'04-01-2020'},
]
```

Initially the list will be empty. We create a dictionary everytime a new entry is created.

The database client file has the following code.
```
entries = []

def add_entry():
    entry_content = input('What have you learned today?: ')
    entry_date = input('Enter the date: ')
    print()
    entries.append({'content':entry_content, 'date':entry_date})


def view_entries():
    for entry in entries:
        print(f'{entry["date"]}\n{entry["content"]}\n\n')
```

The add_entry function does 2 things. It collects data and then stores the data. Similarly the view_entries function does 2 things as well. It retrieves data and then shows the data. This violates the single responsibility principle.

## SQLite DataBase

### Installation
Install sqlite browser by going to https://sqlitebrowser.org/dl/.

### Queries
Once open, you can create a new database. Give it a name like 'newdb.db'. Then, find the create table button and click on it to create a table.

Create table SQL query/command
```
CREATE TABLE accounts (name TEXT, number TEXT);
```
The name of the table is accounts. There are two columns name and number. Both of them are of the TEXT datatype.

SQLite has 5 major datatypes: INTEGER, TEXT, BLOB (unstructured data), REAL, NUMERIC

The 'IF NOT EXISTS' clause is used when creating tables as SQLite throws an error when we try to create table that exists.

### Connecting to db using Python

Import the module. Then connect to the data file. If the data file does not already exist when you try to connect, this will create one. When connected, you can execute SQL queries.

```
import sqlite3
connection = sqlite3.connect('data.db')
connection.execute('CREATE TABLE entries (content TEXT, date TEXT);')
connection.close()
```

We can put this in a function called create_table
```
def create_table():
    connection = sqlite3.connect('data.db')
    connection.execute('CREATE TABLE entries (content TEXT, date TEXT);')
    connection.close()
```

When we call this function to create a table, we open a connection to the db file and then create a table and close the connection. We can open a connection to write or read data into and from a db file and close it any number of times. However, we must note that, if there are multiple connections at the same time, only one connection can write to the database at a time. 

In our case, the programming journal will be a single user console app, so none of the database operations will try to access the db file at the same time. A single connection is enough. We create a connection once and use this single connection for all our database operations. 

### Transactions

We can run multiple queries together in a transaction. Queries run in the order that we specify. All queries must success, else none will. If any query fails, all changes made till that point will be reversed. Therefore. transaction allow us to group related queries, so we are sure they all happen together successfully.

Transactions can either be committed or rolled back. Committing saves the database changes permanently, so they will be available to read later. Rolling back undoes the changes, as if nothing happened in the transaction. These are the two end states of a transaction. When we dont commit or rollback, the transaction is rolled back by default.

Every time we call connection.execute(), a transaction is created. As we have not been committing the changes up till now, none of them are saved and they are automatically rolled back.

There are 2 ways to commit transactions. We can do connection.commit() after executing a query. We can use a context manager to automatically perform the commit operation at the end.

```
def create_table():
    connection.execute('CREATE TABLE entries (content TEXT, date TEXT);')
    connection.commit()
```

```
def create_table():
    with connection:
        connection.execute('CREATE TABLE entries (content TEXT, date TEXT);')
```

### Cursor

A cursor is a structure that allows us to traverse a result set. Database cursors allow the database to only load results when required. Specifically, in SQLite, cursor loads all the data up front, and helps us go over each piece. In effect, SQLite cursor helps us iterate over the data.

```
connection = sqlite3.connect('data.db')
cursor = connection.cursor()
cursor.execute('SELECT * FROM users;')

for row in cursor:
    print(row)
connection.close()
```

We can use cursor for inserting data into table as well.
```
connection = sqlite3.connect('data.db')
cursor = connection.cursor()
cursor.execute('INSERT INTO users ('John Smith', 35);')
connection.close()
```

Using cursor when we dont have to iterate may seem pointless, but we do it to maintain consistency between both read and write operations. We dont have to use cursor while inserting data. We can run the insert query through the connection.execute() function. This function creates a cursor to perform the operation by default.

In general, we can create a cursor when we need to iterate over data. We dont need to create one to make tables and to insert data.

### Inserting Data

```
INSERT INTO users (first_name, surname) VALUES ('Rolf', 'Smith');
```
INSERT INTO - This tells the database we want to add data to table users.
(first_name, surname) - These are the columns we want to add data too. If we leave it empty, data will be inserted to all columns.
VALUES ('Rolf', 'Smith') - This tells the database what values we want to insert in the columns specified. If we skipped columns, we will need to provide values for all columns.

### SQL Injection Attacks

if we use f'string in the query string and use user input in it, then we potentially open the database to users possibly injecting SQL queries which will be executed. This is not what we want. An example of this is
```
connection.execute(f"INSERT INTO table_name VALUES ('{value1}', '{value2}');")
```

SQLite provides a way out of this. We can instead use the following
```
connection.execute("INSERT INTO table_name VALUES (?, ?);",(value1, value2))
```

When your programs are coded in such a way that users can execute any SQL code they want, without accessing your database directly.
Consider a username search app and in the console the app asks us to enter the username. Someone could enter ''; DROP TABLE users;. Then SQLite would run
```
SELECT * FROM users WHERE first_name = ''; DROP TABLE users;
```
At this point, these are 2 seperate queries and the second query will drop our tabe if it is name users.


### Selecting and Retrieving Data

```
SELECT column1, column2 FROM table_name;
```
SELECT - Tells the database we want to find and retrieve data.
column1, column2 - Specifies the columns that we want to retrieve data from.
FROM - The table we want to retrieve data from.

```
connection.execute("SELECT * FROM entries;")
```
This creates a cursor, loads the data into the cursor and returns the cursor.
```
cursor = connection.execute("SELECT * FROM entries;")
```
This is the same as
```
cursor = connection.cursor()
cursor.execute("SELECT * FROM entries;")
```
The cursor now points at the first row of the data. If you want fetch that row, then we can do
```
cursor.fetchone()
```
This returns the data at the first row. The pointer then moves to the second row.

If we want to get all the data
```
cursor.fetchall()
```
Takes all the data and puts it into a list and returns it.

### Filtering

To apply filters while retrieving data, we use the WHERE clause.
```
SELECT * FROM user WHERE first_name = 'John';
SELECT * FROM user WHERE age > 18;
SELECT * FROM user WHERE salary < 35000;
SELECT * FROM user WHERE surname != 'Smith;
```
### Comparison Operators

< - lower than, > - greater than, <= - lower than or equal to, >= - greater than or equal to, = equal to, != - not equal to.

### Multiple Comparisons

Using AND and OR, we can chain comparisons logically.
```
SELECT * FROM user WHERE years_experience > 10 AND salary < 35000;
```

We can group comparisons with brackets
```
SELECT * FROM user WHERE age >= 65 OR (years_experience > 10 AND salary < 35000);
```
The comparison in the bracket will evaluate first.

### Dropping table

```
DROP TABLE table_name;
```

To prevent table_name does not exit error
```
DROP TABLE IF EXISTS table_name
```


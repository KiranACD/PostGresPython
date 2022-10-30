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
DROP TABLE IF EXISTS table_name;
```

### Update table

```
UPDATE users SET surname = 'Wick' WHERE surname = 'Smith';
```
UPDATE - This tells the database we want to update rows in a table.
SET change - The change we want to make to each row in the table.
WHERE condition - Filter so only certain rows get updated.

To update multiple columns
```
UPDATE users SET surname = 'Wick', first_name = 'John' WHERE surname = 'Smith';
```

### Delete table

```
DELETE FROM users WHERE surname = 'Smith'
```
DELETE - This tells the database we want to delete rows from the users table.
WHERE condition - To delete rows that match the condition.

### Order By

```
SELECT * FROM table_name ORDER BY column_name DESC;
```
ORDER BY - This tells the database we want to order the results.

Order by comes after WHERE clause. We can order by multiple columns
```
SELECT * FROM table_name ORDER BY column1_name DESC, column2_name ASC;
```

### Limit

We can get the 10 most experienced employees" with ORDER BY and LIMIT
```
SELECT * FROM employees ORDER BY years_experience DESC LIMIT 10;
```

### Like

Like comparison keyword and how it is used to search. We use wildcards when using this keyword. There are 2 main wildcards:
1) % for 'any number of characters'
2) _ for 'one character'

For example, LIKE 'Do%' would match Doyle, Dot, Douglas etc. LIKE '%th' would match strings ending with 'th'. LIKE 'Do__s' matches string starting with 'Do', ending with 's', and with 2 charactes in between. LIKE 'Bo%b' matches anything starting with 'Bo', ending with 'b', and any number of characters in between. LIKE '%sens%' matches anything containing 'sens', like 'sensibility' or 'insensible'.

## Normalization

This means structuring data so that it only exists in one place. It is important that normalized data has meaning on its own. For example, do not fivide a date into day, month and year tables. They do not have meaning on their own.

## JOINS

Query data from multiple tables.

## Primary Key

```
id  |   first_name  |   surname                  id     |   holder_id   |   number
1          John          Smith                    1            3            8375841
2          Rolf          Smith                    2            4            1343545
3          Anne          Pun                      3            1            9586859 
4          Robert        Baratheon                4            2            1234567
```

```
CREATE TABLE users (id INTEGER PRIMARY KEY, first_name TEXT, surname TEXT);
CREATE TABLE accounts (id INTEGER PRIMARY KEY, holder_id INTEGER, number TEXT, FOREIGN KEY(holder_id) REFERENCES users(id));
```
Adding a foreign key relationship will enforce constratints if you are using any kind of SQL. 

If there is a user with id 5 and an account holder with id 5, we cannot delete the user unless we delete the account.

When we insert values into a table with primary key column and we dont specify the value of the primary key, SQLite assigns it a value automatically. SQLite by default has a hidden column called rowid. This is an autoincrementing column. When we create an INTEGER PRIMARY KEY column, that column becomes an alias for rowid.

SQLite could reuse rowid for new rows which will affect data integrity in certain situations. For example, assume we have a users table and an accounts table. Accounts table has a foreign key that references the primary key in the users table. Assume we delete a row in the users table and we do not delete the corresponding row in the accounts. When we add a new user in the users table, then SQLite may assign the deleted user's rowid as the primary key. The foreign key in corresponding row in the accounts table now references the new user.

In contrast, Postgres autoincrementing values only go up. So, we do not run into such issues when using postgres.

SQLite also has an AUTOINCREMENT keyword. So, we can define a column as
```
id INTEGER PRIMARY KEY AUTOINCREMENT
```
If done this way, SQLite will not resuse old numbers. However, this now requires greater computing power because of the way it is implemented there.

## Database Design

Model after the real-world entities the program deals in.

Let us say we have a movies table with title and release date as columns. There is another table of users. One user can watch many movies. One movie can be watched by many users. This is a 'many-to-many' relationship and can be modelled with a third table that links the other two.

## JOIN

JOIN is used to extract data from 2 or more columns 

```
id  |   first_name  |   surname                  id     |   holder_id   |   number
1          John          Smith                    1            3            8375841
2          Rolf          Smith                    2            4            1343545
3          Anne          Pun                      3            1            9586859 
4          Robert        Baratheon                4            2            1234567
```

```
SELECT * FROM users JOIN accounts ON users.id = accounts.holder_id;
```
When the tables are joined, it looks like this

```
id  |   first_name  |   surname    |    id    |   holder_id   |   number
1          John          Smith          3            1            9586859
2          Rolf          Smith          4            2            1234567
3          Anne          Pun            1            3            8375841
4          Robert        Baratheon      2            4            1343545
```

To choose specific columns
```
SELECT user.*, accounts.number FROM users JOIN accounts ON users.id = accounts.holder_id;
```

The order of the joins matters. accounts JOIN users is not the same as users JOIN accounts.

You can join tables on any column, but using primary and foreign keys is going to be much faster.

## Index

An index is associated with a specific column such that it speeds up filtering and sorting operations (WHERE, ORDER BY, ON). However, it slows down writing to the table. So the index is useful if we read, filter or sort data from the table and have few write operations.

Consider this table
```
id      |       name        |       years_experience        |       salary
1               John                       5                        65000
2               Rolf                       3                        38000
3               Anne                       17                       80000
4               Robert                     9                        55000
5               Sabrina                    6                        60000
6               Frank                      9                        55000
7               Edward                     2                        28000
8               Penelope                   11                       95000
9               Charles                    5                        48500
10              Sarah                      6                        66000
11              George                     1                        35000
12              May                        18                       155000
```
In the background, the database will store the ids in a tree data structure.
```
                             8
                           /   \
                          /     \   
                       3, 5       11
                      / | \       / \     
                     /  |  \     /   \
                 1,2   4  6,7   9,10   12
```
In this tree structure, the top/root node is approximately the median value of all the ids. Each node can be considered to be the root node of the tree that falls below it. All the values to the left of the root node will be smaller than the root node. All the values to the right of the root node will be greater than the root node. Some nodes have 2 values. In such cases, the ids that fall between the 2 values of the root node is directly below it.

Lets say we want to find the row with id = 9. If the id was not stored in a tree structure, then we would start searching for the id from the first id and move linearly until we find the id that we want. In, this case, we would iterate 9 times before we find the index of choice. When it is stored in the tree structure, we find it in 3 steps.

This type of data structure is called a B-tree. A feature of B-trees is that they have to be balanced. A tree structure is considered to be balanced when height of each node is equal or the difference between the height of each branch is not more than and all the nodes are left aligned. Writing to the database is slower when there is an index present because each time we make an entry, the B-tree may become imbalanced. The database will rebalance the B-tree and this takes more time than a simple write operation.

When the queries take a long time, we can add an index to speed things up.


## Difference between SQLite and PostgresSQL

SQLite is easy to setup and use. Database is a small single file. SQLite connection can write to the database only once at a time. SQLite is great for reading, but not for writing. Foreign key constraints can be diabled in SQLite

PostgreSQL is large in size and can require a lengthy setup. It has a server and it listens for incoming connections and responding to them. PostgreSQL is great for reading and writing. PostgreSQL forces us to use foreign key constraints.

Consider a users table and an accounts table. The accounts table is linked to the users table via a foreign key. Foreign key constraints mean that a user cannot be deleted from the users table without deleting the accounts that are held by the user first. The differet types of constraints are:

CASCADE constraint
```
CREATE TABLE accounts (id INTEGER PRIMARY KEY, user_id INTEGER, account_id TEXT, FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
```
When we delete a user, all the accounts associated with the user are aso deleted.

RESTRICT constraint

When we delete a user and user has an account and we have not deleted the account, then the user is not deleted. No error is thrown.

The default is, we get an error when we try to delete a user.

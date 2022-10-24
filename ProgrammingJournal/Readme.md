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

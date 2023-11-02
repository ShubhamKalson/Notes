```markdown
# Using SQLite with Python

SQLite is a lightweight, serverless, and 
self-contained database engine that is widely used for local storage in applications. 

#it has file based storage, that means it uses local storage(Hard disk) for storing data
#Its C based program coded in ANSI-C, mainly file named sqlite.c and sqlite.h

## Prerequisites

Before you start, make sure you have Python installed on your system.

## Installing SQLite

SQLite comes bundled with Python, so there's no need to install it separately.

## Connecting to a Database

To use SQLite in Python, you need to import the `sqlite3` module and establish a connection to a database:

```python
import sqlite3

# Connect to a database (creates a new database if it doesn't exist)
conn = sqlite3.connect('my_database.db')
```

## Creating a Table

You can create a table using the `execute()` method along with an SQL `CREATE TABLE` statement:

```python
# Create a table
conn.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        email TEXT
    )
''')
```

## Inserting Data

To insert data into the table, you can use the `execute()` method with an SQL `INSERT INTO` statement:

```python
# Insert data
conn.execute('''
    INSERT INTO users (username, email)
    VALUES (?, ?)
''', ('john_doe', 'john@example.com'))

# Commit the transaction
conn.commit()
```

## Querying Data

You can retrieve data from the database using the `execute()` method with an SQL `SELECT` statement:

```python
# Query data
cursor = conn.execute('SELECT id, username, email FROM users')
for row in cursor:
    print(row)
```

## Updating and Deleting Data

To update or delete data, use the `execute()` method with SQL `UPDATE` and `DELETE` statements:

```python
# Update data
conn.execute('''
    UPDATE users
    SET email = ?
    WHERE username = ?
''', ('new_email@example.com', 'john_doe'))

# Delete data
conn.execute('DELETE FROM users WHERE id = ?', (1,))
```

## Closing the Connection

After you're done working with the database, make sure to close the connection:

```python
# Close the connection
conn.close()
```




###Cursors
#cursors are best for memeory management
#its not mandatory
#A cursor in SQLite is an object that allows you to interact with the database
#Cursors help manage resources effectively by allowing you to close or release 
#resources associated with a specific query or transaction. 
#Closing a cursor releases the locks and resources used by the query, improving database performance.
#Cursors provide methods like fetchone(), fetchall(), and fetchmany() to retrieve rows from the result set. 
import sqlite3

# Connect to a database
conn = sqlite3.connect('my_database.db')

# Create a cursor
cursor = conn.cursor()

# Execute a query
cursor.execute('SELECT id, username, email FROM users')

# Fetch data
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the cursor
cursor.close()

# Close the connection
conn.close()

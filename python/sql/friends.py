import sqlite3

connection = sqlite3.connect('people.db')

# create cursor object
cursor = connection.cursor()

# execute some SQL
# cursor.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER)")

# insert_query = "INSERT INTO friends VALUES ('Merriwether', 'Lewis', 7)"
# cursor.execute(insert_query)

data = ('Adel', 'Rodriguez', 10)
insert_query = 'INSERT INTO friends VALUES (?, ?, ?)'

cursor.execute(insert_query, data)

# commit changes
connection.commit()

connection.close()
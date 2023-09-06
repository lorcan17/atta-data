import sqlite3

# Connect to the database
connection = sqlite3.connect('data/atta.sqlite')
cursor = connection.cursor()

try:
    # Execute a simple query
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Tables in the database:")
    for table in tables:
        print(table[0])

except sqlite3.Error as e:
    print("An error occurred:", e)

finally:
    connection.close()

import sqlite3

# Connect to the database
connection = sqlite3.connect('data/atta.sqlite')
cursor = connection.cursor()

# Define the SQL query to remove duplicate entries
delete_query = '''
    DELETE FROM city_dim
    WHERE rowid NOT IN (
        SELECT MIN(rowid)
        FROM city_dim
        GROUP BY city, country
    )
'''

# Execute the query to remove duplicates
cursor.execute(delete_query)

# Commit the changes and close the connection
connection.commit()
connection.close()

print("Duplicate entries removed from 'city_dim' table.")

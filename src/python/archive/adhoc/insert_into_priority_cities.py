import json
import sqlite3
from datetime import datetime



with open('data/json/priority_cities.json', 'r') as json_file:
    data = json.load(json_file)

# Connect to the database
connection = sqlite3.connect('data/ATTA.sqlite')
cursor = connection.cursor()


# Clear the table by deleting all rows
delete_query = '''
    DELETE FROM priority_cities
'''
cursor.execute(delete_query)

# Insert data into the table
insert_query = '''
    INSERT INTO priority_cities (city, country)
    VALUES (?, ?)
'''

for row in data:
    current_timestamp = datetime.now()
    cursor.execute(insert_query, (
        row.get("City", None),
        row.get("Country", None)
    ))

connection.commit()
connection.close()

print("Data inserted into 'priority_cities' table.")



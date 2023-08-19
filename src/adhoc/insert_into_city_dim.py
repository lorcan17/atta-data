import json
import sqlite3
from datetime import datetime



with open('data/json/city_dim.json', 'r') as json_file:
    data = json.load(json_file)

# Connect to the database
connection = sqlite3.connect('data/ATTA.sqlite')
cursor = connection.cursor()


# Clear the table by deleting all rows
delete_query = '''
    DELETE FROM city_dim
'''
cursor.execute(delete_query)

# Insert data into the table
insert_query = '''
    INSERT INTO city_dim (city, country, image_filepath)
    VALUES (?, ?, ?)
'''

for row in data:
    current_timestamp = datetime.now()
    cursor.execute(insert_query, (
        row.get("city", None),
        row.get("country", None),
        "images/Generic.jpg"
    ))

connection.commit()
connection.close()

print("Data inserted into 'city_dim' table.")



import json
import sqlite3
from datetime import datetime



# Connect to the database
connection = sqlite3.connect('data/atta.sqlite')
cursor = connection.cursor()
query = '''
SELECT STATION_DIM.* FROM 
    (SELECT DISTINCT CITY, COUNTRY FROM STATION_DIM) AS STATION_DIM
LEFT JOIN 
    CITY_DIM
ON (
    (STATION_DIM.CITY = CITY_DIM.CITY OR (STATION_DIM.CITY IS NULL AND CITY_DIM.CITY IS NULL))
    AND STATION_DIM.COUNTRY = CITY_DIM.COUNTRY)
WHERE (
    CITY_DIM.CITY IS NULL 
    AND CITY_DIM.COUNTRY IS NULL
    )'''
# Fetch data from the database
cursor.execute(query)
data = cursor.fetchall()

# Print the number of records fetched
print(data)
num_records = len(data)
print(f"{num_records} to insert into city_dim")

# Insert data into the table
insert_query = '''
    INSERT INTO city_dim (city, country, image_filepath, auto_generated, etl_insert_ts, etl_update_ts)
    VALUES (?, ?, ?, ?,?,?)
'''

for record in data:
    city, country = record
    current_timestamp = datetime.now()
    cursor.execute(insert_query, (
        city,
        country,
        "images/_Generic.jpg",
        0,
        current_timestamp,
        current_timestamp
    ))

connection.commit()
connection.close()

print("Data inserted into 'city_dim' table.")



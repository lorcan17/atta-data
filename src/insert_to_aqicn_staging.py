import json
import sqlite3


connection = sqlite3.connect('data/atta.sqlite')
cursor = connection.cursor()


with open('sample_offline_data.json', 'r') as json_file:
    data = json.load(json_file)
    data = data["data"]

# Connect to the database
connection = sqlite3.connect('data/ATTA.sqlite')
cursor = connection.cursor()

# Clear the staging table by deleting all rows
delete_staging_query = '''
    DELETE FROM aqicn_staging
'''
cursor.execute(delete_staging_query)

# Insert data into the staging table
insert_staging_query = '''
    INSERT INTO aqicn_staging (uid, lat, lon, aqi, station_name, recorded_at)
    VALUES (?, ?, ?, ?, ?, ?)
'''

for row in data:
    cursor.execute(insert_staging_query, (
        row.get('uid', None),
        row.get('lat', None),
        row.get('lon', None),
        row.get('aqi', None),
        row.get('station', {}).get('name', None),
        row.get('station', {}).get('time', None),
    ))


connection.commit()
connection.close()

print("Data inserted into staging table after clearing previous data.")



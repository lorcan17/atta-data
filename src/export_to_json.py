import sqlite3
import json

# Connect to the database
connection = sqlite3.connect('data/atta.sqlite')
cursor = connection.cursor()

# Define the SQL query
query = '''
    SELECT 
        AQICN.UID,
        AQICN.LAT,
        AQICN.LON,
        AQICN.AQI,
        AQICN.RECORDED_AT,
        STATION_DIM.STATION_NAME,
        CITY_DIM.CITY,
        CITY_DIM.COUNTRY,
        CITY_DIM.IMAGE_FILEPATH,
        CITY_DIM.AUTO_GENERATED,
        COUNTRY_INCOME_GROUP.INCOME_GROUP,
        COUNTRY_INCOME_GROUP.LENDING_CATEGORY
    FROM AQICN
    LEFT JOIN STATION_DIM ON AQICN.UID = STATION_DIM.UID
    LEFT JOIN CITY_DIM ON STATION_DIM.CITY = CITY_DIM.CITY AND STATION_DIM.COUNTRY = CITY_DIM.COUNTRY
    LEFT JOIN COUNTRY_INCOME_GROUP ON STATION_DIM.COUNTRY_CODE2 = COUNTRY_INCOME_GROUP.COUNTRY_CODE2
    -- To filter for the top 25 pre-selected cities, uncommented the below
    -- INNER JOIN PRIORITY_CITIES ON CITY_DIM.CITY = PRIORITY_CITIES.CITY AND CITY_DIM.COUNTRY = PRIORITY_CITIES.COUNTRY
    WHERE CITY_DIM.COUNTRY IS NOT NULL
    '''

# Execute the query
cursor.execute(query)

# Get column names from cursor description
column_names = [description[0] for description in cursor.description]

# Fetch all the results
results = cursor.fetchall()

# Convert results to list of dictionaries
result_dicts = [dict(zip(column_names, row)) for row in results]

# Close the database connection
connection.close()

# Define the output JSON file name
output_file = 'data/ATTA.json'

# Write the results to the JSON file
with open(output_file, 'w') as json_file:
    json.dump(result_dicts, json_file, indent=4)

print(f"Query results exported to '{output_file}' in JSON format with key-value pairs.")

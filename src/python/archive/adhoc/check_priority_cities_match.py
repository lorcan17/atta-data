import sqlite3
import json

# Connect to the database
connection = sqlite3.connect('data/atta.sqlite')
cursor = connection.cursor()

# Define the SQL query
query = '''
    SELECT 
        PRIORITY_CITIES.CITY,
        PRIORITY_CITIES.COUNTRY,        
        CITY_DIM.CITY AS CITY_MATCH,
        CITY_DIM.COUNTRY AS COUNTRY_MATCH
    FROM PRIORITY_CITIES
    LEFT JOIN CITY_DIM ON PRIORITY_CITIES.CITY = CITY_DIM.CITY AND PRIORITY_CITIES.COUNTRY = CITY_DIM.COUNTRY
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
output_file = 'data/priority_cities.json'

# Write the results to the JSON file
with open(output_file, 'w') as json_file:
    json.dump(result_dicts, json_file, indent=4)

print(f"Query results exported to '{output_file}' in JSON format with key-value pairs.")

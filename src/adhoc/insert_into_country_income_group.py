import json
import sqlite3
from datetime import datetime


with open('data/json/sample_class.json', 'r') as json_file:
    data = json.load(json_file)

# Connect to the database
connection = sqlite3.connect('data/ATTA.sqlite')
cursor = connection.cursor()


# Clear the table by deleting all rows
delete_query = '''
    DELETE FROM country_income_group
'''
cursor.execute(delete_query)

# Insert data into the table
insert_query = '''
    INSERT INTO country_income_group (economy, region, country_code2, country_code3, income_group, lending_category, etl_insert_ts, etl_update_ts)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
'''

for row in data:
    current_timestamp = datetime.now()
    cursor.execute(insert_query, (
        row.get("Economy", None),
        row.get("Region", None),
        row.get("country_code2", None),
        row.get("Code", None),
        row.get("Income Group", None),
        row.get("Lending Category", None),
        current_timestamp,
        current_timestamp
    ))

connection.commit()
connection.close()

print("Data inserted into 'country_income_group' table.")



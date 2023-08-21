import sqlite3
import csv

# Connect to the SQLite database
db_connection = sqlite3.connect('data/ATTA.sqlite')
cursor = db_connection.cursor()

# Execute a SELECT query
query = "SELECT * FROM aqicn"
cursor.execute(query)
data = cursor.fetchall()

# Define the CSV file name
csv_file_name = 'output.csv'

# Write data to the CSV file
with open(csv_file_name, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    # Write header row (if needed)
    column_names = [description[0] for description in cursor.description]
    csv_writer.writerow(column_names)
    
    # Write data rows
    csv_writer.writerows(data)

# Close the database connection
db_connection.close()

print(f'Data exported to {csv_file_name}')

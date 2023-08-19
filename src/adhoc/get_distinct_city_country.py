import sqlite3
import csv
import json

# Connect to the database
connection = sqlite3.connect('data/atta.sqlite')
cursor = connection.cursor()
query = '''
SELECT DISTINCT CITY, COUNTRY FROM STATION_DIM'''
# Fetch data from the database
cursor.execute(query)
data = cursor.fetchall()

# Close the database connection
connection.close()

city_country_list = [{"city": city, "country": country} for city, country in data]


with open("data/json/city_dim.json", "w") as outfile:
    json.dump(city_country_list, outfile)

# Write the data to a CSV file using UTF-8 encoding

#with open("hello.csv", "w", newline="", encoding="utf-8") as csvfile:
#    csv_writer = csv.writer(csvfile)
#    csv_writer.writerow(["City", "Country"])  # Write header
#    csv_writer.writerows(staging_data)  # Write data rows

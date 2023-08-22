import sqlite3

# Connect to the database
connection = sqlite3.connect('data/atta.sqlite')
cursor = connection.cursor()

# Define the SQL query to check for duplicate UID values in the query results
duplicate_check_query = '''
    SELECT UID, COUNT(*) as count
    FROM (
        SELECT 
        AQICN.UID
        FROM AQICN
        LEFT JOIN STATION_DIM ON AQICN.UID = STATION_DIM.UID
        LEFT JOIN CITY_DIM ON STATION_DIM.CITY = CITY_DIM.CITY AND STATION_DIM.COUNTRY = CITY_DIM.COUNTRY
        LEFT JOIN COUNTRY_INCOME_GROUP ON STATION_DIM.COUNTRY_CODE2 = COUNTRY_INCOME_GROUP.COUNTRY_CODE2
        -- To filter for the top 25 pre-selected cities, uncomment the below
        -- INNER JOIN PRIORITY_CITIES ON CITY_DIM.CITY = PRIORITY_CITIES.CITY AND CITY_DIM.COUNTRY = PRIORITY_CITIES.COUNTRY
        WHERE CITY_DIM.COUNTRY IS NOT NULL
    ) AS QueryResults
    GROUP BY UID
    HAVING count > 1
'''

# Execute the duplicate check query
cursor.execute(duplicate_check_query)

# Fetch the results of the duplicate check
duplicate_results = cursor.fetchall()

# Close the database connection
connection.close()

if duplicate_results:
    print("Duplicate UID values found:")
    for uid, count in duplicate_results:
        print(f"UID: {uid}, Count: {count}")
else:
    print("No duplicate UID values found.")

import sqlite3

connection = sqlite3.connect('data/ATTA.sqlite')
cursor = connection.cursor()


# Drop the existing table if it exists

drop_table_query = '''
    DROP TABLE IF EXISTS aqicn
'''
cursor.execute(drop_table_query)

# Create the final table if it doesn't exist
create_final_table_query = '''
    CREATE TABLE aqicn (
        uid INTEGER PRIMARY KEY,
        lat REAL,
        lon REAL,
        aqi INTEGER,
        station_name TEXT,
        recorded_at DATETIME,
        etl_insert_ts DATETIME,
        etl_update_ts DATETIME
    )
'''
cursor.execute(create_final_table_query)

# Commit changes and close the connection
connection.commit()
connection.close()

print("Table aqicn created.")

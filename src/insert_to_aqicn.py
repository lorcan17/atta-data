import sqlite3
from datetime import datetime

# Connect to the database
connection = sqlite3.connect('data/atta.sqlite')
cursor = connection.cursor()

# Insert and update data
insert_update_query = '''
    INSERT INTO aqicn (uid, lat, lon, aqi, station_name, recorded_at, etl_insert_ts, etl_update_ts)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ON CONFLICT(uid) DO UPDATE SET
        lat = excluded.lat,
        lon = excluded.lon,
        aqi = excluded.aqi,
        station_name = excluded.station_name,
        recorded_at = excluded.recorded_at,
        etl_update_ts = excluded.etl_update_ts
'''

# Fetch data from the staging table
cursor.execute('SELECT * FROM aqicn_staging')
staging_data = cursor.fetchall()

# Process each record and insert/update in the target table
for record in staging_data:
    uid, lat, lon, aqi, station_name, recorded_at = record
    
    # Define current timestamps
    current_timestamp = datetime.now()
    
    # Insert/update record into target table
    cursor.execute(
        insert_update_query,
        (uid, lat, lon, aqi, station_name, recorded_at, current_timestamp, current_timestamp)
    )

connection.commit()
connection.close()

print("Data from staging inserted into aqicn with updates and timestamp columns.")

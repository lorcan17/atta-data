import sqlite3
from datetime import datetime
from geopy.geocoders import Nominatim
import geopy.exc
import sys

# Initialize the geocoder
geolocator = Nominatim(user_agent="geoapp")

# Connect to the database
connection = sqlite3.connect('data/atta.sqlite')
cursor = connection.cursor()

# Insert and update data
insert_update_query = '''
    INSERT INTO station_dim (uid, lat, lon, station_name, country_code2, city, country, etl_insert_ts, etl_update_ts)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?,?)
    ON CONFLICT(uid) DO UPDATE SET
        lat = excluded.lat,
        lon = excluded.lon,
        station_name = excluded.station_name,
        country_code2 = excluded.country_code2,
        city = excluded.city,
        country = excluded.country,
        etl_update_ts = excluded.etl_update_ts
'''
delete_staging_query = '''
    DELETE FROM station_dim
'''
cursor.execute(delete_staging_query)


# Fetch data from the staging table
cursor.execute('''SELECT aqicn.uid, aqicn.lat, aqicn.lon, aqicn.station_name FROM aqicn
    LEFT JOIN station_dim ON aqicn.uid = station_dim.uid
    WHERE station_dim.uid IS NULL''')
data = cursor.fetchall()

# Print the number of records fetched
num_records = len(data)
print(f"{num_records} to insert into station_dim")

# Process each record and insert/update in the target table
for record in data:
    uid, lat, lon, station_name = record
    
    # Define current timestamps
    current_timestamp = datetime.now()
    # Get location information based on latitude and longitude
    try:
        location = geolocator.reverse((lat, lon), exactly_one=True, language='en')

    except geopy.exc.GeocoderTimedOut:
        print("Geocoding service timed out. Please try again later.")
    except geopy.exc.GeocoderServiceError as e:
        print("Geocoding service error:", e)
    except geopy.exc.GeocoderUnavailable as e:
        print("Geocoding service is currently unavailable:", e)
        print("Exiting the application.")
        sys.exit(1)  # Exit the script with an error status code
    except Exception as e:
        print("An error occurred:", e)

    if location:
        address = location.raw.get("address", {})
        city = address.get("city", None)
        country = address.get("country", None)
        country_code2 = address.get("country_code", None).lower()
    # Insert/update record into target table
    cursor.execute(
        insert_update_query,
        (uid, lat, lon, station_name, country_code2, city, country, current_timestamp,
         current_timestamp)
    )

connection.commit()
connection.close()

print("Data inserted into station_dim")

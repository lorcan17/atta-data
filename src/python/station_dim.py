from google.cloud import bigquery
from datetime import datetime
from geopy.geocoders import Nominatim
import geopy.exc
import sys

# Path to your service account JSON key file
service_account_key_path = "./config/gcloud_service_account.json"

# Create a BigQuery client with the service account
client = bigquery.Client.from_service_account_json(service_account_key_path)

sql_file_path = "./src/sql/temp/station_dim.sql"
 # Read the SQL query from the file
with open(sql_file_path, 'r') as sql_file:
    query = sql_file.read()

try:
    # Execute the SQL query
    query_job = client.query(query)

    # Wait for the query to complete
    data = query_job.result()
    rows = list(data)
    print("Query executed successfully.")
except Exception as e:
    print(f"Error executing query: {e}")

# Print the number of records fetched
num_records = len(rows)
print(f"{num_records} to insert into station_dim")

# Initialize the geocoder
geolocator = Nominatim(user_agent="geoapp")

# Create a list to store enriched data
enriched_data = []

for row in rows:
    uid, lat, lon, station_name = row
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
        # Enrich the row data with geolocation information
        enriched_row = (uid, lat, lon, country_code2, station_name, city, country,\
                        current_timestamp, current_timestamp)            
        enriched_data.append(enriched_row)


if len(enriched_data) != 0:
     
    table_ref = client.dataset('atta').table('station_dim')
    table = client.get_table(table_ref)
    errors = client.insert_rows(table, enriched_data)

    if not errors:
        print("Row inserted successfully.")
    else:
        print(f"Error inserting row: {errors}")

    print("Data inserted into station_dim")
else: 
    print("No rows to insert") 
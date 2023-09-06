from google.cloud import bigquery
from datetime import datetime

# Path to your service account JSON key file
service_account_key_path = "config\gcloud_service_account.json"

# Create a BigQuery client with the service account
client = bigquery.Client.from_service_account_json(service_account_key_path)

sql_file_path = "src/sql/temp/city_dim.sql"
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
print(f"{num_records} to insert into city_dim")

# Create a list to store enriched data
enriched_data = []

for row in rows:
    city, country = row
    current_timestamp = datetime.now()
    auto_generated = 0
    # Enrich the row data with geolocation information
    enriched_row = (city, country,  "images\_Generic.jpg",\
                        auto_generated, current_timestamp, current_timestamp)
    enriched_data.append(enriched_row)
    
table_ref = client.dataset('atta').table('city_dim')
table = client.get_table(table_ref)
errors = client.insert_rows(table, enriched_data)

if not errors:
        print("Row inserted successfully.")
else:
        print(f"Error inserting row: {errors}")
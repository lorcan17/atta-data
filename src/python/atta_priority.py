from google.cloud import bigquery
import json

# Path to your service account JSON key file
service_account_key_path = "config\gcloud_service_account.json"

# Create a BigQuery client with the service account
client = bigquery.Client.from_service_account_json(service_account_key_path)

# Define the SQL query (BigQuery SQL dialect)
sql_file_path = "src/sql/export/atta_priority.sql"

# Read the SQL query from the file
with open(sql_file_path, 'r') as sql_file:
    query = sql_file.read()

# Execute the query
query_job = client.query(query)

# Fetch the results
results = query_job.result()

# Convert results to a list of dictionaries
result_dicts = [dict(row) for row in results]

# Define the output JSON file name
output_file = 'data/atta2.json'

# Write the results to the JSON file
with open(output_file, 'w') as json_file:
    json.dump(result_dicts, json_file, indent=4)

print(f"Query results exported to '{output_file}' in JSON format with key-value pairs.")

import os
from google.cloud import bigquery

# Path to your service account JSON key file
service_account_key_path = "config\gcloud_service_account.json"


# Create a BigQuery client with the service account
client = bigquery.Client.from_service_account_json(service_account_key_path)

sql_file_path = "src/sql/merge/aqicn.sql"
 # Read the SQL query from the file
with open(sql_file_path, 'r') as sql_file:
    query = sql_file.read()

try:
    # Execute the SQL query
    query_job = client.query(query)

    # Wait for the query to complete
    query_job.result()
    print(query_job.dml_stats)
    print("Query executed successfully.")
except Exception as e:
    print(f"Error executing query: {e}")
import os
from google.cloud import bigquery
import pandas as pd
from datetime import datetime

# Read the csv file into a DataFrame
file_path = "./data/raw/priority_cities.csv"  # Update with the actual path
sheet_name = "List of economies"
df = pd.read_csv(file_path)

current_timestamp = datetime.now()

df["etl_insert_ts"] =  current_timestamp
df["etl_update_ts"] =  current_timestamp

# Path to your service account JSON key file
service_account_key_path = "./config/gcloud_service_account.json"

# Create a BigQuery client with the service account
client = bigquery.Client.from_service_account_json(service_account_key_path)

# Reference to the BigQuery staging table
table_ref = client.dataset('atta').table('priority_cities')

# Load data into the staging table
job_config = bigquery.LoadJobConfig(
    write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE
    )

load_job = client.load_table_from_dataframe(
    df, table_ref, job_config=job_config
)

load_job.result()  # Wait for the job to complete

print("Data inserted into staging table after clearing previous data.")
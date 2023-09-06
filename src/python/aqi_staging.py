import os
from google.cloud import bigquery
from utils.aqicn import aqicn

# Path to your service account JSON key file
service_account_key_path = "config\gcloud_service_account.json"

# Create a BigQuery client with the service account
client = bigquery.Client.from_service_account_json(service_account_key_path)

# Reference to the BigQuery staging table
table_ref = client.dataset('staging').table('aqicn_staging')

# GET aqi data

token = os.environ.get("AQICN_TOKEN")
world_bounds =  "-90,-180,90,180"
aqi = aqicn()
data = aqi.get_aqi_within_bounds(token, world_bounds)  # Your data list

# Load data into the staging table
job_config = bigquery.LoadJobConfig(
    write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE
    )
job_config.source_format = bigquery.SourceFormat.NEWLINE_DELIMITED_JSON

load_job = client.load_table_from_json(
    data, table_ref, job_config=job_config
)

load_job.result()  # Wait for the job to complete

print("Data inserted into staging table after clearing previous data.")
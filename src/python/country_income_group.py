# GET SOCIO ECONOMIC FACTORS
import pycountry
import pandas as pd
import os
import io
import json
from google.cloud import bigquery

# Read the Excel file into a DataFrame
excel_file_path = "./data/raw/CLASS.xlsx"  # Update with the actual path
sheet_name = "List of economies"
df = pd.read_excel(excel_file_path, sheet_name=sheet_name)

# Define a dictionary to map current column names to new column names
column_name_mapping = {
    "Economy": "economy",
    "Region": "region",
    "Lending category": "lending_category",
    "Income group": "income_group"
}

# Use the rename method to rename columns
df.rename(columns=column_name_mapping, inplace=True)

# Convert 3-letter country code to 2-letter code within the DataFrame
for index, row in df.iterrows():
    three_letter_code = row["Code"]
    try:
        country = pycountry.countries.get(alpha_3=three_letter_code)
        if country:
            two_letter_code = country.alpha_2
            df.at[index, "country_code2"] = str(two_letter_code.lower())
        else:
            pass
            #print("Country not found")
    except LookupError:
        print("Invalid 3-letter code")


service_account_key_path = "./config/gcloud_service_account.json"

# Create a BigQuery client with the service account
client = bigquery.Client.from_service_account_json(service_account_key_path)

# Reference to the BigQuery staging table
table_ref = client.dataset('atta').table('country_income_group')

# Load data into the staging table
job_config = bigquery.LoadJobConfig(
    write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE
    )

load_job = client.load_table_from_dataframe(
    df, table_ref, job_config=job_config
)

load_job.result()  # Wait for the job to complete

print("Data inserted into staging table after clearing previous data.")
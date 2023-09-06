import os
from google.cloud import bigquery

class BigQueryOperations:
    def __init__(self, json_file):
        self.client = bigquery.Client.from_service_account_json(json_file)

    def run_query(self, query):
        query_job = self.client.query(query)
        return query_job.to_dataframe()

    def create_table(self, dataset_id, table_id, schema):
        dataset_ref = self.client.dataset(dataset_id)
        table_ref = dataset_ref.table(table_id)
        table = bigquery.Table(table_ref, schema=schema)
        return self.client.create_table(table)
    
    def run_sql_query(self,sql_file_path):

        # Read the SQL query from the file
        with open(sql_file_path, 'r') as sql_file:
            query = sql_file.read()

        try:
            # Execute the SQL query
            query_job = client.query(query)

            # Wait for the query to complete
            query_job.result()

            print("Query executed successfully.")
        except Exception as e:
            print(f"Error executing query: {e}")
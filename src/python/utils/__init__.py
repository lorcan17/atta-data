import os
from google.cloud import bigquery

class BigQueryOperations:
    def __init__(self, creds, project_id):
        self.client = bigquery.Client(credentials=creds, project=creds.project_id)

    def run_query(self, query):
        query_job = self.client.query(query)
        return query_job.to_dataframe()

    def create_table(self, dataset_id, table_id, schema):
        dataset_ref = self.client.dataset(dataset_id)
        table_ref = dataset_ref.table(table_id)
        table = bigquery.Table(table_ref, schema=schema)
        return self.client.create_table(table)
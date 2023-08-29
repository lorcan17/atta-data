CREATE OR REPLACE TABLE your_project_id.your_dataset_id.country_income_group (
    economy STRING,
    region STRING,
    country_code2 STRING,
    country_code3 STRING,
    income_group STRING,
    lending_category STRING,
    etl_insert_ts TIMESTAMP,
    etl_update_ts TIMESTAMP
)
OPTIONS (
    expiration_timestamp = TIMESTAMP_ADD(CURRENT_TIMESTAMP(), INTERVAL 100 YEAR)
);

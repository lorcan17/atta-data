CREATE OR REPLACE TABLE your_project_id.your_dataset_id.station_dim (
    uid INT64 PRIMARY KEY,
    lat FLOAT64,
    lon FLOAT64,
    country_code2 STRING,
    station_name STRING,
    city STRING,
    country STRING,
    etl_insert_ts TIMESTAMP,
    etl_update_ts TIMESTAMP
)
OPTIONS (
    expiration_timestamp = TIMESTAMP_ADD(CURRENT_TIMESTAMP(), INTERVAL 100 YEAR)
);

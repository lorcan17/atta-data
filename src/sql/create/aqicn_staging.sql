CREATE OR REPLACE TABLE your_project_id.your_dataset_id.aqicn_staging (
    uid INT64 PRIMARY KEY,
    lat FLOAT64,
    lon FLOAT64,
    aqi INT64,
    station_name STRING,
    recorded_at TIMESTAMP
)
OPTIONS(
    expiration_timestamp = TIMESTAMP_ADD(CURRENT_TIMESTAMP(), INTERVAL 100 YEAR)
);

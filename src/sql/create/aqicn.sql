CREATE OR REPLACE TABLE air-quality-379023.atta.aqicn (
    uid INT64,
    lat FLOAT64,
    lon FLOAT64,
    aqi INT64,
    station_name STRING,
    recorded_at TIMESTAMP,
    etl_insert_ts TIMESTAMP,
    etl_update_ts TIMESTAMP
)
OPTIONS (
    expiration_timestamp = "2999-12-31" -- Set a large expiration time
);

CREATE TABLE air-quality-379023.atta.station_dim (
    uid INT64,
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
    expiration_timestamp = "2999-12-31" -- Set a large expiration time
);

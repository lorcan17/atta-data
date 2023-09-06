CREATE TABLE air-quality-379023.staging.aqicn_staging (
    uid INT64,
    lat FLOAT64,
    lon FLOAT64,
    aqi INT64,
    station STRUCT<
        name STRING,
        time TIMESTAMP
    >
)
OPTIONS (
    expiration_timestamp = "2999-12-31" -- Set a large expiration time

);

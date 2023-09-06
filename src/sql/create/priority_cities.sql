CREATE TABLE air-quality-379023.atta.priority_cities (
    city STRING,
    country STRING,
    etl_insert_ts TIMESTAMP,
    etl_update_ts TIMESTAMP
)
OPTIONS (
    expiration_timestamp = "2999-12-31" -- Set a large expiration time
);

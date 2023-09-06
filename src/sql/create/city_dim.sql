CREATE TABLE air-quality-379023.atta.city_dim (
    city STRING,
    country STRING,
    image_filepath STRING,
    auto_generated INT64,
    etl_insert_ts TIMESTAMP,
    etl_update_ts TIMESTAMP
)
OPTIONS (
    expiration_timestamp = "2999-12-31" -- Set a large expiration time
);

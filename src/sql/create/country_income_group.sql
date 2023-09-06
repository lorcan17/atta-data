CREATE TABLE air-quality-379023.atta.country_income_group (
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
    expiration_timestamp = "2999-12-31" -- Set a large expiration time
);

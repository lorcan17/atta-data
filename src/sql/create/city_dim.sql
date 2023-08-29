CREATE OR REPLACE TABLE your_project_id.your_dataset_id.city_dim (
    city STRING,
    country STRING,
    image_filepath STRING,
    auto_generated INT64,
    etl_insert_ts TIMESTAMP,
    etl_update_ts TIMESTAMP
)
OPTIONS(
    expiration_timestamp = TIMESTAMP_ADD(CURRENT_TIMESTAMP(), INTERVAL 100 YEAR)
);

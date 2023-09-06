MERGE INTO air-quality-379023.atta.aqicn AS target
USING air-quality-379023.staging.aqicn_staging AS source
    ON
        target.uid = source.uid
WHEN MATCHED AND (target.recorded_at != source.station.time) THEN
    UPDATE SET
        lat = source.lat,
        lon = source.lon,
        aqi = source.aqi,
        station_name = source.station.name,
        recorded_at = source.station.time,
        etl_update_ts = current_timestamp()
WHEN NOT MATCHED THEN
    INSERT
        (
            uid,
            lat,
            lon,
            aqi,
            station_name,
            recorded_at,
            etl_insert_ts,
            etl_update_ts
        )
    VALUES
    (
        source.uid,
        source.lat,
        source.lon,
        source.aqi,
        source.station.name,
        source.station.time,
        current_timestamp(),
        current_timestamp()
    );

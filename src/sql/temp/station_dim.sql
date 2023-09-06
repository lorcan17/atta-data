SELECT
    aqicn.uid,
    aqicn.lat,
    aqicn.lon,
    aqicn.station_name
FROM air-quality-379023.atta.aqicn
LEFT JOIN air-quality-379023.atta.station_dim ON aqicn.uid = station_dim.uid
WHERE station_dim.uid IS NULL

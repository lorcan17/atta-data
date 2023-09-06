WITH ranked_stations AS (
    SELECT
        aqicn.uid,
        aqicn.lat,
        aqicn.lon,
        aqicn.aqi,
        FORMAT_TIMESTAMP('%Y-%m-%dT%H:%M:%SZ', aqicn.recorded_at) AS recorded_at,
        station_dim.station_name,
        city_dim.city,
        city_dim.country,
        city_dim.image_filepath,
        city_dim.auto_generated,
        country_income_group.income_group,
        country_income_group.lending_category,
        RANK() OVER (PARTITION BY city_dim.city, city_dim.country ORDER BY aqicn.recorded_at DESC) AS station_rank
    FROM air-quality-379023.atta.aqicn AS aqicn
    LEFT JOIN
        air-quality-379023.atta.station_dim AS station_dim
        ON aqicn.uid = station_dim.uid
    LEFT JOIN
        air-quality-379023.atta.city_dim AS city_dim
        ON
            station_dim.city = city_dim.city
            AND station_dim.country = city_dim.country
    LEFT JOIN
        air-quality-379023.atta.country_income_group AS country_income_group
        ON station_dim.country_code2 = country_income_group.country_code2
    -- To filter for the top 25 pre-selected cities, uncommented the below
    INNER JOIN
        air-quality-379023.atta.priority_cities AS priority_cities
        ON
            city_dim.city = priority_cities.city
            AND city_dim.country = priority_cities.country
    WHERE city_dim.country IS NOT NULL
)
SELECT
    uid,
    lat,
    lon,
    aqi,
    recorded_at,
    station_name,
    city,
    country,
    image_filepath,
    auto_generated,
    income_group,
    lending_category
FROM ranked_stations
WHERE station_rank = 1;

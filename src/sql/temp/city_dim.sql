SELECT station_dim.* FROM
    (SELECT DISTINCT
        city,
        country
    FROM air-quality-379023.atta.station_dim)
        AS station_dim
LEFT JOIN
    air-quality-379023.atta.city_dim
    ON (
        (
            station_dim.city = city_dim.city
            OR (station_dim.city IS NULL AND city_dim.city IS NULL)
        )
        AND station_dim.country = city_dim.country
    )
WHERE (
    city_dim.city IS NULL
    AND city_dim.country IS NULL
)

# ATTA Data

The `data/ATTA.sqlite` database file contains several tables that are utilized by the React application. Below are the details of each table along with their fields:

## aqicn Table

This is the main fact table that stores AQI (Air Quality Index) data. It contains the following fields:

- `uid`: Unique station ID
- `lat`: Latitude
- `lon`: Longitude
- `aqi`: AQI value
- `station_name`: Name of the station where the AQI was recorded
- `recorded_at`: Datetime when the AQI was recorded

## station_dim Table

This is a dimension table providing additional information about stations. It can be joined with the `aqicn` table using the `uid` field. It contains the following fields:

- `uid`: Unique station ID
- `lat`: Latitude
- `lon`: Longitude
- `station_name`: Name of the station
- `city`: City where the station is located
- `country`: Country where the station is located
- `country_code2`: Two-letter country code

## city_dim Table

This dimension table holds image file paths related to cities. It includes the following fields:

- `city`: City name
- `country`: Country name
- `image_filepath`: File path of the associated image
- `auto_generated`: Flag indicating whether the image was auto-generated using the Unsplash API

## country_income_group Table

A dimension table providing income group and lending category information by country. You can join this table with `station_dim` using the `country_code2` field. It contains the following fields:

- `economy`: Economy information
- `region`: Region information
- `country_code2`: Two-letter country code
- `country_code3`: Three-letter country code
- `income_group`: Income group category
- `lending_category`: Lending category information

## priority_cities Table

This table lists shortlisted cities to be displayed initially on the map. It contains the following fields:

- `city`: City name
- `country`: Country name


## Example queries

The below query display how the tables in the database can be joined together.

```sql
SELECT 
AQICN.UID,
AQICN.LAT,
AQICN.LON,
AQICN.AQI,
STATION_DIM.STATION_NAME,
CITY_DIM.CITY,
CITY_DIM.COUNTRY,
CITY_DIM.IMAGE_FILEPATH,
CITY_DIM.AUTO_GENERATED,
COUNTRY_INCOME_GROUP.INCOME_GROUP,
COUNTRY_INCOME_GROUP.LENDING_CATEGORY
FROM AQICN
LEFT JOIN STATION_DIM ON AQICN.UID = STATION_DIM.UID
LEFT JOIN CITY_DIM ON STATION_DIM.CITY = CITY_DIM.CITY AND STATION_DIM.COUNTRY = CITY_DIM.COUNTRY
LEFT JOIN COUNTRY_INCOME_GROUP ON STATION_DIM.COUNTRY_CODE2 = COUNTRY_INCOME_GROUP.COUNTRY_CODE2
-- To filter for the top 25 pre-selected cities, uncommented the below
--INNER JOIN PRIORITY_CITIES ON CITY_DIM.CITY = PRIORITY_CITIES.CITY AND CITY_DIM.COUNTRY = PRIORITY_CITIES.COUNTRY
```

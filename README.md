# atta-data

`data/ATTA.sqlite` is a database file which contains the following tables for use in the React appplication:

- aqicn_staging

This is a staging evironment for the ETL process of loading data to aqicn

- aqicn
This the main fact table where we store aqi, it contains the following fields:
  - uid: unique station id
  - lat: latitude
  - lon: longitude
  - aqi: aqi value
  - station_name: The name of the station where the aqi was recorded
  - recorded_at: the datetime when the aqi was recorded
- station_dim
This is a dimension table for more information about the station, it contains the following fields:
  - uid: unique station id
  - lat: latitude
  - lon: longitude
  - station_name: The name of the station where the aqi was recorded
  - city: the city
  - country: the country
  - country_code2: the 2 letter country code
- city_dim
This is a dimension table which contains the file path of an image relevent to the city
  - city
  - country
  - image_filepath
- country_income_group
  - economy:
  - region:
  - country_code2: the 2 letter country code
  - country_code3: the 3 letter country code
  - income_group:
  - lending_category:
- priority_cities
This is a list of shortlisted cities to display initally on the map
  - city
  - country

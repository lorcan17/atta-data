import sqlite3
import os
import requests
access_key = os.environ.get("UNSPLASH_ACCESS_KEY")
# 50 requests per hour

# Connect to the database
connection = sqlite3.connect('data/atta.sqlite')
cursor = connection.cursor()
query = '''
SELECT DISTINCT CITY, COUNTRY FROM STATION_DIM'''
# Fetch data from the database
cursor.execute(query)
city_country_combinations = cursor.fetchall()

# Close the database connection
connection.close()

# Set a maximum number of images to download
max_images = 49
downloaded_images = 0

for city, country in city_country_combinations:
    # Construct the filename based on city and country
    if city:
        search_query = f"{city} {country} city"
        filename = f"{city}_{country}.jpg"
    else:
        search_query = f"{country}"
        filename = f"{country}.jpg"
    filepath = os.path.join('images', filename)
    
    # Construct the search query for Unsplash API
    if city:
        search_query = f"{city} {country} city"
    else:
        search_query = f"{country} city"
    url = f"https://api.unsplash.com/search/photos/?query={search_query}&client_id={access_key}"
    
    # Make a request to the Unsplash API
    response = requests.get(url)
    data = response.json()
    
    # Check if there are any results
    if "results" in data and len(data["results"]) > 0:
        image_url = data["results"][0]["urls"]["regular"]
        
        # Download the image
        image_response = requests.get(image_url)
        with open(filepath, "wb") as image_file:
            image_file.write(image_response.content)
        
        downloaded_images += 1
        print(f"Downloaded image for {city}, {country}")
    else:
        print(f"No image found for {city}, {country}")



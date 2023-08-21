import sqlite3
import os
import requests

access_key = os.environ.get("UNSPLASH_ACCESS_KEY")

# Connect to the database
connection = sqlite3.connect('data/atta.sqlite')
cursor = connection.cursor()
query = '''
SELECT DISTINCT CITY, COUNTRY FROM CITY_DIM
WHERE AUTO_GENERATED = 0'''
# Fetch data from the database
cursor.execute(query)
city_country_combinations = cursor.fetchall()

# Close the database connection
connection.close()

# Set a maximum number of images to download
max_images = 49
downloaded_images = 0

for city, country in city_country_combinations:
    if downloaded_images >= max_images:
        break
    
    if city:
        search_query = f"{country} {city} city"
        filename = f"{country}_{city}.jpg"
    else:
        search_query = f"{country}"
        filename = f"{country}.jpg"
    
    filepath = os.path.join('images', filename)
    
    url = f"https://api.unsplash.com/search/photos/?query={search_query}&client_id={access_key}"
    
     # Make a request to the Unsplash API with proper SSL verification
    response = requests.get(url, verify=True)
    
    try:
        data = response.json()
    except requests.exceptions.JSONDecodeError:
        print(f"JSON decoding error for {city}, {country}")
        continue
    
    # Check if there are any results
    if "results" in data and len(data["results"]) > 0:
        image_url = data["results"][0]["urls"]["regular"]
        
        # Download the image
        image_response = requests.get(image_url)
        with open(filepath, "wb") as image_file:
            image_file.write(image_response.content)
        
        downloaded_images += 1
        print(f"Downloaded image for {city}, {country}")

        # Update column auto_generated to 1 for this row
        connection = sqlite3.connect('data/atta.sqlite')
        cursor = connection.cursor()
        update_query = '''
        UPDATE CITY_DIM
        SET auto_generated = 1, image_filepath = ?
        WHERE CITY = ? AND COUNTRY = ?
        '''
        cursor.execute(update_query, (filepath, city, country))
        connection.commit()
        connection.close()
        
    else: 
        print(f"No image found for {city}, {country}")

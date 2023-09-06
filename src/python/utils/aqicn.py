import requests
import json
import os


class aqicn:
    def __init__(self):
        pass

    def get_aqi_within_bounds(self, token, bounds):
    
        url = f"https://api.waqi.info/v2/map/bounds/?latlng={bounds}&token={token}"
        response = requests.get(url)
        data = response.json()    
        if data["status"] != "ok":
            error_message = data.get("data", "Unknown error")
            raise Exception(error_message)
        # Convert the 'aqi' values to integers
        data = data["data"]
        for entry in data:
           try:
               entry['aqi'] = int(entry['aqi'])  # Try to convert 'aqi' to integer
           except ValueError:
               # Handle non-integer 'aqi' values, setting them to a default value
               entry['aqi'] = None  # Convert 'aqi' from string to integer
        return data




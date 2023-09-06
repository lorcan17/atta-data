import requests
import json
import os

token = os.environ.get("AQICN_TOKEN")

##################################################
# GET AQI
##################################################
def get_aqi_within_bounds(token, bounds):
    
    url = f"https://api.waqi.info/v2/map/bounds/?latlng={bounds}&token={token}"
    response = requests.get(url)
    return response
    
world_bound =  "-90,-180,90,180"
data = get_aqi_within_bounds(token, world_bound)
data = data.json()
pretty_response = json.dumps(data, indent=4)
#print(pretty_response)
    
if data["status"] != "ok":
    error_message = data.get("data", "Unknown error")
    raise Exception(error_message)


with open("data/json/aqicn.json", "w") as outfile:
    json.dump(data, outfile)

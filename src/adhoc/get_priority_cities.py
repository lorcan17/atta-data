# GET SOCIO ECONOMIC FACTORS
import json
import pandas as pd

# Read the csv file into a DataFrame
file_path = "data/raw/priority_cities.csv"  # Update with the actual path
sheet_name = "List of economies"
df = pd.read_csv(file_path)

# Convert the DataFrame to a list of dictionaries
data_as_dict_list = df.to_dict(orient="records")

with open("data/json/priority_cities.json", "w") as outfile:
    json.dump(data_as_dict_list, outfile)
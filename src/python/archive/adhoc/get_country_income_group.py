# GET SOCIO ECONOMIC FACTORS
import json
import pandas as pd
import pycountry

# Read the Excel file into a DataFrame
excel_file_path = "data/raw/CLASS.xlsx"  # Update with the actual path
sheet_name = "List of economies"
df = pd.read_excel(excel_file_path, sheet_name=sheet_name)

# Convert the DataFrame to a list of dictionaries
data_as_dict_list = df.to_dict(orient="records")

# Convert 3-letter country code to 2-letter code
for entry in data_as_dict_list:
    three_letter_code = entry["Code"]
    try:
        country = pycountry.countries.get(alpha_3=three_letter_code)
        if country:
            two_letter_code = country.alpha_2
            #print(f"3-letter code: {three_letter_code}, 2-letter code: {two_letter_code}")
            entry["country_code2"] = two_letter_code.lower()
        else:
            pass
            #print("Country not found")
    except LookupError:
        print("Invalid 3-letter code")

with open("data/json/sample_class.json", "w") as outfile:
    json.dump(data_as_dict_list, outfile)
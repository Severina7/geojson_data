#!/usr/bin/python
import json
import os
from pathlib import Path
# print(os.getcwd())
# print(os.listdir())

# Setting up the working directory path
working_directory = Path(__file__).absolute().parent

# This script gets the file in a geojson form then extracts the id element 
# in 'external_id' and put it at the same level as 'type', 'properties', and 'geometry'
with open(working_directory / 'la-zip-code-areas-2012.geojson') as f:
    json_contents = json.loads(f.read())
    features = json_contents["features"]
    for i in features:
        i["id"] = i["properties"]["external_id"]
        json_contents["features"] = features
    # Normalized geojson for salesforce map
    out_file = open("la_zip_code_areas_2012.json", "w")
    out_file.write(json.dumps(json_contents))
    out_file.close()
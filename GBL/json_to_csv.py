# convert from JSON to CSV 

import csv
import json
import os
import pandas as pd

json_path = r"edu.cornell-master"	# point to path  <-- change to user input?
csv_name = "cornell"	# name for csv <-- change to user input?

dataset = []	# empty list

# through all items, format and append to dataset list
for path, dir, files in os.walk(json_path):
    for filename in files:
    	if filename.endswith(".json"):
            file_path = os.path.join(path, filename)
            json_file_open = open(file_path, 'rb')
            data = json_file_open.read().decode('utf-8', errors='ignore')
            loaded = json.loads(data)
            dataset.append(loaded)


df = pd.DataFrame(dataset)		# convert dataset into dataframe

df.to_csv("{}.csv".format(csv_name)) 
'''
This script pulls the initial Salmon Run battle
data that I already have on file
'''

import json
import pandas as pd
import requests

# read the secrets information
with open("secrets.json") as f:
    secrets = json.load(f)

# set the variables accordingly
username = secrets['USERNAME']
password = secrets['PASSWORD']
api_key = secrets['API_KEY']

# make the request for the Salmon Run JSON
r = requests.get('https://stat.ink/@super64guy/salmon3.json')
json_obj = json.loads(r.text)

# generate the df
df = pd.DataFrame()

for obj in json_obj:
    tmp_df = pd.DataFrame.from_dict(obj, orient="index").T
    df = pd.concat([df, tmp_df])

print(df.head(5))
df.to_csv('./data/statink-super64guy-salmonrun.csv', index=False)
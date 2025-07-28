'''
This script pulls the initial Salmon Run battle
data that I already have on file
'''

import pandas as pd
import json
import requests

json_objs = []
i = 1
url = 'https://stat.ink/@super64guy/salmon3.json?page='

# start with collecting all of our data
while True:
    data = json.loads(requests.get(url=url+str(i)).text)
    if len(json_objs) != 0 and data == json_objs[-1]:
        break
    json_objs.append(data)
    i += 1

# now parse the data into a csv file
df = pd.DataFrame()
for obj in json_objs:
    for json_obj in obj:
        tmp_df = pd.DataFrame.from_dict(json_obj, orient="index").T
        tmp_df.set_index('id', inplace=True)
        df = pd.concat([df, tmp_df])


# write the data to a file
df.to_csv('./data/statink-super64guy-salmonrun.csv', index=True)
print('Downloaded', len(df.index), 'jobs!')
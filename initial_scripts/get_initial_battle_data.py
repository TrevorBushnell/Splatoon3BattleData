'''
This script pulls all initial worldwide battle data
'''

import pandas as pd
import os
import warnings

warnings.filterwarnings("error")

path = './data/public/'
files = os.listdir(path)
files.sort()

df = pd.DataFrame()

another_df = pd.read_csv(path + '2023-01-01.csv')
print('2023-01-01.csv')
print(another_df['rank'].dtype)

for filename in files:
    try:
        tmp_df = pd.read_csv(path + filename)
    except pd.errors.DtypeWarning:
        print(filename)
        print(tmp_df['rank'].dtype)
    # df = pd.concat([df, tmp_df])
    # os.remove(filename)



# df.to_csv('./data/statink-worldwide.csv', index=False)
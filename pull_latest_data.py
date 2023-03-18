'''
Script that runs daily via GH Actions.

Pulls the latest battle data
'''

from datetime import date
from datetime import timedelta
import requests
import os
import pandas as pd
import json
import time

'''
Driver of the script
'''
def main():
    download_my_battle_data()
    get_missing_salmon_run_data()
    get_worldwide_data()


'''
Import the secret variables (uname, pass, api_key)

Returns: The username, password, and api_key
that are stored in the secrets.json file
'''
def get_secrets():
    # with open('secrets.json') as f:
    #     secrets = json.load(f)
    
    # username = secrets['USERNAME']
    # password = secrets['PASSWORD']
    # api_key = secrets['API_KEY']
    username = os.environ.get("USERNAME")
    password = os.environ.get("PASSWORD")
    api_key = os.environ.get("API_KEY")

    return username, password, api_key

'''
Import the secret variables from a json file (used for testing)
'''
def get_json_secrets():
    with open('secrets.json') as f:
        secrets = json.load(f)

    username = secrets['USERNAME']
    password = secrets['PASSWORD']
    api_key = secrets['API_KEY']

    return username, password, api_key

'''
Helper function that returns today's date

Returns: Today's date in YYYY-MM-DD format
'''
def get_today_date():
    return str(date.today())


'''
Helper function that returns yesterday's date

Returns: Today's date in YYYY-MM-DD format
'''
def get_yesterday_date():
    return str(date.today() - timedelta(days=1))


'''
Uses selenium to download my json file for
battle data, then appends the results to
./data/statink-super64guy.csv
'''
def download_my_battle_data():
    # get the secret values
    username, password, api_key = get_secrets()
    if api_key == None:
        username, password, api_key = get_json_secrets()

    # get the missing battle ids and add them to the csv file
    df = pd.read_csv('./data/statink-super64guy.csv', index_col='id')
    ids = get_missing_battle_ids()

    url = 'https://stat.ink/@super64guy/spl3/index.json'
    r = requests.get(url=url)
    json_data = json.loads(r.text)

    for obj in json_data:
        if obj['uuid'] in ids:
            tmp_df = pd.DataFrame.from_dict(obj, orient="index").T
            tmp_df.set_index('id', inplace=True)
            df = pd.concat([df, tmp_df])

    df.to_csv('./data/statink-super64guy.csv', index=True)


'''
Function that finds the battle_ids that are not already gathered

Returns: a list with all battle ids not already recorded in my csv file
'''
def get_missing_battle_ids():
    username, password, api_key = get_secrets()
    if api_key == None:
        username, password, api_key = get_json_secrets()
    url = 'https://stat.ink/api/v3/s3s/uuid-list'
    header = {'Authorization': 'Bearer ' + api_key}
    json_ids = json.loads(requests.get(url=url, headers=header).text)
    csv_ids = pd.read_csv('./data/statink-super64guy.csv')['uuid'].tolist()
    return list(set(json_ids) - set(csv_ids))


'''
Function that gathers the latest salmon run data and updates it
'''
def get_missing_salmon_run_data():
    ids = get_missing_salmon_run_ids()

    df = pd.read_csv('./data/statink-super64guy-salmonrun.csv', index_col='id')

    url = 'https://stat.ink/@super64guy/salmon3.json'
    r = requests.get(url=url)
    json_data = json.loads(r.text)

    for obj in json_data:
        if obj['uuid'] in ids:
            tmp_df = pd.DataFrame.from_dict(obj, orient="index").T
            tmp_df.set_index('id', inplace=True)
            df = pd.concat([df, tmp_df])

    df.to_csv('./data/statink-super64guy-salmonrun.csv', index=True)


'''
Function that finds the salmon run jobs that are not currently in my csv file

Returns: list of ids for salmon run jobs that are not already in my csv file
'''
def get_missing_salmon_run_ids():
    username, password, api_key = get_secrets()
    if api_key == None:
        username, password, api_key = get_json_secrets()
    url = 'https://stat.ink/api/v3/salmon/uuid-list'
    header = {'Authorization': 'Bearer ' + api_key}
    json_ids = json.loads(requests.get(url=url, headers=header).text)
    csv_ids = pd.read_csv('./data/statink-super64guy-salmonrun.csv')['uuid'].tolist()
    return list(set(json_ids) - set(csv_ids))


'''
Function that finds the lastest worldwide csv file and downloads it
'''
def get_worldwide_data():
    today = get_yesterday_date()
    filename = today + '.csv'
    url = 'https://dl-stats.stat.ink/splatoon-3/battle-results-csv/'
    url += (today[:4] + '/' + today[5:7] + '/' + filename)

    r = requests.get(url=url)
    
    with open('./data/worldwide/' + filename, 'wb') as f:
        f.write(r.content)


if __name__ == "__main__":
    main()

# https://dl-stats.stat.ink/splatoon-3/battle-results-csv/2023/01/
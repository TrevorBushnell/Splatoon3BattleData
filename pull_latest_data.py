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
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
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

    # initialize the web driver
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome('chromedriver',options=chrome_options)
    driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': "./data"}}
    command_result = driver.execute("send_command", params)

    # Go to the json website
    driver.get("https://stat.ink/user/download3?type=user-json")

    # Find the username/email field and send the username to the input field.
    uname = driver.find_element("id", "loginform-screen_name") 
    uname.send_keys(username)

    # Find the password input field and send the password to the input field.
    pword = driver.find_element("id", "loginform-password") 
    pword.send_keys(password)

    # Click sign in button to login the website.
    driver.find_element("xpath", "/html/body/main/div/div[1]/div[1]/div/div[2]/form/div[4]/button").click()

    # Wait for login process to complete. 
    WebDriverWait(driver=driver, timeout=10).until(
        lambda x: x.execute_script("return document.readyState === 'complete'")
    )

    # Verify that the login was successful.
    error_message = "Incorrect username or password."
    # Retrieve any errors found. 
    errors = driver.find_elements(By.CLASS_NAME, "flash-error")

    # When errors are found, the login will fail. 
    if any(error_message in e.text for e in errors): 
        print("[!] Login failed")
    else:
        print("[+] Login successful")

    # give the driver time to download the file, then close
    time.sleep(5)
    driver.close()

    # unpack the .gz file so we can read the JSON objects
    current_dir = os.getcwd()
    os.chdir('./data')
    os.system('gzip -d statink-super64guy.json.gz')
    os.system('rm -rf statink-super64guy.json.gz')
    os.chdir(current_dir)

    # get the missing battle ids and add them to the csv file
    df = pd.read_csv('./data/statink-super64guy.csv')
    ids = get_missing_battle_ids()

    for i in ids:
        url = 'https://stat.ink/api/v3/battle/' + i
        r = requests.get(url=url)
        json_obj = json.loads(r.text)
        tmp_df = pd.DataFrame.from_dict(json_obj, orient="index").T
        df = pd.concat([df, tmp_df])

    df.to_csv('./data/statink-super64guy.csv')
    os.remove('./data/statink-super64guy.json')




'''
Function that finds the battle_ids that are not already gathered

Returns: a list with all battle ids not already recorded in my csv file
'''
def get_missing_battle_ids():
    csv_ids = pd.read_csv('./data/statink-super64guy.csv')['id'].tolist()

    json_ids = []

    with open('./data/statink-super64guy.json') as f:
        for obj in f:
            json_ids.append(json.loads(obj)['id'])

    return list(set(json_ids) - set(csv_ids))


'''
Function that gathers the latest salmon run data and updates it
'''
def get_missing_salmon_run_data():
    ids = get_missing_salmon_run_ids()

    df = pd.read_csv('./data/statink-super64guy-salmonrun.csv')

    for i in ids:
        url = 'https://stat.ink/api/v3/salmon/' + i
        r = requests.get(url=url)
        tmp_df = pd.DataFrame.from_dict(json.loads(r.text), orient="index").T
        df = pd.concat([df, tmp_df])

    df.to_csv('./data/statink-super64guy-salmonrun.csv') 


'''
Function that finds the salmon run jobs that are not currently in my csv file

Returns: list of ids for salmon run jobs that are not already in my csv file
'''
def get_missing_salmon_run_ids():
    username, password, api_key = get_secrets()
    url = 'https://stat.ink/api/v3/salmon/uuid-list'
    header = {'Authorization': 'Bearer ' + api_key}
    json_ids = json.loads(requests.get(url=url, headers=header).text)
    csv_ids = pd.read_csv('./data/statink-super64guy-salmonrun.csv')['id'].tolist()
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
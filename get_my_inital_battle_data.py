'''
This script pulls the initial battle data that 
I currently have uploaded
'''

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os
import pandas as pd
import json

# read the secrets information
with open("secrets.json") as f:
    secrets = json.load(f)

# set the variables accordingly
username = secrets['USERNAME']
password = secrets['PASSWORD']
api_key = secrets['API_KEY']

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


df = pd.DataFrame()
with open("./data/statink-super64guy.json") as f:
    for json_obj in f:
        data = json.loads(json_obj)
        tmp_df = pd.DataFrame.from_dict(data, orient="index").T
        tmp_df.set_index('id', inplace=True)
        df = pd.concat([df, tmp_df])

print(df.head)
df.to_csv('./data/statink-super64guy.csv', index=True)
time.sleep(3)
os.remove('./data/statink-super64guy.json')
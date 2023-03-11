# Project Proposal

## 0. Review of Project

As from before, I am building a project surrounding my Splatoon 3 battle data. Using Streamlit, I will create a dashboard to display various aspects of my battle data as well as the data of every match that takes place worldwide. I will also do machine learning models to predict the outcomes of matches based on the weapons and gear abilities chosen by players in the match.

## 1. Main Motivation

This game pisses me off. I want to have fun, but I lose more than I win. Considering this is a children's game, I always blame my teammates for my loss. While the age of every player is anonymized, data on their performance can still be compared to my performance. As such, I can compare my performance to the performance of my teammates to see if I actually am that much better than everyone else on my team.

Additionally, I don't ever have any good gear loadouts. In Splatoon, you can have 3 pieces of gear equipped on your body. Each piece of gear has 1 main slot and 3 sub slots which can hold abilities. These abilities include recharging your ink faster, using less ink per shot, increasing your running speed, and more. The abilities you get on gear that you buy are randomized, but you can spend money and other resources to get custom gear builds. I would love to be able to see what the gear loadouts of players around the world are so that I can make informed decisions on what gear loadouts I should be building for my character. 

Finally, weapons are always changing in Splatoon. There are always "bad" weapons that rarely get used, and "good" weapons that are used constantly in matches. Additionally, new weapons get released roughly every 60 days and balance patches are introduced that change how certain weapons operate. If this project stays up, I can see what weapons are used in battles and if the weapons that are constantly used change as new weapons are added and other weapons are modified in balance patches.

## 2. Addressing the Project Requirements

### 2.1: Tech Stack

The entirety of this project will be coded in Python, thanks to the incredible simplicity of Streamlit. The initial data cleaning and developing of functions will be conducted inside Jupyter notebooks as a sort of sandbox environment, then migrated to a Streamlit webapp for the deployment of the project. The data will be stored in BigQuery tables so that I don't have to keep 8.5+ million instances downloaded in a single GitHub repository. I will have a GitHub Action that will continuously pull my current Splatoon 3 battle data, put it in a pandas dataframe, and append the resulting data into various BigQuery tables to then be queried as I need data. 

### 2. Data Sources

All of my data is personal to me and the battles that I participate in. There will be three categories of data that I will analyze:

* **generic battle data:** this is data regarding MY matches in the basic PVP format - two teams of 4 covering the ground with ink to have the most turf claimed. 
* **salmon run data:** my jobs from the PVE mode. This is where a team of 4 work together to fight oncoming waves of enemies over time with randomized weapons.
* **worldwide data:** every match that has ever happened in Splatoon 3. Player names ananymized.

Each of the following data categories will be stored in its own BigQuery table to be pulled at the desired time. It is also here that I would like to highlight to community developed tools that I am sincerely grateful for. [s3s](https://github.com/frozenpandaman/s3s) is a Python script that upon running automatically uploads any Splatoon battle that I have played and will continue to upload data as new battles come in. Generally I run this script when I start a play session so that I capture that play session's data live. The script uploads the data to [stat.ink](https://stat.ink) which is a website that hosts a player's Splatoon 3 battle data. This website also has an active developer that I have been in contact with and a simple API that lets me pull down my data from this website into a format that I can use for data analysis. Additionally, the developer cultivates public csv files with every battle that has taken place since the launch of the game back in September 2022. Without these tools, this project would be really difficult and tedious to do, and I am forever grateful to these developers for the work that they have put into these products so that I can have a timely data source.

### 2.3: What I Am Looking to Find

Possible analysis information to find include:

* how often I am the highest ranked player on my team
* how high I rank based on the weapon I play (I play quite a few weapons)
* how high I rank based on the game mode
  * even within my normal battle data, there are various different game modes that rotate every 2 hours. Perhaps there are game modes that I am better at than others. I predict that I am the best at Splat Zones because I generally play long ranged weapons that prevent people from pushing, which is super important in that mode
* how common certain weapons are played in matches
* the average amount of gear abilities stacked on various players gear, to better inform what my gear compositions should be
  * potentially also sort this by weapon, as maybe different weapons play better with different gear abilities (a sniper might not have a need for increased run speed if they stay in the same spot for the majority of the match for example)
* use machine learning to predict a winning team based off of weapon choice and gear composition
  * this might be tough as there are 8 weapons and LOTS of gear abilities so maybe this is not as feasible as I think. Or maybe it is possible and the model would just suck!

### 2.4: Deployment

Deployment will look like a webapp hosted by Streamlit. Right now I anticipate on web page for each data source with plots that you can choose to view and filter and then a final page for a machine learning model predictor where you can input weapon and gear combinations and see if your team would win.

### 2.5: Cloud Platforms and Tools Needed

Right now just Google BigQuery! From my research it seems like those tables will support tons and tons and tons of rows with minimal cost. With pricing at a few cents per GB per month, I'm going to spend a few cents a month to have this dataset which is something I'm completely worth taking. Querying costs also don't seem to be particularly expensive with what I would be querying and how often I would be querying it.

## 3: Risks and Other Concerns

One concern I have right now is whether I even need Google BigQuery to do the work that I need to do. I'm simply using cloud storage with BigQuery because the worldwide data is MASSIVE (as I've said, over 8 million instances). My personal data fits in csv files that are nice and neat in my GitHub repository, so loading them locally and running my data analysis in Python would be easier. It might be worth looking into other solutions for storing the worldwide data so that I can maybe avoid cloud access entirely. There is Google Cloud Storage that I could use and pull data down from, but my concern with that idea is that every day is stored in a csv and what if I want to work with data from multiple days? At that point I feel it would just be easier if everything was in one central table which is why I thought BigQuery would be the smartest move.
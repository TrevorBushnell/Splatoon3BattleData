# CPSC325: Research Proposal

## 1: General Topic Areas

My project that I am wanting to focus on is a project centered around my battle data from Splatoon 3. The final result will be to use EDA and dashboarding/data visualization to help me analyze my past battles so that I can improve my performance in game. Additionally, I will be implementing some machine learning model to determine what team composition is required to win at Splatoon. This way, I can use this model to figure out what I should use in the game (both in terms of weapons and the gear that I equip myself with). Additioanlly, other people could use the model to figure out what they should use when they are playing Splatoon 3. General topic areas to complete this would be EDA, data visualization, webscraping and webpage navigation, continuous data collection, and machine learning.


## 2. General Data Science Skills Required

In order to complete the project, I am going to be using Python, as Python provides not only incredible tools for data analysis but also provides plenty of frameworks for deploying webapps seamlessly as opposed to languages like R or Julia. Additionally, I will need to be able to deploy some sort of web app. Right now, I plan on building this webapp using Streamlit, which makes web development stupid easy - making this perfect for data scientists! I also will need some place to store this data. Right now I am simply storing a bunch of CSV files in this GitHub repository, but that might not be the most efficient way to store all this data. Using Google Cloud Storage for developers or Google Big Query to put all this information into a giant database. Additionally, I can learn to deploy a Streamlit app on GCP instead of having Streamlit host it for me. I also will need to learn how to interact with a web page, since my battle data is stored in a JSON file once I log into my account. I also want to become better at creating visualizations - make more complex graphs beyond what I've learned in my data science classes. I also will need to learn about CRON jobs to continuously grab my latest splatoon battle data. Finally, I will need an understanding of different machine learning frameworks so that I can make a project more effectively. 

## 3. Already Known Skills

Currently, I am already familiar with Streamlit since I built a web app using it in my final project for CPSC321. I also already have a working CRON Job through a GitHub Action that already uses Selenium to log into the website and grab my battle data json (my repo is really disorganized right now, but feel free to check out `pull_latest_data.py` to see everything!). This means that I learned on my own, but now have completed and understand webscraping and CRON jobs as it pertains to my project. I already have an understanding of scikit-learn and some of the basic ML models that come with that package.

## 4. What I Need to Learn

I need to learn how to create better and more complex visualizations with matplotlib and seaborn. This will allow me to create more interesting graphics. I also need to at least explore what other ML models are capable in other ML libraries like PyTorch and TensorFlow - while I may not want to use these packages I don't really know what they are good at, and I should at least understand what they are successful in so that I can decide whether or not I should use them. Finally, I need to learn the various products of Google Cloud Platform so that I can deploy my web app there.

## 5. How I Will Learn These Concepts

DataCamp has courses on basic, intermediate, and advanced plotting with matplotlib and seaborn, so I will complete those courses to get my data viz up to snuff. Additionally I need to learn about the various Google Cloud Platform options, so I will complete the certifications taht were shown in class so I can learn more about them. I also will need to learn how to deploy a Streamlit app to GCP, which the develops have a blog post on that I can read. Potentially what I might do for practice if time allows is to turn my CPSC222 final project into a web app that is built with Streamlit and hosted with GCP so I can solidify streamlit skills without building a huge project and then practice deploying it.

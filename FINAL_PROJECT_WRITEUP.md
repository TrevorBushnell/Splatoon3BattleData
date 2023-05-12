# Final Project Writeup

This project was really fun for me to develop, and it has definitely informed me of what weapons I am good at and how I should modify my gameplay throughout my playtime with Splatoon 3. 


## Updates to the Project

* The worldwide component was removed from the project. It took me a long time for me to get the data visualizations that I really wanted, and the visualizations that I did end up making I did not feel were comprehensive and worthwhile. If I didn't find any value from the visualizations that I made, it didn't make sense for me to include the worldwide data and the visualizations. 
  * This means that Google BigQuery was rendered not needed because my personal data was much smaller and therefore was able to fit into csv files that could be easily parsed in my GitHub repo via my GitHub Action
* The data still pulls "daily", however the daily script won't do anything if I don't play the game. Because of different busy seasons of my life, it's not often that I am consecutively playing daily. The script will still run successfully even if I don't play on that day and therefore the data is still timely as whenever I do play the data gets downloaded appropriately.
* There was no machine learning component. I personally only came up with a machine learning goal because everyone else was. When I was having fun dashboarding and coming up with unique graphs I could use, I found that it was a better product (and more enjoyable experience!) if I did not implement machine learning.
* I added plots for Salmon Run! For some reason I never included this in my project proposal which is shocking because I always intended to do this. I must have forgotten to include that. Either way, people can see plots about my average objectives that I obtain sorted by stage!
* I added some new plots with my normal battle data! Notably KD (kill-death) ratio per weapon (then sorted by game mode). As I was developing, I felt like this plot would be useful to see what weapons I am really good with and which weapons I am still learning with
* Another new plot I added was the average turf inked per stage. This gives me a way to see how well I paint with various weapons which is something that is important to me and I have been actively using in my gameplay.

## Testing

Testing looked like trying to get deployments up early. The beauty of streamlit is that if you hook it up to a GitHub repo, it will automatically update your web app after every push to your repo. So that I wouldn't have any stress about a failed deployment later (since deployment can be a pain) I got a deployment working EARLY so that I could be sure that my deployment could work. I also gave my deployment to my roommates since they see me play this game all the time in the living room. They would give me feedback about how my charts were presented and talk about the readability. I also gave my deployments to my gaming friends that I have met through speedrunning. These people also play lots of hours of splatoon (and one of them is currently majoring in data analytics!) and was able to help give feedback on how my data was presented. 

## Further Improvements

* Seeing how I can integrate the worldwide data to actually have useful plots. There were so many cool ideas that I had that simply didn't pan out how I wanted them to. I'm in a Splatoon Discord server so I might see what people in the community as a whole would want to see.
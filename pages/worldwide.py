import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import utils

st.write("""
# Worldwide Data

THIS PAGE NEEDS TO BE IMPLEMENTED

At the very least I will display the same kinds of statistics that I would be display on my main page, except this time it would just be for all the worldwide data (close to roughly 8.5 million instances). These first all need to be stored in a BigQuery database because my GitHub repo is getting quite massive to be hosting all of this data here on GitHub.
""")


# Weapons Stacked Against Each Other
st.write("""
## Plotting Weapon Performance VS Other Weapons

This would be a heatmap where a weapon would get a point if a given team wins - gives the opportunity to see how weapons stack up against each other. 

Maybe I could also do this for KD ratio or other general stats ona  weapon-by-weapon basis?
""")

# Gear Loadouts for Weapons
st.write("""
## Gear Loadouts Per Weapon

This would be a graph with a selectbox. Pick your weapon with a selectbox and then you would get a graph that shows the average amount of gear stats for each weapon. I would LOVE this graph because I have absolutely terrible gear and I have the in-game resources to customize my gear and I want to have different gear loadouts for the different weapons that I like.
""")
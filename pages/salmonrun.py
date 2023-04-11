import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import utils

salmonrun_df = pd.read_csv('./initial_scripts/test_salmon.csv', index_col='id')

st.write("""
# My Salmon Run Data

Most shooters have two different game modes:

PVP (Player VS Player): you team up with humans and play against other humans
PVE (Player VS Enemy): you team up with humans to try and kill as many computer enemies as possible

In Splatoon 3, the main way to play is PVP - you find a team of four and compete against another team of four humans. The data on my main page (as well as the data on the worldwide page) is all data from the traditional PVP mode. However, Splatoon 3 also has a separate game mode called Salmon Run, which is a PVE mode. In this game mode, you team up with three other humans to kill as many Salmonids (the enemies) as possible over the course of 3 waves. During each wave, you have 100 seconds to kill as many boss salmonids and dump their precious golden eggs into the team basket. You win if you collect the minimum number of golden eggs needed in the alotted time over 3 rounds. You lose if everyone on your team dies or you don't meet the golden egg quota at the end of a wave when time runs out. 

The following charts on this page display the various aspects of my salmon run gameplay:
""")

# General salmon run info
st.write("""## General Salmon Run Stats""")

general_options = st.selectbox(label='Choose General Type', options=['Overall', 'By Stage'])

if general_options == 'Overall':
    st.write("**TOTAL JOBS:**", len(salmonrun_df.index))
    st.write("**CLEAR%:**", salmonrun_df['clear_waves'].value_counts()[3]/len(salmonrun_df.index) * 100)
    st.write("**AVERAGE WAVES CLEARED:**", salmonrun_df['clear_waves'].mean())
    st.write("**NUMBER OF KING SALMONIDS ENCOUNTERED:**", salmonrun_df['king_salmonid'].count())
    st.write("**KING SALMONID WIN%:**", salmonrun_df['clear_extra'].value_counts()[True] / salmonrun_df['king_salmonid'].count() * 100)
    st.write("**AVERAGE DANGER RATE:**", salmonrun_df['danger_rate'].mean())
    st.write("**PEAK DANGER RATE:**", salmonrun_df['danger_rate'].max())
    st.write("**NUMBER OF BIG RUN JOBS:**", salmonrun_df['big_run'].value_counts()[True])
elif general_options == 'By Stage':
    stage_options = st.selectbox(label='Choose Your Stage of Choice', options=set(salmonrun_df['stage'].to_list()))
    grouped_df = salmonrun_df.groupby('stage').get_group(stage_options)
    st.write("**TOTAL JOBS:**", len(grouped_df.index))
    st.write("**CLEAR%:**", grouped_df['clear_waves'].value_counts()[3]/len(salmonrun_df.index) * 100)
    st.write("**AVERAGE WAVES CLEARED:**", grouped_df['clear_waves'].mean())
    # st.write("**NUMBER OF KING SALMONIDS ENCOUNTERED:**", salmonrun_df['king_salmonid'].count())
    # st.write("**KING SALMONID WIN%:**", grouped_df['clear_extra'].value_counts()[True] / salmonrun_df['king_salmonid'].count() * 100)
    st.write("**AVERAGE DANGER RATE:**", grouped_df['danger_rate'].mean())
    st.write("**PEAK DANGER RATE:**", grouped_df['danger_rate'].max())

# Golden Eggs Collected Per Stage
st.write("""
## Eggs Collected Per Stage

To be implemented - have a selectbox to distinguish between golden eggs and normal power eggs (and maybe compare myself against my other teammates?)
""")

# Average Bosses Killed
st.write("""
## Average Bosses Killed

To be implemented - will be done overall and by stage (maybe compare against my other teammates?)
""")

# Compare Rescues (myself) to Rescues (teammates)
st.write("""
## Rescues (myself VS teammates)

To be implemented - do this overall and per stage
""")

# Compare Revives (myself) to Revives (teammates)
st.write("""
## Revives (myself VS teammates)

To be implemented - do this overall and per stage
""")
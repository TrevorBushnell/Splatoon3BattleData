import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import utils
import altair as alt

salmonrun_df = pd.read_csv('./data/salmon-run-data.csv', index_col='id')

st.write("""
# My Salmon Run Data

> NOTE: Due to Nintendo shutting down the ability for me to automatically pull my battle data from the game, this data stops after the end of 2023. Thanks for understanding!

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

Golden eggs are needed to win in Splatoon. Power eggs are needed to gain more rewards upon winning.
""")
         
eggs_options = st.selectbox(label='Specify Egg Type', options=['Golden Eggs', 'Power Eggs'])

if eggs_options == 'Golden Eggs':
    grouped_data = salmonrun_df.groupby('stage')['my_golden_eggs'].mean().reset_index()
    st.altair_chart(alt.Chart(grouped_data).mark_bar().encode(
        x=alt.X('stage:N', title='Stage'),
        y=alt.Y('my_golden_eggs:Q', title='Golden Eggs Aquired')
    ).properties(
        width=400,
        height=400
    ))

elif eggs_options == 'Power Eggs':
    grouped_data = salmonrun_df.groupby('stage')['my_power_eggs'].mean().reset_index()
    st.altair_chart(alt.Chart(grouped_data).mark_bar().encode(
        x=alt.X('stage:N', title='Stage'),
        y=alt.Y('my_power_eggs:Q', title='Power Eggs Aquired')
    ).properties(
        width=400,
        height=400
    ))

# Average Bosses Killed
st.write("""
## Average Bosses Killed Per Stage

To be implemented - will be done overall and by stage (maybe compare against my other teammates?)
""")

grouped_data = salmonrun_df.groupby('stage')['my_boss_kills'].mean().reset_index()
st.altair_chart(alt.Chart(grouped_data).mark_bar().encode(
    x=alt.X('stage:N', title='Stage'),
    y=alt.Y('my_boss_kills:Q', title='Golden Eggs Saved')
).properties(
    width=400,
    height=400
))


# Compare Rescues (myself) to Rescues (teammates)
st.write("""
## Rescues By Stage

Rescues is the number of times you revive your teammates.
""")

grouped_data = salmonrun_df.groupby('stage')['my_rescues'].mean().reset_index()
st.altair_chart(alt.Chart(grouped_data).mark_bar().encode(
    x=alt.X('stage:N', title='Stage'),
    y=alt.Y('my_rescues:Q', title='Number of Rescues')
).properties(
    width=400,
    height=400
))        


# Compare Revives (myself) to Revives (teammates)
st.write("""
## Revives By Stage

Revives are the number of times you get revived by your teammates after you die.
""")

grouped_data = salmonrun_df.groupby('stage')['my_rescued'].mean().reset_index()
st.altair_chart(alt.Chart(grouped_data).mark_bar().encode(
    x=alt.X('stage:N', title='Stage'),
    y=alt.Y('my_rescued:Q', title='Number of Times I Have Been Rescued')
).properties(
    width=400,
    height=400
)) 
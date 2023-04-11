import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import utils


# read in the data
# battle_df = pd.read_csv('./data/statink-super64guy.csv')
battle_df = pd.read_csv('./initial_scripts/test.csv')
salmonrun_df = pd.read_csv('./data/statink-super64guy-salmonrun.csv')

# get general game statistics that I can display in a table
total_battles = len(battle_df.index)
win_percent = len(battle_df[battle_df['result'] == 'win'])/len(battle_df.index)
avg_kills = battle_df['kill'].mean()
avg_deaths = battle_df['death'].mean()
avg_kd = battle_df['kill'].mean() / battle_df['death'].mean()
avg_assists = battle_df['assist'].mean()
avg_special = battle_df['special'].mean()
avg_inked = battle_df['inked'].mean()

st.write("""
# Splatoon3Dashboard

Welcome to my CPSC325 Data Science project! This deployment is currently a work in progress as I continue to develop this project over the course of the rest of the semester, but eventually you will be able to see different charts and displays in regards to all of my battle data for my battles in Splatoon 3!

## General Splatoon 3 Battle Information
""")

general_options = st.selectbox(label='General_Info_Type', options=['General', 'Game Mode Specific', 'Weapon Specific'])

if general_options == 'General':
    st.write("**TOTAL BATTLES:**", total_battles)
    st.write("**WIN %:**", win_percent * 100)
    st.write("**AVERAGE KILLS:**", avg_kills)
    st.write("**AVERAGE DEATHS:**", avg_deaths)
    st.write("**AVERAGE KD RATIO:**", avg_kd)
    st.write("**AVERAGE ASSISTS:**", avg_assists)
    st.write("**AVERAGE SPECIALS USED:**", avg_special)
    st.write("**AVERAGE INKED:**", avg_inked)

elif general_options == 'Game Mode Specific':
    mode_options = st.selectbox(label='Game_Mode_General', options=set(battle_df['rule'].to_list()))
    utils.generate_general_info(battle_df, 'rule', mode_options)

elif general_options == 'Weapon Specific':
    weapon_options = st.selectbox(label='Weapon_General', options=set(battle_df['main_weapon'].to_list()))
    utils.generate_general_info(battle_df, 'main_weapon', weapon_options)


st.write("""
## Position in Team
""")

position_options = st.selectbox(label='Position_Options', options=['General', 'Game Mode Specific', 'Weapon Specific'])

if position_options == 'General':
    st.bar_chart(data=battle_df['rank_in_team'].value_counts())

elif position_options == 'Game Mode Specific':
    mode_options = st.selectbox(label='Game_Mode_Position', options=set(battle_df['rule'].to_list()))
    st.bar_chart(data=utils.generate_position_values(battle_df, 'rule', mode_options))

elif position_options == 'Weapon Specific':
    weapon_options = st.selectbox(label='Weapon_Position', options=set(battle_df['main_weapon'].to_list()))
    st.bar_chart(data=utils.generate_position_values(battle_df, 'main_weapon', weapon_options))

st.write("""
## Turf Inked Per Weapon
""")

turf_inked_options = st.selectbox(label='Select Option for Turf Inked', options=['Over all Game Modes', 'Over Specific Game Mode'])

if turf_inked_options == 'Over all Game Modes':
    st.bar_chart(data=utils.plot_turf_inked_per_weapon(battle_df))

elif turf_inked_options == 'Over Specific Game Mode':
    game_options = st.selectbox(label='Select Game Mode', options=set(battle_df['rule'].to_list()))
    st.bar_chart(data=utils.plot_turf_inked_per_weapon(battle_df, game_mode=game_options))


st.write("""
## Average Win Rate Per Stage

**TO BE IMMPLEMENTED:** Do this on a general game basis and a per-game mode basis
""")


st.write("""
## Average Turf Inked Per Stage

**TO BE IMPLEMENTED:** There shouldn't be any additional options with this one
""")
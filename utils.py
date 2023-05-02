import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import requests
import json

def generate_general_info(df, col_name, attribute):
    new_df = df.groupby(col_name).get_group(attribute)
    total_battles = len(new_df.index)
    win_percent = len(new_df[new_df['result'] == 'win'])/len(new_df.index)
    avg_kills = new_df['kill'].mean()
    avg_deaths = new_df['death'].mean()
    avg_kd = new_df['kill'].mean() / new_df['death'].mean()
    avg_assists = new_df['assist'].mean()
    avg_special = new_df['special'].mean()
    avg_inked = new_df['inked'].mean()

    st.write("**TOTAL BATTLES:**", total_battles)
    st.write("**WIN %:**", win_percent * 100)
    st.write("**AVERAGE KILLS:**", avg_kills)
    st.write("**AVERAGE DEATHS:**", avg_deaths)
    st.write("**AVERAGE KD RATIO:**", avg_kd)
    st.write("**AVERAGE ASSISTS:**", avg_assists)
    st.write("**AVERAGE SPECIALS USED:**", avg_special)
    st.write("**AVERAGE INKED:**", avg_inked)

def generate_position_values(df, col_name, attribute):
    return df.groupby(col_name).get_group(attribute)['rank_in_team'].value_counts()


def plot_turf_inked_per_weapon(df, game_mode=None):
    # setup
    weapon_dict = {}
    weapon_list = list(set(df['main_weapon'].to_list()))

    

    if game_mode == None:
        # get a groupby of all the weapons
        weapon_groups = df.groupby('main_weapon')
        for weapon in weapon_list:
            weapon_df = weapon_groups.get_group(weapon)
            weapon_dict[weapon] = weapon_df['inked'].mean()

    else:
        for weapon in weapon_list:
            tmp_df = df.groupby('rule').get_group(game_mode)
            weapon_groups = tmp_df.groupby('main_weapon')
            for weapon in weapon_list:
                weapon_df = weapon_groups.get_group(weapon)
                weapon_dict[weapon] = weapon_df['inked'].mean()

    return weapon_dict

def get_unique_weapons_list():
    weapons_list = []
    weapons_json = json.loads(requests.get('https://stat.ink/api/v3/weapon').text)

    for val in weapons_json:
        weapons_list.append(val['key'])

    return weapons_list
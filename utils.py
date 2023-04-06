import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

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
    st.write("**WIN %:**", win_percent)
    st.write("**AVERAGE KILLS:**", avg_kills)
    st.write("**AVERAGE DEATHS:**", avg_deaths)
    st.write("**AVERAGE KD RATIO:**", avg_kd)
    st.write("**AVERAGE ASSISTS:**", avg_assists)
    st.write("**AVERAGE SPECIALS USED:**", avg_special)
    st.write("**AVERAGE INKED:**", avg_inked)

def generate_position_values(df, col_name, attribute):
    return df.groupby(col_name).get_group(attribute)['rank_in_team'].value_counts() 
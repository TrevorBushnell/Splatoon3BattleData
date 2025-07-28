import json
import pandas as pd
import sqlite3
import sys
from datetime import datetime
import pytz

from data_utils import *


if __name__ == "__main__":
    df = load_data("./data/statink-super64guy.json")

    for name in ['lobby', 'rule', 'stage', 'game_version', 'rank_before', 'rank_after', 'our_team_role', 'their_team_role', 'third_team_role']:
        pop_general_json_data(df, name)

    for name in ['start_at', 'end_at']:
        pop_timestamp_json_data(df, name)

    pop_weapon_data(df)
    update_lobby(df)

    # our_team_members_df = parse_team_col(df['our_team_members'])
    # their_team_members_df = parse_team_col(df['their_team_members'])



    # df = df.join(our_team_members_df)
    # df = df.join(their_team_members_df)

    df['medals'] = df['medals'].astype(str)

    df.rename(columns={'lobby':'battle_type', 'rule':'mode', 'my_headgear':'headgear', 'my_clothing':'clothing', 'my_shoes':'shoes'}, inplace=True)
    df.drop(columns=['url', 'images', 'user', 'weapon', 'note', 'private_note', 'link_url', 'user_agent', 'automated', 'period', 'created_at', 'our_team_members', 'their_team_members', 'fest_power', 'fest_dragon'], inplace=True)
    # df = df.reindex(['battle_type', 'mode', 'stage', 'main_weapon', 'sub_weapon', 'special_weapon', 'headgear', 'clothing', 'shoes', 'result', 'knockout', 'rank_in_team', 'kill', 'assist', 'kill_or_assist', 'death', 'special', 'signal', 'inked', 'medals', 'our_team_inked', 'their_team_inked', 'third_team_inked', 'our_team_percent', 'their_team_percent', 'third_team_percent', 'our_team_count', 'their_team_count', 'level_before', 'level_after', 'rank_before', 'rank_before_s_plus', 'rank_before_exp', 'rank_after', 'rank_after_s_plus', 'rank_after_exp', 'rank_exp_change', 'rank_up_battle', 'challenge_win', 'challenge_lose', 'x_power_before', 'x_power_after', 'fest_power', 'fest_dragon', 'clout_before', 'clout_after', 'clout_change', 'cash_before', 'cash_after', 'our_team_color', 'their_team_color', 'third_team_color', 'our_team_role', 'their_team_role', 'third_team_role', 'our_team_theme', 'their_team_theme', 'third_team_theme', 'third_team_members', 'teammate_1_name', 'teammate_1_rank', 'teammate_1_main_weapon', 'teammate_1_sub_weapon', 'teammate_1_special_weapon', 'teammate_1_kill', 'teammate_1_assist', 'teammate_1_kill_or_assist', 'teammate_1_death', 'teammate_1_special', 'teammate_1_signal', 'teammate_1_inked', 'teammate_1_headgear', 'teammate_1_clothing', 'teammate_1_shoes', 'teammate_2_name', 'teammate_2_rank', 'teammate_2_main_weapon', 'teammate_2_sub_weapon', 'teammate_2_special_weapon', 'teammate_2_kill', 'teammate_2_assist', 'teammate_2_kill_or_assist', 'teammate_2_death', 'teammate_2_special', 'teammate_2_signal', 'teammate_2_inked', 'teammate_2_headgear', 'teammate_2_clothing', 'teammate_2_shoes', 'teammate_3_name', 'teammate_3_rank', 'teammate_3_main_weapon', 'teammate_3_sub_weapon', 'teammate_3_special_weapon', 'teammate_3_kill', 'teammate_3_assist', 'teammate_3_kill_or_assist', 'teammate_3_death', 'teammate_3_special', 'teammate_3_signal', 'teammate_3_inked', 'teammate_3_headgear', 'teammate_3_clothing', 'teammate_3_shoes', 'opponent_1_name', 'opponent_1_rank', 'opponent_1_main_weapon', 'opponent_1_sub_weapon', 'opponent_1_special_weapon', 'opponent_1_kill', 'opponent_1_assist', 'opponent_1_kill_or_assist', 'opponent_1_death', 'opponent_1_special', 'opponent_1_signal', 'opponent_1_inked', 'opponent_1_headgear', 'opponent_1_clothing', 'opponent_1_shoes', 'opponent_2_name', 'opponent_2_rank', 'opponent_2_main_weapon', 'opponent_2_sub_weapon', 'opponent_2_special_weapon', 'opponent_2_kill', 'opponent_2_assist', 'opponent_2_kill_or_assist', 'opponent_2_death', 'opponent_2_special', 'opponent_2_signal', 'opponent_2_inked', 'opponent_2_headgear', 'opponent_2_clothing', 'opponent_2_shoes', 'opponent_3_name', 'opponent_3_rank', 'opponent_3_main_weapon', 'opponent_3_sub_weapon', 'opponent_3_special_weapon', 'opponent_3_kill', 'opponent_3_assist', 'opponent_3_kill_or_assist', 'opponent_3_death', 'opponent_3_special', 'opponent_3_signal', 'opponent_3_inked', 'opponent_3_headgear', 'opponent_3_clothing', 'opponent_3_shoes', 'opponent_4_name', 'opponent_4_rank', 'opponent_4_main_weapon', 'opponent_4_sub_weapon', 'opponent_4_special_weapon', 'opponent_4_kill', 'opponent_4_assist', 'opponent_4_kill_or_assist', 'opponent_4_death', 'opponent_4_special', 'opponent_4_signal', 'opponent_4_inked', 'opponent_4_headgear', 'opponent_4_clothing', 'opponent_4_shoes', 'game_version', 'start_at', 'end_at'], axis=1)

    # df.dtypes.T.to_csv('./data/col_types.csv')
    df.to_csv('./data/battle-data.csv')

    # conn = sqlite3.connect('./data/splatoon3.db')
    # df.to_sql('battles', conn, if_exists="replace", index=True)
    # conn.close()
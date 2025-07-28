import json
import pandas as pd
import sqlite3
import sys
from datetime import datetime
import pytz

from data_utils import *

if __name__ == "__main__":
    df = load_data("./data/statink-salmon-super64guy.json")
    for col_name in ["stage", "fail_reason", "king_salmonid", "title_before", "title_after", "game_version"]:
        pop_general_json_data(df, col_name)

    pop_timestamp_json_data(df, 'start_at')

    df.drop(columns=["url", "user", "uuid", "fail_reason", "private", "note", "private_note", "link_url", "user_agent", "automated", "period", "shift", "end_at", "created_at", "guessed_king_salmonid"], inplace=True)
    
    df.to_csv('./data/salmon-run-data.csv')
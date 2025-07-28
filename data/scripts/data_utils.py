from datetime import datetime
import pytz
import pandas as pd
import json

def load_data(filepath):
    with open(filepath) as f:
        data_json = f.readlines()

    df = pd.DataFrame()
    for json_obj in data_json:
        tmp_df = pd.DataFrame.from_dict(json.loads(json_obj), orient="index").T
        tmp_df.set_index('id', inplace=True)
        df = pd.concat([df, tmp_df])
    
    return df

def pop_general_json_data(df, col_name):
    for i in df.index:
        if df[col_name][i] is not None:
            df.loc[i, col_name] = df[col_name][i]['name']['en_US']

def pop_timestamp_json_data(df, col_name):
    times = []
    for i in df.index:
        time = df[col_name][i]['iso8601']
        time = datetime.fromisoformat(time)
        time = time.astimezone(pytz.timezone('America/Los_Angeles'))
        time = time.replace(tzinfo=None)
        times.append(time)
    
    df[col_name] = times

def pop_weapon_data(df):
    main_list = []
    sub_list = []
    special_list = []
    for i in df.index:
        tmp_dict = df.loc[i, 'weapon']
        main_list.append(tmp_dict['name']['en_US'])
        sub_list.append(tmp_dict['sub']['name']['en_US'])
        special_list.append(tmp_dict['special']['name']['en_US'])
    if len(main_list) == len(sub_list) == len(special_list):
        df['main_weapon'] = main_list
        df['sub_weapon'] = sub_list
        df['special_weapon'] = special_list

def update_lobby(df):
    for i in df.index:
        if df['lobby'][i] == 'Regular Battle':
            df.loc[i, 'rule'] = df['rule'][i] + ' (Regular)'
        elif df['lobby'][i] == 'Anarchy Battle (Open)':
            df.loc[i, 'rule'] = df['rule'][i] + ' (Open)'
        elif df['lobby'][i] == 'Anarchy Battle (Series)':
            df.loc[i, 'rule'] = df['rule'][i] + ' (Series)'
        elif df['lobby'][i] == 'Private Battle':
            df.loc[i, 'rule'] = df['rule'][i] + ' (Private)'
        elif df['lobby'][i] == 'Splatfest (Open)' and df['rule'][i] != 'Tricolor Turf War':
            df.loc[i, 'rule'] = df['rule'][i] + ' (Splatfest Open)'
        elif df['lobby'][i] == 'Splatfest (Series)':
            df.loc[i, 'rule'] = df['rule'][i] + ' (Splatfest Series)'

def parse_gear(gear_dict):
    gear_data = {'primary':'', 'secondary':[]}

    if gear_dict is None:
        return gear_data

    gear_data['primary'] = gear_dict['primary_ability']['name']['en_US']
    
    for s in gear_dict['secondary_abilities']:
        if s is not None:
            gear_data['secondary'].append(s['name']['en_US'])

    return json.dumps(gear_data)

def parse_team_data(players, col_header):
    team_df = pd.DataFrame()
    col_header = None
    curr_player = 1

    for player in players:
        df = pd.DataFrame()
        col_name = f'{col_header}_{curr_player}'
        if player['me'] == True:
            col_name = 'my'
        else: # if it's not me, then we can parse all non gear data
            df[f'{col_name}_name'] = [player['name']]
            df[f'{col_name}_rank'] = player['rank_in_team']
            df[f'{col_name}_main_weapon'] = [player['weapon']['name']['en_US']]
            df[f'{col_name}_sub_weapon'] = [player['weapon']['sub']['name']['en_US']]
            df[f'{col_name}_special_weapon'] = [player['weapon']['special']['name']['en_US']]
            df[f'{col_name}_kill'] = [player['kill']]
            df[f'{col_name}_assist'] = [player['assist']]
            df[f'{col_name}_kill_or_assist'] = [player['kill_or_assist']]
            df[f'{col_name}_death'] = [player['death']]
            df[f'{col_name}_special'] = [player['special']]
            df[f'{col_name}_signal'] = [player['signal']]
            df[f'{col_name}_inked'] = [player['inked']]
        # now parse gear data
        df[f'{col_name}_headgear'] = [parse_gear(player['gears']['headgear'])]
        df[f'{col_name}_clothing'] = [parse_gear(player['gears']['clothing'])]
        df[f'{col_name}_shoes'] = [parse_gear(player['gears']['shoes'])]

        if player['me'] == False:
            curr_player += 1

        if team_df.empty:
            team_df = df
        else:
            team_df = team_df.join(df)

    return team_df
    
def parse_team_col(team_col):
    team_df = pd.DataFrame()
    col_header = ''
    if team_col.name == 'our_team_members':
        col_header = 'teammate'
    elif team_col.name == 'their_team_members':
        col_header = 'opponent'
    elif team_col.name == 'third_team_members':
        col_header = 'third'

    for val in team_col:
        if val is None:
            df = parse_team_data(val, col_header)
        else:
            df = pd.DataFrame()
        if team_df.empty:
            team_df = df
        else:
            pd.concat([team_df, df])

    team_df.reset_index(drop=True, inplace=True)
    

    return team_df

def parse_salmon_boss_data(boss_col):
    for i in range(20):
        print(len(boss_col[i]))
import pandas as pd


def get_settings():
    settings = {'id_column': 'SID',
                'time_column': 'timestamp',
                'ai_column': 'ai_column',
                'act_column': 'label',
                'walk_column': 'walking_intensity_prediction',
                'nw_column': 'snt_prediction'}

    settings.update({'ot_run': True,
                     'ot_format': 1})

    settings.update({'nw_ends': True,
                     'bug_ends': True,
                     'nw_ends_min': 45,
                     'nw_ends_pct': 0.05,
                     'bug_ends_min': 45,
                     'bug_ends_pct': 0.5,
                     'nw_days': True,
                     'bug_days': True,
                     'bug_lying': True,
                     'bug_sitting': True,
                     'bug_standing': True,
                     'nw_days_pct': 0.5,
                     'bug_days_pct': 0.8})

    settings.update({'remove_stairs': True,
                     'remove_bending': True,
                     'remove_shuffling': True,
                     'merge_cyc_codes': True,
                     'adjust_cyc_interval': True,
                     'min_cyc_epochs': 3,
                     'remove_partial_days': True})

    settings.update({'act_variables': True,
                     'ai_variables': True,
                     'walk_variables': True,
                     'ait_variables': True,
                     'bout_variables': True,
                     'nw_variables': True})

    settings.update({'daily_variables': True,
                     'average_variables': True,
                     'week_wknd_variables': True,
                     'ot_variables': True})

    act_codes = [1, 2, 6, 7, 8, 13] if settings['merge_cyc_codes'] else [1, 2, 6, 7, 8, 13, 130, 140]
    walk_codes = [101, 102, 103, 104] if settings['remove_stairs'] else [101, 102, 103]

    settings.update({'nw_codes': [1, 2, 3, 4],
                     'ai_codes': ['A', 'I'],
                     'act_codes': act_codes,
                     'walk_codes': walk_codes,
                     'bout_codes': [1, 2, 6, 7, 8]})

    settings.update({'i_cat': {1: [60, 300], 2: [301, 600], 3: [601, 1200], 4: [1201, 3600], 5: [3601, 9999999]},
                     'a_cat': {1: [60, 300], 2: [301, 600], 3: [601, 1200], 4: [1201, 3600], 5: [3601, 9999999]},
                     'noise_threshold': 0.15})

    settings.update(
        {'code_name': {'I': 'inactive', 'A': 'active', 8: 'lying', 7: 'sitting', 6: 'standing', 1: 'walking',
                       2: 'running', 20: 'jumping', 13: 'cycling', 130: 'cyc_sit_inactive', 140: 'cyc_stand_inactive',
                       101: '101', 102: '102', 103: '103', 104: '104'}})

    if settings['ot_run']:
        if settings['ot_format'] == 1:
            ot_df = pd.read_csv(
                'C:/Users/skjel/OneDrive/Skrivebord/STUNTH/arbeidsreg/Arbeidstid og NASA TLX T3 (vasket).csv',
                delimiter=';')
        elif settings['ot_format'] == 2:
            ot_df = pd.read_csv(
                'C:/Users/skjel/OneDrive/Skrivebord/STUNTH/arbeidsreg/Arbeidstid og NASA TLX T3 (vasket).csv',
                delimiter=';')
        else:
            ot_df = False
    else:
        ot_df = False

    data_path = 'C:/Users/skjel/OneDrive/Skrivebord/Axivity post process/files 2024/'

    return settings, ot_df, data_path

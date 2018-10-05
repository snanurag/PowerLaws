import datetime
import numpy as np
import pandas as pd

def get_day_from_timestamp(x):
    return pd.to_datetime(x, format="%Y-%m-%d %H:%M:%S").dayofweek

def get_week_from_timestamp(x):
    return pd.to_datetime(x, format="%Y-%m-%d %H:%M:%S").week

def get_hour_from_timestamp(x):
    return pd.to_datetime(x, format="%Y-%m-%d %H:%M:%S").hour

def get_date_from_timestamp(x):
    return datetime.datetime.strptime(x, "%Y-%m-%d %H:%M:%S").date()

def ohe_true_false(x):
    if type(x) == bool:
        return int(x == True)
    else:
        return x

def replace_day_with_off(row):
    if row['on_off'] == 0 and row['monday_is_day_off'] == 0:
        row['on_off'] = 1
    elif row['on_off'] == 1 and row['tuesday_is_day_off'] == 0:
        row['on_off'] = 1
    elif row['on_off'] == 2 and row['wednesday_is_day_off'] == 0:
        row['on_off'] = 1
    elif row['on_off'] == 3 and row['thursday_is_day_off'] == 0:
        row['on_off'] = 1
    elif row['on_off'] == 4 and row['friday_is_day_off'] == 0:
        row['on_off'] = 1
    elif row['on_off'] == 5 and row['saturday_is_day_off'] == 0:
        row['on_off'] = 1
    elif row['on_off'] == 6 and row['sunday_is_day_off'] == 0:
        row['on_off'] = 1
    else:
        row['on_off'] = 0
    return row

# Takes array as input
def is_temp_na(x):   
    return np.isnan(x)

def is_temp_not_na(x):   
    return np.isnan(x) == False

def day_time(x):
    return x < 13 or x > 15

def custom_temp_range(x):
    return x < 14 or x >21

def daily(x):
    return x == 'daily'

def weekly(x):
    return x == 'weekly'

def hourly(x):
    return x == 'hourly'

def is_one(x):
    return x == 1

def is_zero(x):
    return x == 0

def square(x):
    return x*x

def count_hour_is_less(x):
    return x < 24

def count_day_is_less(x):
    return x < 7

def multiply_by_7(x):
    return x * 7
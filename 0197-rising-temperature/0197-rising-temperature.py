import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather = weather.sort_values(by = 'recordDate')
    weather['diff_date'] = weather['recordDate'].diff().dt.days
    weather['diff'] = weather['temperature'].diff(periods = 1)
    id_pos = (weather['diff'] > 0) & (weather['diff_date'] == 1)
    return weather.loc[id_pos, ['id']]
import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    new_df = pd.merge(employees, employee_uni, on = 'id', how = 'outer')
    new_df = new_df.dropna(subset = ['name'])
    return new_df[['unique_id', 'name']]
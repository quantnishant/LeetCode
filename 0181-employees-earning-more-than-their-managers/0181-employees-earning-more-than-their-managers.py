import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee[['id', 'salary']].rename(columns = {'id' : 'managerId', 'salary': 'manager_s'})
    merged = employee.merge(df, on = 'managerId')
    idx_great = merged[merged.salary > merged.manager_s].rename(columns = {'name' : 'Employee'})
    return idx_great[['Employee']]

import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(employee, department, left_on = 'departmentId', right_on = 'id', how = 'left').rename(columns = {'name_x' : 'Employee', 'name_y' : 'Department', 'salary' : 'Salary'})
    mask = merged['Salary'] == merged.groupby(by = 'Department')['Salary'].transform('max')
    return merged.loc[mask, ['Employee', 'Department', 'Salary']]
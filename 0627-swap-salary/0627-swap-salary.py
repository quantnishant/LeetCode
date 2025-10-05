import pandas as pd
import numpy as np
def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
    salary['sex'] = np.where(salary['sex'] == 'm', 'f', 'm')
    return salary
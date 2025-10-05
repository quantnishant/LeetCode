import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    counts = my_numbers['num'].value_counts()
    singles = counts[counts == 1].index
    if singles.empty:
        return pd.DataFrame({"num" : [None]})
    else:
        return pd.DataFrame({'num' : [singles.max()]})


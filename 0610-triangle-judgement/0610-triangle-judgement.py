import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    mask = ((triangle.x + triangle.y > triangle.z) & (triangle.x + triangle.z > triangle.y) & (triangle.z + triangle.y > triangle.x))
    triangle['triangle'] = 'No'
    triangle.loc[mask, 'triangle'] = 'Yes'
    return triangle
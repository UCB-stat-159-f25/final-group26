import pandas as pd

def group_data(df: pd.DataFrame, variable: str):
    """
    Group a DataFrame by a column and return counts sorted by index.
    """
    return df.groupby(variable).size().sort_index()

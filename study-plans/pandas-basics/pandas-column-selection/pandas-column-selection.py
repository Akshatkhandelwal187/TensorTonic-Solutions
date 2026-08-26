import pandas as pd

def select_column(data, column):
    """
    Returns: dict with 'values' (list) and 'length' (int)
    """
    df = pd.DataFrame(data)

    df_column = df[column].tolist()
    length = len(df_column)

    return {
        "values" : df_column,
        "length" : length
    }
    
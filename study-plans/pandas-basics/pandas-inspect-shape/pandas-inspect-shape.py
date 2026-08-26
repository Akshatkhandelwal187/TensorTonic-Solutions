import pandas as pd

def inspect_dataframe(data):
    """
    Returns: dict with 'rows', 'cols' (ints), 'columns' (list),
    'dtypes' (dict), 'total_values' (int)
    """

    #create the pandas dataframe
    df = pd.DataFrame(data)

    #extract the properties and format the output
    return {
        "rows" : df.shape[0],
        "cols" : df.shape[1],
        "columns" : list(df.columns),
        "dtypes" : df.dtypes.astype(str).to_dict(),
        "total_values" : df.size
    }
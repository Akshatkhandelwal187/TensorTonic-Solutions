import pandas as pd

def create_dataframe(data):
    """
    Returns: dict with 'data', 'shape', 'columns'
    """# create the pandas dataframe
    df = pd.DataFrame(data)

    # extract the required information and return as a dictionary
    # how to return a dictioanry = findamental doubt in how dict works

    return {
        "data" : data,
        "shape" : list(df.shape),
        "columns" : list(df.columns)
    }
    
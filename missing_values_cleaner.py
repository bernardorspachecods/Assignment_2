import pandas as pd

def missing_values_cleaner(df) -> pd.DataFrame:
    
    df = df.copy()
    
    """
    Takes a Pandas DataFrame as input and returns the same DataFrame after removing all rows that contain null values in the "CustomerID" or "Description" columns 
    """
    
    # Removes rows where CustomerID or Description have null values
    df = df.dropna(subset=['CustomerID', 'Description'])

    # Returns the cleaned df
    return df

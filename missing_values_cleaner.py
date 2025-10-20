import pandas as pd

def missing_values_cleaner(df) -> pd.DataFrame:
    
    df = df.copy()
    
    # Your code goes here
    """
    Takes a Pandas DataFrame as input and returns the same DataFrame after removing all rows that contain null values in the "CustomerID" or "Description" columns 
    """
    
    # Remove rows where CustomerID or Description have null values
    df = df.dropna(subset=['CustomerID', 'Description'])

    # Return the cleaned DataFrame
    return df

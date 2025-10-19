import pandas as pd

def missing_values_cleaner(df) -> pd.DataFrame:
    
    df = df.copy()
    
    # Your code goes here
    # Remove rows where CustomerID or Description have null values
    df = df.dropna(subset=['CustomerID', 'Description'])

    # Return the cleaned DataFrame
    return df

import pandas as pd

def quantity_handler(df) -> pd.DataFrame:
    
    df = df.copy()

    """
    Takes a Pandas DataFrame as input and returns it after removing all rows where the Quantity column has values less than or equal to zero
    """
    
    # Removes rows where quantity is <= 0
    df = df[df["Quantity"] > 0]

    return df

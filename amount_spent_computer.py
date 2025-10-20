import pandas as pd

def amount_spent_computer(df) -> pd.DataFrame:
    
    df = df.copy()
    
    # Your code goes here
    """
    Takes a Pandas DataFrame as input and returns it with a new column, amount_spent, representing the product of Quantity and UnitPrice.
    """

    # adds the new column amount_spent
    df["amount_spent"] = df["Quantity"] * df["UnitPrice"]
    
    return df

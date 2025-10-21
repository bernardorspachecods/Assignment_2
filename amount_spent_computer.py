import pandas as pd

def amount_spent_computer(df) -> pd.DataFrame:

    df = df.copy()

    """
    Takes a Pandas DataFrame as input and returns it with a new column, amount_spent, representing the product of Quantity and UnitPrice.
    """

    # Adds the new column amount_spent
    df["amount_spent"] = df["Quantity"] * df["UnitPrice"]
    
    return df

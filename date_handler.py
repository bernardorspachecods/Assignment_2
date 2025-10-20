import pandas as pd

def date_handler(df) -> pd.DataFrame:
    # Your code goes here
    """
    Takes a Pandas DataFrame as input and returns it without any rows corresponding to invoices from the year 2011
    """
    
    df = df.copy()
    
    # Convert to datetime type
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
    
    # only present rows in which the year is != 2011
    df = df[df["InvoiceDate"].dt.year != 2011]

    return df

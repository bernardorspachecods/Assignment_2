import pandas as pd

def top_five_cust(df) -> list:
    
    """
    Takes a Pandas DataFrame as input and returns a list of CustomerID values for the five customers with the highest number of orders.
    """

    df = df.copy()
    
    # Removes duplicate pairs to count each order only once
    unique = df.drop_duplicates(subset=["CustomerID", "InvoiceNo"])
    
    # Counts the number of unique invoices
    counts = unique["CustomerID"].value_counts()
    
    # Selects the top 5 customers
    top5 = counts.head(5).index.tolist()
    
    return top5

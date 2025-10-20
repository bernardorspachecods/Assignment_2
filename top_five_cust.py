import pandas as pd

def top_five_cust(df) -> list:
    # Your code goes here
    """
    Takes a Pandas DataFrame as input and returns a list of CustomerID values for the five customers with the highest number of orders.
    """
    df = df.copy()
    
    # Remove duplicate pairs to count each order only once
    unique = df.drop_duplicates(subset=["CustomerID", "InvoiceNo"])
    
    # Count number of unique invoices
    counts = unique["CustomerID"].value_counts()
    
    # top 5 customers
    top5 = counts.head(5).index.tolist()
    
    return top5

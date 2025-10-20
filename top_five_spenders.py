import pandas as pd

def top_five_spenders(df) -> list:
    # Your code goes here
    """
    Takes a Pandas DataFrame as input and returns a list of CustomerID values for the five customers who have spent the most money
    """
    df = df.copy()
    
    # group by CustomerID and sum total amount spent per customer
    totals = df.groupby("CustomerID")["amount_spent"].sum()
    
    # get the top spenders
    top5 = totals.sort_values(ascending=False).head(5).index.tolist()

    return top5

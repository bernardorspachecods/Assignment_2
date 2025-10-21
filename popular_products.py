import pandas as pd
from typing import List

def popular_products(df) -> List[str]:
<<<<<<< HEAD
    
    """
    This function receives a Pandas DataFrame as input containing retail transaction data as input and than
    identifies and returns a list of the 5 product descriptions purchased most frequently.
    """
    
    # Counts how many times an item was purchased
    purchased_counts = df["Description"].value_counts(sort = True)
=======
    # Your code goes here
    # Counts how many times an item was purchased
    purchased_counts = df["Description"].value_counts(sort = True)

    # Selects the top 5 purchased products
    purchased_most_times = purchased_counts.head(5)

    # Returns these products in a list
    return purchased_most_times.index.tolist()
>>>>>>> ff13b4d4f7699cc5cddcdef06a7bed85824c8ed6

    # Selects the top 5 purchased products
    purchased_most_times = purchased_counts.head(5)

    # Returns these products in a list
    return purchased_most_times.index.tolist()

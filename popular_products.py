import pandas as pd
from typing import List

def popular_products(df) -> List[str]:
    
    """
    This function receives a Pandas DataFrame as input containing retail transaction data as input and than
    identifies and returns a list of the 5 product descriptions purchased most frequently.
    """
    
    # Counts how many times an item was purchased
    purchased_counts = df["Description"].value_counts(sort = True)

    # Selects the top 5 purchased products
    purchased_most_times = purchased_counts.head(5)

    # Returns these products in a list
    return purchased_most_times.index.tolist()

import pandas as pd
from typing import List

def top_twenty_countries(df) -> List[str]:
    
    """
    Takes a Pandas DataFrame as input and returns a list of the 20 countries with the highest number of orders. Be careful to count each invoice only once, even if it appears multiple times
    """

    df = df.copy()
    
    # Removes duplicate InvoiceNo to count each order only once per country
    orders = df.drop_duplicates(subset=["Country", "InvoiceNo"])
    
    # Counts the number of orders per country
    counts = orders["Country"].value_counts()
    
    # Gets the top 20 countries
    top20 = counts.head(20).index.tolist()

    return top20

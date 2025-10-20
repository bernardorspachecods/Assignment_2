import pandas as pd
from typing import List

def popular_products(df) -> List[str]:
    # Your code goes here
    times_purchased = df["Description"].value_counts(sort = True)
    purchased_most_times = times_purchased.head(5)
    return purchased_most_times.tolist()


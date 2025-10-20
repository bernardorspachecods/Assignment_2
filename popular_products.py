import pandas as pd
from typing import List

def popular_products(df) -> List[str]:
    # Your code goes here
    purchased_counts = df["Description"].value_counts(sort = True)
    purchased_most_times = purchased_counts.head(5)
    return purchased_most_times.index.tolist()


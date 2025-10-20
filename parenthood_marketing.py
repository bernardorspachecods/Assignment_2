import pandas as pd
from typing import List

def parenthood_marketing(df, customers) -> List[str]:
    merged=df[["CustomerID","Country"]].drop_duplicates().merge(customers[["CustomerID","NumChildren"]], on = "CustomerID")
    highest_num_child = merged.groupby("Country")["NumChildren"].mean().sort_values(ascending=False).head(5)
    return highest_num_child.index.tolist()

import pandas as pd

def babuska_clients(df, customers) -> float:
    # Your code goes here
    merged=df[["CustomerID","Description"]].drop_duplicates().merge(customers[["CustomerID","Age"]], on = "CustomerID")
    merged_babuska = merged[merged["Description"]=="HAND WARMER BABUSHKA DESIGN"]
    return merged_babuska["Age"].mean()

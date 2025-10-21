import pandas as pd

def babuska_clients(df, customers) -> float:
    
    """
    Calculates the average age of customers who have purchased the  'HAND WARMER BABUSHKA DESIGN' product.
    """
    
    # Prepares data for merge and ensures each customer is only counted once per product
    merged=df[["CustomerID","Description"]].drop_duplicates().merge(customers[["CustomerID","Age"]], on = "CustomerID")

    # Filters the merged df to select only transactions related to the specific product
    merged_babuska = merged[merged["Description"]=="HAND WARMER BABUSHKA DESIGN"]

    # Returns the average of the customers age
    return merged_babuska["Age"].mean()

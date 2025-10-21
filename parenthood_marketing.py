import pandas as pd
from typing import List

def parenthood_marketing(df, customers) -> List[str]:

    """
    This function receives a retail transaction DataFrame and a customer info DataFrame as input.
    It identifies the top 5 countries whose customers have the highest average number of children among those who made at least one purchase.
    """

    # Selects CustomerID and Country from the retail data, ensures each country is counted only once per customer and merges this data with CustomerID and NumChildren from the customer data
    merged=df[["CustomerID","Country"]].drop_duplicates().merge(customers[["CustomerID","NumChildren"]], on = "CustomerID")

    # Calculates the average number of children per country, sorts in descending order and selects the top 5 countries
    highest_num_child = merged.groupby("Country")["NumChildren"].mean().sort_values(ascending=False).head(5)

    # Returns the country names as a list of strings
    return highest_num_child.index.tolist()

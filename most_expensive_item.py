import pandas as pd

def most_expensive_item(df) -> str:
     
     """
     Takes a Pandas DataFrame as input and returns the Description of the most expensive item as a string
     """

     df = df.copy()
    
     # Selects row with the max unit price
     max_price = df.loc[df["UnitPrice"].idxmax()]
    
     # Returns the description of the max price row
     return max_price["Description"]

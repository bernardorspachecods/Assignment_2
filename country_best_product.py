import pandas as pd

def country_best_product(df, country) -> str:
    # Your code goes here
    if country in df["Country"].unique():
        
    
    
        times_purchased = df.groupby("Country")["Description"].value_counts(sort = True)
        purchased_most_times = times_purchased[0]
        return purchased_most_times
        

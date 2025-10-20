import pandas as pd

def country_best_product(df, country) -> str:
    # Your code goes here
    if country in df["Country"].unique():

        # Subsets the data set to the country
        df_country =df[df["Country"]==country]

        # Counts how many times each item was purchased in descending order
        purchased_counts = df_country["Description"].value_counts(sort=True)
        
        return purchased_counts.index[0] 
    else:
        return None
        

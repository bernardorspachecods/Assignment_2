import pandas as pd

def country_best_product(df, country) -> str:

    """
    This function receives a Pandas DataFrame and a string representing a country as input.
    It returns the description of the item that is most frequently purchased 
    in that country, or None if the country is not present in the DataFrame.
    """

    if country in df["Country"].unique():

        # Subsets the data set to the country
        df_country =df[df["Country"]==country]

        # Counts how many times each item was purchased in descending order
        purchased_counts = df_country["Description"].value_counts(sort=True)
        
        return purchased_counts.index[0] 

    else:

        # Returns None if the country is not present in the df
        return None
        

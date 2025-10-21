import pandas as pd

def load_retail_data(filepath: str) -> pd.DataFrame:
    
    """
    Loads the dataset from the CSV file into a pandas DataFrame
    """

    # Loads the online retail dataset into a pandas DataFrame
    df = pd.read_csv(filepath, encoding='ISO-8859-1') # Enconding avoids decode errors and loads all characters correctly

    return df

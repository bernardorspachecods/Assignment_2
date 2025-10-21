import pandas as pd

def load_customer_data(filepath: str) -> pd.DataFrame:

    """
    This function receives a string filepath as input. 
    It loads the customer information CSV file into a Pandas DataFrame and returns it.
    """

    # Reads the file
    customers = pd.read_csv(filepath, encoding='ISO-8859-1')

    return customers

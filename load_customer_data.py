import pandas as pd

def load_customer_data(filepath: str) -> pd.DataFrame:
    # Your code goes here
    customers = pd.read_csv(filepath, encoding='ISO-8859-1')
    return customers

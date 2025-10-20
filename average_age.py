import pandas as pd
from top_five_cust import top_five_cust

def average_age(df, customers) -> float:
    # Your code goes here
    top_customers = top_five_cust(df)
    ages = []
    for customer_id in top_customers:
        age = customers.loc[customers["CustomerID"]==customer_id, "Age"].iloc[0]
        ages.append(age)
    return float(pd.Series(ages).mean())

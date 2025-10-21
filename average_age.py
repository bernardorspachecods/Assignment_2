import pandas as pd
from top_five_cust import top_five_cust

def average_age(df, customers) -> float:
    
    """
    This function receives a retail transaction DataFrame and a customer info DataFrame as input.
    It first identifies the 5 customers with the highest total purchases using the top_five_cust function, 
    and then calculates the average age of these top 5 customers.
    """
    top_customers = top_five_cust(df)
    ages = []
    for customer_id in top_customers:
        age = customers.loc[customers["CustomerID"]==customer_id, "Age"].iloc[0]
        ages.append(age)
    return float(pd.Series(ages).mean())

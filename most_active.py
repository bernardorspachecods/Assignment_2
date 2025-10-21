import pandas as pd
from typing import List

def most_active(customers) -> List[str]:
    
    """
    Identifies the customers who have been active for the longest period and returns their corresponding email addresses.
    """

    # Selects the customers of the df corresponding to the maximum value of active years
    most_active = customers[customers["YearsActive"] == customers["YearsActive"].max()]

    # Extracts their emails and saves them in a list of strings
    most_active_emails= list(most_active["Email"])

    return most_active_emails

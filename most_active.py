import pandas as pd
from typing import List

def most_active(customers) -> List[str]:
    
    """
    This function receives a Pandas DataFrame containing customer information as input.
    It identifies the customers who have been active for the longest period and returns their corresponding email addresses.
    """

    # Selects the customers of the df corresponding to the maximum value of active years
    most_active = customers[customers["YearsActive"] == customers["YearsActive"].max()]
<<<<<<< HEAD

    # Extracts their emails and saves them in a list of strings
    most_active_emails= list(most_active["Email"])

=======
    most_active_emails = most_active["Email"].unique().tolist()
>>>>>>> ff13b4d4f7699cc5cddcdef06a7bed85824c8ed6
    return most_active_emails

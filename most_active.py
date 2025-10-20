import pandas as pd
from typing import List

def most_active(customers) -> List[str]:
    # Your code goes here
    most_active = customers[customers["YearsActive"] == customers["YearsActive"].max()]
    most_active_emails= list(most_active["Email"])
    return most_active_emails

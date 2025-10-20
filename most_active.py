import pandas as pd
from typing import List

def most_active(customers) -> List[str]:
    # Your code goes here
    most_active = customers[customers["YearsActive"] == customers["YearsActive"].max()]
    most_active_emails = most_active["Email"].unique().tolist()
    return most_active_emails

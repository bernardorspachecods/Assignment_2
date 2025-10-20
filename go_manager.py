import pandas as pd
from go_sports import go_sports

def go_manager(teams, managers) -> str:
    
   # Builds the sports DataFrame
    sports = go_sports(teams, managers)

   # Calculates the total of wins for each managerID
    manager_wins = sports.groupby('managerID')['W'].sum()

    # Finds the manager with the highest number of wins
    best_manager_id = manager_wins.idxmax()

    # --- note --- : we assumed the last 3 characters of the manager ID were index or role identifiers (not part of the name)
    # Extracts the core name and capitalizes it
    best_manager_name = best_manager_id[:-3].capitalize()

    return best_manager_name

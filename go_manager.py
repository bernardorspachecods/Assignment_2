import pandas as pd
from go_sports import go_sports

def go_manager(teams, managers) -> str:
   
   """
   Identifies the manager ID with the highest total number of wins across all teams they have managed.
   """

   # Builds the sports DataFrame
   sports = go_sports(teams, managers)

   # Calculates the total of wins for each managerID
   manager_wins = sports.groupby('managerID')['W'].sum()

    # Finds the manager with the highest number of wins
   best_manager_id = manager_wins.idxmax()
   return best_manager_id

import pandas as pd
from go_sports import go_sports

def go_manager(teams, managers) -> str:
   
   """
   This function receives two Pandas DataFrames as input.
   It identifies the manager ID with the highest total number of wins across all 
   teams they have managed and returns the manager's ID.
   """

   # Builds the sports DataFrame
   sports = go_sports(teams, managers)

   # Calculates the total of wins for each managerID
   manager_wins = sports.groupby('managerID')['W'].sum()

   # Finds the manager with the highest number of wins
   best_manager_id = manager_wins.idxmax()
   return best_manager_id

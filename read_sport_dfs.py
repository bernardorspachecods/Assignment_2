import pandas as pd
from typing import Tuple

def read_sport_dfs(teams_filepath: str, managers_filepath: str) -> Tuple[pd.DataFrame]:
    
    """
    This function receives two string filepaths as input.
    It loads the teams and managers CSV files into two separate Pandas DataFrames and returns them as a tuple.
    """

    # Reads the csv files
    teams = pd.read_csv(teams_filepath)
    managers = pd.read_csv(managers_filepath)
    
    return (teams, managers)

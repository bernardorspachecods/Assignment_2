import pandas as pd
from typing import Tuple

def read_sport_dfs(teams_filepath: str, managers_filepath: str) -> Tuple[pd.DataFrame]:
    # Your code goes here
    teams = pd.read_csv(teams_filepath,encoding='utf-8')
    managers = pd.read_csv(managers_filepath,encoding='utf-8')
    return (teams, managers)

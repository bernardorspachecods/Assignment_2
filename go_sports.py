import pandas as pd

def go_sports(teams, managers) -> pd.DataFrame:
    """
    Merges team stats with manager data, returning a DataFrame of team name, 
    manager ID, year, wins (W), and losses (L), sorted chronologically.
    """

    # Creates copies of the df to avoid modifying the original dfs
    teams = teams.copy()
    managers = managers.copy()
    
    # Converts the teams year ID to datetime objects and extracts the year and sets invalid dates to NaT
    teams["yearID"] = pd.to_datetime(teams["yearID"], errors='coerce').dt.year

    # --- note --- : the raw data contained spaces in manager IDs, so we assumed these were entry errors and not part of the actual ID
    # Cleans managerID and removes duplicate manager entries for the same team in the same year
    managers["managerID"] = managers["managerID"].str.replace(" ", "")
    managers = managers.drop_duplicates(subset=["yearID", "teamID", "lgID"])

    # Merges the 2 dfs including only teams with corresponding manager entry
    merged = teams.merge(managers, on = ["yearID", "teamID", "lgID"], how="inner")
    
    # Selects the required columns with the required names
    teams_info = merged[["name", "managerID", "yearID", "W_x", "L_x"]]
    teams_info = teams_info.rename(columns={"W_x": "W", "L_x": "L"})

    # Returns the df required sorted firts by year and then by team name
    return teams_info.sort_values(by=['yearID', 'name'], ascending=[True, True])

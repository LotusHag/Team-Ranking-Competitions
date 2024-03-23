# functions.py
import pandas as pd

# Function to convert rank string to its numerical value based on the ranking method
def convert_rank(rank_str, rank_enum):
    try:
        return rank_enum[rank_str].value
    except KeyError:
        return 0  # Default value if the string is not found in the Enum

# Function to calculate metrics
def calculate_metrics(group):
    top5_ranks = group.nlargest(5, 'Rank')['Rank'].reset_index(drop=True)
    average_rank = top5_ranks.mean()
    if len(top5_ranks) == 5:
        difference = top5_ranks.iloc[0] - top5_ranks.iloc[-1]
    else:
        difference = 0  # Default difference if there are not enough players
    return pd.Series([average_rank, difference], index=['Average', 'Difference'])

# Function to apply ranking method and calculate metrics
def average_top5player_teams_with_metrics(df, rank_enum):
    df['Rank'] = df['Rank'].apply(lambda x: convert_rank(x, rank_enum))
    result_df = df.groupby('Team').apply(calculate_metrics).reset_index()
    result_df = result_df.sort_values(by='Average', ascending=False)
    return result_df

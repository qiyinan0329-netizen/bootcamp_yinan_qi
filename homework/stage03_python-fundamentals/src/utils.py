import pandas as pd

def get_summary_stats(df):
    '''
    Group a DataFrame by the 'category' columns and calculate the mean of numeric columns.
    Return a DataFrame with aggregate results.
    '''
    summary = df.groupby('category').mean(numeric_only=True).reset_index()
    return summary
    
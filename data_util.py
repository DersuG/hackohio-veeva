# No streamlit here, shouldn't be needed. These are util functions. Please comment what they return, or at least make the names verbose.
import pandas as pd



def get_column_sum(df_data, c='TRx_Month_1'):
    """
    Calculates the sum of a DataFrame column.

    Parameters:
    :param DataFrame df_data: The dataframe.
    :string c: The name of the column.
    
    Returns:
    :number sum: The sum of the column.  
    """

    sum = 0
    for _, df_row in df_data.iterrows():
        sum += df_row[c]
    #print(f'{sum = }')
    return sum
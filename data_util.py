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

def get_column_average(df_data, c='TRx_Month_1'):
    """
    Calculates the average of a DataFrame column.

    Parameters:
    :param DataFrame df_data: The dataframe.
    :string c: The name of the column.
    
    Returns:
    :number avg: The average of the column.  
    """

    sum = get_column_sum(df_data, c)
    avg = sum / len(df_data.index)
    return avg

def state_total_trx (df_data, s) :
    total_trx = 0
    for index, row in df_data.iterrows():
        if row['State'] == s :
            total_trx += sum_trx(row)
    return total_trx

def product_total_trx (df_data, p):
    total_trx = 0
    for index, row in df_data.iterrows():
        if row['Product'] == p :
            total_trx += sum_trx(row)
    return total_trx

def state_total_trx_product (df_data, s, p):
    total_trx = 0
    for index, row in df_data.iterrows():
        if row['State'] == s and row['Product'] == p:
            total_trx += sum_trx(row)
    return total_trx

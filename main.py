#import streamlit as sl
import pandas as pd
from data import * # Lmao

# Load data:
df_data = pd.read_csv('Prescriber_Data.csv')

# Lets get some statistics:


# If this is the file executed, run the following:
if __name__ == '__main__':
    get_total_minmax_trx(df_data)

    print('Minmax TRx for each month (1-6):')
    get_monthly_minmax_trx(df_data, 'TRx_Month_1')
    get_monthly_minmax_trx(df_data, 'TRx_Month_2')
    get_monthly_minmax_trx(df_data, 'TRx_Month_3')
    get_monthly_minmax_trx(df_data, 'TRx_Month_4')
    get_monthly_minmax_trx(df_data, 'TRx_Month_5')
    get_monthly_minmax_trx(df_data, 'TRx_Month_6')


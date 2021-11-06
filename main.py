import streamlit as sl
import pandas as pd
from data import * # Lmao
from data_util import * # Lmao

# Load data:
df_data = pd.read_csv('Prescriber_Data.csv')

# Lets get some statistics:
# comment lol


# If this is the file executed, run the following:
if __name__ == '__main__':
    df_data

    get_total_minmax_trx(df_data)

    print('Minmax TRx for each month (1-6):')
    get_monthly_minmax_trx(df_data, 'TRx_Month_1')
    get_monthly_minmax_trx(df_data, 'TRx_Month_2')
    get_monthly_minmax_trx(df_data, 'TRx_Month_3')
    get_monthly_minmax_trx(df_data, 'TRx_Month_4')
    get_monthly_minmax_trx(df_data, 'TRx_Month_5')
    get_monthly_minmax_trx(df_data, 'TRx_Month_6')

    print(f'Month 1 total TRx: {get_column_sum(df_data, "TRx_Month_1")}')
    print(f'Month 2 total TRx: {get_column_sum(df_data, "TRx_Month_2")}')
    print(f'Month 3 total TRx: {get_column_sum(df_data, "TRx_Month_3")}')
    print(f'Month 4 total TRx: {get_column_sum(df_data, "TRx_Month_4")}')
    print(f'Month 5 total TRx: {get_column_sum(df_data, "TRx_Month_5")}')
    print(f'Month 6 total TRx: {get_column_sum(df_data, "TRx_Month_6")}')

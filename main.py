import altair
import streamlit as st
import pandas as pd
from data import * # Lmao
from data_util import * # Lmao



# Load data:
df_data = pd.read_csv('Prescriber_Data.csv')

# Lets get some statistics:
# comment lol


def get_monthly_total_product_TRx(df_data, product='Cholecap'):
    df_product_data = df_data[df_data['Product'] == product]
    total = {}
    total['Month 1'] = get_column_sum(df_product_data, 'TRx_Month_1')
    total['Month 2'] = get_column_sum(df_product_data, 'TRx_Month_2')
    total['Month 3'] = get_column_sum(df_product_data, 'TRx_Month_3')
    total['Month 4'] = get_column_sum(df_product_data, 'TRx_Month_4')
    total['Month 5'] = get_column_sum(df_product_data, 'TRx_Month_5')
    total['Month 6'] = get_column_sum(df_product_data, 'TRx_Month_6')
    return total


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

    show_monthly_nrx_by_product(df_data)
    show_monthly_trx_by_product(df_data)
    
    #print(df_data[df_data['State'] == 'Ohio'])

    #show_state_total_trx(df_data)

# Need bar chart showing doctor name, number of prescriptions, etc.
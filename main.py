import streamlit as st
import pandas as pd
from data import * # Lmao
from data_util import * # Lmao



# Load data:
df_data = pd.read_csv('Prescriber_Data.csv')

# Lets get some statistics:


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


    # sums = []
    # sums.append(get_column_sum(df_data, "TRx_Month_1"))
    # sums.append(get_column_sum(df_data, "TRx_Month_2"))
    # sums.append(get_column_sum(df_data, "TRx_Month_3"))
    # sums.append(get_column_sum(df_data, "TRx_Month_4"))
    # sums.append(get_column_sum(df_data, "TRx_Month_5"))
    # sums.append(get_column_sum(df_data, "TRx_Month_6"))

    # print(f'Month 1 total TRx: {get_column_sum(df_data, "TRx_Month_1")}')
    # print(f'Month 2 total TRx: {get_column_sum(df_data, "TRx_Month_2")}')
    # print(f'Month 3 total TRx: {get_column_sum(df_data, "TRx_Month_3")}')
    # print(f'Month 4 total TRx: {get_column_sum(df_data, "TRx_Month_4")}')
    # print(f'Month 5 total TRx: {get_column_sum(df_data, "TRx_Month_5")}')
    # print(f'Month 6 total TRx: {get_column_sum(df_data, "TRx_Month_6")}')

    # Get a list of product names:
    products = []
    for p in df_data['Product']:
        if p not in products:
            products.append(p)

    d = {}
    for p in products:
        d[p] = get_monthly_total_product_TRx(df_data, p)
    print(f'{d}')


    st.vega_lite_chart(d, {
        'mark': {'type': 'bar', 'tooltip': True},
        'encoding': {
            'x': {'field': 'Month', 'type': 'quantitative'},
            'y': {'field': 'Total TRx', 'type': 'quantitative'},
        },
    })

    



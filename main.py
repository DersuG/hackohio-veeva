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
    product_names = []
    for p in df_data['Product']:
        if p not in product_names:
            product_names.append(p)

    product_monthly_trx = []
    for p in product_names:
        # product_monthly_trx.append(get_monthly_total_product_TRx(df_data, p))
        d = []
        d.append(get_column_sum(df_data[df_data['Product'] == p], 'TRx_Month_1'))
        d.append(get_column_sum(df_data[df_data['Product'] == p], 'TRx_Month_2'))
        d.append(get_column_sum(df_data[df_data['Product'] == p], 'TRx_Month_3'))
        d.append(get_column_sum(df_data[df_data['Product'] == p], 'TRx_Month_4'))
        d.append(get_column_sum(df_data[df_data['Product'] == p], 'TRx_Month_5'))
        d.append(get_column_sum(df_data[df_data['Product'] == p], 'TRx_Month_6'))
        product_monthly_trx.append(d)

    print(f'{product_names = }')
    print(f'{product_monthly_trx = }')



    df_chart_data = pd.DataFrame(columns=['month', 'product', 'total_trx'])
    for month in ['TRx_Month_1', 'TRx_Month_2', 'TRx_Month_3', 'TRx_Month_4', 'TRx_Month_5', 'TRx_Month_6']:
        for p in product_names:
            sum = get_column_sum(df_data[df_data['Product'] == p], month)
            df_chart_data = df_chart_data.append(
                {
                    'month': month,
                    'product': p,
                    'total_trx': sum
                },
                ignore_index=True
            )

    chart = altair.Chart(df_chart_data).mark_line(point=True).encode(
        x='month',
        y='total_trx',
        color='product'
    )
    st.altair_chart(
        chart,
        use_container_width=True
    )

    # chart = altair.Chart(df_chart_data).mark_bar().encode(
    #     x='month',
    #     y='total_trx',
    #     color='product'
    # )
    # st.altair_chart(
    #     chart,
    #     use_container_width=True
    # )


    # st.vega_lite_chart(
    #     chart_data,
    #     {
    #         'mark': {'type': 'bar', 'tooltip': True},
    #         'encoding': {
    #             'x': {
    #                 'field': 'month',
    #                 'type': 'ordinal',
    #                 'title': 'Month'
    #             },
    #             'y': {
    #                 'field': 'total_trx',
    #                 'aggregate': 'sum',
    #                 'stack': None,
    #                 'title': 'Total Monthly TRx'
    #             },
    #             'color': {
    #                 'field': 'product',
    #                 'title': 'Product'
    #             },
    #             "opacity": {"value": 0.7}
    #         }
    #     }
    # )

    
    


# Need bar chart showing doctor name, number of prescriptions, etc.
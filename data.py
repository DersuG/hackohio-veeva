import altair as altair
import streamlit as st
import pandas as pd

from data_util import *



def sum_trx(df_row):
    total_trx = 0
    total_trx += df_row['TRx_Month_1']
    total_trx += df_row['TRx_Month_2']
    total_trx += df_row['TRx_Month_3']
    total_trx += df_row['TRx_Month_4']
    total_trx += df_row['TRx_Month_5']
    total_trx += df_row['TRx_Month_6']
    return total_trx

def get_total_minmax_trx(df_data):
    #print('[r] get_total_minmax_trx()')

    max_trx = sum_trx(df_data.iloc[0, :]) # First row.
    max_trx_id = 0
    min_trx = sum_trx(df_data.iloc[-1, :]) # Last row.
    min_trx_id = 0

    for _, df_row in df_data.iterrows():
        total_trx = sum_trx(df_row)

        if total_trx > max_trx:
            max_trx = total_trx
            max_trx_id = df_row['id']
        if total_trx < min_trx:
            min_trx = total_trx
            min_trx_id = df_row['id']

        #print(f'Total TRx: {total_trx}, id = {df_row["id"]}')

    print(f'{max_trx = } ({max_trx_id = })')
    print(f'{min_trx = } ({min_trx_id = })')

def get_monthly_minmax_trx(df_data, c='TRx_Month_1'):
    #print('\n[r] get_monthly_minmax_trx()')

    max_monthly_trx = df_data.iloc[0, :][c]
    max_monthly_trx_id = 0
    min_monthly_trx = df_data.iloc[-1, :][c]
    min_monthly_trx_id = 0

    for _, df_row in df_data[['id', c]].iterrows(): # Double brackets to get a full dataframe.

        if df_row[c] > max_monthly_trx:
            max_monthly_trx = df_row[c]
            max_monthly_trx_id = df_row['id']
        if df_row[c] < min_monthly_trx:
            min_monthly_trx = df_row[c]
            min_monthly_trx_id = df_row['id']

    print(f'{max_monthly_trx = } ({max_monthly_trx_id = })')
    print(f'{min_monthly_trx = } ({min_monthly_trx_id = })')

#Displays global prescription totals per month in metric and line graph
def TRxByProduct(data):
    start = 0 
    TRx1 = 0 
    TRx2 = 0
    TRx3 = 0
    TRx4 = 0
    TRx5 = 0
    TRx6 = 0
    productsData = pd.DataFrame()
    st.header('Total Global Prescriptions')
    for x in range(len(data.index)):
        if(x>0):
            if(data.iloc[x,4] != data.iloc[x-1,4]):
                dataProduct = data.iloc[start:x,:]
                for index, row in dataProduct.iterrows():
                    TRx1+=row['TRx_Month_1']
                    TRx2+=row['TRx_Month_2']
                    TRx3+=row['TRx_Month_3']
                    TRx4+=row['TRx_Month_4']
                    TRx5+=row['TRx_Month_5']
                    TRx6+=row['TRx_Month_6']
                head1,head2 = st.columns(2)
                head1.header(dataProduct.iloc[0,4])
                head2=head2.checkbox(label=dataProduct.iloc[0,4],value=True)
                if head2:
                    col1,col2,col3,col4,col5,col6 = st.columns(6)
                    col1.metric('Month 1',TRx1)
                    col2.metric('Month 2',TRx2,TRx2-TRx1)
                    col3.metric('Month 3',TRx3,TRx3-TRx2)
                    col4.metric('Month 4',TRx4,TRx4-TRx3)
                    col5.metric('Month 5',TRx5,TRx5-TRx4)
                    col6.metric('Month 6',TRx6,TRx6-TRx5)
                    productsData = pd.concat([productsData,pd.DataFrame({dataProduct.iloc[0,4]:[TRx1,TRx2,TRx3,TRx4,TRx5,TRx6]})],axis=1)
                start = x
    if productsData.size>0:   
        st.line_chart(productsData)

def create_product_totalTRx_Graph(products):
    data = []
    for p in products:
        data.append(product_total_trx(p))
    fig = go.Figure([go.Bar(x=products, y=data)])
    fig.update_xaxes(title_text="Product")
    fig.update_yaxes(title_text="Total Number of Prescriptions")
    st.plotly_chart(fig)

def top_doctors_by_productNRx(df_data, p):
    doctors = []
    trx = []
    for index, row in df.iterrows():
        if row['Product'] == p :
            total_trx = sum_trx(row)
            if (len(doctors) == 0):
                doctors.append(row['first_name'] + ' ' + row['last_name'])
                trx.append(total_trx)
            elif (len(doctors) < 10 and len(doctors) != 0):
                for i in range(len(doctors)):
                    if total_trx > trx[i]:
                        doctors.insert(i, row['first_name'] + ' ' + row['last_name'])
                        trx.insert(i, total_trx)
                        break
                    else:
                        doctors.append(row['first_name'] + ' ' + row['last_name'])
                        trx.append(total_trx)
            elif (len(doctors) >= 10):
                for i in range(len(doctors)):
                    if total_trx > trx[i]:
                        doctors.insert(i, row['first_name'] + ' ' + row['last_name'])
                        trx.insert(i, total_trx)
                        del doctors[-1]
                        del trx[-1]
                        break
    df_doctors = pd.DataFrame({"Doctor": doctors, "Total TRx": trx})
    return df_doctors
    
def show_monthly_trx_by_product(df_data):
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

import altair as altair
import streamlit as st
import pandas as pd

from data_util import *



def sum_trx(df_row):
    total_trx = 0
    total_trx += df_row['TRx_Month_1']
    total_trx += df_row['TRx_Month_2']
    total_trx += df_row['TRx_Month_3']
    total_trx += df_row['TRx_Month_4']
    total_trx += df_row['TRx_Month_5']
    total_trx += df_row['TRx_Month_6']
    return total_trx

def get_total_minmax_trx(df_data):
    #print('[r] get_total_minmax_trx()')

    max_trx = sum_trx(df_data.iloc[0, :]) # First row.
    max_trx_id = 0
    min_trx = sum_trx(df_data.iloc[-1, :]) # Last row.
    min_trx_id = 0

    for _, df_row in df_data.iterrows():
        total_trx = sum_trx(df_row)

        if total_trx > max_trx:
            max_trx = total_trx
            max_trx_id = df_row['id']
        if total_trx < min_trx:
            min_trx = total_trx
            min_trx_id = df_row['id']

        #print(f'Total TRx: {total_trx}, id = {df_row["id"]}')

    print(f'{max_trx = } ({max_trx_id = })')
    print(f'{min_trx = } ({min_trx_id = })')

def get_total_minmax_nrx(df_data):
    #print('[r] get_total_minmax_nrx()')

    max_nrx = sum_nrx(df_data.iloc[0, :]) # First row.
    max_nrx_id = 0
    min_nrx = sum_nrx(df_data.iloc[-1, :]) # Last row.
    min_nrx_id = 0

    for _, df_row in df_data.iterrows():
        total_nrx = sum_nrx(df_row)

        if total_nrx > max_nrx:
            max_nrx = total_nrx
            max_nrx_id = df_row['id']
        if total_nrx < min_nrx:
            min_nrx = total_nrx
            min_nrx_id = df_row['id']

        #print(f'Total NRx: {total_nrx}, id = {df_row["id"]}')

    print(f'{max_nrx = } ({max_nrx_id = })')
    print(f'{min_nrx = } ({min_nrx_id = })')

def get_monthly_minmax_trx(df_data, c='TRx_Month_1'):
    #print('\n[r] get_monthly_minmax_trx()')

    max_monthly_trx = df_data.iloc[0, :][c]
    max_monthly_trx_id = 0
    min_monthly_trx = df_data.iloc[-1, :][c]
    min_monthly_trx_id = 0

    for _, df_row in df_data[['id', c]].iterrows(): # Double brackets to get a full dataframe.

        if df_row[c] > max_monthly_trx:
            max_monthly_trx = df_row[c]
            max_monthly_trx_id = df_row['id']
        if df_row[c] < min_monthly_trx:
            min_monthly_trx = df_row[c]
            min_monthly_trx_id = df_row['id']

    print(f'{max_monthly_trx = } ({max_monthly_trx_id = })')
    print(f'{min_monthly_trx = } ({min_monthly_trx_id = })')

def get_monthly_minmax_nrx(df_data, c='NRx_Month_1'):
    #print('\n[r] get_monthly_minmax_trx()')

    max_monthly_nrx = df_data.iloc[0, :][c]
    max_monthly_nrx_id = 0
    min_monthly_nrx = df_data.iloc[-1, :][c]
    min_monthly_nrx_id = 0

    for _, df_row in df_data[['id', c]].iterrows():

        if df_row[c] > max_monthly_nrx:
            max_monthly_nrx = df_row[c]
            max_monthly_nrx_id = df_row['id']
        if df_row[c] < min_monthly_nrx:
            min_monthly_nrx = df_row[c]
            min_monthly_nrx_id = df_row['id']

    print(f'{max_monthly_nrx = } ({max_monthly_nrx_id = })')
    print(f'{min_monthly_nrx = } ({min_monthly_nrx_id = })')

#Displays global prescription totals per month in metric and line graph
def TRxByProduct(data):
    start = 0 
    TRx1 = 0 
    TRx2 = 0
    TRx3 = 0
    TRx4 = 0
    TRx5 = 0
    TRx6 = 0
    productsData = pd.DataFrame()
    st.header('Total Global Prescriptions')
    for x in range(len(data.index)):
        if(x>0):
            if(data.iloc[x,4] != data.iloc[x-1,4]):
                dataProduct = data.iloc[start:x,:]
                for index, row in dataProduct.iterrows():
                    TRx1+=row['TRx_Month_1']
                    TRx2+=row['TRx_Month_2']
                    TRx3+=row['TRx_Month_3']
                    TRx4+=row['TRx_Month_4']
                    TRx5+=row['TRx_Month_5']
                    TRx6+=row['TRx_Month_6']
                head1,head2 = st.columns(2)
                head1.header(dataProduct.iloc[0,4])
                head2=head2.checkbox(label=dataProduct.iloc[0,4],value=True)
                if head2:
                    col1,col2,col3,col4,col5,col6 = st.columns(6)
                    col1.metric('Month 1',TRx1)
                    col2.metric('Month 2',TRx2,TRx2-TRx1)
                    col3.metric('Month 3',TRx3,TRx3-TRx2)
                    col4.metric('Month 4',TRx4,TRx4-TRx3)
                    col5.metric('Month 5',TRx5,TRx5-TRx4)
                    col6.metric('Month 6',TRx6,TRx6-TRx5)
                    productsData = pd.concat([productsData,pd.DataFrame({dataProduct.iloc[0,4]:[TRx1,TRx2,TRx3,TRx4,TRx5,TRx6]})],axis=1)
                start = x
    if productsData.size>0:   
        st.line_chart(productsData)
    
def show_monthly_trx_by_product(df_data):
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

def show_monthly_nrx_by_product(df_data):
    # Get a list of product names:
    product_names = []
    for p in df_data['Product']:
        if p not in product_names:
            product_names.append(p)

    product_monthly_trx = []
    for p in product_names:
        # product_monthly_trx.append(get_monthly_total_product_TRx(df_data, p))
        d = []
        d.append(get_column_sum(df_data[df_data['Product'] == p], 'NRx_Month_1'))
        d.append(get_column_sum(df_data[df_data['Product'] == p], 'NRx_Month_2'))
        d.append(get_column_sum(df_data[df_data['Product'] == p], 'NRx_Month_3'))
        d.append(get_column_sum(df_data[df_data['Product'] == p], 'NRx_Month_4'))
        d.append(get_column_sum(df_data[df_data['Product'] == p], 'NRx_Month_5'))
        d.append(get_column_sum(df_data[df_data['Product'] == p], 'NRx_Month_6'))
        product_monthly_trx.append(d)

    print(f'{product_names = }')
    print(f'{product_monthly_trx = }')



    df_chart_data = pd.DataFrame(columns=['month', 'product', 'total_nrx'])
    for month in ['NRx_Month_1', 'NRx_Month_2', 'NRx_Month_3', 'NRx_Month_4', 'NRx_Month_5', 'NRx_Month_6']:
        for p in product_names:
            sum = get_column_sum(df_data[df_data['Product'] == p], month)
            df_chart_data = df_chart_data.append(
                {
                    'month': month,
                    'product': p,
                    'total_nrx': sum
                },
                ignore_index=True
            )

    chart = altair.Chart(df_chart_data).mark_line(point=True).encode(
        x='month',
        y='total_nrx',
        color='product'
    )
    st.altair_chart(
        chart,
        use_container_width=True
    )

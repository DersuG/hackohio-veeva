import streamlit as sl
import pandas as pd



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
    sl.header('Total Global Prescriptions')
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
                head1,head2 = sl.columns(2)
                head1.header(dataProduct.iloc[0,4])
                head2=head2.checkbox(label=dataProduct.iloc[0,4],value=True)
                if head2:
                    col1,col2,col3,col4,col5,col6 = sl.columns(6)
                    col1.metric('Month 1',TRx1)
                    col2.metric('Month 2',TRx2,TRx2-TRx1)
                    col3.metric('Month 3',TRx3,TRx3-TRx2)
                    col4.metric('Month 4',TRx4,TRx4-TRx3)
                    col5.metric('Month 5',TRx5,TRx5-TRx4)
                    col6.metric('Month 6',TRx6,TRx6-TRx5)
                    productsData = pd.concat([productsData,pd.DataFrame({dataProduct.iloc[0,4]:[TRx1,TRx2,TRx3,TRx4,TRx5,TRx6]})],axis=1)
                start = x
    if productsData.size>0:   
        sl.line_chart(productsData)
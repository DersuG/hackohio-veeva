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


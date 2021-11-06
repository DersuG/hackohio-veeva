#import streamlit as sl
import pandas as pd

# Load data:
data_df = pd.read_csv('Prescriber_Data.csv')
print(f'{data_df}')

print(f'{data_df["id"]}')






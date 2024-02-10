import streamlit as st
import pandas as pd
import numpy as np

st.title('EfPeeL - Likelihood FC')

df_data = pd.read_csv('merged_gw_23.csv')

pemainku = [
    'Jordan Pickford',
    'Oleksandr Zinchenko',
    'William Saliba',
    'Vitalii Mykolenko',
    'Cole Palmer',
    'Richarlison de Andrade',
    'Kevin De Bruyne',
    'Bukayo Saka',
    'Julián Álvarez',
    'Ollie Watkins',
    'Dominic Solanke',
    'Guglielmo Vicario',
    'Virgil van Dijk',
    'Pedro Porro',
    'Anthony Gordon'
]
nama_tim = df_data['team'].unique()

kolom1, kolom2 = st.columns(2)
with kolom1:
    selected_tim1 = st.selectbox(
        'Pilih tim 1',
        nama_tim
    )
    selected_pemain1 = st.selectbox(
        'Select player1?',
         pemainku    
        )

    st.write('You selected:', selected_pemain1)
    df_data1 = df_data[df_data['team'] == selected_tim1]
    player_data1 = df_data1[df_data1['name'] == selected_pemain1]
    st.line_chart(
    player_data1, x='GW', y='total_points', color=["#FF0000"]  # Optional
    )

with kolom2:
    selected_tim2 = st.selectbox(
        'Pilih tim 2',
        nama_tim
    )
    selected_pemain2 = st.selectbox(
        'Select player2?',
         pemainku    
        )
    st.write('You selected:', selected_pemain2)
    df_data2 = df_data[df_data['team'] == selected_tim2]
    player_data2 = df_data2[df_data2['name'] == selected_pemain2]
    st.line_chart(
    player_data2, x='GW', y='total_points', color=["#0000FF"]
    )
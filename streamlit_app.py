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

selected_pemain1 = st.selectbox(
    'Select player1?',
     pemainku    
    )

st.write('You selected:', selected_pemain1)

selected_pemain2 = st.selectbox(
    'Select player2?',
     pemainku    
    )
st.write('You selected:', selected_pemain2)

player_data1 = df_data[df_data['name'] == selected_pemain1]
player_data2 = df_data[df_data['name'] == selected_pemain2]
gameweek = player_data1['GW']
st.line_chart(
   chart_data, x=gameweek, y=[player_data1['total_points'], player_data2['total_points']], color=["#FF0000", "#0000FF"]  # Optional
)

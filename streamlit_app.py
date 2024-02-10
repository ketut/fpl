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

option = st.selectbox(
    'Select player1?',
    [pemain: pemain in pemainku]    
    )

st.write('You selected:', option)



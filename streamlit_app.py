import streamlit as st
import pandas as pd
import numpy as np
import requests 


st.title('EfPeeL - Likelihood FC')

df_data = pd.read_csv('merged_gw_23.csv')
nama_tim = df_data['team'].unique()

liga = requests.get('https://fantasy.premierleague.com/api/leagues-classic/2381820/standings/').json()
df_liga = pd.DataFrame(liga['standings']['results'])
st.subheader(liga['league']['name'], divider=grey)
st.table(df_liga[['entry_name','rank','last_rank','total']])


kolom1, kolom2 = st.columns(2)
with kolom1:
    selected_tim1 = st.selectbox(
        'Pilih tim 1',
        nama_tim
    )
    
    df_data1 = df_data[df_data['team'] == selected_tim1]
    selected_pemain1 = st.selectbox(
        'Pilih pemain 1',
         df_data1['name'].unique()    
        )
    st.write(f"{selected_tim1} >> {selected_pemain1}")

    player_data1 = df_data1[df_data1['name'] == selected_pemain1]
    st.line_chart(
    player_data1, x='GW', y='total_points', color=["#FF0000"]  # Optional
    )
    st.write(f'Bonus per gameweek - {selected_pemain1}')
    st.line_chart(
    player_data1, x='GW', y='bonus', color=["#0000FF"]
    )

with kolom2:
    selected_tim2 = st.selectbox(
        'Pilih tim 2',
        nama_tim
    )
    
    df_data2 = df_data[df_data['team'] == selected_tim2]
    selected_pemain2 = st.selectbox(
        'Pilih pemain 2',
         df_data2['name'].unique()   
        )
    st.write(f"{selected_tim2} >> {selected_pemain2}")
    player_data2 = df_data2[df_data2['name'] == selected_pemain2]
    st.line_chart(
    player_data2, x='GW', y='total_points', color=["#0000FF"]
    )
    st.write(f'Bonus per gameweek - {selected_pemain2}')
    st.line_chart(
    player_data2, x='GW', y='bonus', color=["#0000FF"]
    )
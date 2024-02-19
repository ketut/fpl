import streamlit as st
import pandas as pd
import numpy as np
import requests 


st.title('EfPeeL - Likelihood FC')
st.subheader('Ngutang kandik, nuduk sanshaw', divider='grey')

df_data = pd.read_csv('merged_gw.csv')
df_data = df_data.sort_values(by='total_points', ascending=False)
nama_tim = df_data['team'].unique()
players =  requests.get('https://fantasy.premierleague.com/api/bootstrap-static/').json()
players_df = pd.DataFrame(players['elements'])
teams_df = pd.DataFrame(players['teams'])
fixtures_df = pd.DataFrame(players['events'])
gameweek =  fixtures_df.iloc[0].id
daftar_tim = {'Lorosae Familia' : 10647937,'JPL11' : 10639843,'The Kang Squad' : 10498059,'Pearson FC' : 10640142,'Shinryuji Naga' : 10647775,'oxxxa team' : 10647999,'Raurus' : 10636098,'Kang Jurus' : 10512926,'Lethimcook' : 10636038,'Kang Fasih' : 10537732,'Mas Bro FC' : 10636210,'Bukit Kangin FC' : 10636233,'Persibu Buleleng' : 10636113,'Ilmu Padi FC' : 10647932,'Germa Team' : 10639504,'CukJitNe Bros' : 10636154,'Haus Gol' : 10648262,'Mengkeb United' : 10537734,'Level Up' : 10639569,'Mega' : 10537875,'Abang Cilok' : 10636052,'Sakit Gede' : 10648189,'Foodball �' : 10636376,'Anbu FC' : 10647979,'Sembung' : 10564238,'Likelihood FC' : 10537782}

liga = requests.get('https://fantasy.premierleague.com/api/leagues-classic/2381820/standings/').json()
df_liga = pd.DataFrame(liga['standings']['results'])
# df_liga = df_liga.sort_values(by='total', ascending=False)
st.subheader(liga['league']['name'], divider='grey')
# st.subheader(f"Gameweek ke-{gameweek}")
st.table(df_liga[['entry_name','rank','last_rank','total']])
st.bar_chart(df_liga, x='entry_name', y='total')

liga_bps5100 = requests.get('https://fantasy.premierleague.com/api/leagues-classic/2403108/standings/').json()
df_liga_bps5100 = pd.DataFrame(liga_bps5100['standings']['results'])
# df_liga_bps5100 = df_liga_bps5100.sort_values(by='total', ascending=False)
st.subheader(liga_bps5100['league']['name'], divider='grey')
# st.subheader(f"Gameweek ke-{gameweek}")
st.table(df_liga_bps5100[['entry_name','rank','last_rank','total']])

st.bar_chart(df_liga_bps5100, x='entry_name', y='total')

st.subheader("Intip Tim Lawan", divider="grey")
selected_tim_bps5100 = st.selectbox(
    'Pilih Tim',
    [x['entry_name'] for x in liga_bps5100['standings']['results']]
)
selected_gameweek = st.selectbox(
    'Pilih gameweek',
    [g for g in range(23,39)]
)

for baris in liga_bps5100['standings']['results']:
    if baris['entry_name'] == selected_tim_bps5100:
        id_tim = daftar_tim[selected_tim_bps5100]
        # st.success(id_tim)
        team = requests.get(f"https://fantasy.premierleague.com/api/entry/{id_tim}/event/{selected_gameweek}/picks/").json()
        # st.warning(len(team))
        if len(team) == 1:
            st.warning("Pilih gameweek yang sesuai")
        else:
            players = [x['element'] for x in team['picks']]
            pemain = []
            for id_pemain in players:
                pemain.append(list(players_df[players_df['id'] == id_pemain]['web_name'])[0])
            st.success(f"Squad {selected_tim_bps5100} >> {', '.join(pemain)}")
            
            
        # try:
        #     if team['detail']:
        #         st.warning("Pilih gameweek yang sesuai")
        #     else: 
        #         players = [x['element'] for x in team['picks']]
        #         pemain = []
        #         for id_pemain in players:
        #             pemain.append(list(players_df[players_df['id'] == id_pemain]['web_name'])[0])
        #         st.success(f"Squad {selected_tim_bps5100} >> {pemain}")
        # except:
        #     players = [x['element'] for x in team['picks']]
        #     pemain = []
        #     for id_pemain in players:
        #         pemain.append(list(players_df[players_df['id'] == id_pemain]['web_name'])[0])
        #     st.success(f"Squad {selected_tim_bps5100} >> {pemain}")

st.subheader("Komparasi pemain", divider="grey")
kolom1, kolom2 = st.columns(2)

with kolom1:
    selected_tim1 = st.selectbox(
        'Pilih tim 1',
        nama_tim
    )
    
    df_data1 = df_data[df_data['team'] == selected_tim1]
    # df_data1 = df_data1.sort_values(by=, ascending=False)
    selected_pemain1 = st.selectbox(
        'Pilih pemain 1',
         df_data1['name'].unique()    
        )
    st.write(f"{selected_tim1} >> {selected_pemain1}")
    st.write("Total points per gameweek - {selected_pemain1}")
    player_data1 = df_data1[df_data1['name'] == selected_pemain1]
    st.line_chart(
    player_data1, x='GW', y='total_points', color=["#FF0000"]  # Optional
    )
    # st.write(f'Bonus per gameweek - {selected_pemain1}')
    # st.line_chart(
    # player_data1, x='GW', y='bonus', color=["#0000FF"]
    # )

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
    st.write("Total points per gameweek - {selected_pemain2}")
    player_data2 = df_data2[df_data2['name'] == selected_pemain2]
    st.line_chart(
    player_data2, x='GW', y='total_points', color=["#0000FF"]
    )
    # st.write(f'Bonus per gameweek - {selected_pemain2}')
    # st.line_chart(
    # player_data2, x='GW', y='bonus', color=["#0000FF"]
    # )
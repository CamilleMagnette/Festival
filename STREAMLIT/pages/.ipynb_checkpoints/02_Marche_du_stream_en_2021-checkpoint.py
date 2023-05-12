import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np 
import seaborn as sns
from PIL import Image


# Afficher notre logo dans le sidebar
notre_logo = Image.open('images/logo.png')
image_container = st.container()
with image_container:
    st.sidebar.image(notre_logo, width=300)
    
st.markdown("# LE MARCHÉ DU STREAM ACTUEL 🎧")
st.subheader('Les talents du moment...et jeunes talents à venir')
#st.sidebar.markdown("# Les talents du moment 🎼")



# Importer le dataset TOP 2000 : Janvier 2017 à dec 2021
df_top_200 = pd.read_csv("datasets/top_200.csv", sep = ",")
# Importer le dataset Amine : 
df_dataset = pd.read_csv("datasets/dataset.csv", sep = ",")

# Afficher le dataframe
# st.write(df_top_200)

# CREER DES TAB 
tab1, tab2, tab3, tab4 = st.tabs(['TOP 10 ARTISTES', 'TOP 10 MORCEAUX', 'BOX PLOT', 'TOP 10 PROGRESSION'])


# TRAVAILLER SUR LES TAB 

with tab1 : 

    st.subheader('Artistes les plus streamés sur Spotify en 2021')
    st.markdown('Par volume de stream et par volume de titre')

    df3 = df_top_200

    # Sélection du df sur l'année 2021
    df3['date'] = pd.to_datetime(df3['date'])
    mask = df3['date'] > '2020-12-31'
    df3 = df3[mask].copy()

    # Constitue 2 DF : un global et un france uniquement 
    df3_france = df3[df3['region'] =='France'].copy()
    df_grouped_france_titre = df3_france.groupby('title').agg({'streams': 'max', 'artist': lambda x: x.iloc[0]}).reset_index()

    df3_global = df3[df3['region']=='Global'].copy()
    df_grouped_global_titre = df3_global.groupby('title').agg({'streams': 'max', 'artist': lambda x: x.iloc[0]}).reset_index()
    
    # création de la grille horizontale
    col1, col2 = st.columns(2)
    
    with col1 :

        # Détermination du dataframe pour le graphique TOP10 France par Artiste en volume de stream avec volume de titre
        df_grouped_france_artiste = df_grouped_france_titre.groupby('artist').agg({'streams': 'sum'})
        df_grouped_france_artiste = df_grouped_france_artiste.sort_values(by='streams', ascending=False)
        df4 = df_grouped_france_artiste.head(10).copy().reset_index()
        df5 = df_grouped_france_titre[df_grouped_france_titre['artist'].isin(df4['artist'])]
        df5 = df5.sort_values(by='streams', ascending=False)
        df6 = df5.groupby('artist').agg({'title': 'count', 'streams': 'sum'}).reset_index()
        df6 = df6.rename(columns={'title': 'nbre_de_titre', 'streams': 'total_stream'})
        df6 = df6.sort_values(by='total_stream', ascending=False)

        # Créer le graphique 
        top10FR = px.bar(df6, x='artist', y='total_stream', color='nbre_de_titre')
        top10FR.update_layout(
        title='TOP 10 des artistes écoutés en FRANCE',
        xaxis_title='',
        yaxis_title='Volume de Stream')

        # Afficher le graphique
        st.plotly_chart(top10FR)

    with col2 :

         # Détermination du dataframe pour le graphique TOP10 MONDE par Artiste en volume de stream avec volume de titre
        df_grouped_global_artiste = df_grouped_global_titre.groupby('artist').agg({'streams': 'sum'})
        df_grouped_global_artiste = df_grouped_global_artiste.sort_values(by='streams', ascending=False)
        df7 = df_grouped_global_artiste.head(10).copy().reset_index()
        df8 = df_grouped_global_titre[df_grouped_global_titre['artist'].isin(df7['artist'])]
        df8 = df8.sort_values(by='streams', ascending=False)
        df9 = df8.groupby('artist').agg({'title': 'count', 'streams': 'sum'}).reset_index()
        df9 = df9.rename(columns={'title': 'nbre_de_titre', 'streams': 'total_stream'})
        df9 = df9.sort_values(by='total_stream', ascending=False)

        # Créer le graphique 
        top10GB = px.bar(df9, x='artist', y='total_stream', color='nbre_de_titre')
        top10GB.update_layout(
        title='TOP 10 des artistes écoutés dans le MONDE',
        xaxis_title='',
        yaxis_title='Volume de Stream')

        # Afficher le graphique
        st.plotly_chart(top10GB)
    
    
with tab2 : 
    
    st.subheader('Morceaux les plus streamés sur Spotify en 2021')
    
    # création de la grille horizontale
    col1, col2 = st.columns(2)
    
    with col1 :
        
        df3 = df_top_200
        
        # Sélection du df sur l'année 2021
        df3['date'] = pd.to_datetime(df3['date'])
        mask = df3['date'] > '2020-12-31'
        df3 = df3[mask].copy()
        
        df3_france = df3[df3['region'] =='France'].copy()
        df_grouped_france_titre = df3_france.groupby('title').agg({'streams': 'max', 'artist': lambda x: x.iloc[0]}).reset_index()
        # Filtrer les 10 titres ayant la valeur de stream maximale et trier les données
        df_grouped_france_titre_sorted = df_grouped_france_titre.sort_values(by= 'streams', ascending=False).head(10)
        #st.write(df_grouped_france_titre_sorted)

        # Créer le graphique
        fig6, ax = plt.subplots(figsize=(10, 6))

        # Ajouter les barres pour les streams
        fig6 = px.bar(df_grouped_france_titre_sorted, x = 'title', y ='streams', color = 'artist')
        fig6.update_layout(title='TOP 10 streamés en France', xaxis_title='Titles',yaxis_title='Volume de Stream')

        # Afficher le graphique
        st.plotly_chart(fig6)

        
    with col2 :
        
        df3 = df_top_200
        
        # Sélection du df sur l'année 2021
        df3['date'] = pd.to_datetime(df3['date'])
        mask = df3['date'] > '2020-12-31'
        df3 = df3[mask].copy()
        
        df3_global = df3[df3['region']=='Global'].copy()
        df_grouped_global_titre = df3_global.groupby('title').agg({'streams': 'max', 'artist': lambda x: x.iloc[0]}).reset_index()

        # Filtrer les 10 titres ayant la valeur de stream maximale et trier les données
        df_grouped_global_titre_sorted = df_grouped_global_titre.sort_values(by= 'streams', ascending=False).head(10)

        # Créer le graphique
        fig5, ax = plt.subplots(figsize=(10, 6))

        # Ajouter les barres pour les streams
        fig5 = px.bar(df_grouped_global_titre_sorted, x = 'title', y ='streams', color = 'artist')
        fig5.update_layout(title='TOP 10 streamés dans le Monde', xaxis_title='Titles',yaxis_title='Volume de Stream')

        # Afficher le graphique
        st.plotly_chart(fig5)
        
        
with tab3 : 
    
    st.subheader('Distribution des streams en 2021 par artiste (dernier quartile uniquement)')
    
    st.markdown('Une pépite en france = Entre 230 et 350 stream avec une forte progression')
    st.markdown('Une pépite total monde = Entre 2,2M et 3M stream avec une forte progression')


    df3 = df_top_200
    
    # Sélection du df sur l'année 2021
    df3['date'] = pd.to_datetime(df3['date'])
    mask = df3['date'] > '2020-12-31'
    df3 = df3[mask].copy()
    
    # création de la grille horizontale
    col1, col2 = st.columns(2)
    
    with col1 :
    
        Q3_FR = df_grouped_france_artiste['streams'].quantile(0.75)
        df_stat_frQ3 = df_grouped_france_artiste[df_grouped_france_artiste['streams']>Q3_FR]

        # BOXPLOT sur la distribution du stream pour le df France 2021, minimum fixé au Q3
        #fig, ax = plt.subplots(figsize=(10, 6))
        fig1 = px.box(df_stat_frQ3, x='streams', orientation='h', boxmode='overlay', color_discrete_sequence=['blue'], title='Streams en France')

        # Afficher le graphique plotly
        st.plotly_chart(fig1)
   
    with col2 :

        df3_global = df3[df3['region']=='Global'].copy()
        df_grouped_global_artiste = df3_global.groupby('title').agg({'streams': 'max', 'artist': lambda x: x.iloc[0]}).reset_index()

        Q3_GB = df_grouped_global_titre['streams'].quantile(0.75)
        df_stat_gbQ3 = df_grouped_global_artiste[df_grouped_global_artiste['streams']>Q3_GB]

        fig2 = px.box(df_stat_gbQ3, x='streams', orientation='h', boxmode='overlay', color_discrete_sequence=['blue'], title='Streams dans le Monde')

        # Afficher le graphique plotly
        st.plotly_chart(fig2)


with tab4 : 

    st.subheader('Artistes avec la plus forte augmentation de streams en 2021')
    
    # création de la grille horizontale
    col1, col2 = st.columns(2)

    # Sélection du df sur l'année 2021
    df_top_200['date'] = pd.to_datetime(df_top_200['date'])
    mask = df_top_200['date'] > '2020-12-31'
    annee_2021 = df_top_200[mask].copy()
    
    with col1 :

        # On selectionne que les artiste écoutés en FRANCE 
        annee_2021_FR = annee_2021[annee_2021['region'] == 'France']

        # Filtrer les artistes avec 'NEW_ENTRY' dans la colonne 'trend'
        new_entry_artists_FR = annee_2021_FR[annee_2021_FR['trend'] == 'NEW_ENTRY']

        # Trouver la valeur maximale de streams
        title_max = annee_2021_FR.groupby('title').agg({'streams': 'max', 'artist': lambda x: x.iloc[0]}).reset_index()

        # Merge new entry artists et title max
        df_merge_FR = pd.merge(new_entry_artists_FR, title_max, how="left", on='title')    

        # Garder uniquement les colonnes souhaitées
        df_merge_FR = df_merge_FR[['title', 'region', 'artist_x', 'streams_x', 'streams_y']]

        # Renommer les colonnes
        df_merge_FR = df_merge_FR.rename(columns={'streams_x': 'entry_streams', 'streams_y': 'streams_max', 'artist_x' : 'artist' })

        # On regroupe par artiste
        df_merge_groupby_artiste_FR = df_merge_FR.groupby('artist').agg({'entry_streams': 'sum', 'streams_max' : 'sum' }).reset_index()

        # On ajoute une colonne avec la différence
        df_merge_groupby_artiste_FR['difference'] = df_merge_groupby_artiste_FR['streams_max'] - df_merge_groupby_artiste_FR['entry_streams']
        df_merge_groupby_artiste_FR_sorted = df_merge_groupby_artiste_FR.sort_values('difference', ascending=False).head(10)

        # Graphique
        Top_evolution_FR = px.bar(df_merge_groupby_artiste_FR_sorted, x='artist', y='difference', color='artist')
        Top_evolution_FR.update_layout(title='TOP 10 streamés en France',xaxis_title='',yaxis_title='Volume de Streams',showlegend=False)
        st.plotly_chart(Top_evolution_FR)
    
    with col2 :

        # On selectionne que les artiste écoutés GLOBAL
        annee_2021_GB = annee_2021[annee_2021['region'] == 'Global']
        
        # Filtrer les artistes avec 'NEW_ENTRY' dans la colonne 'trend'
        new_entry_artists_GB = annee_2021_GB[annee_2021_GB['trend'] == 'NEW_ENTRY']
        
        # Trouver la valeur maximale de streams
        title_max = annee_2021_GB.groupby('title').agg({'streams': 'max', 'artist': lambda x: x.iloc[0]}).reset_index()
        
        # Merge new entry artists et title max
        df_merge_GB = pd.merge(new_entry_artists_GB, title_max, how="left", on='title')
        
        # Garder uniquement les colonnes souhaitées
        df_merge_GB = df_merge_GB[['title', 'region', 'artist_x', 'streams_x', 'streams_y']]
        
        # Renommer les colonnes
        df_merge_GB = df_merge_GB.rename(columns={'streams_x': 'entry_streams', 'streams_y': 'streams_max', 'artist_x' : 'artist' })
        
        # On regroupe par artiste
        df_merge_groupby_artiste_GB = df_merge_GB.groupby('artist').agg({'entry_streams': 'sum', 'streams_max' : 'sum' }).reset_index()
        
        # On ajoute une colonne avec la différence
        df_merge_groupby_artiste_GB['difference'] = df_merge_groupby_artiste_GB['streams_max'] - df_merge_groupby_artiste_GB['entry_streams']
        df_merge_groupby_artiste_GB_sorted = df_merge_groupby_artiste_GB.sort_values('difference', ascending=False).head(10)
        
        # Graphique
        Top_evolution_GB = px.bar(df_merge_groupby_artiste_GB_sorted, x='artist', y='difference', color='artist')
        Top_evolution_GB.update_layout(title='TOP 10 streamés dans le Monde',xaxis_title='',yaxis_title='Volume de Streams',showlegend=False)
        st.plotly_chart(Top_evolution_GB)
    



import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np  


st.markdown("# LE MARCHE DU STREAM ACTUEL 🎧")
st.subheader('Les talents du moment...et jeunes talents à venir')

#st.sidebar.markdown("# Les talents du moment 🎼")


# Importer le dataset : Janvier 2017 à dec 2021
df_top_200 = pd.read_csv("datasets/top_200.csv", sep = ",")
# Afficher le dataframe
# st.write(df_top_200)

# CREER DES TAB 
tab1, tab2, tab3, tab4, tab5 = st.tabs(['TOP 10 ARTISTES', 'TOP 10 MORCEAUX', 'TOP 10 PEPITES', 'BOX PLOT', 'BACK UP'])


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
        title='TOP 10 artistes FRANCE',
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
        title='TOP 10 artistes MONDE',
        xaxis_title='',
        yaxis_title='Volume de Stream')

        # Afficher le graphique
        st.plotly_chart(top10GB)
    
    
with tab2 : 
    
    st.subheader('Morceaux les plus streamés en 2021 - Total MONDE')
    
    df3 = df_top_200
    df3_global = df3[df3['region']=='Global'].copy()
    df_grouped_global_titre = df3_global.groupby('title').agg({'streams': 'max', 'artist': lambda x: x.iloc[0]}).reset_index()
    
    df_grouped_global_titre_sorted = df_grouped_global_titre.sort_values(by='streams', ascending=False)

    # Filtrer les 10 titres ayant la valeur de stream maximale et trier les données
    df_grouped_global_titre_sorted = df_grouped_global_titre_sorted.sort_values('streams', ascending=False).head(10)
    
    # Créer le graphique
    fig5, ax = plt.subplots(figsize=(10, 6))

    # Ajouter les barres pour les streams
    fig5 = px.bar(df_grouped_global_titre_sorted, x = 'title', y ='streams', color = 'artist')
    
    # Afficher le graphique
    st.plotly_chart(fig5)

    
with tab3 : 
    
    st.subheader('Artistes avec la plus forte augmentation de streams sur les 6 derniers mois')

    # Convertir la colonne date en datetime et filtrer les données pour n'inclure que les 6 derniers mois
    df_top_200['date'] = pd.to_datetime(df_top_200['date'])
    last_six_months = df_top_200[df_top_200['date'] >= df_top_200['date'].max() - pd.DateOffset(months=6)]

    # Grouper les données par artiste et sommer les valeurs de streams pour chaque artiste
    artist_streams = last_six_months.groupby('artist')['streams'].sum()

    # Trier les valeurs par ordre décroissant et sélectionner les 10 premiers artistes
    top10 = artist_streams.sort_values(ascending=False).head(10)

    # Créer le graphique
    fig, ax = plt.subplots(figsize=(10, 6))

    # Ajouter les barres pour les streams
    ax.bar(top10.index, top10.values, color='blue')

    # Configurer le graphique
    ax.set_title('Top 10 artistes', fontsize=16)
    ax.set_xlabel('Artiste', fontsize=12)
    ax.set_ylabel('Stream', fontsize=12)

    plt.xticks(rotation=90)

    # Afficher le graphique
    st.pyplot(fig.figure)


with tab4 : 

    st.subheader('Distribution des streams en 2021 (dernier quartile uniquement)')

    df3 = df_top_200
    
    # Sélection du df sur l'année 2021
    df3['date'] = pd.to_datetime(df3['date'])
    mask = df3['date'] > '2020-12-31'
    df3 = df3[mask].copy()
    
    # création de la grille horizontale
    col1, col2 = st.columns(2)
    
    with col1 :
    
        Q3_FR = df_grouped_france_titre['streams'].quantile(0.75)
        df_stat_frQ3 = df_grouped_france_titre[df_grouped_france_titre['streams']>Q3_FR]

        # BOXPLOT sur la distribution du stream pour le df France 2021, minimum fixé au Q3
        #fig, ax = plt.subplots(figsize=(10, 6))
        fig1 = px.box(df_stat_frQ3, x='streams', orientation='h', boxmode='overlay', color_discrete_sequence=['blue'], title='STREAMS FRANCE')

        # Afficher le graphique plotly
        st.plotly_chart(fig1)
   
    with col2 :

        df3_global = df3[df3['region']=='Global'].copy()
        df_grouped_global_titre = df3_global.groupby('title').agg({'streams': 'max', 'artist': lambda x: x.iloc[0]}).reset_index()

        Q3_GB = df_grouped_global_titre['streams'].quantile(0.75)
        df_stat_gbQ3 = df_grouped_global_titre[df_grouped_global_titre['streams']>Q3_GB]

        fig2 = px.box(df_stat_gbQ3, x='streams', orientation='h', boxmode='overlay', color_discrete_sequence=['blue'], title='STREAMS MONDE')

        # Afficher le graphique plotly
        st.plotly_chart(fig2)
    


with tab5 : 
    
    st.subheader('Morceaux les plus streamés en 2021 - total MONDE')
    
    # Groupby par titre pour avoir la somme des streams de chaque titre
    top_by_title = df_top_200.groupby(['title', 'artist']).sum()

    # Filtrer les 10 titres ayant la valeur de stream maximale et trier les données
    top10 = top_by_title.sort_values('streams', ascending=True).tail(10)
    
    # Créer une liste contenant le titre et l'artiste pour chaque titre dans top10
    titles_artists = [f"{title} - {artist}" for title, artist in top10.index]


    # Créer le graphique
    fig, ax = plt.subplots(figsize=(10, 6))

    # Ajouter les barres pour les streams
    colors = plt.cm.YlGnBu(np.linspace(0, 1, len(top10)))
    ax.barh(titles_artists, top10['streams'], color=colors)


    # Configurer le graphique
    ax.set_title('Top 10 titres', fontsize=16)
    ax.set_xlabel('Stream (en millions)', fontsize=12)
    ax.set_ylabel('Titre - Artiste', fontsize=12)

    plt.xticks(rotation=90)

    # Afficher le graphique
    st.pyplot(fig.figure)
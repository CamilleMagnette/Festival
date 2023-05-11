import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


st.markdown("# LE MARCHE DU STREAM ACTUEL 🎧")
st.subheader('Les talents du moment...et jeunes talents à venir')

#st.sidebar.markdown("# Les talents du moment 🎼")


# Importer le dataset : Janvier 2017 à dec 2021
df_top_200 = pd.read_csv("datasets/top_200.csv", sep = ",")
# Afficher le dataframe
# st.write(df_top_200)


# CREER DES TAB 
tab1, tab2, tab3, tab4 = st.tabs(['TOP 10 ARTISTES FRANCE', 'TOP 10 MORCEAUX', 'STATISTIQUES STREAM', 'blabla'])



# TRAVAILLER SUR LES TAB 

with tab1 : 

    st.subheader('Artistes les plus streamés sur Spotify en 2021')
    st.write("Taille des bulles : nombre total de stream en 2021")
    
    # Filtrer les données pour la région France
    top_200_france = df_top_200[df_top_200['region'] == 'France']

    # Regrouper les données par artiste et calculer le nombre total de streams pour chaque artiste
    artist_streams = top_200_france.groupby('artist')['streams'].sum()

    # Ajouter une colonne pour le trend de chaque artiste (MOVE_UP, SAME_POSITION, ou MOVE_DOWN)
    artist_trend = top_200_france.groupby('artist')['trend'].max()
    artist_streams_trend = pd.concat([artist_streams, artist_trend], axis=1)

    # Trier les artistes en fonction de leur position dans le top 200
    top_artists = artist_streams_trend.sort_values('streams', ascending=False)[:10]

    # Créer le graphique à bulles
    fig, ax = plt.subplots(figsize=(12,8))
    for artist, row in top_artists.iterrows():
        ax.scatter(artist, row['streams'], s=row['streams']/100000, alpha=0.5)
        ax.annotate(artist, (artist, row['streams']), ha='center')

    #pd.options.display.float_format = '{:.0f}'.format

    
    # Configurer le graphique
    ax.set_title('Artistes français', fontsize=16)
    ax.set_xlabel('Artistes', fontsize=12)
    ax.set_ylabel('Nombre total de streams (Milliards)', fontsize=12)
    ax.grid(True)

    # Afficher le graphique
    st.pyplot(fig.figure)
    
with tab2 : 
    
    st.subheader('Morceaux les plus streamés en 2021')
    
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

    
with tab4 : 
    
    st.subheader('blabla')

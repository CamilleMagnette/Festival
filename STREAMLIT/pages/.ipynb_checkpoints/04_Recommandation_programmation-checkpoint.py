import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image
import numpy as np 
import seaborn as sns


# Afficher notre logo dans le sidebar
notre_logo = Image.open('images/logo.png')
image_container = st.container()
with image_container:
    st.sidebar.image(notre_logo, width=300)
st.markdown("# PROGRAMMATION 🎤")
st.subheader('Quels artistes, à quel moment ? ')

#st.sidebar.markdown("# Les talents du moment 🎼")


# Importer le dataset : Janvier 2017 à dec 2021
df_top_200 = pd.read_csv("datasets/top_200.csv", sep = ",")
# Importer le dataset Amine : 
df_dataset = pd.read_csv("datasets/dataset.csv", sep = ",")
# Afficher le dataframe
# st.write(df_top_200)


# CREER DES TAB 
tab1, tab2, tab3 = st.tabs(['ENJEUX', 'NOTRE RECOMMANDATION', 'POUR ALLER PLUS LOIN'])



# TRAVAILLER SUR LES TAB 

with tab1 : 
    
    # création de la grille horizontale
    col1, col2 = st.columns(2)
    
    with col1 : 

        st.subheader('Trouver un bon équilibre entre pépites et étoile')
        st.write(' ')

        image_reco_prog = Image.open('images/reco progr.png')

        image_container = st.container()
        with image_container:
            st.image(image_reco_prog, width=500)
    
    
    with col2 : 

        # télécharger le dataframe data sets Amine
        st.subheader("Trouver un bon équilibre entre les genres musicaux pour maintenir un bon niveau d'énergie")
        st.write(' ')

        
        top_10_genres = df_dataset['track_genre'].value_counts().head(10)
        top_10 = df_dataset.nsmallest(10, 'popularity')
        top_10_genre_counts = top_10['track_genre'].value_counts()

        top_10_genres = df_dataset['track_genre'].value_counts().head(10).index.tolist()
        top_10_genres_df = df_dataset[df_dataset['track_genre'].isin(top_10_genres)]
        average_ernegy_top_10_genres = top_10_genres_df.groupby('track_genre')['energy'].mean()

        average_ernegy_top_10_genres = average_ernegy_top_10_genres.sort_values(ascending=False)

        # Create a colormap
        cmap = plt.cm.get_cmap('RdYlBu_r')
        plt.figure(figsize=(12, 6))
        bars = sns.barplot(x=average_ernegy_top_10_genres.index, y=average_ernegy_top_10_genres.values, palette=cmap(range(len(average_ernegy_top_10_genres))))
        #plt.title('Energy moyenne pour les 10 meilleurs genres', fontsize=14, fontweight='bold')
        plt.xlabel('Genre', fontsize=12)
        plt.ylabel('Energie moyenne', fontsize=12)
        plt.xticks(rotation=45, ha='right', fontsize=10)
        plt.yticks(fontsize=10)
        plt.gca().spines['top'].set_visible(False)  # Hide top spine
        plt.gca().spines['right'].set_visible(False)  # Hide right spine
        plt.tight_layout()
        for i, bar in enumerate(bars.patches):
            bar.set_color(cmap((len(average_ernegy_top_10_genres) - i - 1)/len(average_ernegy_top_10_genres)))

        # Afficher le graphique
        st.pyplot(bars.figure)
    
with tab2 : 
    
    image_reco_prog_2 = Image.open('images/reco programmation 2.png')

    image_container = st.container()
    with image_container:
        st.image(image_reco_prog_2, use_column_width=True)
   
    
with tab3 : 
    
    # création de la grille horizontale
    col1, col2 = st.columns(2)
    
    with col1 : 

        st.subheader('Services annexes')
        """
        - Mise en relation avec des partenaires pour vous accompagner dans l’organisation du festival : 

            => Montage financier / recherche de financement (région, SACEM, état…)

            => Organisation pure de l’événement (Billetterie, recrutement et gestion des intérimaires…)

        - Analyse datas des réseaux sociaux de vos artistes 
            => 6 000€ HT annuel (1 personne dédiée pour une journée par mois)

        - Etude de marché sur le streaming mise à jour annuellement => 1 000€ annuel

        - Automatisation de la détection de vos futures pépites => 7 500€
        """
  
    with col2 : 
        
        st.write(' ')
        st.write(' ')
        st.write(' ')

        prestation = Image.open('images/prestations.png')

        image_container = st.container()
        with image_container:
            st.image(prestation, width=600)
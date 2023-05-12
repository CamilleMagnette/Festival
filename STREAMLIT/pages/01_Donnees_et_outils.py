# SOURCES DE DONNEES ET DIAGRAM DES TABLES 
# METHODE 

import streamlit as st
from PIL import Image
import pandas as pd

##################################################################################################################################
########### Preparation :

df = pd.read_csv('datasets/top_200.csv')


##### images 
schema = Image.open('images/exemple_database.png')
logopython = Image.open('images/logopython.png')
logoseaborn = Image.open('images/logoseaborn.png')
logoplotly = Image.open('images/logoplotly.png')
logostream = Image.open('images/logostreamlit.png')


##########################################################################################################
###### Debut de la page
# afficher un titre centrer
st.markdown('<p style="color: #25316D; font-size: 40px; text-align: center;">Donnees et outils</p>', unsafe_allow_html=True)

# Ajouter espaces
st.markdown("<br><br>", unsafe_allow_html=True)

main_container = st.container()

data_container, sep_container, stack_container = main_container.columns([6, 1, 3])
    

with data_container:
      # Ajouter espaces
    st.markdown("<br>", unsafe_allow_html=True)

    # afficher un titre centrer
    st.markdown('<p style="color: #25316D; font-size: 25px; text-align: center; text-decoration: underline;">Les donnees</p>', unsafe_allow_html=True)

    # Ajouter espaces
    st.markdown("<br>", unsafe_allow_html=True)
    
    # texte
    st.markdown('<p style="color: #25316D; font-size: 16px;">Pour realiser notre projet nous avons recuperer des donnees publiques provenant de Spotify</p>', unsafe_allow_html=True)
    
    # Ajouter espaces
    st.markdown("<br>", unsafe_allow_html=True)
        
    st.markdown('<p style="color: #25316D; font-size: 16px;">https://www.kaggle.com/datasets/dhruvildave/spotify-charts</p>', unsafe_allow_html=True)
    
    # Ajouter espaces
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown('<p style="color: #25316D; font-size: 16px;">Voici un extrait du Dataset final que nous avons utiliser pour notre algorithme de recommandation d\'artiste </p>', unsafe_allow_html=True)
    
    # Ajouter espaces
    st.markdown("<br>", unsafe_allow_html=True)

    st.write(df)


with stack_container:
      # Ajouter espaces
    st.markdown("<br>", unsafe_allow_html=True)

    # afficher un titre centrer
    st.markdown('<p style="color: #25316D; font-size: 25px; text-align: center; text-decoration: underline;">La stack technique</p>', unsafe_allow_html=True)
    # Ajouter espaces
    st.markdown("<br>", unsafe_allow_html=True)

    # texte
    st.markdown('<p style="color: #25316D; font-size: 16px;text-align: center;">Pour realiser notre projet nous avons utilise differents outils :</p>', unsafe_allow_html=True)


    # Ajouter espaces
    st.markdown("<br>", unsafe_allow_html=True)# Ajouter espaces


    # texte presentation
    st.markdown('<p style=" font-family:Roboto Condensed:ital;text-align: center; font-size: 16px;">traitement des donnees :</p>', unsafe_allow_html=True)


    # logo
    st.image(logopython, width=280)

    # Ajouter espaces
    st.markdown("<br>", unsafe_allow_html=True)# Ajouter espaces
    
    st.markdown('<p style=" font-family:Roboto Condensed:ital; text-align: center; font-size: 16px;">Realisation de graphique:</p>', unsafe_allow_html=True)
        
    # logo
    st.image(logoplotly, width=300)
    # logo
    st.image(logoseaborn, width=300)
    
    # Ajouter espaces
    st.markdown("<br><br>", unsafe_allow_html=True)
    

    # texte presentation
    st.markdown('<p style=" font-family:Roboto Condensed:ital; text-align: center; font-size: 16px;">Realisation web-app:</p>', unsafe_allow_html=True)
        

    # logo
    st.image(logostream, width=350)
        

    
    

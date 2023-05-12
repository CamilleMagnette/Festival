import streamlit as st
from PIL import Image
import pandas as pd


# Afficher notre logo dans le sidebar
notre_logo = Image.open('STREAMLIT/images/logo.png')
image_container = st.container()
with image_container:
    st.sidebar.image(notre_logo, width=300)


# Charger le dataframe
df = pd.read_csv('STREAMLIT/datasets/top_200.csv')
#df = pd.read_csv('datasets/top_200.csv') => LIEN EN LOCAL

##### images 
#logopython = Image.open('images/logopython.png')   => LIEN EN LOCAL 
logopython = Image.open('STREAMLIT/images/logopython.png')
logoseaborn = Image.open('STREAMLIT/images/logoseaborn.png')
logoplotly = Image.open('STREAMLIT/images/logoplotly.png')
logostream = Image.open('STREAMLIT/images/logostreamlit.png')

st.markdown("# DONNÉES ET OUTILS 🔧")
# st.subheader('BLABLABLA')
# afficher un titre centré
#st.markdown('<p style="color: #25316D; font-size: 40px; text-align: center;">DONNÉES ET OUTILS</p>', unsafe_allow_html=True)

main_container = st.container()
data_container, sep_container, stack_container = main_container.columns([6, 1, 3])

with data_container:
    
    # Ajouter espaces
    st.markdown("<br>", unsafe_allow_html=True)

    # afficher un titre centrer
    #st.markdown('<p style="color: #25316D; font-size: 25px; text-align: center; text-decoration: underline;">Données</p>', unsafe_allow_html=True)
    st.subheader('Données')
    
    # texte    
    #st.markdown('<p style="color: #25316D; font-size: 16px;">Source : https://www.kaggle.com/datasets/dhruvildave/spotify-charts</p>', unsafe_allow_html=True)
    st.write('Sources publiques Spotify : https://www.kaggle.com/datasets/dhruvildave/spotify-charts')
    st.write('Extrait du Dataset final utilisé afin de construire notre algorithme de recommandation d\'artistes :')

    # Ajouter espaces
    st.markdown("<br>", unsafe_allow_html=True)
    st.write(df)

with stack_container:
    
    # Ajouter espaces
    st.markdown("<br>", unsafe_allow_html=True)

    # afficher un titre centrer
    #st.markdown('<p style="color: #25316D; font-size: 25px; text-align: center; text-decoration: underline;">Stack technique</p>', unsafe_allow_html=True)
    st.subheader('Stack technique')

    # texte presentation
    #st.markdown('<p style=" font-family:Roboto Condensed:ital;text-align: center; font-size: 16px;">traitement des données :</p>', unsafe_allow_html=True)
    st.markdown('<p style=" ; font-size: 20px;">Traitement des données :</p>', unsafe_allow_html=True)

    # logo
    st.image(logopython, width=200)

    # texte presentation
    st.markdown('<p style=" ; font-size: 20px;">Réalisation des graphiques :</p>', unsafe_allow_html=True)
        
    # logo
    st.image(logoplotly, width=250)
    # logo
    st.image(logoseaborn, width=250)
    
    # texte presentation
    st.markdown('<p style=" ; font-size: 20px;">Réalisation web-app :</p>', unsafe_allow_html=True)   

    # logo
    st.image(logostream, width=250)
        

    
    

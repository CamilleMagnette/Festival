import streamlit as st
import pandas as pd
from PIL import Image



st.set_page_config(
    page_title="HACKATHON",
    layout="wide",
    page_icon=":🎼:")

# st.sidebar.markdown("# BLABLABLA")

st.markdown("# FESTIVAL LES PETITS POUCETS 🎼")
st.subheader('Les 5 et 6 juillet 2023')

# Afficher notre logo dans le sidebar
notre_logo = Image.open('logo.png')
image_container = st.container()
with image_container:
    st.sidebar.image(notre_logo, width=300)

# IMPORTER LE DATAFRAME
#link = "blablabla"
#df = pd.read_csv(link)


# CREER DES TAB 
tab1, tab2, tab3, tab4 = st.tabs(['BESOIN CLIENT', 'ENJEUX & PROBLEMATIQUE', 'EQUIPE VASCALYTICS', 'NOTRE PROPOSITION PAR ETAPE'])


# TRAVAILLER SUR LES TAB 

with tab1 : 

    # DEMANDE CLIENT 

    st.subheader('PROPOSITION DE PROGRAMMATION MUSICALE')

    st.write("Jeune label en quête de notoriété vous souhaitez promouvoir vos artistes via l'organisation d'un festival musical.") 


    # PHOTO CONCERT EXTERIEUR    
    image_coeur = Image.open('images/image_festival_coeur.jpg')
    
    image_container = st.container()
    with image_container:
        st.image(image_coeur, width=900)


with tab2 : 
    
    # ENJEUX & PROBLEMATIQUE

    st.subheader('VOS ENJEUX')

    st.write("1) 🔈 Gagner en visibilité avec des artistes reconnus") 
    st.write("2) 💰 Vous rémunérer") 
    st.write("3) 🔦 Faire découvrir de nouveaux talents") 
    st.write("4) 🔎 Trouver un équilibre entre tête d'affiche et nouveaux talents") 

    st.subheader('NOTRE PROBLEMATIQUE')
    
    st.write("Quelle programmation d'artistes mettre en place pour la réussite de cet evenement ?") 


with tab3 : 
    
    # EQUIPE VASCALYTICS

    st.subheader('UNE EQUIPE A VOTRE ECOUTE')
    
    st.write("Nous mettons à votre disposition 6 jeunes consultants pendant 2 jours ") 

    # PHOTO CONCERT EXTERIEUR    
    vincent = Image.open('images/Vincent.png')
    chrysanthe = Image.open('images/Chrysanthe.jpeg')
    camille = Image.open('images/Camille.jpg')
    stephanie = Image.open('images/Stephanie.jpeg')
    anthony = Image.open('images/Anthony.jpeg')
    amine = Image.open('images/Amine.jpeg')

    image_container = st.container()

    # création de la grille horizontale
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    
    # Centrage horizontal des boutons
    #st.markdown("""<style>.centered-image {display: flex;justify-content: center;align-items: center;}</style>""", unsafe_allow_html=True)
    
    # Images en ligne
    with col1 :
        
        #with image_container:
            st.image(vincent, width=100)
            st.write("Vincent Messika")           
    with col2 :
        #with image_container:
            st.image(chrysanthe, width=100)
            st.write("Chrysanthe Delrieu")      
    with col3 :
        #with image_container:
            st.image(camille, width=100)
            st.write("Camille Magnette")         
    with col4 :
        #with image_container:
            st.image(stephanie, width=100)
            st.write("Stephanie Bourganel")   
    with col5 :
        #with image_container:
            st.image(anthony, width=100)
            st.write("Anthony Iervasi")   
    with col6 :
        #with image_container:
            st.image(amine, width=100)
            st.write("Amine Aissami") 

    #st.markdown("""<style>.stimage { display: flex; justify-content: center; align-items: center;}</style>""", unsafe_allow_html=True)

with tab4 : 
    
    # NOTRE PROPOSITION PAR ETAPE

    # création de la grille horizontale
    col1, col2 = st.columns(2)

    with col1 :
        lunettes = Image.open('images/image_lunette.jpg')
        st.image(lunettes, width=400)
        
    with col2 :

        st.subheader('Sommaire')

        st.write("1) Les sources de données et outils utilisés") 
        st.write("2) Etat des lieux du marché du stream musical actuel") 
        #st.write("3) Performance et positionnement des artistes managés") 
        st.write("3) Recommandation d'artistes à pousser pour le festival") 
        st.write("4) Recommandation de programmation sur deux jours") 

    
    
# METHODOLOGIE : mapping à présenter 
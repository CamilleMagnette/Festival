import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image



st.markdown("# PROGRAMMATION 🎤")
st.subheader('Quels artistes, à quel moment ? ')

#st.sidebar.markdown("# Les talents du moment 🎼")


# Importer le dataset : Janvier 2017 à dec 2021
df_top_200 = pd.read_csv("datasets/top_200.csv", sep = ",")
# Afficher le dataframe
# st.write(df_top_200)


# CREER DES TAB 
tab1, tab2, tab3, tab4 = st.tabs(['PARTIS PRIS', 'NOTRE RECOMMANDATION', 'BLABLA', 'BLABLA'])



# TRAVAILLER SUR LES TAB 

with tab1 : 

    st.subheader('Bon équilibre entre pépites et étoile (têtes d''affiches)')
    image_reco_prog = Image.open('images/reco progr.png')
    
    image_container = st.container()
    with image_container:
        st.image(image_reco_prog, width=700)
    
with tab2 : 
    
    st.subheader('BLABLA')
    st.write("BLABLABLA")

    
with tab4 : 
    
    st.subheader('blabla')

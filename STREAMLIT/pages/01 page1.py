# SOURCES DE DONNEES ET DIAGRAM DES TABLES 
# METHODE 

import streamlit as st

st.markdown("# blabla")
st.sidebar.markdown("# blabla 🎼")

# Importer le dataframe
import pandas as pd
link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_voitures = pd.read_csv(link)


st.write("blabla")

st.write("blabla")

# CREER DES TAB 
tab1, tab2, tab3, tab4 = st.tabs(['blabla', 'blabla', 'blabla', 'blabla'])


# TRAVAILLER SUR LES TAB 

with tab1 : 

    # ONGLET TECHNIQUE : sources de données + diagram

    st.subheader('blabla')


    
with tab2 : 
    
    # ONGLET METHODOLOGIE : quelles données, pk 
    st.subheader('blabla')
    
    
with tab4 : 
    
    # ONGLET SOMMAIRE DE NOTRE  : quelles données, pk 
   
    st.subheader('blabla')

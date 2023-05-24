# 🎥 Recommandation de programmation de festival :

hackathon réalisé en 1 jour et demi lors de ma formation à la Wild Code School.

## 🎯 Objectif du projet :

Produire une analyse basée sur des données, qui aidera les acteurs du marché de la musique 🔎👨‍💻
Problémtique et analyse libre !

## ⌛ Délai : 28h

## ✅ Etapes : 

#### Semaine 1 :  
Appropriation et première exploration des données     
Outils principaux : Pandas, Matplotlib, jupyterLab   

💪 🕺

💡 📊

[LIEN STREAMLIT DE LA PRESENTATION](https://camillemagnette-festival-streamlitpresentation-du-projet-pniqto.streamlit.app/)

**Programmation** :   Python (plotly, Seaborn) avec JupyterLab, Streamlit, github 


## 🎬 Source des données :  
-[base IMDb](https://datasets.imdbws.com/)   
-[Explication datasets](https://www.imdb.com/interfaces/)


## 📎 Méthodologie technique :

1) [Nettoyage de l'ensemble des fichiers sources](https://github.com/CamilleMagnette/Systeme_de_recommandation_machine_learning/blob/main/JupyterlabNotebooks/Projet%202%20-%20Nettoyage%20des%20donn%C3%A9es.ipynb) pour n'en former que deux : 
-  un premier très macro pour réaliser notre analyse,
-  un second pour réaliser notre algorithme

2) [Analyse de la base de données](https://github.com/CamilleMagnette/Systeme_de_recommandation_machine_learning/blob/main/JupyterlabNotebooks/Projet%202%20-%20Graphiques%20Plotly%20avec%20donn%C3%A9es%20nettoy%C3%A9es.ipynb) via le 1er fichier nettoyé : mise en forme de graphiques via [datapane](https://cloud.datapane.com/reports/VkGQlN3/exploration-des-donn%C3%A9es/)

3) [Préparation de notre 2nd fichier nettoyé pour le machine learning](https://github.com/CamilleMagnette/Systeme_de_recommandation_machine_learning/blob/main/JupyterlabNotebooks/Projet%202-%20Pr%C3%A9paration%20du%20fichier%20pour%20le%20machine%20learning.ipynb) : transformation en format pickle et split des colonnes non numériques 

4) [Tests de machine learning](http://localhost:8891/lab/tree/Documents/FORMATION%20DATA%20ANALYST/COURS%20DATA%20ANALYST/PROJET%202/JUPITERLAB%20NOTEBOOKS/Projet%202%20-%20Machine%20learning%20TEST%20ACTEURS.ipynb) : normalisation des données et mise en place d'un algorithme basé sur les plus proches voisins (algorithme K-nearest neighbors (kNN))

5) [Mise en place de l’application utilisateur Streamlit](https://github.com/CamilleMagnette/Systeme_de_recommandation_machine_learning/blob/main/app_acteurs.py)

6) [Publication de l'interface utilisateur Streamlit](https://camillemagnette-systeme-de-recommandation-ma-app-acteurs-k992u6.streamlit.app/)

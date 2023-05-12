import streamlit as st
from PIL import Image
import pandas as pd

##################################################################################################################################
########### Preparation :


##### images 
lisa = Image.open('images/lisa.jpg')
doja = Image.open('images/doja.jpg')
damso = Image.open('images/damso.jpg')
bella = Image.open('images/bella.png')
maneskinn = Image.open('images/maneskin.jpg')
masked = Image.open('images/masked.jpg')
ckay = Image.open('images/ckay.jpeg')
kali = Image.open('images/kaliu.jpg')
vege = Image.open('images/vege.jpeg')
ziak = Image.open('images/ziak.jpg')



##################################################################################################################################
###### Debut de la page
# afficher un titre centrer
st.markdown('<p style="color: #25316D; font-size: 40px; text-align: center;">LES ARTISTES</p>', unsafe_allow_html=True)

# Ajouter espaces
st.markdown("<br><br>", unsafe_allow_html=True)

########################################## artiste 1 ######################################################
artiste_container1 = st.container()

info_container1, sep_container1, photo_container1, sep1 = artiste_container1.columns([5, 1, 3,1])

with info_container1:

    
    #nom de l'artiste
    st.markdown('<p style="color: #FFD700; font-size: 35px; text-align: center;">Lisa</p>', unsafe_allow_html=True)
     # texte
    st.markdown('<p style="color: #25316D; font-size: 16px; text-align: center;">Pourquoi est-elle dans notre sélection : Troisième membre de Blackpink à faire ses débuts en solo, son album Lalisa sort le 10 septembre 2021 et cumule plus de 2,5 millions de téléchargements sur deux morceaux le premier jour. Le 22 octobre son titre “MONEY” comptera à lui seul plus de 4,3 millions de téléchargements.Attention à sa fanbase qui déplacera des montagnes…</p>', unsafe_allow_html=True)
    st.markdown('<p style="color: #25316D; font-size: 16px; text-align: center;">Style musical : K-pop</p>', unsafe_allow_html=True)
    st.markdown('<p style="color: #25316D; font-size: 16px; text-align: center;">Programmation : Star globale</p>', unsafe_allow_html=True)
    
    
with photo_container1:
    
    # image
    st.image(lisa, width=500)
    
# Ajouter espaces
st.markdown("<br><br>", unsafe_allow_html=True)

########################################## artiste 2 ######################################################
    
artiste_container2 = st.container()

photo_container2, sep_container2, info_container2 = artiste_container2.columns([3, 1, 6])

with photo_container2:
    
    # image
    st.image(doja, width=500)
    
with info_container2:
    # Ajouter espaces
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    #nom de l'artiste
    st.markdown('<p style="color: #FF6B8B; font-size: 35px; text-align: center;">Doja Cat</p>', unsafe_allow_html=True)
     
# Ajouter espaces
st.markdown("<br><br>", unsafe_allow_html=True)

    
########################################## artiste 3 ######################################################
artiste_container3 = st.container()

info_container3, sep_container3, photo_container3, sep3 = artiste_container3.columns([5, 1, 3,1])

with info_container3:
    
    
    #nom de l'artiste
    st.markdown('<p style="color: #6699CC; font-size: 35px; text-align: center;">Damso</p>', unsafe_allow_html=True)
    
    # texte
    st.markdown('<p style="color: #25316D; font-size: 16px; text-align: center;">Pourquoi est-il dans notre sélection : Avec plusieurs millions de streams cumulés grâce à ses collaborations nombreuses avec d’autres artistes, Damso est une valeur sûre pour déplacer de nombreux fans et donnera de la visibilité à nos jeunes pépites.</p>', unsafe_allow_html=True)
    st.markdown('<p style="color: #25316D; font-size: 16px; text-align: center;">Style musical : Rap</p>', unsafe_allow_html=True)
    st.markdown('<p style="color: #25316D; font-size: 16px; text-align: center;">Programmation : Star française</p>', unsafe_allow_html=True)
    
    
with photo_container3:
    
    # image
    st.image(damso, width=500)
    
# Ajouter espaces
st.markdown("<br><br>", unsafe_allow_html=True)


########################################## artiste 4 ######################################################
    
artiste_container4 = st.container()

photo_container4, sep_container4, info_container4 = artiste_container4.columns([3, 2, 5])

with photo_container4:
    
    # image
    st.image(vege, width=500)
    
with info_container4:

    
    #nom de l'artiste
    st.markdown('<p style="color: #4B0082; font-size: 35px; text-align: center;">Vegedream</p>', unsafe_allow_html=True)
     # texte
    st.markdown('<p style="color: #25316D; font-size: 16px; text-align: center;">Pourquoi est-il dans notre sélection : La popularité acquise par Vegedream avec ses succès et ses collaborations diverses sera un plus pour notre festival. En mars 2021 il revient sur les téléchargements avec son single “Touché dans le coeur” mais c’est surtout avec la coupe du monde que son titre phare brillera avec des millions de téléchargements par jour</p>', unsafe_allow_html=True)
    st.markdown('<p style="color: #25316D; font-size: 16px; text-align: center;">Style musical : Rap</p>', unsafe_allow_html=True)
    st.markdown('<p style="color: #25316D; font-size: 16px; text-align: center;">Programmation : Star française</p>', unsafe_allow_html=True)
    
# Ajouter espaces
st.markdown("<br><br>", unsafe_allow_html=True)


########################################## artiste 5 ######################################################
artiste_container5 = st.container()

info_container5, sep_container5, photo_container5, sep5 = artiste_container5.columns([5, 1, 3, 1])

with info_container5:
    
    # Ajouter espaces
    st.markdown("<br>", unsafe_allow_html=True)
    
    #nom de l'artiste
    st.markdown('<p style="color: #BFC4AD; font-size: 35px; text-align: center;">Maneskin</p>', unsafe_allow_html=True)
     
    # texte
    st.markdown('<p style="color: #25316D; font-size: 16px; text-align: center;">Pourquoi sont-ils dans notre sélection : Première apparition dans notre base de données spotify le 7 mars 2021, ils montent à plus de 8 millions de streams le 16 juillet 2021</p>', unsafe_allow_html=True)
    st.markdown('<p style="color: #25316D; font-size: 16px; text-align: center;">Style musical : Pop-Rock</p>', unsafe_allow_html=True)
    st.markdown('<p style="color: #25316D; font-size: 16px; text-align: center;">Programmation : pépite globale</p>', unsafe_allow_html=True)
    
    
    
with photo_container5:
    
    # image
    st.image(maneskinn, width=500)
    
# Ajouter espaces
st.markdown("<br><br>", unsafe_allow_html=True)

########################################## artiste 6 ######################################################
    
artiste_container6 = st.container()

photo_container6, sep_container6, info_container6 = artiste_container6.columns([3, 2, 5])

with photo_container6:
    
    # image
    st.image(masked, width=500)
    
with info_container6:
    
    #nom de l'artiste
    st.markdown('<p style="color: #A2A1AC; font-size: 35px; text-align: center;">Masked wolf</p>', unsafe_allow_html=True)
     
    # Ajouter espaces
    st.markdown("<br>", unsafe_allow_html=True)
     
    # texte
    st.markdown('<p style="color: #25316D; font-size: 16px; text-align: center;">Pourquoi est-il dans notre sélection : Première apparition dans notre base de données spotify le 14 janvier 2021, il monte à plus de 4,6 millions de streams le 9 avril de la même année</p>', unsafe_allow_html=True)
    st.markdown('<p style="color: #25316D; font-size: 16px; text-align: center;">Style musical : Hip-hop trap</p>', unsafe_allow_html=True)
    st.markdown('<p style="color: #25316D; font-size: 16px; text-align: center;">Programmation : pépite globale</p>', unsafe_allow_html=True)
    
# Ajouter espaces
st.markdown("<br><br>", unsafe_allow_html=True)

    
########################################## artiste 7 ######################################################
artiste_container7 = st.container()

info_container7, sep_container7, photo_container7, sep7 = artiste_container7.columns([5, 1, 3,1])

with info_container7:
    
    # Ajouter espaces
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    #nom de l'artiste
    st.markdown('<p style="color: #FF1493; font-size: 35px; text-align: center;">Ckay</p>', unsafe_allow_html=True)
     # texte
    st.markdown('<p style="color: #25316D; font-size: 16px; text-align: center;">descriptif artiste , genre de musique , pourquoi on la choisit etc..</p>', unsafe_allow_html=True)
    
    
with photo_container7:
    
    # image
    st.image(ckay, width=500)
    
# Ajouter espaces
st.markdown("<br><br>", unsafe_allow_html=True)


########################################## artiste 8 ######################################################
    
artiste_container8 = st.container()

photo_container8, sep_container8, info_container8 = artiste_container8.columns([3, 2, 5])

with photo_container8:
    
    # image
    st.image(kali, width=500)
    
with info_container8:
    
    # Ajouter espaces
    st.markdown("<br>", unsafe_allow_html=True)
    
    #nom de l'artiste
    st.markdown('<p style="color: #8AE68A; font-size: 35px; text-align: center;">Kali Uchis</p>', unsafe_allow_html=True)
     # texte
    st.markdown('<p style="color: #25316D; font-size: 16px; text-align: center;">Pourquoi est-elle dans notre sélection : Première apparition dans notre base de données spotify le 16 février 2021, elle monte à près de 4,2 millions de streams en à peine un mois ( le 19 mars).</p>', unsafe_allow_html=True)
    st.markdown('<p style="color: #25316D; font-size: 16px; text-align: center;">Style musical : Soul R&B pop electronic</p>', unsafe_allow_html=True)
    st.markdown('<p style="color: #25316D; font-size: 16px; text-align: center;">Programmation: pépite globale</p>', unsafe_allow_html=True)
    
# Ajouter espaces
st.markdown("<br><br>", unsafe_allow_html=True)


########################################## artiste 9 ######################################################
artiste_container9 = st.container()

info_container9, sep_container9, photo_container9, sep9 = artiste_container9.columns([5, 1, 3,1])

with info_container9:

    
    #nom de l'artiste
    st.markdown('<p style="color: #556B2F; font-size: 35px; text-align: center;">Bella Poarch</p>', unsafe_allow_html=True)
   # texte
    st.markdown('<p style="color: #25316D; font-size: 16px; text-align: center;">Pourquoi est-elle dans notre sélection : Bella Poarch crée un compte sur Tik Tok en janvier 2020 puis poste de façon active des vidéos diverses. Elle compte aujourd’hui plus de 92 millions d’abonnés et 2.2 milliards de “j’aime”. Elle arrive sur notre base de données spotify le 14 mai 2021 avec son titre “Build a bitch “ qui s’attaque aux standards de beautés asiatiques irréalistes avec presque 900 000 streams le premier jour puis se hisse à l’orée des 3 millions en 14 jours seulement.</p>', unsafe_allow_html=True)
    st.markdown('<p style="color: #25316D; font-size: 16px; text-align: center;">Style musical : Pop</p>', unsafe_allow_html=True)
    st.markdown('<p style="color: #25316D; font-size: 16px; text-align: center;">Programmation : pépite globale</p>', unsafe_allow_html=True)
    
    
    
with photo_container9:
    
    # image
    st.image(bella, width=500)
    
# Ajouter espaces
st.markdown("<br><br>", unsafe_allow_html=True)


########################################## artiste 10 ######################################################
    
artiste_container10 = st.container()

photo_container10, sep_container10, info_container10 = artiste_container10.columns([3, 2, 5])

with photo_container10:
    
    # image
    st.image(ziak, width=500)
    
with info_container10:

    
    #nom de l'artiste
    st.markdown('<p style="color: #808080; font-size: 35px; text-align: center;">Ziak</p>', unsafe_allow_html=True)
     # texte
    st.markdown('<p style="color: #25316D; font-size: 16px; text-align: center;">Pourquoi est-il dans notre sélection : Ziak arrive tranquillement dans notre base de données spotify avec le titre Galerie le 20 mai 2021 et s’y maintiendra toute l’année jusqu’à dépasser les 1,2 millions d’écoutes cumulées sur trois titres le 20 novembre. Avec son personnage mystérieux, Ziak est une star en devenir.</p>', unsafe_allow_html=True)
    st.markdown('<p style="color: #25316D; font-size: 16px; text-align: center;">Style musical : rap</p>', unsafe_allow_html=True)
    st.markdown('<p style="color: #25316D; font-size: 16px; text-align: center;">Programmation : pépite france</p>', unsafe_allow_html=True)
    
# Ajouter espaces
st.markdown("<br><br>", unsafe_allow_html=True)

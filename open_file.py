# Ouvrir un fichier HTML
from tkinter import filedialog
from widgets import *
from bs4 import BeautifulSoup
import os

def open_htmlfile(app_maitre):
    "Ouvrir un fichier HTML"
    types = [("Document HTML", "*.html")]
    global html_file 
    html_file = filedialog.askopenfilename(title="Sélectionnez un document HTML", filetypes=types, initialdir="C:") # On demande à l'utilisateur de sélectionner le document HTML à ouvrir
    app_maitre.title(os.path.basename(html_file))
    extraire_titre(app_maitre)
    extraire_texte(app_maitre)


def get_htmlfile_path():
    return html_file


def extraire_titre(app_maitre):
    "Extraire le titre de la page web"
    with open(html_file, "r", encoding="utf-8") as htmldoc: # Ouvrir le document HTML en lecture  
        soup = BeautifulSoup(htmldoc, "html.parser") 
        for titre in soup.find_all("title"): # Rechercher toute balise "title" dans le document
            tit = ajouter_titre(application_maitre=app_maitre) # Ajouter un widget titre
            tit.insert("end", titre.text) # Insérer le titre de la page web au widget titre


def extraire_texte(app_maitre):
    "Extraire le texte de la page web"
    with open(html_file, "r", encoding="utf-8") as htmldoc: # Ouvrir le document HTML en lecture 
        soup = BeautifulSoup(htmldoc, "html.parser")          
        for para in soup.find_all("p"): # Rechercher chaque balise représentant un paragraphe
            texte = ajouter_texte(application_maitre=app_maitre)
            texte.insert("end", para.text)





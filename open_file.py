# Ouvrir un fichier HTML
from tkinter import filedialog
from widgets import *
from bs4 import BeautifulSoup

def open_htmlfile(app_maitre):
    "Ouvrir un fichier HTML"
    types = [("Document HTML", "*.html")]
    global html_file 
    html_file = filedialog.askopenfilename(title="Sélectionnez un document HTML", filetypes=types, initialdir="C:") # On demande à l'utilisateur de sélectionner le document HTML à ouvrir

    extraire_titre(app_maitre)


def extraire_titre(app_maitre):
    "Extraire le titre de la page web"
    with open(html_file, "r") as htmldoc:
        soup = BeautifulSoup(htmldoc, "html.parser")
        for titre in soup.find_all("title"):
            tit = ajouter_titre(application_maitre=app_maitre)
            tit.insert("end", titre.text)

# Widgets
from pywebio.input import *
from pywebio.output import *
from tkinter import *
from htmltexte import *
from image import *


def ajouter_titre(application_maitre):
    "Ajouter un titre à la page web"
    label_titre = Label(application_maitre, text="Titre de la page web (texte qui apparaît dans un onglet de navigateur):")
    label_titre.pack(side="top")
    global titre
    titre = Entry(application_maitre)
    titre.pack(fill="both", side="top")
    liste_widgets.append(titre)

def obtenir_titre():
    "Obtenir le titre de la page web"
    return titre.get()  

def ajouter_texte(application_maitre):
    "Ajouter du texte à la page web"
    texte = HtmlTexte(application_maitre) # Ajouter un widget "Text" à l'application

    liste_widgets.append(texte)
    liste_htmltextes.append(texte)
    



def ajouter_image(app_maitre):
    "Ajouter une image à la page web"   
    image = ouvrir_image(app_maitre)

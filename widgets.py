# Widgets
from pywebio.input import *
from pywebio.output import *
from tkinter import *
from htmltexte import *

liste_html_textes = []

def ajouter_titre(application_maitre):
    "Ajouter un titre à la page web"
    label_titre = Label(application_maitre, text="Titre de la page web :")
    label_titre.pack()
    global titre
    titre = Entry(application_maitre)
    titre.pack(fill="both")

def obtenir_titre():
    "Obtenir le titre de la page web"
    return titre.get()  

def ajouter_texte(application_maitre):
    "Ajouter du texte à la page web"
    texte = HtmlTexte(application_maitre) # Ajouter un widget "Text" à l'application
    liste_html_textes.append(texte)

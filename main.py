# Script principal
from tkinter import *
from widgets import *


class Application(Tk):
    "Application"
    def __init__(self):
        super().__init__() # Hériter des attributs de la classe Tk
        self.title("Editeur HTML interactif")

        self.barre_menus = Menu(self, tearoff=0) # Ajouter une barre de menus
        self.menu_fichier = Menu(self.barre_menus, tearoff=0) # Ajouter un menu "Fichier"
        self.barre_menus.add_cascade(label="Fichier", menu=self.menu_fichier)

        self.menu_ajouter = Menu(self.barre_menus, tearoff=0) # Ajouter un menu "Ajouter" pour permettre à l'utilisateur d'ajouter des éléments à sa page web
        self.menu_ajouter.add_command(label="Titre de la page...", command=lambda:ajouter_titre(self)) # Permettre à l'utilisateur de spécifier le titre de la page
        self.menu_ajouter.add_command(label="Image...", command=None) # Permettre à l'utilisateur d'insérer une image
        self.menu_ajouter.add_command(label="Texte...", command = lambda:ajouter_texte(self)) # Permettre à l'utilisateur d'insérer du texte
        self.barre_menus.add_cascade(label="Ajouter", menu=self.menu_ajouter)

        

        self.config(menu=self.barre_menus) # On configure le menu de la fenêtre



app = Application()
app.mainloop()
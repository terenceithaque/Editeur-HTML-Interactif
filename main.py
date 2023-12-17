# Script principal
from tkinter import *

class Application(Tk):
    "Application"
    def __init__(self):
        super().__init__() # Hériter des attributs de la classe Tk

        self.barre_menus = Menu(self, tearoff=0) # Ajouter une barre de menus
        self.menu_fichier = Menu(self.barre_menus, tearoff=0) # Ajouter un menu "Fichier"
        self.barre_menus.add_cascade(label="Fichier", menu=self.menu_fichier)

        self.config(menu=self.barre_menus) # On configure le menu de la fenêtre



app = Application()
app.mainloop()
# HtmlkTexte
from tkinter import *

class HtmlTexte(Text):
    "Widget pour insérer du texte dans la page web, dérivé de Text"
    def __init__(self, app_maitre):
        super().__init__() # Hériter des attributs du widget Text de tkinter
        self.width = 1000
        self.height = 500
        self.dimensionner(self.width, self.height)
        self.bind("<Button-3>", self.display_menu)

    def dimensionner(self, width, height):
        "Dimensionner la taille du widget HtmlTexte"
        print(f"Dimensionné à {width} x {height}")
        self.place(width=width, height=height)

    def display_menu(self, event):
        "Afficher un menu contextuel"
        menu_contextuel = Menu(self, tearoff=0)
        menu_dimension = Menu(menu_contextuel, tearoff=0)
        menu_dimension.add_command(label="50x50", command=lambda:self.dimensionner(50,50))
        menu_dimension.add_command(label="100x100", command=lambda:self.dimensionner(100,100))
        menu_dimension.add_command(label="200x200", command=lambda:self.dimensionner(200,200))
        menu_dimension.add_command(label="500x500", command=lambda:self.dimensionner(500,500))
        menu_dimension.add_command(label="800x500", command=lambda:self.dimensionner(800,500))
        menu_dimension.add_command(label="1000x500", command=lambda:self.dimensionner(1000,500))
        menu_dimension.add_command(label="1000x1000", command=lambda:self.dimensionner(1000,1000))
        menu_dimension.add_command(label="1600x1000", command=lambda:self.dimensionner(1600,1000))
        menu_contextuel.add_cascade(label="Dimension", menu=menu_dimension)
        menu_contextuel.post(event.x_root, event.y_root)

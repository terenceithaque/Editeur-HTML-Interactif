# Image
from urllib.request import urlopen
from tkinter import *
from tkinter import filedialog

def ouvrir_image(app_maitre):
    "Ouvrir une image depuis le stockage local ou depuis le web"
    browsewindow = Toplevel(app_maitre)
    label_recherche_stockage_local = Label(browsewindow, text="Chemin de l'image sur un disque local :")
    label_recherche_stockage_local.pack()
    global entree_recherche_locale
    entree_recherche_locale = Entry(browsewindow) # Entrée de recherche pour le stockage local
    entree_recherche_locale.pack(side="top", fill="x")
    bouton_recherche_locale = Button(browsewindow, text="Rechercher...", command=rechercher_image_locale)
    bouton_recherche_locale.pack(side="top")
    
    browsewindow.mainloop()


def rechercher_image_locale():
    "Rechercher une image sur un disque local"
    types_images = [("Image JPEG", "*.jpg"), ("Image PNG", "*.png"), ("Fichier GIF", "*.gif"), ("Fichier RAW", "*.raw"), ("Fichier SVG", "*.svg")]
    image_path = filedialog.askopenfilename(initialdir="C:", filetypes=types_images)   
    entree_recherche_locale.insert("end", image_path)
    return image_path
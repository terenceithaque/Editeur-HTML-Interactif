# Script principal
from tkinter import *
from tkinter import messagebox
from tkinter.font import *
from widgets import *
from menu_police import *
from pywebio.output import *
from pywebio import *
import webbrowser
import threading
from open_file import *


class Application(Tk):
    "Application"
    def __init__(self):
        super().__init__() # Hériter des attributs de la classe Tk
        self.title("Editeur HTML interactif")

        self.barre_menus = Menu(self, tearoff=0) # Ajouter une barre de menus
        self.menu_fichier = Menu(self.barre_menus, tearoff=0) # Ajouter un menu "Fichier"
        self.menu_fichier.add_command(label="Ouvrir un fichier HTML...", command=lambda:open_htmlfile(self))
        self.barre_menus.add_cascade(label="Fichier", menu=self.menu_fichier)

        self.menu_ajouter = Menu(self.barre_menus, tearoff=0) # Ajouter un menu "Ajouter" pour permettre à l'utilisateur d'ajouter des éléments à sa page web
        self.menu_ajouter.add_command(label="Titre de la page...", command=lambda:ajouter_titre(self)) # Permettre à l'utilisateur de spécifier le titre de la page
        self.menu_ajouter.add_command(label="Image...", command=lambda:ouvrir_image(self)) # Permettre à l'utilisateur d'insérer une image
        self.menu_ajouter.add_command(label="Texte...", command = lambda:ajouter_texte(self)) # Permettre à l'utilisateur d'insérer du texte
        self.barre_menus.add_cascade(label="Ajouter", menu=self.menu_ajouter)

        self.menu_apercu = Menu(self.barre_menus, tearoff=0)
        self.menu_apercu.add_command(label="Aperçu dans le navigateur web...", command=self.executer_page)
        self.barre_menus.add_cascade(label="Aperçu", menu=self.menu_apercu)

        self.polices_ecriture = ["Helvetica Neue", "Liberation Sans", "Liberation Serif", "Linux Biolinum G", "Lucida Console",
                                 "Malgun Gothic", "Microsoft Sans Serif", "Roboto", "OCR A Extended"] # Polices d'écriture que l'utilisateur peut choisir pour le texte.

        self.var = StringVar()
        self.var.set(self.polices_ecriture[0])

        self.menu_polices = OptionMenu(self,self.var, *self.polices_ecriture, command=lambda option=self.var.get():self.changer_police_car(option))
        self.menu_polices.config(text="Helvetica Neue", width=15, font=("Helvetica Neue", 12))    

        self.menu_polices.pack()


        

        self.config(menu=self.barre_menus) # On configure le menu de la fenêtre

        liste_widgets.append(self.barre_menus)
        liste_widgets.append(self.menu_polices)

        

    def changer_police_car(self, police_choisie):
        "Changer la police de caractères du texte"
        self.menu_polices.config(text=police_choisie, font=(police_choisie, 12))
        for widget in liste_htmltextes:
            widget.set_police(police_choisie)


    async def web_application(self):
        for widget in liste_widgets: # Pour chaque widget ajouté à la page web
            if(type(widget).__name__) == "HtmlTexte":
                print("Le widget est un texte")
                output.put_text(widget.get("1.0", "end")).style(f"font-family:{self.var.get()}")

            if(type(widget).__name__) == "Entry": 
                session.set_env(title=widget.get())
       





    def executer_page(self):
        "Exécuter le code de la page web"  
         
        


        threading.Thread(target=start_server, args=(self.web_application, 8080, "0.0.0.0", True)).start()



        webbrowser.open("http://192.168.1.101:8080/")        
                  

    






   



app = Application()
app.mainloop()
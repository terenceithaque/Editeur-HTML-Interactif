# Menu pour choisir la police d'écriture du texte
from tkinter import *

class MenuPolice(OptionMenu):
    "Menu pour choisir la police d'écriture"
    def __init__(self, app_maitre, polices, text_widget):
        super().__init__(app_maitre, StringVar(app_maitre), polices) # Hériter des attributs de la classe OptionMenu
        self.options = StringVar(app_maitre)
        self.text_widget = text_widget()



        menu_police = OptionMenu(app_maitre, self.options, polices[0], command=self.text_widget.set_police)
        
        menu_police.grid(column=1, row=0, sticky=W, padx=5, pady=5)

       


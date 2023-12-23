# Sauvegarder au format HTML
from tkinter import filedialog
from open_file import get_htmlfile_path
import os
from htmltexte import liste_widgets

def enregistrer_sous():
    "Enregistrer dans un nouveau fichier"
    types = [("Document HTML", "*.html")] # Types dans lesquels l'utilisateur peut enregistrer le fichier
    chemin_sauv = filedialog.asksaveasfilename(title="Enregistrer sous forme de document HTML", filetypes=types, defaultextension=".html") # Demander à l'utilisateur où il souhaite enregistrer le fichier

    with open(chemin_sauv, "a") as f: # Ouvrir le fichier enregistré en écriture
        modele_doc = "<!DOCTYPE html><html><head>" # Modèle du document à enregistrer
        widgets_enregistres = [] # Liste des widgets enregistrés dans la page web
        while len(widgets_enregistres) < len(liste_widgets):
            for widget in liste_widgets: # Pour chaque widget ajouté à la page web par l'utilisateur
                if type(widget).__name__ == "Entry": # On suppose qu'une entrée équivaut au titre de la page web
                    modele_doc += f"<title>{widget.get()}</title>" # On insère le contenu de l'entrée dans une balise titre
                    modele_doc += "<meta content='width = device-width, initial-scale = 1 name = 'viewport''>"
                    
                    widgets_enregistres.append(widget)

                if type(widget).__name__ == "HtmlTexte":  # Si le widget est un widget de type HtmlTexte
                    if "<body>" not in modele_doc: # S'il n'y a pas de balise <body> dans le modèle du document
                        modele_doc += "<body>"   
                        modele_doc += f"<p>{widget.get("1.0", "end")}</p>"
                        widgets_enregistres.append(widget)



            break

        if "<head>" in  modele_doc:
            modele_doc += "</head>" # On ferme la balise head

        if "<body>" in  modele_doc:
            modele_doc += "</body>" # On ferme la balise body


        modele_doc += "</html>"     




        f.write(modele_doc)
        f.close()            






                
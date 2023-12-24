# Sauvegarder au format HTML
from tkinter import filedialog
from open_file import html_file
import os
from htmltexte import liste_widgets

def enregistrer_sous():
    "Enregistrer dans un nouveau fichier"
    global html_file
    types = [("Document HTML", "*.html")] # Types dans lesquels l'utilisateur peut enregistrer le fichier
    chemin_sauv = filedialog.asksaveasfilename(title="Enregistrer sous forme de document HTML", filetypes=types, defaultextension=".html") # Demander à l'utilisateur où il souhaite enregistrer le fichier

    with open(chemin_sauv, "w") as f: # Ouvrir le fichier enregistré en écriture
        modele_doc = "<!DOCTYPE html><html><head>" # Modèle du document à enregistrer
        global widgets_enregistres
        widgets_enregistres = [] # Liste des widgets enregistrés dans la page web
        while len(widgets_enregistres) < len(liste_widgets):
            for widget in liste_widgets: # Pour chaque widget ajouté à la page web par l'utilisateur
                if type(widget).__name__ == "Entry": # On suppose qu'une entrée équivaut au titre de la page web
                    modele_doc += f"<title>{widget.get()}</title>" # On insère le contenu de l'entrée dans une balise titre
                    name = "viewport"
                    modele_doc += '<meta content="width = device-width, initial-scale = 1 name = {}">'.format(name)
                    
                    widgets_enregistres.append(widget)

                if type(widget).__name__ == "HtmlTexte":  # Si le widget est un widget de type HtmlTexte
                    if "<body>" not in modele_doc: # S'il n'y a pas de balise <body> dans le modèle du document
                        modele_doc += "<body>"   
                        modele_doc += f"<p>{widget.get("1.0", "end")}</p>"
                        widgets_enregistres.append(widget)



            break

        if "<head>" in  modele_doc:
            if "<meta content='width = device-width, initial-scale = 1 name = 'viewport''>" in modele_doc:
                "<meta content='width = device-width, initial-scale = 1 name = 'viewport''>".replace("'", "")

            modele_doc += "</head>" # On ferme la balise head

    

        if "<body>" in  modele_doc:
            modele_doc += "</body>" # On ferme la balise body


        modele_doc += "</html>"     




        f.write(modele_doc)
        f.close()



    html_file = chemin_sauv    


def enregistrer():
    "Enregistrer les modifications apportées à un fichier"
    if html_file == "": # Si le fichier HTML n'existe pas encore
        enregistrer_sous() # Enregistrer dans un nouveau fichier
    else:
        with open(html_file, "a") as f:
            widgets_page_web = {"Entry" : "<title>",
                                "HtmlTexte": "<p>"} # Widgets insérés par l'utilisateur et leur équivalent dans la page web
            
            for widget in widgets_page_web: 
                if widget not in widgets_enregistres: # Si le widget n'a pas été enregistré dans la page web
                    widget_web = widgets_page_web[widget] # Equivalent du widget dans la page web
                    print(widget_web)
                    if type(widget).__name__ == "Entry":
                        widget_web += f"{widget.get()}</{widget_web}>"
                        f.write(widget_web)

                    if type(widget).__name__ == "HtmlTexte":
                        widget_web += f"{widget.get("1.0", "end")}</{widget_web}>" 
                        f.write(widget_web)

        f.close()               










                
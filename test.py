import applicationJSON as app

# Afficher la liste des notes
for eleve in app.liste_notes:
    print("Nom:" + eleve["nom"])
    print("Prenom:" +eleve["prenom"])
    print("Note:" +str(eleve["note"]))
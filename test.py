import applicationJSON as app

# Print the list of student notes by detail
for eleve in app.liste_notes:
    print("Nom:" + eleve["nom"])
    print("Prenom:" +eleve["prenom"])
    print("Note:" +str(eleve["note"]))

# Print the list of student notes by object
for eleve in app.liste_notes:
    print(eleve)

# Print the list of student notes by list
print(app.liste_notes)
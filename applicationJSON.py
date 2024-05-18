import json
liste_notes = [
    {"nom": "Abbassi", "prenom": "Khalid", "note": 15.5},
    {"nom": "Moh", "prenom": "Kamal", "note": 12.5},
    {"nom": "Hanine", "prenom": "Hicham", "note": 13}
]

# Écrire la liste de notes des eleves dans un fichier JSON avec la fonction dump
with open("donnees.json", "w") as mon_fichier:
    json.dump(liste_notes, mon_fichier)

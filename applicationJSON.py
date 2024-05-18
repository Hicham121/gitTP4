import json
liste_notes = [
    {"nom": "Abbassi", "prenom": "Khalid", "note": 15.5},
    {"nom": "Moh", "prenom": "Kamal", "note": 12.5},
    {"nom": "Hanine", "prenom": "Hicham", "note": 13}
]

# Write the list of student notes  from the JSON file 
with open("donnees.json", "w") as mon_fichier:
    json.dump(liste_notes, mon_fichier)

# Read the list of student notes  from the JSON file
with open("donnees.json", "r") as mon_fichier:
    liste_notes = json.load(mon_fichier)

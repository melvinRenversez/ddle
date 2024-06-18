# Écrire un programme Python qui lit un fichier texte, analyse le contenu et génère un rapport contenant les informations suivantes :

# Le nombre total de mots dans le texte.
# Le nombre total de caractères (espaces inclus et exclus).
# La fréquence d'apparition de chaque mot.
# Les cinq mots les plus fréquents.
# La longueur moyenne des mots.

import os

os.system('cls')


text = input("Entrez le nom du fichier : ")

print(text)

with open(text, "r", encoding="utf-8") as f:
    text = f.read()

print(text)

x = text.split(' ')

print(x)

# _*_ coding:Utf8 _*_

liste = []

entree = input("Entrer une valeur a ajouter dans la liste: ")
if entree != '':
    liste.append(entree)

while entree != '':
    entree = input("Entrer une valeur a ajouter dans la liste: ")
    if entree != '':
        liste.append(entree)

print(liste)

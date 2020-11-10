#! /usr/bin/env python
# -*- coding:Utf8 -*-

def ecrireDansFichier():
    of = open(nomF, 'a')
    while 1:
        ligne = input("Entrez une ligne de texte (ou <Enter>) : ")
        if ligne == '':
            break
        else:
            of.write(ligne + '\n')
    of.close()

def lireDansFichier():
    of = open(nomF, 'r')
    while 1:
        ligne = of.readline()
        if ligne == "":
            break
        print(ligne)
    of.close()

def sansDc(ch):
    "Cette fonction renvoie la chaine ch sans le dernier caractère"
    nouv = ""
    i, j = 0, len(ch) -1
    while i < j:
        nouv = nouv + ch[i]
        i = i +1
    return nouv

nomF = input('Nom de fichier à traiter : ')
choix = input('Entrez "e" pour écrire, "c" pour consulter les données :')

if choix == "e":
    ecrireDansFichier()
elif choix == "c":
    lireDansFichier()
else:
    print("'e' ou 'c'")

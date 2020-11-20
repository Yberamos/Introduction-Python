#! /usr/bin/env python
# -*- coding:Utf8 -*-
def triple(ligne):
    new, i = "", 0
    while i < len(ligne):
        if ligne[i] == ' ':
            new = new + '   '
        else:
            new = new + ligne[i]
        i += 1
    return new


def lireDansFichier():
    of = open(nomF, 'r')
    i = 0
    lignes = of.readlines()
    of.close()

    while i < len(lignes):
        lignes[i] = round(eval(lignes[i]))
        i += 1

    of = open(nomdestination, 'w')
    while i < len(lignes):
        of.write(lignes[i])
        i += 1
    of.close()


nomF = input('Nom de fichier à traiter : ')
nomdestination = input('Nom de fichier à traiter : ')

lireDansFichier()

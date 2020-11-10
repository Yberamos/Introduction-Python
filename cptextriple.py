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
    of = open(nomF, 'r+')
    i = 0
    lignes = of.readlines()

    while i < len(lignes):
        lignes[i] = triple(lignes[i])
        i += 1
    of.seek(0)
    of.writelines(lignes)
    of.close()


nomF = input('Nom de fichier à traiter : ')
lireDansFichier()


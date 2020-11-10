#! /usr/bin/env python
# -*- coding:Utf8 -*-

def ecrireDansFichier():
    i = 2
    of = open(nomF, 'a')
    while i <= 30:
        of.write(CalcTable(i))
        i += 1
    of.write('\n')
    of.close()


def CalcTable(x):
    i = 1
    mult = ""
    while i <= 20:
        mult = mult + str(i*x) + ' '
        i += 1
    mult = mult + '\n'
    return mult


nomF = input('Nom de fichier à traiter : ')
ecrireDansFichier()

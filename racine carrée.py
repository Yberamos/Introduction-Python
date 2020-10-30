# _*_ coding:Utf8 _*_

from math import sqrt
# calcul du périmetre et aire d'un triangle quelconque

print('Entrez le coté a : ', end = '')
a = float(input())

print('Entrez le coté b : ', end = '')
b = float(input())

print('Entrez le coté c : ', end = '')
c = float(input())

demiperimetre = (a+b+c)

aire = ( a * b ) / 2
perimetre = sqrt(demiperimetre*(demiperimetre-a)*(demiperimetre - b)*(demiperimetre - c))

print("Ce triangle a une aire de", aire*2, 'et un perimetre de ', perimetre)


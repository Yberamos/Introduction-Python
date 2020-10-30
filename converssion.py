# _*_ coding:Utf8 _*_
from math import *

print('Entrez le nombre de miles parcouru: ', end = '')
milesStr = input()

mph = float(milesStr)
mps = ( mph * 1609) / 3600
kmph = mph * 1.1609

print(mph, 'miles/heure =', kmph, 'km/h, ou', mps, 'm/s')

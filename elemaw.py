def elemax(liste, debut=0, fin=-1):
    cpt, maxele = debut, -1
    if fin == -1:
        fin = len(liste)
    while cpt < fin:
        if liste[cpt] > maxele:
            maxele = liste[cpt]
        cpt += 1
    return maxele


serie = [9, 3, 6, 1, 7, 5, 4, 8, 2]
print(elemax(serie))
print(elemax(serie, 2, 5))
print(elemax(serie, 2))
print(elemax(serie, fin=3, debut=1))

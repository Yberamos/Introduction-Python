def compteCar(ca, ch):
    "Comptage d'un char dans une chaine"
    cpt = 0
    for c in ch:
        if c == ca:
            cpt += 1
    return cpt


print(compteCar('e', 'Cette phrase est un exemple'))
print(compteCar.__doc__)

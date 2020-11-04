def indexMax(liste):
    cpt, position, maxval = 0, 0, 0

    while cpt < len(liste):
        if liste[cpt] > maxval:
            maxval, position = liste[cpt], cpt + 1
        cpt += 1
    return position


print(indexMax([1, 5, 56, 2, 10]))

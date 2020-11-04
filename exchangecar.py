def changeCar(ch, ca1, ca2, debut=0, fin=-1):
    cpt = 0
    new_ch = ""
    if fin == -1:
        fin = len(ch)
    else:
        fin -= 1

    while cpt < len(ch):
        if debut <= cpt <= fin and ch[cpt] == ca1:
            new_ch = new_ch + ca2
        else:
            new_ch = new_ch + ch[cpt]
        cpt += 1

    return new_ch


phrase = 'Ceci est une toute petite phrase.'
print(changeCar(phrase, ' ', '*'))
print(changeCar(phrase, ' ', '*', 8, 12))
print(changeCar(phrase, ' ', '*', 12))
print(changeCar(phrase, ' ', '*', fin=12))

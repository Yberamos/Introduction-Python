Borne_A, Borne_B = eval(input('Entrez les deux bornes: '))

print('Les bornes sont: ', Borne_A, 'et', Borne_B)
i = Borne_A
totalAND = 0
totalOR = 0

while i <= Borne_B:
    if not (i % 3) and not (i % 5):
        totalAND += i
    if not (i % 3) or not (i % 5):
        totalOR += i
    i += 1

print('le total and est de :', totalAND)
print('le total or est de :', totalOR)

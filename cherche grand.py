print("ce script recherche le plus grand de trois nombres")
ch = input('Entrez trois nombres séparées par des virgules :')

# association des fonctions eval et list, permet de convertir
# en liste toute les chaine de valeur sépareé par les virgules
nn = list(eval(ch))

maximum, index = nn[0], 'première'

if nn[1] > maximum:
    maximum = nn[1]
    index = 'seconde'

if nn[2] > maximum:
    maximum = nn[2]
    index = 'troisième'
print(nn)
print('Le plus grand est ', maximum)
print('Il est en ', index, 'position')


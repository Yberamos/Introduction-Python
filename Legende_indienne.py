# _*_ coding:Utf8 _*_

# un grain de riz par case (puis 2, puis 4) (times 2) etc 64 case
# nb exact (entier)
# notation scientifique

nb_grain_riz = 1.0
iterateur = 1

while iterateur < 65:
    print("Nombre de grain sur la case ", iterateur, "est de ", nb_grain_riz)
    nb_grain_riz = nb_grain_riz*2
    iterateur += 1

print('Il y aura un total de ', int(nb_grain_riz), ' grains de riz.')
print('Il y aura un total de ', nb_grain_riz, ' grains de riz.')
scientific_notation = "{:e}".format(nb_grain_riz)
print('En notation scientific: ', scientific_notation)

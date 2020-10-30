# _*_ coding:Utf8 _*_

chaine = 'Gaston'
i = 1
new_chaine = chaine[0]

while i < len(chaine):
    new_chaine = new_chaine + '*' + chaine[i]
    i += 1

print('La chaine ', chaine, ' devient ', new_chaine)

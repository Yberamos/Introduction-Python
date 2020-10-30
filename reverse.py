# _*_ coding:Utf8 _*_

chaine = 'zorglub'
lc = len(chaine)
i = lc - 1
New_chaine = ''

while i >= 0:
    New_chaine = New_chaine + chaine[i]
    i -= 1

print('La chaine ', chaine, ' est devenue ', New_chaine)

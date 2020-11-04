# _*_ coding:Utf8 _*_
ch = 'Monty python flying circus'
cr = 'e'

lc = len(ch)
i = 0
r = 0

while i < lc:
    if ch[i] == cr:
        r = r + 1
    i = i + 1

print('Le caractère', cr, end=' ')
if r > 0:
    print('est présent ', r, ' fois', end=' ')
else:
    print('est introuvable', end='')
print('dans la chaîne', ch)

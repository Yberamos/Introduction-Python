# _*_ coding:Utf8 _*_

tt = [31, 5, 12, 8, 3, 75, 2, 15]
paire = []
impaire = []
i = 0

while i < len(tt):
    if tt[i] % 2:
        impaire.append(tt[i])
    else:
        paire.append(tt[i])
    i += 1

print('Paire : ')
print(paire)
print('Impaire : ')
print(impaire)

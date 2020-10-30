# _*_ coding:Utf8 _*_

tt = [31,5,12,8,3,75,2,15]
greater = -1
i = 0

while i < len(tt):
    if greater < tt[i]:
        greater = tt[i]
    i += 1

print('La valeur la plus grande est ', greater)

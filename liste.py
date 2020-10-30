# _*_ coding:Utf8 _*_

t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['Janvier', 'Fevrier', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet',
      ' Aout', 'Septembre', 'Octobre', 'Novembre', 'Decembre']

t3 =[]

i = 0
while i< len(t1):
    t3.append(t2[i])
    t3.append(t1[i])
    i += 1
print(t3)

lectureff, lecturedf = "", ""

nameff = input('Premier fichier: ')
namedf = input('Deuxieme fichier: ')
namerf = input('Resultat fichier: ')


ff = open(nameff, 'r')
df = open(namedf, 'r')
rf = open(namerf, 'w')

while True:
    lectureff = ff.readline()
    lecturedf = df.readline()

    if lectureff != '':
        rf.write(lectureff)

    if lecturedf != '':
        rf.write(lecturedf)

    if lectureff == '' and lecturedf == '':
        break

ff.close()
df.close()
rf.close()

annee = eval(input('Entrez une année: '))

if not (annee % 4) and (annee % 100 or not(annee % 400)):
    print('valide')
else:
    print('non valide')

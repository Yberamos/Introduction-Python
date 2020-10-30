note = 0
minimum = 99999999
maximum = 0
liste_notes= []
total = 0
nb_notes = 0

while note >= 0:
    note = float(input('Entrez un note (negatif pour arreter): '))
    if note >= 0:
        nb_notes += 1
        total += note
        liste_notes.append(note)
        if note < minimum:
            minimum = note
        if note > maximum:
            maximum = note
        print('Nombre de notes: ', nb_notes)
        print('Note minimum: ', minimum)
        print('Note maximum: ', maximum)
        print('Moyenne des notes: ', total/nb_notes)
print(liste_notes)

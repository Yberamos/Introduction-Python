def loadbd():
    bd = {}
    fname = input('Entrez le nom du fichier: ')
    file = open(fname, 'r')
    lignes = file.readlines()
    file.close()
    for ligne in lignes:
        temp = ligne.split('@')
        key = temp[0]
        temp = temp[1]
        values = temp.split('#')[0], temp.split('#')[1][:-1]
        bd[key] = values
    return bd


def savebd(bd):
    fname = input('Entrez le nom du fichier: ')
    file = open(fname, 'a')
    for key in bd:
        file.write(key+'@'+str(bd[key][0])+'#'+str(bd[key][1])+'\n')
    file.close()


def recherchebd(bd):
    output = 'Nom: {}   -  âge: {} ans   - taille: {} m'
    while True:
        target = input('Rentrer le nom que vous recherchez: ')
        if target != '':
            record = bd.get(target, '')
            if record != '':
                print(output.format(target, bd[target][0], bd[target][1]))
            else:
                print('Nom inconnu')
        else:
            break


def affichagebd(bd):
    output = 'Nom: {}   -  âge: {} ans   - taille: {} m'
    for key in bd:
        print(output.format(key, bd[key][0], bd[key][1]))


def ajoutdansbd(bd):
    while True:
        record = lecturerecord()
        if record != "":
            bd[record[0]] = (record[1], record[2])
        else:
            break


def lecturerecord():
    output = 'Nom: {}   -  âge: {} ans   - taille: {} m'
    while True:
        nom = input("Entrez le nom: ")
        if nom == "":
            return ""
        age = int(input("Entrez l'age: "))
        taille = float(input("Entrez la taille: "))

        print(output.format(nom, age, taille))
        choix = input("Ces informations sont-elles correctes? (n/Y)")
        if choix == '':
            break

    return [nom, age, taille]


def _main():
    bd = {}
    while True:
        choix = input("Que voulez-vous faire? (A)jouter - (C)onsulter - (R)echercher - (E)nregistrer - (L)oad - (Q)uitter ")
        choix = choix.lower()
        if choix == 'a':
            ajoutdansbd(bd)
        elif choix == 'c':
            affichagebd(bd)
        elif choix == 'r':
            recherchebd(bd)
        elif choix == 'e':
            savebd(bd)
        elif choix == 'l':
            bd = loadbd()
        elif choix == 'q':
            break


if __name__ == "__main__":
    _main()

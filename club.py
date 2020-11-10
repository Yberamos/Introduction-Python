import os


def lecturerecord():
    while True:
        nom = input("Entrez le nom: ")
        if nom == "":
            return ""
        prenom = input("Entrez le prenom: ")
        adresse = input("Entrez l'adress: ")
        cp = input("Entrez le code postal: ")
        tel = input("Entrez le numeros de telephone: ")

        print(nom + ' ' + prenom + ' ' + adresse + ' ' + cp + ' ' + tel)
        choix = input("Ces informations sont-elles correctes? (n/Y)")
        if choix == '':
            break

    return [nom, prenom, adresse, cp, tel]


def enregistrementrecord(record):
    of = open(fname, 'a')
    i = 0
    while i < len(record):
        of.write(record[i]+'#')
        i += 1
    of.write('\n')
    of.close()


#fname = input('Nom du fichier: ')
fname = 'db.dat'
if os.path.exists(fname):
    os.remove(fname)

while True:
    newrecord = lecturerecord()
    if newrecord != "":
        print("enregitrement")
        enregistrementrecord(newrecord)
    else:
        break

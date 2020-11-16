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

def modificationrecord(record_fichier):
    while True:
        print(record_fichier)
        date = input('Entrer la date de naissance: ')
        sexe = input('Entrere le sexe: ')
        print(date + ' ' + sexe)
        choix = input("Ces informations sont-elles correctes? (n/Y)")
        if choix == '':
            break
    record_fichier = record_fichier + '#' + date + '#' + sexe + '#'

    return record_fichier


def enregistrementrecord(record, nom):
    of = open(nom, 'a')
    i = 0
    while i < len(record):
        of.write(record[i]+'#')
        i += 1
    of.write('\n')
    of.close()


fname = 'db.dat'
fnamebis = 'db2.dat'

choix = input('Voulez-vous modifier ou creer un nouveau fichier(1 ou 2):')
if choix == '1':
    # fname = input("Nom du fichier d'origine: ")
    # fnamebis = input("Nom du fichier de copie: ")
    of = open(fname, 'r')
    while True:
        newrecord = modificationrecord(of.readline())
        if newrecord != "":
            # if os.path.exists(fnamebis):
            #    os.remove(fnamebis)
            enregistrementrecord(newrecord, fnamebis)
        else:
            break
elif choix == '2':
    # fname = input("Nom du fichier d'origine: ")
    while True:
        newrecord = lecturerecord()
        if newrecord != "":
            print("enregitrement")
            if os.path.exists(fname):
                os.remove(fname)
            enregistrementrecord(newrecord, fname)
        else:
            break

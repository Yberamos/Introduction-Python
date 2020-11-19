#Écrivez un script qui permette de créer et de relire aisément un fichier texte. Votre
#programme demandera d’abord à l’utilisateur d’entrer le nom du fichier. Ensuite il lui
#proposera le choix, soit d’enregistrer de nouvelles lignes de texte, soit d’afficher le contenu du
#fichier.
#L’utilisateur devra pouvoir entrer ses lignes de texte successives en utilisant simplement la
#touche <Enter> pour les séparer les unes des autres. Pour terminer les entrées, il lui suffira
#d’entrer une ligne vide (c’est-à-dire utiliser la touche <Enter> seule).
#L’affichage du contenu devra montrer les lignes du fichier séparées les unes des autres de la
#manière la plus naturelle (les codes de fin de ligne ne doivent pas apparaître).


def Ecrire():
    while True:
        entree_util = input('Que veux-tu écrire? ')
        if entree_util != '':
            entree_util = entree_util + '\n'
            file = open(fname, 'a')
            file.write(entree_util)
            file.close()
        else:
            break


def Lecture():
    file = open(fname, 'r')
    contenu = file.readlines()
    file.close()

    for ligne in contenu:
        print(ligne)


fname = 'MonText.dat'
while True:
    choix = input('Que veux-tu faire( 1 ou 2 ou 3) ?')

    if choix == '1':
        Ecrire()
    elif choix == '2':
        Lecture()
    elif choix == '3':
        break
    else:
        print('pov con')




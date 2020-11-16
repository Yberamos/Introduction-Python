def inverse():
    new_dict = {}
    for key in dico:
        new_dict[dico[key]] = key
    return new_dict


dico = {
    'Computer' : 'Ordinateur',
    'Mouse' : 'Souris',
    'Keyboard' : 'Clavier',
    'Screen' : 'Ecran',
    'Hard Disk' : 'Disque dur'
}

print(dico)
print(inverse())
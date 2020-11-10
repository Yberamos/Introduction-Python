from tkinter import *


def evaluer(event):
    chaine.configure(text='Résultat = ' + str(eval(entree.get())))


fenetre = Tk()
entree = Entry(fenetre)
entree.bind("<Return>", evaluer)
chaine = Label(fenetre)
entree.pack()
chaine.pack()
fenetre.mainloop()
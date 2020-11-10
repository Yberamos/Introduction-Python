from tkinter import *


def avance(x, y):
    global x1, y1

    x1, y1 = x1 + x, y1 + y
    can1.coords(oval1, x1, y1, x1+30, y1+30)


def deplacement_gauche():
    avance(-10, 0)


def deplacement_droite():
    avance(10, 0)


def deplacement_haut():
    avance(0, -10)


def deplacement_bas():
    avance(0, 10)


x1, y1 = 10, 10
fenetre = Tk()
fenetre.title("Exercice d'animation avec Tkinter")

can1 = Canvas(fenetre, bg='dark grey', height=300, width=300)
oval1 = can1.create_oval(x1, y1, x1+30, y1+30, fill='red')
can1.pack(side=LEFT)
Button(fenetre, text='Quitter', command=fenetre.quit).pack(side=BOTTOM)
Button(fenetre, text='Gauche', command=deplacement_gauche).pack()
Button(fenetre, text='Droite', command=deplacement_droite).pack()
Button(fenetre, text='Haut', command=deplacement_haut).pack()
Button(fenetre, text='Bas', command=deplacement_bas).pack()

fenetre.mainloop()


from tkinter import *
from random import randrange


def damier():
    "dessine un damier"
    i, j = 0, 0
    global size_carré

    while j < 10:
        while i < 10:
            if (i+j) % 2 != 1:
                can.create_rectangle(i*size_carré, j*size_carré, (i+1)*size_carré, (j+1)*size_carré, outline='black', fill='navy')
            i += 1
        j += 1
        i = 0


def pion():
    "dessine un pion aléatoire"
    global size_carré
    position = randrange(0, 99)
    i = position % 10
    j = position // 10

    can.create_oval((i*size_carré)+4, (j*size_carré)+4, ((i+1)*size_carré)-4, ((j+1)*size_carré)-4, fill='red')

size_carré = 20
fen = Tk()

can = Canvas(fen, width=size_carré*10, height=size_carré*10, bg='ivory')
can.pack(side=TOP, padx=5, pady=5)

Button(fen, text='damier', command=damier).pack(side=LEFT, padx=3, pady=3)
Button(fen, text='pion', command=pion).pack(side=RIGHT, padx=3, pady=3)
Button(fen, text='Quitter', command=fen.destroy).pack(side=BOTTOM, padx=3, pady=3)

fen.mainloop()

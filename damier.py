
from tkinter import *
from random import randrange


def damier():
    "dessine un damier"
    i, j = 0, 0

    while j < 10:
        while i < 10:
            if (i+j) % 2 != 1:
                can.create_rectangle(i*20, j*20, (i+1)*20, (j+1)*20, outline='black', fill='black')
            i += 1
        j += 1
        i = 0


def pion():
    "dessine un pion aléatoire"

    position = randrange(0, 99)
    i = position % 10
    j = position // 10

    can.create_oval(i*20, j*20, (i+1)*20, (j+1)*20, fill='red')


fen = Tk()

can = Canvas(fen, width=200, height=200, bg='ivory')
can.pack(side=TOP, padx=5, pady=5)

b1 = Button(fen, text='damier', command=damier)
b1.pack(side=LEFT, padx=3, pady=3)

b2 = Button(fen, text='pion', command=pion)
b2.pack(side=RIGHT, padx=3, pady=3)

fen.mainloop()

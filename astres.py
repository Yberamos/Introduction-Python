from tkinter import *
from math import sqrt


def distance(x1, y1, x2, y2):
    """distance séparant les points x1, y1, x2, y2"""
    d = sqrt((x2-x1)**2+ (y2-y1)**2)  # théorem de Pythagore
    return d


def forceG(m1, m2, di):
    """force de gravitation s'exerçant entre m1 et m2 pour une distance di"""
    return m1*m2*6.67e-11/di**2  # loi de Newton


def avance(n, new_x, new_y):
    """déplacement de l'astre n, de gauche a droite ou de haut en bas"""
    global x, y, step
    # nouvelle coordonnées:
    x[n], y[n] = x[n] + new_x, y[n] + new_y

    # déplacement du dessin dans le canevas
    can1.coords(astre[n], x[n]-10, y[n]-10, x[n]+10, y[n]+10)

    # calcule de la nouvelle interdistance
    di = distance(x[0], y[0],x[1],y[1])

    # conversion de la distance "écran" en distance "astronomique": 1 pixel = 1 million de km
    diA = di*1e6

    # calcule de la force de gravitation correspondante
    f = forceG(m1, m2, diA)

    # affichage des nouvelles valeurs de distance et force
    valDis.configure(text='Distance = '+str(diA) + ' m')
    valFor.configure(text='For = '+str(f) + ' N')

    # adaptation du 'pas' de déplacement en fonction de la distance
    step = di/10


def gauche1():
    avance(0, -step, 0)


def droite1():
    avance(0, step, 0)


def haut1():
    avance(0, -0, -step)


def bas1():
    avance(0, 0, step)


def gauche2():
    avance(1, -step, 0)


def droite2():
    avance(1, step, 0)


def haut2():
    avance(1, -0, -step)


def bas2():
    avance(1, 0, step)


m1 = 6e24         # (valeur de la masse de la terre, en kg)
m2 = 6e24
astre = [0]*2     # liste servant à mémoriser les référence des dessins
x = [50., 350.]   # liste des coord X de chaque astre
y = [100., 100.]  # liste des coord Y de chaque astre
step = 10         # 'pas' de déplacement initiale

# Contruction de la fenetre
fenetre = Tk()
fenetre.title("Gravitation universelle suivant Newton")

# Libellé
valM1 = Label(fenetre, text='M1 = ' + str(m1) + ' kg')
valM1.grid(row=1, column=0)
valM2 = Label(fenetre, text='M2 = ' + str(m2) + ' kg')
valM2.grid(row=1, column=1)
valDis = Label(fenetre, text='Distance')
valDis.grid(row=3, column=0)
valFor = Label(fenetre, text='Force')
valFor.grid(row=3, column=1)

# Canevas avec le dessin des 2 astres
can1 = Canvas(fenetre, bg='light yellow', height=200, width=400)
can1.grid(row=2, column=0, columnspan=2)
astre[0] = can1.create_oval(x[0]-10, y[0]-10, x[0]+10, y[0]+10, fill='red', width=1)
astre[1] = can1.create_oval(x[1]-10, y[1]-10, x[1]+10, y[1]+10, fill='blue', width=1)

# 2 groupe de 4 boutton
fra1 = Frame(fenetre)
fra1.grid(row=4, column=0, sticky=W, padx=10, pady=10)
Button(fra1, text='<-', fg='red', command=gauche1).pack(side=LEFT)
Button(fra1, text='->', fg='red', command=droite1).pack(side=LEFT)
Button(fra1, text='^', fg='red', command=haut1).pack(side=LEFT)
Button(fra1, text='v', fg='red', command=bas1).pack(side=LEFT)

fra2 = Frame(fenetre)
fra2.grid(row=4, column=0, sticky=E, padx=10, pady=10)
Button(fra2, text='<-', fg='blue', command=gauche2).pack(side=LEFT)
Button(fra2, text='->', fg='blue', command=droite2).pack(side=LEFT)
Button(fra2, text='^', fg='blue', command=haut2).pack(side=LEFT)
Button(fra2, text='v', fg='blue', command=bas2).pack(side=LEFT)

fenetre.mainloop()

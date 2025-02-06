from turtle import *
from jeu import*
from random import*

largeur= 60
x_base= -200
y_base= 200

def afficher(self):
    colorier_fond()
    for i in range(6):
        for j in range(6):
            up()
            goto(x_base + j * largeur, y_base - i * largeur)
            down()
            fillcolor("white")
            begin_fill()
            circle(largeur / 2)
            end_fill()

        for k in range(6):
            up()
            goto(x_base + k * largeur, y_base - 6 * largeur )
            write(str(k))
            down()

def colorier_fond(self):
    up()
    goto(-270, 280)  
    bgcolor("orange")
    begin_fill()
    down()
    for color_fond in range(4):
        forward(470)
        right(90)
        end_fill()

def dessiner_pion(self,colone,ligne):
        joueur = randint(1,2)
        up()
        x = emplacement_colone(colone)
        y = emplacement_ligne(ligne)
        goto(x,y)
        down()
        if joueur == 1:
            color('red')
        else:
            color('blue')
        begin_fill()
        circle(largeur / 2)
        end_fill()


def emplacement_ligne(self,ligne):
    y = 0
    if ligne == 0:
        y = -100
    elif ligne == 1:
        y = -40
    elif ligne == 2:
        y = 20
    elif ligne == 3:
        y = 80
    elif ligne == 4:
        y = 140
    else:
        y = 200
    return y

def emplacement_colone(self,colone):
    x = 0
    if colone == 0:
        x = -200
    elif colone == 1:
        x = -140
    elif colone == 2:
        x = -80
    elif colone == 3:
        x = -20
    elif colone == 4:
        x = 40
    else:
        x = 80
    return x

speed(70)
afficher()
done()

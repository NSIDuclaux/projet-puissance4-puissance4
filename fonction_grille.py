from turtle import *
from jeu import*
from random import*

largeur= 60
x_base= -200
y_base= 200

def afficher():
    onscreenclick(gerer_clic)
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

def colorier_fond():
    up()
    goto(-270, 280)  
    bgcolor("orange")
    begin_fill()
    down()
    for color_fond in range(4):
        forward(470)
        right(90)
        end_fill()

def gerer_clic(x,y):
    j = gerer_clic_2(x,y)
    dessiner_pion(x_base + j * largeur,y_base)
    

def gerer_clic_2(x,y):
    if x < -170:
        x = 0
    elif -170 < x <-110:
        x = 1
    elif -110< x <-50:
        x = 2
    elif -50 < x < 10:
        x = 3
    elif 10 < x < 70:
        x = 4
    else:
        x = 5
    return x

def dessiner_pion(x, y):
        joueur = randint(1,2)
        up()
        goto(x,y)
        down()
        if joueur == 1:
            color('red')
        else:
            color('blue')
        begin_fill()
        circle(largeur / 2)
        end_fill()
    
        
onscreenclick(gerer_clic_2)
speed(70)
afficher()
done()

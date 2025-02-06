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

<<<<<<< HEAD
def gerer_clic(x,y):
    dessiner_pion(x,y)
    fillcolor("blue")
    begin_fill()
    down()
    for color_fond in range(4):
        forward(440)
        right(90)
        end_fill()

# def gerer_click(x,y):

#     if x < -170:
#         x=0
#     elif -170 < x <-110:
#         x=1
#     elif -110< x <-50:
#         x=2
#     elif -50 < x < 10:
#         x=3
#     elif 10 < x < 70:
#         x=4
#     else:
#         x=5
#     print(x)
#     return x
    
        
# onscreenclick(gerer_click)

def gerer_click(x,y):
    if x < -170:
        x=0
    elif -170 < x <-110:
        x=1
    elif -110< x <-50:
        x=2
    elif -50 < x < 10:
        x=3
    elif 10 < x < 70:
        x=4
    else:
        x=5
    
    if y < -40:
        y=0
    elif -40 < y < 20:
        y=1
    elif 20 < y < 80:
        y=2
    elif 80 < x < 140:
        y=3
    elif 140 < x < 200:
        y=4
    else:
        y=5
    print(x,y)


def dessiner_pion(x, y):
=======
def dessiner_pion(self,colone,ligne):
        joueur = randint(1,2)
>>>>>>> 476d4a3489d22f1c33a8f2d916ae41622d7c3d04
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

<<<<<<< HEAD
        
onscreenclick(gerer_click)
=======

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
>>>>>>> 476d4a3489d22f1c33a8f2d916ae41622d7c3d04

speed(70)
afficher()
done()
<<<<<<< HEAD
=======

>>>>>>> 476d4a3489d22f1c33a8f2d916ae41622d7c3d04

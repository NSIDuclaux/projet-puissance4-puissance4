from turtle import *

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
            down()
            write(str(k))

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
    dessiner_pion(x,y)
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
        up()
        goto(x_base + (x) * largeur, y_base - (y + 1) * largeur)
        down()
        color('red')
        begin_fill()
        circle(largeur / 2)
        end_fill()
        # rajouter print pour verifie tout ca
        #en fontion des coordonne du tableu
    


speed(70)
afficher()
done()

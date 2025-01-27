from turtle import *

largeur= 60
x_base= -150
y_base= 150

def afficher():
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
    goto(-250, 230)  
    fillcolor("orange")
    begin_fill()
    for color_fond in range(4):
        forward(600)
        right(90)
        end_fill()
        

speed(70)
afficher()
done()
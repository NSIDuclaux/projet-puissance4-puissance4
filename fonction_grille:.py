from turtle import *

largeur= 60
x_base= -150
y_base= 150

def afficher():
    for i in range(6):
        for j in range(6):
            up()
            goto(x_base + j * largeur, y_base - i * largeur)
            down()
            fillcolor("white")
            begin_fill()
            circle(largeur / 2)
            end_fill()

        for i in range(6):
            up()
            goto(x_base + i * largeur, y_base -  6 * largeur )
            down()
            write(str(i))

def colorier_fond():
    up()
    goto(-250, 230)  
    fillcolor("blue")
    down()  
    begin_fill()
    for color_fond in range(4):
        forward(500)
        right(90)
        end_fill()
        

speed(50)
afficher()
colorier_fond()
done()
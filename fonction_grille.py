from turtle import *

largeur= 60
x_base= -200
y_base= 200

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
            write(str(k))
            down()

def colorier_fond():
    up()
    goto(-270, 280)  
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

from turtle import *
from random import *

largeur = 60
x_base = -200
y_base = 200
grille = [[0]*6 for _ in range(6)]  # Crée une grille vide de 6x6

# Fonction pour dessiner le fond et les cases
def afficher():
    colorier_fond()
    for i in range(6):
        for j in range(6):  # Il y a 6 colonnes
            up()
            goto(x_base + j * largeur, y_base - i * largeur)
            down()
            fillcolor("white")
            begin_fill()
            circle(largeur / 2)
            end_fill()

    for k in range(6):  # Affichage des numéros de colonnes
        up()
        goto(x_base + k * largeur, y_base - 6 * largeur)
        write(str(k))
        down()

# Fonction pour colorier le fond
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

# Gestion du clic pour déterminer la colonne
def gerer_clic(x, y):
    col = gerer_click(x, y)
    ligne = hauteur(grille, col)  # Trouve la ligne libre dans la colonne
    if ligne is not None:
        dessiner_pion(x_base + col * largeur, y_base - ligne * largeur, col)

# Fonction pour déterminer la colonne à partir du clic
def gerer_click(x, y):
    if x < -170:
        col = 0
    elif -170 < x < -110:
        col = 1
    elif -110 < x < -50:
        col = 2
    elif -50 < x < 10:
        col = 3
    elif 10 < x < 70:
        col = 4
    elif 70 < x < 130:
        col = 5
    else:
        col = 6
    return col

# Fonction pour dessiner un pion
def dessiner_pion(x, y, col):
    joueur = randint(1, 2)  # Choisit un joueur aléatoirement (1 ou 2)
    up()
    goto(x, y)
    down()
    if joueur == 1:
        color('red')
    else:
        color('blue')
    begin_fill()
    circle(largeur / 2)
    end_fill()

    # Mise à jour de la grille avec la position du pion
    for i in range(6):
        if grille[i][col] == 0:
            grille[i][col] = joueur
            break

# Fonction pour obtenir la hauteur disponible dans une colonne
def hauteur(grille, col):
    for i in range(6):
        if grille[i][col] == 0:  # Trouve la première case vide
            return i
    return None  # Si la colonne est pleine

# Fonction pour démarrer le jeu
def main():
    speed(70)
    afficher()
    onscreenclick(gerer_clic)  # Lié à la gestion du clic
    done()

# Démarrage du jeu
main()

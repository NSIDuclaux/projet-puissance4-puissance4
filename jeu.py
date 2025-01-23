from turtle import *

largeur= 60
x_base= -150
y_base= 150

class Puissance4():

    def __init__(self):
        self.joueur1=1
        self.joueur2=2
        self.grille=[
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0]]
        self.joueur=self.joueur1

    def joueur_actif(self):
        if self.joueur == self.joueur1:
            return self.joueur2
        else:
            return self.joueur1

    def jeu(self):
        self.afficher(self.grille)
        self.joueur = self.joueur_actif()
        onscreenclick(self.detecter_clic)
        done()
        

    def verif_colone(self,grille):
        for k in range(6):
                if grille[k][0]==grille[k][1] and grille[k][1]==grille[k][2] and grille[k][2]==grille[k][3] and grille[k][3]==grille[k][4]:
                    return"Victoire"
                elif grille[k][1]==grille[k][2] and grille[k][2]==grille[k][3] and grille[k][3]==grille[k][4] and grille[k][4]==grille[k][5]:
                    return "Vicotire"
                elif grille[k][5]==grille[k][6] and grille[k][2]==grille[k][3] and grille[k][3]==grille[k][4] and grille[k][4]==grille[k][5]:

                    return "Vicotire"
            
        self.verif_ligne(self.grille)

    def verif_ligne(self,grille):
        for k in range(6):
            if grille[0][k]==grille[1][k] and grille[1][k]==grille[2][k] and grille[2][k]==grille[3][k] and grille[3][k]==grille[4][k]:
                return "Victoire"
            elif grille[1][k]==grille[2][k] and grille[2][k]==grille[3][k] and grille[3][k]==grille[4][k] and grille[4][k]==grille[5][k]:
                return "Vicotire"
            elif grille[5][k]==grille[6][k] and grille[2][k]==grille[3][k] and grille[3][k]==grille[4][k] and grille[4][k]==grille[5][k]:
                return "Vicotire"
        self.jeu()

    
    def hauteur(self,grille,colone):
        for k in range (len(grille)):
            if grille[colone][k]==0:
                return k
            

    def afficher(self):
        print(self.dessiner_grille())
        

    def dessiner_grille():
        up()
        goto(x_base, y_base)
        down()
        
        
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
        goto(-300, 300)  
        fillcolor("blue")  
        begin_fill()
        for color_fond in range(4):
            forward(600)
            right(90)
        end_fill()

    def dessiner_pion(self, x, y, joueur):
        up()
        goto(x_base + (x) * largeur, y_base - (y + 1) * largeur)
        down()
        if joueur == self.joueur1:
            # Pion ROUGE
            color('red')
        else:
            # Pion BLEU
            color('blue')
        begin_fill()
        circle(largeur / 2.5)
        end_fill()

teste=Puissance4()
teste.jeu()

            

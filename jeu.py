from turtle import *
import random
from copy import deepcopy




class Puissance4():

    def __init__(self):
        self.joueur1 = 1
        self.joueur2 = 2
        self.grille=[
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0]]
        self.tirage= random.randint(1,2)
        self.joueur = 0
        self.colone=0
        self.ligne=0
        self.largeur= 60
        self.x_base= -200
        self.y_base= 200
        self.listeplein=[]
    
    def pile_ou_face(self):#D
        bon=0
        choix=input("pile ou face? ")
        if choix=="pile":
            bon=1
        else:
            bon=2
        if self.tirage==1:
            print("pile!")
        else:
            print("face")
        if bon==self.tirage:
            self.joueur=self.joueur2
            print("A toi de jouer")
        else:
            self.joueur=self.joueur1
            print("Patience")

        
    def bot_move(self):
        meilleur_coup = self.calculer_meilleur_coup(self.grille)
        return meilleur_coup

    def calculer_meilleur_coup(self, grille):
        colonnes_valides = [i for i in range(6) if any(grille[i][j] == 0 for j in range(6))]
        coups_victoire = []
        for col in colonnes_valides:
            ligne = self.hauteur(grille, col)
            grille_temp = deepcopy(grille)
            grille_temp[col][ligne] = self.joueur2  

            if self.verif_victoire(grille_temp, col, ligne):
                coups_victoire.append(col)

        if coups_victoire:
                return random.choice(coups_victoire)
        
        coups_bloquer = []
        for col in colonnes_valides:
            ligne = self.hauteur(grille, col)
            grille_temp = deepcopy(grille)
            grille_temp[col][ligne] = self.joueur1 
            if self.verif_victoire(grille_temp, col, ligne):
                coups_bloquer.append(col)

        if coups_bloquer:
                return random.choice(coups_bloquer)

    

        meilleures_scores = []
        for col in colonnes_valides:
            ligne = self.hauteur(grille, col)
            grille_temp = deepcopy(grille)
            grille_temp[col][ligne] = self.joueur2  

            score = self.evaluer_plateau(grille_temp)
            meilleures_scores.append((col, score))

        max_score = max(meilleures_scores, key=lambda x: x[1])[1]
        coups_possibles = [coup[0] for coup in meilleures_scores if coup[1] == max_score]

        return random.choice(coups_possibles)
    
    def evaluer_plateau(self, grille):
        score = 0
        for i in range(6):
            for j in range(6):
                if grille[i][j] == self.joueur2:
                    score += 10  
                    if self.verif_victoire(grille, i, j):
                        score += 100  
                elif grille[i][j] == self.joueur1:
                    score -= 10  
                    if self.verif_victoire(grille, i, j):
                        score -= 100  
        return score
    
    def verif_victoire(self, grille, col, ligne):
        joueur = grille[col][ligne]
        

        count = 0
        for i in range(6):
            if grille[col][i] == joueur:
                count += 1
                if count >= 4:
                    return True
            else:
                count = 0

        count = 0
        for i in range(6):
            if grille[i][ligne] == joueur:
                count += 1
                if count >= 4:
                    return True
            else:
                count = 0

        count = 1
        for dx, dy in [(1, 1), (-1, -1)]:
            x, y = col + dx, ligne + dy
            while 0 <= x < 6 and 0 <= y < 6 and grille[x][y] == joueur:
                count += 1
                x += dx
                y += dy
        if count >= 4:
            return True

        count = 1
        for dx, dy in [(1, -1), (-1, 1)]:
            x, y = col + dx, ligne + dy
            while 0 <= x < 6 and 0 <= y < 6 and grille[x][y] == joueur:
                count += 1
                x += dx
                y += dy
        if count >= 4:
            return True

        return False



    def jeu(self):
        self.plein()
        compteur=6
        self.afficher()
        self.joueur=self.joueur_actif()
        if self.joueur == self.joueur2:
            self.colone = self.bot_move()
        else:
            self.colone = self.x()
            while self.colone in self.listeplein:
                print("case déjà prise")
                self.colone = self.x()

            
        self.ligne=self.hauteur(self.grille,self.colone)

        while compteur!=self.ligne:
            self.dessiner_pion(self.colone,compteur,self.joueur)
            self.noir(self.colone,compteur+1)
            compteur=compteur-1
        self.noir(self.colone,self.ligne+1)
        self.dessiner_pion(self.colone,self.ligne,self.joueur)
        self.grille[self.colone][self.ligne]=self.joueur
        self.verif_ligne(self.grille)
    
    def plein(self):#D
        for k in range(6):
            if self.grille[k][-1]!=0:
                self.listeplein.append(k)
    
    def afficher(self):#N
        speed(0)
        self.colorier_fond()
        for i in range(6):
            for j in range(6):
                up()
                goto(self.x_base + j * self.largeur, self.y_base - i * self.largeur)
                if self.grille[j][5-i]==2:
                    down()
                    fillcolor("#FFD700")
                    begin_fill()
                    circle(self.largeur / 2)
                    end_fill()
                elif self.grille[j][5-i]==1:
                    down()
                    fillcolor("red")
                    begin_fill()
                    circle(self.largeur / 2)
                    end_fill()
                else:
                    down()
                    fillcolor("black")
                    begin_fill()
                    circle(self.largeur / 2)
                    end_fill()
            for k in range(6):
                up()
                goto(self.x_base + k * self.largeur, self.y_base - 6 * self.largeur )
                write(str(k+1))
                down()

    def joueur_actif(self):#D
        if self.joueur == self.joueur1:
            return self.joueur2
        else:
            return self.joueur1
    
    def x(self):#D
        x=int(eval(input("colone?")))
        if x==1:
            colone=0
            return colone
        elif x==2:
            colone=1
            return colone
        elif x==3:
            colone=2
            return colone
        elif x==4:
            colone=3
            return colone
        elif x==5:
            colone=4
            return colone
        elif x==6:
            colone=5
            return colone
        else:
            print("Le chiffre doit être entre 1 et 6")
            return self.x()
    
    def hauteur(self,grille,colone):#D
        for k in range (len(grille)):
            if grille[colone][k]==0:
                return k
    
    def dessiner_pion(self,colone,ligne,joueur):#N
            speed(0)
            up()
            x = self.emplacement_colone(colone)
            y = self.emplacement_ligne(ligne)
            goto(x,y)
            down()
            if joueur == 1:
                color('red')
            else:
                color('#FFD700')
            begin_fill()
            circle(self.largeur / 2)
            end_fill()
    
    def noir(self,colone,ligne):#D et N
            speed(0)
            if ligne<6:
                up()
                x = self.emplacement_colone(colone)
                y = self.emplacement_ligne(ligne)
                goto(x,y)
                down()
                color('black')
                begin_fill()
                circle(self.largeur / 2)
                end_fill()
    
    def emplacement_ligne(self,ligne):#D
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

    def emplacement_colone(self,colone):#D
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
            x = 100
        return x
    

    def verif_ligne(self,grille):#D
        for k in range(6):
            if grille[k][3]!=0:
                if grille[k][0]==grille[k][1] and grille[k][1]==grille[k][2] and grille[k][2]==grille[k][3]:
                    if grille[k][2]==1:
                        return self.victoire()
                    else:
                        return self.defaite()
                elif grille[k][1]==grille[k][2] and grille[k][2]==grille[k][3] and grille[k][3]==grille[k][4]:
                    if grille[k][2]==1:
                        return self.victoire()
                    else:
                        return self.defaite()
                elif grille[k][5]==grille[k][4] and grille[k][2]==grille[k][3] and grille[k][3]==grille[k][4]:
                    if grille[k][2]==1:
                        return self.victoire()
                    else:
                        return self.defaite()     
        self.verif_colone(self.grille)
    
    def verif_colone(self,grille):#D
        for k in range(6):
            if grille[3][k]!=0 :
                if grille[0][k]==grille[1][k] and grille[1][k]==grille[2][k] and grille[2][k]==grille[3][k] :
                    if grille[2][k]==1:
                        return self.victoire()
                    else:
                        return self.defaite()
                elif grille[1][k]==grille[2][k] and grille[2][k]==grille[3][k] and grille[3][k]==grille[4][k]:
                    if grille[2][k]==1:
                        return self.victoire()
                    else:
                        return self.defaite()
                elif grille[5][k]==grille[4][k] and grille[2][k]==grille[3][k] and grille[3][k]==grille[4][k] :
                    if grille[5][k]==1:
                        return self.victoire()
                    else:
                        return self.defaite()
        self.verif_diago_croi(self.grille)


    def verif_diago_croi(self,grille):#D
        
        if grille[0][2]==grille[1][3] and grille[1][3]==grille[2][4] and grille[2][4]==grille[3][5] and grille[3][5]!=0:
            if grille[0][2]==1:
                return self.victoire()
            else:
                return self.defaite()
        elif grille[0][1]==grille[1][2] and grille[1][2]==grille[2][3] and grille[2][3]==grille[3][4] and grille[3][4]!=0:
            if grille[1][2]==1:
                return self.victoire()
            else:
                return self.defaite()
        elif grille[0][0]==grille[1][1] and grille[1][1]==grille[2][2] and grille[2][2]==grille[3][3] and grille[3][3]!=0:
            if grille[2][2]==1:
                return self.victoire()
            else:
                return self.defaite()
        elif grille[1][0]==grille[2][1] and grille[2][1]==grille[3][2] and grille[3][2]==grille[4][3] and grille[4][3]!=0:
            if grille[2][1]==1:
                return self.victoire()
            else:
                return self.defaite()
        elif grille[1][1]==grille[2][2] and grille[2][2]==grille[3][3] and grille[3][3]==grille[4][4] and grille[4][4]!=0:
            if grille[2][2]==1:
                return self.victoire()
            else:
                return self.defaite()
        elif grille[1][2]==grille[2][3] and grille[2][3]==grille[3][4] and grille[3][4]==grille[4][5] and grille[4][5]!=0:
            if grille[1][2]==1:
                return self.victoire()
            else:
                return self.defaite()
        elif grille[2][0]==grille[3][1] and grille[3][1]==grille[4][2] and grille[4][2]==grille[5][4] and grille[5][4]!=0:
            if grille[2][0]==1:
                return self.victoire()
            else:
                return self.defaite()
        elif grille[2][1]==grille[3][2] and grille[3][2]==grille[4][3] and grille[4][3]==grille[5][4] and grille[5][4]!=0:
            if grille[2][2]==1:
                return self.victoire()
            else:
                return self.defaite()
        elif grille[2][2]==grille[3][3] and grille[3][3]==grille[4][4] and grille[4][4]==grille[5][5] and grille[5][5]!=0:
            if grille[2][2]==1:
                return self.victoire()
            else:
                return self.defaite()
        self.verif_diago_decroi(self.grille)

    def verif_diago_decroi(self,grille):#D 
        if grille[0][3]==grille[1][2] and grille[1][2]==grille[2][1] and grille[2][1]==grille[3][0] and grille[3][0]!=0 :
            if grille[1][2]==1:
                return self.victoire()
            else:
                return self.defaite()
        elif grille[0][1]==grille[1][2] and grille[1][2]==grille[2][3] and grille[2][3]==grille[3][4] and grille[3][4]!=0:
            if grille[1][2]==1:
                return self.victoire()
            else:
                return self.defaite()
        elif grille[0][0]==grille[1][1] and grille[1][1]==grille[2][2] and grille[2][2]==grille[3][3]and grille[3][3]!=0:
            if grille[2][2]==1:
                return self.victoire()
            else:
                return self.defaite()
        elif grille[1][0]==grille[2][1] and grille[2][1]==grille[3][2] and grille[3][2]==grille[4][3] and grille[4][3]!=0:
            if grille[1][0]==1:
                return self.victoire()
            else:
                return self.defaite()
        elif grille[1][1]==grille[2][2] and grille[2][2]==grille[3][3] and grille[3][3]==grille[4][4] and grille[4][4]!=0:
            if grille[2][2]==1:
                return self.victoire()
            else:
                return self.defaite()
        elif grille[1][2]==grille[2][3] and grille[2][3]==grille[3][4] and grille[3][4]==grille[4][5] and grille[4][5]!=0:
            if grille[2][2]==1:
                return self.victoire()
            else:
                return self.defaite()
        elif grille[2][0]==grille[3][1] and grille[3][1]==grille[4][2] and grille[4][2]==grille[5][4] and grille[5][4]!=0:
            if grille[2][0]==1:
                return self.victoire()
            else:
                return self.defaite()
        elif grille[2][1]==grille[3][2] and grille[3][2]==grille[4][3] and grille[4][3]==grille[5][4] and grille[5][4]!=0:
            if grille[2][1]==1:
                return self.victoire()
            else:
                return self.defaite()
        elif grille[2][2]==grille[3][3] and grille[3][3]==grille[4][4] and grille[4][4]==grille[5][5] and grille[5][5]!=0:
            if grille[2][2]==1:
                return self.victoire()
            else:
                return self.defaite()
        self.joue=False
        self.jeu()


    def victoire(self):#N
       return self.afficher_message("Victoire !","green","white")
    
    def defaite(self):#N
        return self.afficher_message("Défaite !","red","white")
    
    def afficher_message(self,message,couleur_fond,couleur_texte):#N
        screen = Screen()
        screen.title(message)
        screen.bgcolor(couleur_fond)

        t = Turtle()
        t.hideturtle()
        t.penup()
        t.color(couleur_texte)
        
        t.goto(0,0)
        t.write(message,align="center",font=("Arial",40,"bold"))
        screen.exitonclick()

    
    def colorier_fond(self):#N
        up()
        goto(-270, 280)  
        bgcolor("#0000CD")
        begin_fill()
        down()
        for _ in range(4):
            forward(470)
            right(90)
            end_fill()
            

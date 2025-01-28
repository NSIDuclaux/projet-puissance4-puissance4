from turtle import *
from fonction_grille import *

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
        self.joueur = self.joueur2
        self.colone = 0
        speed(200)
        afficher()

    def joueur_actif(self):
        if self.joueur == self.joueur1:
            return self.joueur2
        else:
            return self.joueur1

    def jeu(self):
        self.afficher(self.grille)
        self.joueur=self.joueur_actif()
        self.colone = self.x()
        self.grille[self.colone][self.hauteur(self.grille,self.colone)]=self.joueur
        self.verif_ligne(self.grille)
    

    def verif_ligne(self,grille):
        for k in range(6):
            if grille[k][3]!=0:
                if grille[k][0]==grille[k][1] and grille[k][1]==grille[k][2] and grille[k][2]==grille[k][3]:
                    print("Victoire")
                    return "fini"
                elif grille[k][1]==grille[k][2] and grille[k][2]==grille[k][3] and grille[k][3]==grille[k][4]:
                    print("Vicotire")
                    return "fini"
                elif grille[k][5]==grille[k][4] and grille[k][2]==grille[k][3] and grille[k][3]==grille[k][4]:
                    print("Vicotire") 
                    return "fini"      
        self.verif_colone(self.grille)
    
    def verif_colone(self,grille):
        for k in range(6):
            if grille[3][k]!=0 :
                if grille[0][k]==grille[1][k] and grille[1][k]==grille[2][k] and grille[2][k]==grille[3][k] :
                    print("Victoire")
                    return "fini"
                elif grille[1][k]==grille[2][k] and grille[2][k]==grille[3][k] and grille[3][k]==grille[4][k]:
                    print("Victoire")
                    return "fini"
                elif grille[5][k]==grille[4][k] and grille[2][k]==grille[3][k] and grille[3][k]==grille[4][k] :
                    print("Victoire")
                    return "fini"
        self.verif_diago_croi(self.grille)


    def verif_diago_croi(self,grille):
        
        if grille[0][2]==grille[1][3] and grille[1][3]==grille[2][4] and grille[2][4]==grille[3][5] and grille[3][5]!=0:
            print("Victoire")
            return "Victoire"
        elif grille[0][1]==grille[1][2] and grille[1][2]==grille[2][3] and grille[2][3]==grille[3][4] and grille[3][4]!=0:
            print("Victoire")
            return "Victoire"
        elif grille[0][0]==grille[1][1] and grille[1][1]==grille[2][2] and grille[2][2]==grille[3][3] and grille[3][3]!=0:
            print("Victoire")
            return "Victoire"
        elif grille[1][0]==grille[2][1] and grille[2][1]==grille[3][2] and grille[3][2]==grille[4][3] and grille[4][3]!=0:
            print("Victoire")
            return "Victoire"
        elif grille[1][1]==grille[2][2] and grille[2][2]==grille[3][3] and grille[3][3]==grille[4][4] and grille[4][4]!=0:
            print("Victoire")
            return "Victoire"
        elif grille[1][2]==grille[2][3] and grille[2][3]==grille[3][4] and grille[3][4]==grille[4][5] and grille[4][5]!=0:
            print("Victoire")
            return "Victoire"
        elif grille[2][0]==grille[3][1] and grille[3][1]==grille[4][2] and grille[4][2]==grille[5][4] and grille[5][4]!=0:
            print("Victoire")
            return "Victoire"
        elif grille[2][1]==grille[3][2] and grille[3][2]==grille[4][3] and grille[4][3]==grille[5][4] and grille[5][4]!=0:
            print("Victoire")
            return "Victoire"
        elif grille[2][2]==grille[3][3] and grille[3][3]==grille[4][4] and grille[4][4]==grille[5][5] and grille[5][5]!=0:
            print("Victoire")
            return "Victoire"
        self.verif_diago_decroi(self.grille)

    def verif_diago_decroi(self,grille): 
        if grille[0][3]==grille[1][2] and grille[1][2]==grille[2][1] and grille[2][1]==grille[3][0] and grille[3][0]!=0 :
            print("Victoire")
            return "Victoire"
        elif grille[0][1]==grille[1][2] and grille[1][2]==grille[2][3] and grille[2][3]==grille[3][4] and grille[3][4]!=0:
            print("Victoire")
            return "Victoire"
        elif grille[0][0]==grille[1][1] and grille[1][1]==grille[2][2] and grille[2][2]==grille[3][3]and grille[3][3]!=0:
            print("Victoire")
            return "Victoire"
        elif grille[1][0]==grille[2][1] and grille[2][1]==grille[3][2] and grille[3][2]==grille[4][3] and grille[4][3]!=0:
            print("Victoire")
            return "Victoire"
        elif grille[1][1]==grille[2][2] and grille[2][2]==grille[3][3] and grille[3][3]==grille[4][4] and grille[4][4]!=0:
            print("Victoire")
            return "Victoire"
        elif grille[1][2]==grille[2][3] and grille[2][3]==grille[3][4] and grille[3][4]==grille[4][5] and grille[4][5]!=0:
            print("Victoire")
            return "Victoire"
        elif grille[2][0]==grille[3][1] and grille[3][1]==grille[4][2] and grille[4][2]==grille[5][4] and grille[5][4]!=0:
            print("Victoire")
            return "Victoire"
        elif grille[2][1]==grille[3][2] and grille[3][2]==grille[4][3] and grille[4][3]==grille[5][4] and grille[5][4]!=0:
            print("Victoire")
            return "Victoire"
        elif grille[2][2]==grille[3][3] and grille[3][3]==grille[4][4] and grille[4][4]==grille[5][5] and grille[5][5]!=0:
            print("Victoire")
            return "Victoire"
        self.joue=False
        self.jeu()

    
    def hauteur(self,grille,colone):
        for k in range (len(grille)):
            if grille[colone][k]==0:
                return k
    def afficher(self, grille):
        print(grille)
    def x(self):
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
        else x==6:
            colone=5
            return colone
        

teste=Puissance4()
teste.jeu()

            

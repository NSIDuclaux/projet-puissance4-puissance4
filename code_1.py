class Puissance4():

    def __init__(self):
        self.joueur1=1
        self.joueur2=2
        self.grille=[]
        self.joueur=self.joueur1
    def grille(self):
        self.grille=[
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0]
        ]
    def joueur_actif(self):
        if self.joueur==self.joueur1:
            return self.joueur2
        else:
            return self.joueur1

    def jeu(self):
        afficher()
        self.joueur=joueur_actif()
        colone=eval(input("Numero colone?"))
        self.grille[colone][hauteur(self.grille,colone)]=self.joueur
        afficher()
        verif_ligne()
        verif_colone()
        

    def verif_colone(self,grille):
        for k in range(6):
            if self.grille[k][0]==self.grille[k][1] and self.grille[k][1]==self.grille[k][2] and self.grille[k][2]==self.grille[k][3] and self.grille[k][3]==self.grille[k][4]:
                return "Victoire"
            elif self.grille[k][1]==self.grille[k][2] and self.grille[k][2]==self.grille[k][3] and self.grille[k][3]==self.grille[k][4] and self.grille[k][4]==self.grille[k][5]:
                return "Vicotire"
            elif self.grille[k][5]==self.grille[k][6] and self.grille[k][2]==self.grille[k][3] and self.grille[k][3]==self.grille[k][4] and self.grille[k][4]==self.grille[k][5]:
                return "Vicotire"
            else:
                return jeu()
    def verif_ligne(self,grille):
        for k in range(6):
            if grille[0][k]==grille[1][k] and grille[1][k]==grille[2][k] and grille[2][k]==grille[3][k] and grille[3][k]==grille[4][k]:
                return "Victoire"
            elif grille[1][k]==grille[2][k] and grille[2][k]==grille[3][k] and grille[3][k]==grille[4][k] and grille[4][k]==grille[5][k]:
                return "Vicotire"
            elif grille[5][k]==grille[6][k] and grille[2][k]==grille[3][k] and grille[3][k]==grille[4][k] and grille[4][k]==grille[5][k]:
                return "Vicotire"
            else:
                return jeu()
    
    def hauteur(self,grille,colone):
        for k in range (len(grille)):
            if grille[colone][k]==0:
                return k
    def afficher(self,grille):
        print(grille)
        


teste=Puissance4()
teste.jeu()
            




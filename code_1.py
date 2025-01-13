class Puissance4:

 def __init__(self):
       self.joueur1=1
       self.joueur2=2
       self.grille=grille
       self.joueur=self.joueur1
joueur=joueur1
def grille(self):
    self.grille=[
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0]
    ]
def joueur_actif(self,joueur):
    if joueur==joueur1:
        return joueur2
    else:
        return joueur1

def jeu(self,joueur):
    joueur=joueur_actif(joueur)
    colone=eval(input("Numero colone?"))
    grille[colone][hauteur()]=joueur
    verif_ligne()
    verif_colone()

def verif_colone(self,grille):
    for k in range(6):
        if grille[k][0]==grille[k][1] and grille[k][1]==grille[k][2] and grille[k][2]==grille[k][3] and grille[k][3]==grille[k][4]:
            return "Victoire"
        elif grille[k][1]==grille[k][2] and grille[k][2]==grille[k][3] and grille[k][3]==grille[k][4] and grille[k][4]==grille[k][5]:
            return "Vicotire"
        elif grille[k][5]==grille[k][6] and grille[k][2]==grille[k][3] and grille[k][3]==grille[k][4] and grille[k][4]==grille[k][5]:
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
def hauteur(self,grille,):
    for k in range (len(grille))
        




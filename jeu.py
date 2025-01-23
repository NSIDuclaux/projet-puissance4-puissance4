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
        self.joueur=self.joueur2

    def joueur_actif(self):
        if self.joueur==self.joueur1:
            return self.joueur2
        else:
            return self.joueur1

    def jeu(self):
        self.afficher(self.grille)
        self.joueur=self.joueur_actif()
        colone=eval(input("Numero colone?"))
        self.grille[colone][self.hauteur(self.grille,colone)]=self.joueur
        self.verif_colone(self.grille)
        

    def verif_colone(self,grille):
        for k in range(6):
            if grille[k][3]!=0:
                if grille[k][0]==grille[k][1] and grille[k][1]==grille[k][2] and grille[k][2]==grille[k][3] and grille[k][3]==grille[k][4]:
                    print("Victoire")
                    return "fini"
                elif grille[k][1]==grille[k][2] and grille[k][2]==grille[k][3] and grille[k][3]==grille[k][4] and grille[k][4]==grille[k][5]:
                    print("Vicotire")
                    return "fini"
                elif grille[k][5]==grille[k][6] and grille[k][2]==grille[k][3] and grille[k][3]==grille[k][4] and grille[k][4]==grille[k][5]:
                    print("Vicotire") 
                    return "fini"      
        self.verif_ligne(self.grille)
    
    def verif_ligne(self,grille):
        for k in range(6):
            if grille[3][k]!=0 :
                if grille[0][k]==grille[1][k] and grille[1][k]==grille[2][k] and grille[2][k]==grille[3][k] and grille[3][k]==grille[4][k]:
                    print("Victoire")
                    return "fini"
                elif grille[1][k]==grille[2][k] and grille[2][k]==grille[3][k] and grille[3][k]==grille[4][k] and grille[4][k]==grille[5][k]:
                    print("Victoire")
                    return "fini"
                elif grille[5][k]==grille[6][k] and grille[2][k]==grille[3][k] and grille[3][k]==grille[4][k] and grille[4][k]==grille[5][k]:
                    print("Victoire")
                    return "fini"
        self.verif_diago_croi(self.grille)
    def verif_diago_croi(self,grille):def verif_diago_croi(self,grille):
        if grille[0][2]==grille[1][3] and grille[1][3]==grille[2][4] and grille[2][4]==grille[3][5]:
            print("Victoire")
            return "Victoire"
        elif grille[0][1]==grille[1][2] and grille[1][2]==grille[2][3] and grille[2][3]==grille[3][4]:
            print("Victoire")
            return "Victoire"
        elif grille[0][0]==grille[1][1] and grille[1][1]==grille[2][2] and grille[2][2]==grille[3][3]:
            print("Victoire")
            return "Victoire"
        elif grille[1][0]==grille[2][1] and grille[2][1]==grille[3][2] and grille[3][2]==grille[4][3]:
            print("Victoire")
            return "Victoire"
        elif grille[1][1]==grille[2][2] and grille[2][2]==grille[3][3] and grille[3][3]==grille[4][4]:
            print("Victoire")
            return "Victoire"
        elif grille[1][2]==grille[2][3] and grille[2][3]==grille[3][4] and grille[3][4]==grille[4][5]:
            print("Victoire")
            return "Victoire"
        elif grille[2][0]==grille[3][1] and grille[3][1]==grille[4][2] and grille[4][2]==grille[5][4]:
            print("Victoire")
            return "Victoire"
        elif grille[2][1]==grille[3][2] and grille[3][2]==grille[4][3] and grille[4][3]==grille[5][4]:
            print("Victoire")
            return "Victoire"
        elif grille[2][2]==grille[3][3] and grille[3][3]==grille[4][4] and grille[4][4]==grille[5][5]:
            print("Victoire")
            return "Victoire"
    self.verif_diago_decroi(self.grille)

    def veif_diago_decroi(self,grille):
        #modifier les valeurs 
        if grille[0][2]==grille[1][3] and grille[1][3]==grille[2][4] and grille[2][4]==grille[3][5]:
            print("Victoire")
            return "Victoire"
        elif grille[0][1]==grille[1][2] and grille[1][2]==grille[2][3] and grille[2][3]==grille[3][4]:
            print("Victoire")
            return "Victoire"
        elif grille[0][0]==grille[1][1] and grille[1][1]==grille[2][2] and grille[2][2]==grille[3][3]:
            print("Victoire")
            return "Victoire"
        elif grille[1][0]==grille[2][1] and grille[2][1]==grille[3][2] and grille[3][2]==grille[4][3]:
            print("Victoire")
            return "Victoire"
        elif grille[1][1]==grille[2][2] and grille[2][2]==grille[3][3] and grille[3][3]==grille[4][4]:
            print("Victoire")
            return "Victoire"
        elif grille[1][2]==grille[2][3] and grille[2][3]==grille[3][4] and grille[3][4]==grille[4][5]:
            print("Victoire")
            return "Victoire"
        elif grille[2][0]==grille[3][1] and grille[3][1]==grille[4][2] and grille[4][2]==grille[5][4]:
            print("Victoire")
            return "Victoire"
        elif grille[2][1]==grille[3][2] and grille[3][2]==grille[4][3] and grille[4][3]==grille[5][4]:
            print("Victoire")
            return "Victoire"
        elif grille[2][2]==grille[3][3] and grille[3][3]==grille[4][4] and grille[4][4]==grille[5][5]:
            print("Victoire")
            return "Victoire"
    
    def hauteur(self,grille,colone):
        for k in range (len(grille)):
            if grille[colone][k]==0:
                return k
    
    def afficher(self,grille):
        print(grille)
        


teste=Puissance4()
teste.jeu()
            

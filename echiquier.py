from pieces import *
from config import *

class Echiquier:
    def __init__(self):
        
        Cn = Cavalier('noir')
        Cb = Cavalier('blanc')
        Fn = Fou('noir')
        Fb = Fou('blanc')
        Tn = Tour('noir')
        Tb = Tour('blanc')
        Dn = Dame('noir')
        Db = Dame('blanc')
        Rn = Roi('noir')
        Rb = Roi('blanc')
        Pn = Pion('noir')
        Pb = Pion('blanc')
        O = Vide()

        self.case_vide = O
              
        self.tab = [[Tb,Cb,Fb,Db,Rb,Fb,Cb,Tb],
                    [Pb,Pb,Pb,Pb,Pb,Pb,Pb,Pb],
                    [O ,O ,O ,O ,O ,O ,O ,O ],
                    [O ,O ,O ,O ,O ,O ,O ,O ],
                    [O ,O ,O ,O ,O ,O ,O ,O ],
                    [O ,O ,O ,O ,O ,O ,O ,O ],
                    [Pn,Pn,Pn,Pn,Pn,Pn,Pn,Pn],
                    [Tn,Cn,Fn,Dn,Rn,Fn,Cn,Tn]]
    
    def __repr__(self):
        return str(self.tab[7])+'\n'+str(self.tab[6])+'\n'+str(self.tab[5])+'\n'+str(self.tab[4])+'\n'+str(self.tab[3])+'\n'+str(self.tab[2])+'\n'+str(self.tab[1])+'\n'+str(self.tab[0])+'\n'
        
    #Cette fonction transforme une position sur l'écran (en pixels) en position sur l'échiquier
    def projectionEchiquier(self, pos = ()):
    
        (x,y) = pos

        i = int(x/TAILLE_CASE)
        j = 7-int((y - ORIGINE_Y)/TAILLE_CASE)

        return (i,j)

    #Cette fonction transforme une position sur l'échiquier en position sur l'écran
    def projectionEcran(self, pos =()):

        (i,j) = pos

        x = (i+0.5) * TAILLE_CASE
        y = ORIGINE_Y + (7-j+0.5) * TAILLE_CASE

        return(x,y)

    #Cette fonction retourne la liste des mouvements possibles en utilisant les libertés + les restrictions générales
    def mouvPossibles(self, case_i =()):

        mouvements_possibles=[]
        (i,j) = case_i
        piece = self.tab[j][i]

        #Libertés
        if piece.estPiece():
            mouvements_possibles = piece.libertes(case_i, self.tab)
        
        #Restrictions générales (communes à toutes les pièces)
        i = 0
        while i < len(mouvements_possibles):
 
            (xf,yf) = mouvements_possibles[i]
   
            #Prise d'un roi
            if self.tab[yf][xf].nom == 'Roi':
                mouvements_possibles.pop(i)
   
            else :
                i+=1

        return mouvements_possibles
    
    #Cette fonction permet de réaliser un déplacement si il est possible
    def deplacerPiece(self, case_i =(), case_f =()):

        self.tab[case_f[1]][case_f[0]] = self.tab[case_i[1]][case_i[0]]
        self.tab[case_i[1]][case_i[0]] = self.case_vide


        



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

    def estEchec(self, couleur):
        
        #Menaces totales des ennemis
        menaces_ennemies = []
        for ligne in range(8):
            for colonne in range(8):
                
                piece = self.tab[ligne][colonne]
                pos = (colonne,ligne)
        
                if piece.estPiece():
                    if piece.couleur != couleur:
                        menaces_ennemies += piece.menaces(pos, self.tab)
                    elif piece.nom == 'Roi':
                        pos_roi = pos
   
        if pos_roi in menaces_ennemies:
            return True
        else:
            return False
    
    def estMat(self, couleur):
        
        #Position du roi
        for ligne in range(8):
            for colonne in range(8):
                
                piece = self.tab[ligne][colonne]
                pos = (colonne,ligne)
        
                if piece.estPiece():
                    if piece.nom == 'Roi' and piece.couleur == couleur:
                        pos_roi = pos

        mouv_roi = self.mouvPossibles(pos_roi)

        if mouv_roi == []:
            return True
        else:
            return False

    def estPat(self, couleur):
        
        for ligne in range(8):
            for colonne in range(8):
                
                piece = self.tab[ligne][colonne]
                pos = (colonne,ligne)
                
                if piece.estPiece():
                    if piece.couleur == couleur:
                        for each in self.mouvPossibles(pos):
                            if self.estMouvementLegal(pos, each):
                                return False

        return True

    #Cette fonction teste si un mouvement est legal (ne mene pas a l'echec)
    def estMouvementLegal(self, pos_i=(), pos_f=()):
        
        (xi,yi) = pos_i
        (xf,yf) = pos_f
        piece = self.tab[yi][xi]
        
        #On sauvegarde la piece à la position finale
        piece_sauvee = self.tab[yf][xf]
        
        #On fait le déplacement
        self.tab[yf][xf] = piece
        self.tab[yi][xi] = self.case_vide
        
        if self.estEchec(piece.couleur):
            sortie = False
        else :
            sortie = True
            
        #On remet le tableau dans sa forme initiale
        self.tab[yf][xf] = piece_sauvee
        self.tab[yi][xi] = piece
        
        return sortie

    
    #Cette fonction retourne la liste des mouvements possibles en utilisant les libertés + les restrictions générales
    def mouvPossibles(self, case_i =()):
  
        mouvements_possibles=[]
        
        (x,y) = case_i
        piece = self.tab[y][x]

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

            #Mouvement menant à un échec
            elif not self.estMouvementLegal(case_i, mouvements_possibles[i]):
                mouvements_possibles.pop(i)

            else:
                i+=1
  
        return mouvements_possibles

        
        



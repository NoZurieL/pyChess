from jeu import Jeu
from pieces import *
from config import *
import math

class IA:
    def __init__(self, couleur = ''):
        
        self.heuristique = 0
        self.couleur = couleur
    
    #Cette fonction permet d'évaluer un état de jeu, plus l'heuristique est élevé plus l'IA est en position de force
    def evaluer(self, jeu = Jeu()):

        tab = jeu.echiquier.tab
        heuristique = 0

        #On comptabilise les pièces de l'échiquier
        for ligne in tab:
            for piece in ligne:
  
                if isinstance(piece, Pion):
                    if self.couleur == piece.couleur:
                        heuristique += 10
                    else:
                        heuristique -= 10

                if isinstance(piece, Cavalier) or isinstance(piece, Fou):
                    if self.couleur == piece.couleur:
                        heuristique += 30
                    else:
                        heuristique -= 30
            
                if isinstance(piece, Tour):
                    if self.couleur == piece.couleur:
                        heuristique += 50
                    else:
                        heuristique -= 50
                
                if isinstance(piece, Dame):
                    if self.couleur == piece.couleur:
                        heuristique += 90
                    else:
                        heuristique -= 90

        #On vérifie une potentielle victoire ou défaite de l'IA
        if self.couleur == 'blanc':
            if jeu.echiquier.estEchec('noir') and jeu.echiquier.estMat('noir'):
                heuristique += 900
            if jeu.echiquier.estEchec('blanc') and jeu.echiquier.estMat('blanc'):
                heuristique -= 900
        else:
            if jeu.echiquier.estEchec('noir') and jeu.echiquier.estMat('noir'):
                heuristique -= 900
            if jeu.echiquier.estEchec('blanc') and jeu.echiquier.estMat('blanc'):
                heuristique += 900
        
        return heuristique
    
    #Programme de calcul à une certaine profondeur de l'IA
    def minimax(self, jeu = Jeu(), profondeur = 0):
   
        if profondeur == 0 or jeu.running == False: #Si on a atteint la profondeur max OU le jeu est fini
            heuristique = self.evaluer(jeu)
            return heuristique
        
        mouv_totaux = jeu.echiquier.mouvTotaux(jeu.trait) #mouvements totaux du joueur qui a le trait
        print(profondeur)

        if jeu.trait == self.couleur: #Si c'est au tour de l'IA : on maximise l'heuristique
            heuristique = -math.inf
            for each in mouv_totaux: #Pour chaque mouvement possible :
                jeu.deplacerPiece(each[0],each[1]) #on fait le mouvement
                heuristique = max(heuristique, self.minimax(jeu, profondeur-1)) #maximise l'heuristique
            
        else: #C'est au tour du joueur : on minimise l'heuristique
            heuristique = math.inf
            for each in mouv_totaux: #Pour chaque mouvement possible :
                jeu.deplacerPiece(each[0],each[1]) #on fait le mouvement
                heuristique = min(heuristique, self.minimax(jeu, profondeur-1)) #minimise l'heuristique
        
        return heuristique
    
    #Programme d'action de l'IA
    def actionIA(self, jeu = Jeu()):
        
        #Sauvegarde de l'état initial du jeu
        tab_static = [[],[],[],[],[],[],[],[]]
        for ligne in range(8):
            for colonne in range(8):
                tab_static[ligne].append(jeu.echiquier.tab[ligne][colonne])
        
        #Calcul tactique
        self.heuristique = self.minimax(jeu, PROFONDEUR_IA)

        #Remise à l'état initial (comme si l'IA n'avait rien fait)
        jeu.running = True
        jeu.defaite = {'blanc': False, 'noir': False}
        jeu.trait = self.couleur
        for ligne in range(8):
            for colonne in range(8):
                jeu.echiquier.tab[ligne][colonne] = tab_static[ligne][colonne]
        
        #On effectue le déplacement qui mène au meilleur heuristique
        jeu.passerTrait()
        print(self.heuristique)
            
import pygame
from echiquier import Echiquier
from config import *

#Le jeu contient un échiquier et gère les règles du jeu (tour, score, rapport de partie,...)
class Jeu: 
    def __init__(self):
        
        self.echiquier = Echiquier()
        self.horloge = pygame.time.Clock()
        self.trait = 'blancs'
        self.score_noir = 0
        self.score_blanc = 0

    def estEchec(self, couleur_roi):
        mouvements_ennemis = []
        for ligne in range(8):
            for colonne in range(8):
                
                piece = self.echiquier.tab[ligne][colonne]
                pos_piece = (colonne,ligne)
        
                if piece.estPiece():
                    if piece.couleur != couleur_roi:
                        
                        mouvements_ennemis += piece.libertes(pos_piece,self.echiquier.tab)
                    
                    elif piece.nom == 'Roi':
                        
                        pos_roi = pos_piece
                            
        if pos_roi in mouvements_ennemis:
            return True
        else :
            return False
        
        
                        
        
from jeu import Jeu
from pieces import *
from config import *

class IA:
    def __init__(self, couleur = ''):
        
        self.heuristique = 0
        self.couleur = couleur
    
    #Cette fonction permet d'évaluer un état de jeu
    def evaluer(self, tab):

        self.heuristique = 0

        for ligne in tab:
            for piece in ligne:
  
                if isinstance(piece, Pion):
                    if self.couleur == piece.couleur:
                        self.heuristique += 10
                    else:
                        self.heuristique -= 10

                if isinstance(piece, Cavalier) or isinstance(piece, Fou):
                    if self.couleur == piece.couleur:
                        self.heuristique += 30
                    else:
                        self.heuristique -= 30
            
                if isinstance(piece, Tour):
                    if self.couleur == piece.couleur:
                        self.heuristique += 50
                    else:
                        self.heuristique -= 50
                
                if isinstance(piece, Dame):
                    if self.couleur == piece.couleur:
                        self.heuristique += 90
                    else:
                        self.heuristique -= 90

                if isinstance(piece, Roi):
                    if self.couleur == piece.couleur:
                        self.heuristique += 900
                    else:
                        self.heuristique -= 900


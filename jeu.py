import pygame
from echiquier import Echiquier
from config import *

#Le jeu contient un échiquier et gère les règles du jeu (tour, score, rapport de partie,...)
class Jeu: 
    def __init__(self):
        
        self.echiquier = Echiquier()
        self.horloge = pygame.time.Clock()
        self.trait = 'blanc'
        self.score_noir = 0
        self.score_blanc = 0
    
    def passerTrait(self):

        if self.trait == 'blanc':
            self.trait = 'noir'
        else :
            self.trait = 'blanc'
    
    #Cette fonction permet de réaliser un déplacement si il est possible
    def deplacerPiece(self, case_i =(), case_f =()):

        if case_f in self.echiquier.mouvPossibles(case_i):
            
            piece = self.echiquier.tab[case_i[1]][case_i[0]]
            
            if self.trait == piece.couleur:
        
                self.echiquier.tab[case_f[1]][case_f[0]] = piece
                self.echiquier.tab[case_i[1]][case_i[0]] = self.echiquier.case_vide
                self.passerTrait()


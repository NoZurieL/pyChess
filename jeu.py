import pygame
from echiquier import Echiquier
from config import *
from pieces import *

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

            self.echiquier.tab[case_f[1]][case_f[0]] = piece
            self.echiquier.tab[case_i[1]][case_i[0]] = self.echiquier.case_vide
            self.evaluer_score()
            self.passerTrait()
    
    def evaluer_score(self):

        self.score_noir =39
        self.score_blanc=39
    

        for ligne in range(8):
            for colonne in range(8):

                piece = self.echiquier.tab[ligne][colonne]
                
                if  piece.estPiece():
                    if piece.couleur =='blanc':

                        if isinstance(piece,Pion):
                            self.score_noir -=1
                        


                        elif isinstance(piece,Dame):
                            self.score_noir -=9

                        elif isinstance(piece,Cavalier) or isinstance(piece,Fou):
                            self.score_noir -=3

                        elif isinstance(piece,Tour):
                            self.score_noir -=5

                    if piece.couleur =='noir':

                        if isinstance(piece,Pion):
                            self.score_blanc -=1

                        elif isinstance(piece,Dame):
                            self.score_blanc  -=9

                        elif isinstance(piece,Cavalier) or isinstance(piece,Fou):
                            self.score_blanc  -=3

                        elif isinstance(piece,Tour):
                            self.score_blanc  -=5
    
    def fichier_score(self):
        fichier = open("Score_partie.txt", "w")
        fichier.write("Le score final de la partie est:\n")
        fichier.write("Total des points pour les blancs: " + str(self.score_blanc) +"\n")
        fichier.write("Total des points pour les noirs: " + str(self.score_noir)+"\n")
        fichier.close()


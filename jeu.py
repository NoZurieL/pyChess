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
        self.score = {'blanc': 0, 'noir': 0}
        self.defaite = {'blanc': False, 'noir': False}
        self.pat = False
        self.running = True
    
    def passerTrait(self):

        if self.trait == 'blanc':
            self.trait = 'noir'
        else :
            self.trait = 'blanc'
    
    #Cette fonction permet de réaliser un déplacement si il est possible
    def deplacerPiece(self, case_i =(), case_f =()):

        if case_f in self.echiquier.mouvPossibles(case_i):
            
            piece = self.echiquier.tab[case_i[1]][case_i[0]]

            #Si c'est le premier mouvement du roi
            if isinstance(piece, Roi): 
                if piece.immobile: piece.immobile = False

            self.echiquier.tab[case_f[1]][case_f[0]] = piece
            self.echiquier.tab[case_i[1]][case_i[0]] = self.echiquier.case_vide
            self.evaluerScore()
            self.passerTrait()
            self.evaluerFin()
    
    #Cette fonction évalue le score des blancs et des noirs en fonction de la valeur de chaque pièce
    def evaluerScore(self):

        self.score['noir'] = 39
        self.score['blanc'] = 39

        for ligne in range(8):
            for colonne in range(8):

                piece = self.echiquier.tab[ligne][colonne]
                
                if  piece.estPiece():
                    for couleur in ['blanc', 'noir']:
                        if piece.couleur == couleur:    
                            if isinstance(piece,Pion):
                                self.score[couleur] -=1

                            elif isinstance(piece,Dame):
                                self.score[couleur]  -=9

                            elif isinstance(piece,Cavalier) or isinstance(piece,Fou):
                                self.score[couleur] -=3

                            elif isinstance(piece,Tour):
                                self.score[couleur] -=5
                            
    #Cette fonction permet d'evaluer la condition de fin de partie du joueur qui a le trait
    def evaluerFin(self):

        couleur = self.trait
        if self.echiquier.estMat(couleur):
            
            if self.echiquier.estEchec(couleur):
                self.defaite[couleur] = True
                self.running = False
            
            elif self.echiquier.estPat(couleur):
                self.pat = True
                self.running = False
    
    
    #Cette fonction crée un fichier .txt et écrit le score à l'intérieur
    def rapportPartie(self):
        fichier = open("Rapport_partie.txt", "w")
        fichier.write("Le score final de la partie est:\n")
        fichier.write("Total des points pour les blancs: " + str(self.score['blanc']) +"\n")
        fichier.write("Total des points pour les noirs: " + str(self.score['noir'])+"\n")
        fichier.close()


import pygame
from pieces import *
from echiquier import Echiquier
from config import *

#Cette classe gère le système de glisser/déposer
class Curseur():
    def __init__(self):

        self.pos_curseur = ()
        self.case_init = ()
        self.piece = Vide()
    
    #Mise à jour de la position du curseur
    def update(self, pos=()):
        self.pos_curseur = pos
    
    #On prend une pièce du tableau et on la met dans le curesur
    def prendrePiece(self, ech = Echiquier(), case_piece = ()):

        self.case_init = case_piece
        (i,j) = case_piece
        piece_choisie = ech.tab[j][i]
        
        if piece_choisie.estPiece():

            self.piece = piece_choisie
            ech.tab[j][i] = ech.case_vide

    #On pose la pièce sélectionnée
    def poserPiece(self, ech = Echiquier(), case_finale = ()):
        
        if self.piece.estPiece():
            if case_finale in self.piece.libertes(self.case_init, ech.tab):
                            
                ech.tab[case_finale[1]][case_finale[0]] = self.piece

            else:

                ech.tab[self.case_init[1]][self.case_init[0]] = self.piece

            self.piece = Vide()


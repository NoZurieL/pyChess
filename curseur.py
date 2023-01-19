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
        self.mouv_possibles = []
    
    #Mise à jour de la position du curseur
    def update(self, pos=()):
        self.pos_curseur = pos
    
    #On prend une pièce et on la copie dans le curseur : Elle sera affichée sur le curseur
    def prendrePiece(self, ech = Echiquier(), case_piece = ()):

        self.case_init = case_piece
        (i,j) = case_piece
        piece_choisie = ech.tab[j][i]
        
        #Si c'est une pièce, on la récupère + on récupère les libertés
        if piece_choisie.estPiece():

            self.piece = piece_choisie
            self.mouv_possibles = ech.mouvPossibles(self.case_init)

    #On pose la pièce sélectionnée : On effectue le déplacement dans l'échiquier
    def poserPiece(self, ech = Echiquier(), case_finale = ()):
        
        #On fait le déplacement uniquement s'il y a une pièce sélectionnée
        if self.piece.estPiece():

            if case_finale in self.mouv_possibles:

                ech.deplacerPiece(self.case_init, case_finale)
            
            self.piece = ech.case_vide
            self.case_init = ()


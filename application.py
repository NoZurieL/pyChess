import pygame
from jeu import Jeu
from curseur import Curseur
from config import *

#L'application contient une fenêtre dans laquelle on affiche un jeu, et un curseur
class Application:
    def __init__(self):

        self.ecran = pygame.display.set_mode((LARGEUR,HAUTEUR))        
        self.jeu = Jeu()
        self.curseur = Curseur()

        #Définition des paramètres de la fenêtre
        pygame.display.set_caption('pyChess')
        icone = pygame.image.load('assets/Cn.png')
        pygame.display.set_icon(icone)

    #Mise à jour de l'affichage
    def update(self):

        self.ecran.fill('gray20') #arrière-plan
        self.afficherPlateau()
        self.afficherPieces()
        self.afficherSelection()
                    
        #UPDATE
        pygame.display.update()

        #HORLOGE
        self.jeu.horloge.tick(FPS)
    
    #Cette fonction permet d'afficher les cases de l'échiquier
    def afficherPlateau(self):
        
        for j in range(8):
            for i in range(8):
                
                pos = (i,j)
                (x,y) = self.jeu.echiquier.projectionEcran(pos)

                if (i+j)%2 == 0:
                    couleur = COULEUR_CLAIRE
                else:
                    couleur = COULEUR_SOMBRE
                
                rect = pygame.Rect(x, y, TAILLE_CASE, TAILLE_CASE)
                rect.center = (x,y)
                pygame.draw.rect(self.ecran, couleur, rect)

    #Cette fonction permet d'afficher les pièces
    def afficherPieces(self):

        for j in range(8):
            for i in range(8):

                pos = (i,j)
                (x,y) = self.jeu.echiquier.projectionEcran(pos)
                piece = self.jeu.echiquier.tab[j][i]

                if piece.estPiece():

                    rect = piece.texture.get_rect(center=(x,y))
                    self.ecran.blit(piece.texture, rect)
    
    #Cette fonction affiche la pièce sélectionnée au lieu du curseur et on surligne les cases libres
    def afficherSelection(self):
    
        #Si une pièce est sélectionnée
        if self.curseur.piece.estPiece():
        
            #AFFICHAGE DES CASES LIBRES
            surf = pygame.Surface((TAILLE_CASE,TAILLE_CASE))
            surf.set_alpha(128) #Transparence
            surf.fill(COULEUR_LIBERTES)
            
            for pos in self.curseur.piece.libertes(self.curseur.case_init, self.jeu.echiquier.tab):
                
                (x,y) = self.jeu.echiquier.projectionEcran(pos)
                rect = surf.get_rect(center = (x,y))
                self.ecran.blit(surf, rect)
            
            #AFFICHAGE DE LA PIECE SELECTIONNEE
            rectangle_selec = self.curseur.piece.texture.get_rect(center = self.curseur.pos_curseur)
            self.ecran.blit(self.curseur.piece.texture, rectangle_selec) 
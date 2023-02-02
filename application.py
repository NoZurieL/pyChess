import pygame,sys
from jeu import Jeu
from curseur import Curseur
from ia import IA
from config import *

#L'application contient une fenêtre dans laquelle on affiche un jeu, et un curseur
class Application:
    def __init__(self):
            
        pygame.init()
        pygame.font.init()
        
        self.ecran = pygame.display.set_mode((LARGEUR,HAUTEUR))
        self.jeu = Jeu()
        self.curseur = Curseur()

        #Définition des paramètres de la fenêtre
        pygame.display.set_caption('pyChess')
        icone = pygame.image.load('assets/Cn.png')
        pygame.display.set_icon(icone)
        
        self.police = pygame.font.Font('fonts/retro.ttf', TAILLE_POLICE)
        

    #Fonction de mise à jour de l'application
    def run(self):
        
        echiquier = self.jeu.echiquier
        curseur = self.curseur
       
        #Boucle d'update, est appellée en continu
        while True :
            
            #EVENEMENTS
            for event in pygame.event.get():

                #Si l'event est la croix de fermeture de la fenêtre : on ferme la fenêtre ET le programme
                if event.type == pygame.QUIT:
                    self.jeu.fichier_score()
                    pygame.quit()
                    sys.exit()
                
                #Si on appuie sur le bouton gauche de la souris, le curseur prend la pièce
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                    case = echiquier.projectionEchiquier(event.pos)
                    if echiquier.tab[case[1]][case[0]].couleur == self.jeu.trait:
                        curseur.prendrePiece(echiquier, case)
                    
                    curseur.update(event.pos)
                    
                #Si on relâche le boutton gauche de la souris, le curseur pose la pièce
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    
                    case = echiquier.projectionEchiquier(event.pos)
                    curseur.poserPiece(self.jeu, case)

                #Si on bouge la souris et qu'une pièce est dans le cuseur, on met à jour la position du curseur
                if event.type == pygame.MOUSEMOTION and curseur.piece.estPiece():
                    curseur.update(event.pos)
                
            #AFFICHAGE
            self.ecran.fill(COULEUR_BANDEAU) #arrière-plan
            self.afficherPlateau()
            self.afficherPieces()
            self.afficherSelection()
            self.afficherBandeaux()
                    
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

                #On affiche toutes les pièces non vides sauf la pièce sélectionnée par le curseur
                if piece.estPiece() and self.curseur.case_init != pos:

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
            
            for pos in self.curseur.mouv_possibles:
                
                (x,y) = self.jeu.echiquier.projectionEcran(pos)
                rect = surf.get_rect(center = (x,y))
                self.ecran.blit(surf, rect)
            
            #AFFICHAGE DE LA PIECE SELECTIONNEE
            surface_selec = pygame.transform.scale(self.curseur.piece.texture, (ZOOM,ZOOM))
            rectangle_selec = surface_selec.get_rect(center = self.curseur.pos_curseur)
            self.ecran.blit(surface_selec, rectangle_selec)
            
    #Cette fonction affiche les bandeaux avec les informations
    def afficherBandeaux(self):
    
        #Traits
        surf_trait_blanc = self.police.render('Trait aux Blancs', False, 'white')
        rect_trait_blanc = surf_trait_blanc.get_rect()
        rect_trait_blanc.center = (LARGEUR/2, HAUTEUR-ORIGINE_Y/2) 
        
        surf_trait_noir = self.police.render('Trait aux Noirs', False, 'white')
        rect_trait_noir = surf_trait_noir.get_rect()
        rect_trait_noir.center = (LARGEUR/2, ORIGINE_Y/2)
        
        if self.jeu.trait == 'blanc':
            self.ecran.blit(surf_trait_blanc, rect_trait_blanc)
        elif self.jeu.trait == 'noir':
            self.ecran.blit(surf_trait_noir, rect_trait_noir)
        
        #Scores
        txt_score_blanc = 'Score : '+str(self.jeu.score_blanc)
        surf_score_blanc = self.police.render(txt_score_blanc, False, 'white')
        rect_score_blanc = surf_score_blanc.get_rect()
        rect_score_blanc.midleft = (5, HAUTEUR-ORIGINE_Y/2) 
        self.ecran.blit(surf_score_blanc, rect_score_blanc)
        
        txt_score_noir = 'Score : '+str(self.jeu.score_noir)
        surf_score_noir = self.police.render(txt_score_noir, False, 'white')
        rect_score_noir = surf_score_noir.get_rect()
        rect_score_noir.midleft = (5, ORIGINE_Y/2) 
        self.ecran.blit(surf_score_noir, rect_score_noir)

        
        
        
        
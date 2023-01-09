import pygame, sys
from echiquier import Echiquier
from config import *

#L'application englobe la fenêtre et ses fonctions d'affichage et de récupération des évènements
class Application:
    def __init__(self):

        pygame.init()

        self.ecran = pygame.display.set_mode((LARGEUR,HAUTEUR))
        self.horloge = pygame.time.Clock()
        self.echiquier = Echiquier()

        #Définition des paramètres de la fenêtre
        pygame.display.set_caption('pyChess')
        icone = pygame.image.load('assets/Cn.png')
        pygame.display.set_icon(icone)
        

    def run(self):
        
        piece_selec = False
       
        #Boucle d'update, est appellée en continu
        while True :
            
            #Pour chaque évènement (appui sur un bouton, etc...)
            for event in pygame.event.get():

                #Si l'event est la croix de fermeture de la fenêtre : on ferme la fenêtre ET le programme
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                #Si on effectue un clic gauche de la souris
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    
                    #Si c'est le premier clic 
                    if not piece_selec:
                        
                        pos_i = self.echiquier.transfertCoordonnes(event.pos)

                        if self.echiquier.tab[pos_i[1]][pos_i[0]].estPiece():
                            
                            piece_selec = True
                
                    #Si une pièce est sélectionnée, on veut déplacer la pièce à cet endroit
                    else:
                        
                        pos_f = self.echiquier.transfertCoordonnes(event.pos)

                        if pos_i == pos_f:
                            pass
                        else :
                            self.echiquier.deplacerPiece(pos_i, pos_f)
                            piece_selec = False

            #AFFICHAGE
            self.ecran.fill('gray20') #arrière-plan
            self.echiquier.afficherPlateau(self.ecran)
            self.echiquier.afficherPieces(self.ecran)
                
            #UPDATE
            pygame.display.update()

            #On force le jeu à tourner à 60 FPS (images par seconde)
            self.horloge.tick(FPS)


pyChess = Application()
pyChess.run()


        
import pygame, sys
from application import Application
from config import *

#Menu principal qui permet de lancer l'application
class Menu:
    def __init__(self, app = Application()):
        
        self.app = app

    #Fonction de mise à jour de l'application
    def run(self):
          
        #Boucle d'update, est appellée en continu
        while True :

            #BOUTTON
            boutton_jouer = pygame.Rect(0,0,200,50)
            boutton_jouer.center = (LARGEUR/2,HAUTEUR/2-ORIGINE_Y)
            
            #EVENEMENTS
            for event in pygame.event.get():

                #Si l'event est la croix de fermeture de la fenêtre : on ferme la fenêtre ET le programme
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                #Si on appuie sur le bouton jouer, l'application se lance
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if boutton_jouer.collidepoint(event.pos):
                        self.app.run()

            #AFFICHAGE
            self.app. ecran.fill(COULEUR_BG)

            dessin = pygame.image.load('assets/background.png')
            dessin = pygame.transform.scale(dessin,(LARGEUR,LARGEUR/1.25))
            rect_dessin = dessin.get_rect(bottomleft=(0,HAUTEUR))
            self.app.ecran.blit(dessin, rect_dessin)

            pygame.draw.rect(self.app.ecran, 'gray20', boutton_jouer)

            #UPDATE
            pygame.display.update()
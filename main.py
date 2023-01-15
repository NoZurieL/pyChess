import pygame, sys
from application import Application
from config import *

class Main:
    def __init__(self):

        pygame.init()
        self.app = Application()

    #Fonction de mise à jour de l'application
    def run(self):
        
        echiquier = self.app.jeu.echiquier
        curseur = self.app.curseur
       
        #Boucle d'update, est appellée en continu
        while True :
            
            #EVENEMENTS
            for event in pygame.event.get():

                #Si l'event est la croix de fermeture de la fenêtre : on ferme la fenêtre ET le programme
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                #Si on appuie sur le bouton gauche de la souris, le curseur prend la pièce
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                    case = echiquier.projectionEchiquier(event.pos)
                    curseur.prendrePiece(echiquier, case)
                    curseur.update(event.pos)
                    

                #Si on relâche le boutton gauche de la souris, le curseur pose la pièce
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    
                    case = echiquier.projectionEchiquier(event.pos)
                    curseur.poserPiece(echiquier, case)

                #Si on bouge la souris et qu'une pièce est dans le cuseur, on met à jour la position du curseur
                if event.type == pygame.MOUSEMOTION and curseur.piece.estPiece():
                    curseur.update(event.pos)
                
            #AFFICHAGE
            self.app.update()

if __name__ == '__main__' :
    
    pyChess = Main()
    pyChess.run()


        

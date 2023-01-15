import pygame
from config import *
#Ce fichier définit les classes de pièces, qui sont les objets composant l'échiquier.
#Chaque pièce a des propriétés différentes, comme son nom, sa couleur ou encore ses libertés de mouvement

class Piece:
    def __init__(self, nom, couleur):
        self.nom = nom
        self.couleur = couleur
        
        if self.estPiece():
            self.texture = pygame.image.load('assets/' + self.nom[0]+self.couleur[0]+'.png')
            self.texture = pygame.transform.scale(self.texture,(TAILLE_PIECE,TAILLE_PIECE))
        else:
            self.texture = None

    def __repr__(self):
        return str(self.nom[0]) + str(self.couleur[0])

    def estPiece(self):

        if self.nom != '0':
            return True
        else:
            return False


class Pion(Piece):

    def __init__(self, couleur):
        super().__init__('Pion', couleur)
        
      
    def libertes(self, pos=(), tab =[]):

        x = pos[0]
        y = pos[1]

        if self.couleur== 'noir':
            libertes = [(x,y+1), (x, y+2), (x-1,y+1), (x+1,y+1)]
            if y != 6:
                libertes.pop(1)
            
            
        elif self.couleur== 'blanc': 
            libertes = [(x,y-1), (x, y-2), (x-1,y-1), (x+1,y-1)]
            if y != 1:
                libertes.pop(1)

        return libertes

class Cavalier(Piece):

    def __init__(self, couleur):
        super().__init__('Cavalier', couleur)
    
    def libertes(self, pos=(), tab =[]):

        x = pos[0]
        y = pos[1]

        libertes = [(x-1,y+2),(x+1,y+2),(x+2,y+1),(x+2,y-1),(x+1,y-2),(x-1,y-2),(x-2,y-1),(x-2,y+1)]
        
        i = 0
        while i < len(libertes):
 
            xf = libertes[i][0]
            yf = libertes[i][1]
            
            if xf > 7 or xf < 0 or yf > 7 or yf < 0:
                libertes.pop(i)
                
            elif tab[yf][xf].couleur == self.couleur:
                libertes.pop(i)
            
            else :
                i+=1

        return libertes

class Fou(Piece):

    def __init__(self, couleur):
        super().__init__('Fou', couleur)
     
    def libertes(self, pos=(), tab =[]):

        x = pos[0]
        y = pos[1]

        libertes = []

        return libertes

class Tour(Piece):

    def __init__(self, couleur):
        super().__init__('Tour', couleur)
    
    def libertes(self, pos=(), tab =[]):

        x = pos[0]
        y = pos[1]

        libertes = []

        return libertes

class Roi(Piece):

    def __init__(self, couleur):
        super().__init__('Roi', couleur)
    
    def libertes(self, pos=(), tab =[]):

        x = pos[0]
        y = pos[1]

        libertes = []

        return libertes

class Dame(Piece):

    def __init__(self, couleur):
        super().__init__('Dame', couleur)
    
    def libertes(self, pos=(), tab =[]):

        x = pos[0]
        y = pos[1]

        libertes = []

        return libertes

class Vide(Piece):

    def __init__(self):
        super().__init__('0', ' ')
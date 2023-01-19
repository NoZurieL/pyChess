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

        (x,y) =pos 
        libertes =[]

        if tab[y][x].couleur== 'blanc':

            if (y+1)<=7 :
                if not tab[y+1][x].estPiece():
                    libertes.append((x,y+1))

                    if y == 1 and not tab[y+2][x].estPiece():
                        libertes.append((x,y+2))

            if (y+1)<=7 and (x-1)>=0:
                if tab[y+1][x-1].couleur =='noir':  
                    libertes.append((x-1,y+1)) 

            if (y+1)<=7 and (x+1)<=7:
                if tab[y+1][x+1].couleur =='noir':
                    libertes.append((x+1,y+1))
           
        elif tab[y][x].couleur== 'noir': 

            if (y-1)>=0:
                if not tab[y-1][x].estPiece():
                    libertes.append((x,y-1))

                if y == 6 and not tab[y-2][x].estPiece():
                    libertes.append((x,y-2))

            if (x-1)>=0 and (y-1)>=0 :
                if tab[y-1][x-1].couleur =='blanc':
                    libertes.append((x-1,y-1)) 

            if (x+1)<=7 and (y-1)>=0:
                if tab[y-1][x+1].couleur =='blanc':
                    libertes.append((x+1,y-1))

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
 
            (xf,yf) = libertes[i]
   
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
        
        (x,y) = pos
        libertes = []
        
        i = 1
        while (x+i)<=7 and (y+i)<=7:
            if tab[y+i][x+i].couleur != self.couleur:
                libertes.append((x+i,y+i))
                if not tab[y+i][x+i].estPiece():
                    i+=1
                else:
                    break
            else:
                break
        
        i = 1
        while (x+i)<=7 and (y-i)>=0:
            if tab[y-i][x+i].couleur != self.couleur :
                libertes.append((x+i,y-i))
                if not tab[y-i][x+i].estPiece():
                    i+=1
                else:
                    break
            else:
                break
        
        i = 1
        while (x-i)>=0 and (y-i)>=0:
            if tab[y-i][x-i].couleur != self.couleur :
                libertes.append((x-i,y-i))
                if not tab[y-i][x-i].estPiece():
                    i+=1
                else:
                    break
            else:
                break
                       
        i = 1
        while (x-i)>=0 and (y+i)<=7:
            if tab[y+i][x-i].couleur != self.couleur :
                libertes.append((x-i,y+i))
                if not tab[y+i][x-i].estPiece():
                    i+=1
                else:
                    break
            else:
                break
        
        return libertes

class Tour(Piece):

    def __init__(self, couleur):
        super().__init__('Tour', couleur)
    
    def libertes(self, pos=(), tab =[]):

        x = pos[0]
        y = pos[1]

        libertes = []
        
        i=1
        while x <= 7 and x >=0 and (y+i) <= 7:
            if not tab[y+i][x].estPiece() and tab[y+i][x].couleur == self.couleur :    
                libertes.append((x,y+i))  
                i+=1
            else:
                break
                
        while x <= 7 and x >=0 and (y-i) >= 0:
            if not tab[y-i][x].estPiece() and tab[y-i][x].couleur == self.couleur :    
                libertes.append((x,y-i))  
                i+=1
            else:
                break    
                
        while (x+i) <=7 and y <= 7 and y>=0:
            if not tab[y][x+i].estPiece() and tab[y][x+i].couleur == self.couleur :    
                libertes.append((x+i,y))  
                i+=1
            else:
                break    
        while (x-i) >=0 and y <= 7 and y>=0:
            if not tab[y][x-i].estPiece() and tab[y][x-i].couleur == self.couleur :    
                libertes.append((x-i,y))  
                i+=1
            else:
                break     
            
            

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

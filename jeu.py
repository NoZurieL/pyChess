import pygame
from echiquier import Echiquier
from config import *

#Le jeu contient un échiquier et gère les règles du jeu (tour, score, rapport de partie,...)
class Jeu: 
    def __init__(self):
        
        self.echiquier = Echiquier()
        self.horloge = pygame.time.Clock()
        self.trait = 'blancs'
        self.score_noir = 0
        self.score_blanc = 0


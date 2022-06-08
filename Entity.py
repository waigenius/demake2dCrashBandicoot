import pygame 
from pygame import * 


class Entity(pygame.sprite.Sprite): #Create the base visual for the sprite
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #Constructor for the sprite
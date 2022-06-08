import pygame 
from pygame import * 
from Entity import *



class Platform(Entity):    #Class to create the platform
    def __init__(self, x, y): # X and Y is the position of the platform
        Entity.__init__(self) #Inherit the class Entity which contain the sprite function
        self.image = pygame.image.load("assets/images/imagesPlateforme/grassDirtBlock.png").convert() #Load the image and convert it
        self.image = pygame.transform.scale(self.image,(16*3,16*3)) #Transform the size of the platform
        self.rect = Rect(x, y, 16*3, 16*3) #Create the rectangle for the platform

    def update(self): #Update onto the game:
        pass

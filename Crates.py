import pygame 
from pygame import * 
from Platform import *



class CrashBox(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = pygame.image.load("assets/images/boxes/boxCrash.png").convert_alpha()  # Load the image and convert it
        self.image = pygame.transform.scale(self.image, (16 * 3, 16 * 3))
        self.rect = Rect(x, y, 16 * 3, 16 * 3)
        self.lifeplus = 1

    def __del__(self):
        if self.lifeplus == 0:
            print("objet detruit ! ")

class DirtBlock(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = pygame.image.load("assets/images/imagesPlateforme/DirtBlock.png").convert_alpha()  # Load the image and convert it
        self.image = pygame.transform.scale(self.image, (16 * 3, 16 * 3))
        self.rect = Rect(x, y, 16 * 3, 16 * 3)


class WumpaBigBox(Platform): #Replace the name by WumpaBigBox
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = pygame.image.load("assets/images/boxes/boite2-1.png").convert_alpha()  # Load the image and convert it
        self.image = pygame.transform.scale(self.image, (16 * 3, 16 * 3))
        self.rect = Rect(x, y, 16 * 3, 16 * 3)
        self.wumpafruitplus = 10

    def __del__(self):
        print("objet detruit ! ")





class IronBox(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = pygame.image.load("assets/images/boxes/boxAcier.png").convert_alpha()  # Load the image and convert it
        self.image = pygame.transform.scale(self.image, (16 * 3, 16 * 3))
        self.rect = Rect(x, y, 16 * 3, 16 * 3)


class NitroBox(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = pygame.image.load("assets/images/boxes/boxNitro.png").convert_alpha()  # Load the image and convert it
        self.image = pygame.transform.scale(self.image, (16 * 3, 16 * 3))
        self.rect = Rect(x, y, 16 * 3, 16 * 3)
        self.damage = 1

class TntBox(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = pygame.image.load("assets/images/boxes/boxTNT.png").convert_alpha()  # Load the image and convert it
        self.image = pygame.transform.scale(self.image, (16 * 3, 16 * 3))
        self.rect = Rect(x, y, 16 * 3, 16 * 3)
        self.damage = 1


class ArrowBox(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = pygame.image.load("assets/images/boxes/boxFleche.png").convert_alpha()  # Load the image and convert it
        self.image = pygame.transform.scale(self.image, (16 * 3, 16 * 3))
        self.rect = Rect(x, y, 16 * 3, 16 * 3)

    def __del__(self):
        print("objet detruit ! ")

class Wumpa(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = pygame.image.load("assets/images/boxes/wumpa.png").convert_alpha()  # Load the image and convert it
        self.image = pygame.transform.scale(self.image, (16 * 3, 16 * 3))
        self.rect = Rect(x, y, 16 * 3, 16 * 3)
        self.wumpafruitplus = 1

    def __del__(self):
        if self.wumpafruitplus == 0:
            print("objet detruit ! ")


class AkuBox(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = pygame.image.load("assets/images/boxes/boxAku.png").convert_alpha()  # Load the image and convert it
        self.image = pygame.transform.scale(self.image, (16 * 3, 16 * 3))
        self.rect = Rect(x, y, 16 * 3, 16 * 3)
        self.lifePointAku = 1
    def __del__(self):
        if self.lifePointAku == 0:
            print("objet detruit ! ")


class WumpaSmallBox(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = pygame.image.load("assets/images/boxes/basicBox copy.png").convert_alpha()  # Load the image and convert it
        self.image = pygame.transform.scale(self.image, (16 * 3, 16 * 3))
        self.rect = Rect(x, y, 16 * 3, 16 * 3)
        self.wumpafruitplus = 5

    def __del__(self):
        if self.wumpafruitplus == 0:
            print("objet detruit ! ")






class Obstacle(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x , y )
        self.image = pygame.image.load("assets/images/obstacles/hole.png")
        self.image = pygame.transform.scale(self.image, (60, 20))
        self.rect = Rect(x, y, 32, 32)
        self.damage = 1

    def __del__(self):
            print("objet detruit ! ")



class ObstacleWater(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x , y )
        self.image = pygame.image.load("assets/images/obstacles/water.png")
        self.image = pygame.transform.scale(self.image, (100, 50))
        self.rect = Rect(x, y, 32, 32)

    def __del__(self):
            print("objet detruit ! ")

###" Fournir des images des obstacles
class ObstacleSpikePillar(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x , y )
        self.image = pygame.image.load("assets/images/obstacles/spikePillar.png")
        self.image = pygame.transform.scale(self.image, (16*3, 16*3))
        self.rect = Rect(x, y, 16*3, 16*3)

    def __del__(self):
            print("objet detruit ! ")




class Gagner(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = pygame.image.load("assets/images/imagesPlateforme/exit.png").convert_alpha()  # Load the image and convert it
        self.image = pygame.transform.scale(self.image, (16* 3, 16 * 3))
        self.rect = Rect(x, y, 16 * 3, 16 * 3)

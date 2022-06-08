import pygame
from pygame import *
from Entity import *
from Crates import *

class Akuaku (Entity):
    def __init__(self, name, life_points, xPos=300, yPos=300):
        Entity.__init__(self)
        self.name = name
        self.image= pygame.image.load("assets/images/imagesPlateforme/iconeAku.png")
        self.xvel = 0
        self.yvel = 0

        self.rect = Rect(xPos, yPos, 16 *4, 32*4) # Rectangle representant le globe qui contient l'image de Aku Aku

        self.life_points = life_points
        self.onGround = False  # Etre au sol
        self.faceright = True  # Etre droite
        self.airborne = True  # Etre en air
        self.attacking = False  # Etre attaquer
        self.counter = 0
        self.attackcounter = 0

    def update(self, up, down, left, right, attack, platforms):  # Update the movement with the condition

        #Permet à Aku Aku de Sauter
        if up:
            # only jump if on the ground
            if self.onGround:
                self.yvel -= 10   # Jump only if on ground decrement the position for y from the ground
                #self.aku.yvel -= 10


        if down: #Do Nothing
            pass
        # if attack: #Do spin attack with pressing space
        #     self.attack = False
        #     self.attacking = True
        if left: # setting the direction of left using negative x
            self.xvel = -7
            #self.faceright = False
        if right: # setting the direction of right using positive x
            self.xvel = 7
            #self.faceright = True
        if not self.onGround: #If in air
            # only accelerate with gravity if in the air
            self.yvel += 0.3   # starting y = negative adding positive to move player back down bit by bit (gravity)
            # max falling speed
            if self.yvel > 50: self.yvel = 50   # cannot fall faster than 100 pixels
        if not (left or right):
            self.xvel = 0        # if player not pressing left or right the falling positon 0 basically in the same positon
        if self.yvel < 0 or self.yvel > 1.2: self.airborne = True  # declare the state to airborn if y equal negative number or greater than 1.2 when in air

        self.rect.left += self.xvel
        # do x-axis collisions
        self.collide(self.xvel, 0, platforms)
        # increment in y direction
        self.rect.top += self.yvel
        # assuming we're in the air
        self.onGround = False
        # do y-axis collisions
        self.collide(0, self.yvel, platforms)
        return up or down or left or right or attack or platforms

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):

                if isinstance(p, CrashBox): # When crash interact with the box
                    p.kill() # Faire disparaître l'image san,
                    continue
                if isinstance(p, WumpaBigBox): # When crash interact with the box
                    p.kill()
                    continue

                if xvel > 0:
                    self.rect.right = p.rect.left

                if xvel < 0:
                    self.rect.left = p.rect.right

                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.airborne = False
                    self.yvel = 0

                if yvel < 0:
                    self.rect.top = p.rect.bottom
                # if self.aku == (self.rect.right or self.rect.left or self.rect.bottom or self.rect.top):
                #     self.aku = self.update(up,down,left,right,attack,platforms)
                #     print("HereAku")

    def _getname(self):
        return self.name

    def _getxposition(self):
        if self.xPos < 0:
            return "la valeur de la position {} est negative ".format(self.xPos)
        else:
            return self.xPos

    def _setxposition(self, position):
        if position < 0:
           self.position = 0
           self.xPos += position
        else:
           self.xPos = position

    def _getlife(self):
        if self.life_points < 0:
            self.life_points = 0
            return self.life_points
        else:
            return self.life_points

    def _setlife(self, life):
        if life < 0 and self.life_points >= life:
            self.life -=life
        else:
          self.life_points += life

    names = property(_getname)
    xpos= property(_getxposition, _setxposition)
    life = property(_getlife, _setlife)

pygame.quit()

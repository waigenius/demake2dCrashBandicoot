

from Entity import *
from Crates import *

spritesheet = pygame.image.load("assets/images/ennemies/crab.png")
spritesheet1 = pygame.image.load("assets/images/ennemies/skunk.png")

character = Surface((16,16),pygame.SRCALPHA)
character.blit(spritesheet1,(0,0))
character = pygame.transform.scale(character, (16*3,16*3))
skunk1 = character

character = Surface((48,48),pygame.SRCALPHA)
character.blit(spritesheet,(0,0))
character = pygame.transform.scale(character, (48,48))
crab = character

class crabe(Entity):
    def __init__(self,x,y):
        Entity.__init__(self)
        self.xvel = 1
        self.yvel = 0
        self.onGround = False
        self.destroyed = False
        self.counter = 0
        self.image = crab
        self.rect = Rect(x, y , 16*3 , 16*3)

    def update(self, platforms, entities):
        if not self.onGround:
            self.yvel += 0.3
            if self.yvel > 100: self.yvel = 100

        # increment in x direction
        self.rect.left += self.xvel
        # do x-axis collisions
        self.collide(self.xvel, 0, platforms, entities)
        # increment in y direction
        self.rect.top += self.yvel
        # assuming we're in the air
        self.onGround = False
        # do y-axis collisions
        self.collide(0, self.yvel, platforms, entities)

        self.animate()

    def collide(self, xvel, yvel, platforms, entities):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if xvel > 0:
                    self.rect.right = p.rect.left
                    self.xvel = -abs(xvel)

                if xvel < 0:
                    self.rect.left = p.rect.right
                    self.xvel = abs(xvel)

                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.airborne = False
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom

        for p in entities:
            if pygame.sprite.collide_rect(self, p):
                dif = p.rect.bottom - self.rect.top
                if dif <= 8:
                    self.destroyed = True
                    self.counter = 0
                    self.xvel = 0



    def animate(self):

        if not self.destroyed: self.walkloop()
        else: self.destroyloop()

    def walkloop(self):
        if self.counter == 10:
            self.updatecharacter(crab)
        elif self.counter == 20:
            self.updatecharacter(crab)
            self.counter = 0
        self.counter = self.counter + 1

    def destroyloop(self):
        if self.counter == 0:
            self.updatecharacter(crab)
        elif self.counter == 10: self.kill()
        self.counter = self.counter + 1

    def updatecharacter(self, ansurf):
        self.image = ansurf







class skunk(Entity):
    def __init__(self,x,y):
        Entity.__init__(self)
        self.xvel = 1
        self.yvel = 0
        self.onGround = False
        self.destroyed = False
        self.counter = 0
        self.image = skunk1
        self.rect = Rect(x, y , 16*3 , 16*3)

    def update(self, platforms, entities):
        if not self.onGround:
            self.yvel += 0.3
            if self.yvel > 100: self.yvel = 100

        # increment in x direction
        self.rect.left += self.xvel
        # do x-axis collisions
        self.collide(self.xvel, 0, platforms, entities)
        # increment in y direction
        self.rect.top += self.yvel
        # assuming we're in the air
        self.onGround = False
        # do y-axis collisions
        self.collide(0, self.yvel, platforms, entities)

        self.animate()

    def collide(self, xvel, yvel, platforms, entities):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if xvel > 0:
                    self.rect.right = p.rect.left
                    self.xvel = -abs(xvel)

                if xvel < 0:
                    self.rect.left = p.rect.right
                    self.xvel = abs(xvel)

                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.airborne = False
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom

        for p in entities:
            if pygame.sprite.collide_rect(self, p):
                dif = p.rect.bottom - self.rect.top
                if dif <= 8:
                    self.destroyed = True
                    self.counter = 0
                    self.xvel = 0



    def animate(self):

        if not self.destroyed: self.walkloop()
        else: self.destroyloop()

    def walkloop(self):
        if self.counter == 10:
            self.updatecharacter(skunk1)
        elif self.counter == 20:
            self.updatecharacter(skunk1)
            self.counter = 0
        self.counter = self.counter + 1

    def destroyloop(self):
        if self.counter == 0:
            self.updatecharacter(skunk1)
        elif self.counter == 10: self.kill()
        self.counter = self.counter + 1

    def updatecharacter(self, ansurf):
        self.image = ansurf
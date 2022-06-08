import pygame
from pygame import *
#from pygame.locals import *
import time, sys, random
from Entity import *
from Crates import *
from akuaku import *



#DECLARATION OF CRASH SPRITE
spritesheet = pygame.image.load("assets/images/personnages/spriteSheetCrash.png")

#Running right

character = Surface((15,32),pygame.SRCALPHA)
character.blit(spritesheet,(0,0))
character = pygame.transform.scale(character, (16*3,32*3))
Running1 = character

character = Surface((16,32),pygame.SRCALPHA)
character.blit(spritesheet,(-18,0))
character = pygame.transform.scale(character, (16*3,32*3))
Running2 = character

character = Surface((16,31),pygame.SRCALPHA)
character.blit(spritesheet,(-37,-1))
character = pygame.transform.scale(character, (16*3,32*3))
Running3 = character

character = Surface((16,32),pygame.SRCALPHA)
character.blit(spritesheet,(-55,0))
character = pygame.transform.scale(character, (16*3,32*3))
Running4 = character

character = Surface((16,31),pygame.SRCALPHA)
character.blit(spritesheet,(-73,-1))
character = pygame.transform.scale(character, (16*3,32*3))
Running5 = character

#Jumping
character = Surface((16,32),pygame.SRCALPHA)
character.blit(spritesheet,(-1,-145))
character = pygame.transform.scale(character, (16*3,32*3))
Jumping1 = character

character = Surface((16,32),pygame.SRCALPHA)
character.blit(spritesheet,(-20,-145))
character = pygame.transform.scale(character, (16*3,32*3))
Jumping2 = character


#Spining

character = Surface((16,32),pygame.SRCALPHA)
character.blit(spritesheet,(0,-73))
character = pygame.transform.scale(character, (16*3,32*3))
Spinning = character

character = Surface((16,32),pygame.SRCALPHA)
character.blit(spritesheet,(-19,-72))
character = pygame.transform.scale(character, (16*3,32*3))
Spinning2 = character

character = Surface((16,32),pygame.SRCALPHA)
character.blit(spritesheet,(-37,-73))
character = pygame.transform.scale(character, (16*3,32*3))
Spinning3 = character

character = Surface((16,32),pygame.SRCALPHA)
character.blit(spritesheet,(-56,-72))
character = pygame.transform.scale(character, (16*3,32*3))
Spinning4 = character

character = Surface((16,32),pygame.SRCALPHA)
character.blit(spritesheet,(-74,-73))
character = pygame.transform.scale(character, (16*3,32*3))
Spinning5 = character

    



class Crash(Entity):
    def __init__(self, name,x, y, life_points, damage=1, attack=0):
        Entity.__init__(self) # On initialise la classe parente de Crash
        
        self.name = name
        #self.crash = pygame.image.load("Droite.png")
        self.life_points = life_points
        self.damage = damage
        self.attack = attack
        self.rect = Rect(x, y, 16 * 3, 32 * 3)  # Rectangle contenant l'image
        self.wumpafruit = 0
        self.aku = Akuaku("Aku", 2, x-50, y-50)




        self.xvel = 0 # starting position of X
        self.yvel = 0  # starting positon of y
        self.onGround = False  # Etre au sol
        self.faceright = True  # Etre droite
        self.airborne = True   # Etre en air
        self.attacking = False  # Etre attaquer
        self.counter = 0
        self.attackcounter = 0
       # self.image = faceright1  # Gerer l'image




    def _getname(self):
        return self.name

    def _getxposition(self):
        if self.xPos < 0:
            return "la valeur de la position est negative", self.xPos # A REVOIR
        else:
            return self.xPos

    def _setxposition(self, position):
        if position < 0:
           self.position = 0
           self.xPos = position
        else:
           self.xPos = position

    def _getlife(self):
        if self.life_points < 0:
            self.life_points = 0
            return self.life_points
        else:
            return self.life_points

    def _setlife(self, life):
        if life < 0 and self.life_points>=abs(life):
           self.life_points += life
        else:
          self.life_points += life

    def _getdamage(self):
        if self.damage < 0:
            return self.damage == 0
        else:
            return self.damage

    def _setdamage(self, takedamage):
        if takedamage > 0 and self.life_points >= takedamage:
            self.life_points -= takedamage
        elif takedamage > 0 and self.life_points > 0 and self.life_points < takedamage:
            self.life_points = 0
        else:
            self.life_points = self.life_points # verify this condition !

    def _getattack(self):
     if self.attack > 0:
        return str("{} a recu {} attaques ".format(self.names, self.attack))
     else:
         #return self.attack
        return str("{} n'a pas recu d'attaques ".format(self.names))

    def _setattack(self, addattack):
        if addattack > 0:
            self.attack += addattack
        else:
            self.attack += 0

    def attack_target(self, target_player):
        target_player._setdamage(self.damage)
        target_player.attack += 1

    def _getwumpafruit(self):
        return self.wumpafruit

    def _setwumpafruit(self, nb):
        if nb <1:
            self.wumpafruit+=0
        else:
            self.wumpafruit+=nb


    def soundbox(self, chemin):
        self.boxsound = pygame.mixer.Sound(chemin)
        self.boxsound.play(loops=0, maxtime=1500)
        self.boxsound.set_volume(0.3)



    def update(self, up, down, left, right, attack, platforms, enemygroup):  # Update the movement with the condition

        if up:
            # only jump if on the ground
            if self.onGround:
                self.yvel -= 10  # Jump only if on ground decrement the position for y from the ground
                #self.aku.yvel -= 10


        if down: #Do Nothing
            if self.onGround:
                self.yvel += 10
        if attack: #Do spin attack with pressing space
            self.attack = False
            self.attacking = True
        if left: # setting the direction of left using negative x
            self.xvel = -8
            self.faceright = False
        if right: # setting the direction of right using positive x
            self.xvel = 8
            self.faceright = True

        if not self.onGround: #If in air
            # only accelerate with gravity if in the air
            self.yvel += 0.3 # starting y = negative adding positive to move player back down bit by bit (gravity)
            # max falling speed
            #if self.yvel > 50: self.yvel = 50 # cannot fall faster than 100 pixels
        if not (left or right):
            self.xvel = 0        # if player not pressing left or right the falling positon 0 basically in the same positon
        if self.yvel < 0 or self.yvel > 1.2: self.airborne = True  # declare the state to airborn if y equal negative number or greater than 1.2 when in air
        # increment in x direction
        self.rect.left += self.xvel
        # do x-axis collisions
        self.collide(self.xvel, 0, platforms, enemygroup)
        # increment in y direction
        self.rect.top += self.yvel
        # assuming we're in the air
        self.onGround = False
        # do y-axis collisions
        self.collide(0, self.yvel, platforms, enemygroup)

        if self.attackcounter > 8: # Stop update the attack animation after 9 updates
            self.attacking = False
            self.attackcounter = 0
            self.counter = 0
            print("OK")

        self.animate()

        return up or down or left or right or attack or platforms

    def collide(self, xvel, yvel, platforms, enemygroup):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):

                if isinstance(p, CrashBox): # When crash interact with the box
                    self.life_points += p.lifeplus # Add 5 on top of 5
                    p.lifeplus -= p.lifeplus
                    p.kill() # Faire disparaître l'image san,
                    continue
                if isinstance(p, WumpaBigBox): # When crash interact with the box
                    self.wumpafruit += p.wumpafruitplus # Add 5 on top of 5
                    p.wumpafruitplus -= p.wumpafruitplus
                    self.soundbox("assets/sons/sonConsommeWumpa.ogg")
                    p.kill()
                    continue

                if isinstance(p, AkuBox):   # When crash interact with the box     isinstance(5, int)
                    print("This A")
                    self.aku.life_points += p.lifePointAku  # Add 5 on top of 5
                    p.lifePointAku -= p.lifePointAku
                    p.kill()  # Faire disparaître l'image san,
                    continue

                if isinstance(p, NitroBox):

                    if self.aku.life_points > 0 and self.aku.life_points <= 3:  ### LifeAku apparttient [0, 3]
                        self.aku.life_points -= p.damage
                        p.damage -= p.damage
                        self.soundbox("assets/sons/bombeNitro.ogg")
                        p.kill()
                        continue

                    else:
                        self.life_points -= p.damage
                        p.damage -= p.damage
                        p.kill()
                        continue

                if isinstance(p, TntBox):
                    print("Interact with Tnt")
                    if self.aku.life_points > 0 and self.aku.life_points <= 3:  ### LifeAku apparttient [0, 3]
                        self.aku.life_points -= p.damage
                        p.damage -= p.damage
                        self.soundbox("assets/sons/bombeNitro.ogg")
                        p.kill()
                        continue
                    else:
                        self.life_points -= p.damage
                        p.damage -= p.damage
                        p.kill()
                        continue

                if isinstance(p, ArrowBox):
                    print("Interact with Arrow")
                    self.yvel = -8
                    continue

                if isinstance(p,Wumpa):
                    self.soundbox("assets/sons/sonConsommeWumpa.ogg")
                    self.wumpafruit += p.wumpafruitplus  # Add 5 on top of 5
                    p.wumpafruitplus -= p.wumpafruitplus
                    p.kill()  # Faire disparaître l'image san,
                    continue

                if isinstance(p, WumpaSmallBox):
                    self.soundbox("assets/sons/sonConsommeWumpa.ogg")
                    self.wumpafruit += p.wumpafruitplus  # Add 5 on top of 5
                    p.wumpafruitplus -= p.wumpafruitplus
                    p.kill()  # Faire disparaître l'image san,
                    continue

                if isinstance(p, Obstacle):     # When crash interact with the box

                    if self.aku.life_points <=3 and self.aku.life_points > 0:   ### LifeAku apparttient [0, 3]
                        self.aku.life_points -= 1
                        self.soundbox("assets/sons/sonFall.ogg")
                        continue
                    else:
                        self.life_points -= 1
                        self.soundbox("assets/sons/sonFall.ogg")
                        self.rect.x = 100  # Revenir au point du depart
                        self.rect.y = 100
                        continue

                if isinstance(p, ObstacleWater):     # When crash interact with the box

                    if self.aku.life_points <= 3 and self.aku.life_points > 0:  ### LifeAku apparttient [0, 3]
                        self.aku.life_points -= 1
                        self.soundbox("assets/sons/son1.ogg")
                        continue
                    else:
                        self.life_points -= 1
                        self.soundbox("assets/sons/son1.ogg")
                        self.rect.x = 100  # Revenir au point du depart
                        self.rect.y = 100
                        continue

                if isinstance(p, ObstacleSpikePillar):  # When crash interact with the box

                    if self.aku.life_points <= 3 and self.aku.life_points > 0:  ### LifeAku apparttient [0, 3]
                        self.aku.life_points -= 1
                        self.soundbox("assets/sons/sonAttak.ogg")
                        continue
                    else:
                        self.life_points -= 1
                        self.soundbox("assets/sons/sonAttak.ogg")
                        self.rect.x = 100  # Revenir au point du depart
                        self.rect.y = 100
                        continue

                if xvel > 0:
                    self.rect.right = p.rect.left
                    print("collide right")
                if xvel < 0:
                    self.rect.left = p.rect.right
                    print("collide left")
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.airborne = False
                    self.yvel = 0

                if yvel < 0:
                    self.rect.top = p.rect.bottom

                for e in enemygroup:
                    if pygame.sprite.collide_rect(self, e):
                        dif = self.rect.bottom - e.rect.top
                        if dif <= 15:
                            pass
                        else:
                            if self.aku.life_points <= 3 and self.aku.life_points > 0:  ### LifeAku apparttient [0, 3]
                                self.aku.life_points -= 1
                                self.soundbox("assets/sons/sonAttak.ogg")
                            else:
                                self.life_points -= 1
                                self.soundbox("assets/sons/sonAttak.ogg")

            self.animate()


    def animate(self):
        if self.xvel > 0 or self.xvel < 0: #Moving
            self.walkloop() # do the walkloop animation
            if self.airborne:
                self.updatecharacter(Jumping1) # if in air do the falling animation
        else:
            self.updatecharacter(Running1) # if standing use the default pic
            if self.airborne:
                self.updatecharacter(Jumping1) # use falling animation if in air
            if self.attacking:
                self.attackloop() # do the attack animation if state = attacking

 #---------------------------EXPLICATION: Elle a un lien avec le Spin attack--------------------------


    def attackloop(self):
        print(f"self.attackcounter : {self.attackcounter}")
        if self.attackcounter == 0:
            self.counter = 0
            self.updatecharacter(Spinning)
           # self.attackcounter = 3
        elif self.attackcounter == 1:
            self.updatecharacter(Spinning5)
            #self.attackcounter = 6
        elif self.attackcounter == 2:
            self.updatecharacter(Spinning4)
            #self.attackcounter = 9
        elif self.attackcounter == 3:
            self.updatecharacter(Spinning3)
            #self.attackcounter = 12
        elif self.attackcounter == 4:
            self.updatecharacter(Spinning2)
            #self.attackcounter = 9
        elif self.attackcounter == 5:
            self.updatecharacter(Spinning)
           # self.attackcounter = 3

        self.attackcounter = self.attackcounter + 1

#################################### Fonction qui gère le déplacement à droite et à gauche
    def walkloop(self):
        if self.counter == 5:  # Nombre de fois qu'on  se déplace
            self.updatecharacter(Running5)
        elif self.counter == 10:
            self.updatecharacter(Running4)
        elif self.counter == 15:
            self.updatecharacter(Running3)
        elif self.counter == 20:
            self.updatecharacter(Running2)
        elif self.counter == 25:
            self.updatecharacter(Running2)
        elif self.counter == 30:
            self.updatecharacter(Running3)
        elif self.counter == 35:
            self.updatecharacter(Running4)
        elif self.counter == 40:
            self.updatecharacter(Running5)
            self.counter = 0
        self.counter = self.counter + 1


    def updatecharacter(self, ansurf): #ansurf animation surface change self.image property to anything you want
        if not self.faceright : ansurf = pygame.transform.flip(ansurf,True,False) # flip the animate vertically if left
        self.image = ansurf # replace another image on current image




###########################################################Explication########################################################
    names = property(_getname)
    xposition = property(_getxposition, _setxposition)
    life = property(_getlife, _setlife)
    damages = property(_getdamage, _setdamage)
    attacks = property(_getattack, _setattack)
    wumpafruits = property(_getwumpafruit,_setwumpafruit)








































# #TEST
# crash1 = Crash("Crash", 5, xPos = 480, yPos = 272, damage=2, attack=2, wumpafruit=2)
# aku = Crash("Aku", 10, xPos=10, yPos=50, damage=0, attack=0)
# print(" life crash ", crash1.life)
#
# print("la position de crash sur l'axe des x : ", crash1.xposition)
# crash1.xposition += 1
# print("la position de crash maintenant sur l'axe des x :", crash1.xposition)
# #print("damage : ", crash1.damageCrash)
# #crash1.damageCrash = 5
# #print("damage : ", crash1.damageCrash)
# print("crash life", crash1.life, "attack", crash1.attack)
# print("aku life", aku.life, "attack", aku.attack)
# print("attaque de crash sur Aku")
# crash1.attack_target(aku)
# crash1.attack_target(aku)
# print("points de vie apres attaque")
# print(crash1.life)
# print(aku.life)
# print('fruit wumpa avant ajout',crash1.wumpafruit)
# crash1.wumpafruit +=10
# print('fruit wumpa apres ajout',crash1.wumpafruit)
# crash1.life -=3
#
# print("{} a attaque {}. Maintenant les PV de {} sont a {}. {}".format(crash1.names, aku.names, aku.names, aku.life, aku.attacks))
#
# """
# #TESTS
# crash_test = Crash("Nina", life_points=5, damage=1)
# crash_test22 = Crash("Rosa", life_points=5, damage=4)
# print("le prenom du 1st perso: {} et du 2nd :{}".format(crash_test.getName(), crash_test22.getName()))
#
# crash_test.takeDamage()
# print("points de vie apres une attaque que {} s'est prise {}".format(crash_test.getName(), crash_test.getLife_points()))
#
#
#
# """
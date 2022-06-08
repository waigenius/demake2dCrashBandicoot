# Rachel's code 306116

########################Importation des modules internes de python et nos modules crées ################
import pygame
from pygame import *
#from pygame.locals import *
import time,sys,os

import tkinter
from tkinter import *
from tkinter import ttk
from crash import Crash
from akuaku import Akuaku

from Entity import *
from Camera import *
from Platform import *
from Crates import *
from ennemy import *


def histoire_crash_bandicoot(): #methode contenant l histoire du jeu
    window_histoire = tkinter.Tk()
    window_histoire.geometry("800x300")
    window_histoire.title("Histoire de Crash Bandicoot")
    window_histoire1 = ttk.Label(window_histoire, text="\n\n\n\nCrash Bandicoot est un jeu vidéo de plates-formes développé\npar Naughty Dog et édité par Sony Computer Entertainment\nen 1996 sur PlayStation. Il constitue le premier épisode\nde la série Crash Bandicoot\n\n\n\n\n\n\n\n\n\n")
    window_histoire1.config(justify=CENTER, foreground='yellow', background='purple', width=1000, font=('Courier', 15, 'bold'))
    window_histoire1.pack()
    #window_histoire.mainloop()

def regle(): #methode contenant la regle du jeu
    window_regle=tkinter.Tk()
    window_regle.geometry("1000x300")
    window_regle.title("La règle du jeu Crash Bandicoot")
    window_regle1=ttk.Label(window_regle, text = "\n\n\n\n\n\tCrash Bandicoot doit sauver sa petite amie, Tawna. \nParmis les ennemis il y a le crabe, le personnage Slim et la moufette.\nCrash doit les affronter tous et les vaincre pour pouvoir sauver sa bien-aimée!\n\n\n\n\n\n\n\n\n\n\n")
    window_regle1.config(justify=CENTER, foreground='yellow', width=1000, background='purple', font=('Courier',15,'bold'))
    window_regle1.pack()
    #window.mainloop()

def membres(): #liste des membres de l'equipe du projet 1PROJ
    window_membre = tkinter.Tk()
    window_membre.geometry("1200x450")
    window_membre.title("Liste des membres de l'equipe de travail 1PROJ")
    window_membre1=ttk.Label(window_membre, text = " PRENOM    | NOM \t      |  ROLE")
    window_membre=ttk.Label(window_membre, text = " Nana Jacelie\tBAKALAFOUA M'BOUSSI \t Marketing et Communication\n\n Nihad Rachel \tOULKHIARI \t\t Développeuse et Manager de projet\n\n Waï Berty \tLEKONE ANTA \t\t Développeuse\n\n Koundian \tSISSOKO \t\t Designer\n\n Seng Davy \tSIENG \t\t\t Cheffe designer\n\n Soronik \tSIENG \t\t\t Développeur\n\n Nazih \t\tKAF \t\t\t Marketing")
    window_membre.config(justify=LEFT, foreground='yellow', width=100, background='purple', relief= RIDGE, font=('Courier', 20,'bold'))
    window_membre1.config(justify=LEFT, foreground='yellow', width=70,background='purple', relief=GROOVE, borderwidth=10, font=('Courier', 25,'bold'))
    window_membre1.pack()
    window_membre.pack()
    window_membre.mainloop()

def membre(): #photo membres du groupe
    membre= Tk()
    membre.title('Photo des membres')
    membre.geometry('800x500')
    membre.iconbitmap('logocrash.png')
    membre.config(background='purple')
    my_pic=ImageTk.PhotoImage(file="team.png")
    label=Label(master=membre, image=my_pic)
    label.pack(pady=20)

def menu(): #contient l'ensemble des fenetres via l'appel des fonctions definies plus haut.

    wind = tkinter.Tk()
    wind.geometry("1000x500")
    wind.title("Crash Bandicoot")
    menu1 = tkinter.Menu(wind)
    col1 = tkinter.Menu(menu1, tearoff=0)
    #Background
    bgImage = PhotoImage(file="assets/images/imagesPlateforme/menu2.png")
    tkinter.Label(wind, image=bgImage).place(relwidth = 1, relheight= 1 )

    menu1.add_cascade(label="Menu", menu=col1)
    menu1.add_cascade(label="Options")
    col1.add_command(label="Regle du jeu", command=regle)
    col1.add_command(label="Histoire de Crash Bandicoot", command=histoire_crash_bandicoot)
    col1.add_command(label="Membres de l'equipe", command=membres) #Nom des membres et leur role durant le projet
    col1.add_command(label="Quitter", command=wind.quit)
    wind.config(menu=menu1, background='purple')
   # frame=tkinter.Frame(wind,width=100, height=100, background="white")
    button=Button(wind, text="Lancer le Jeu", bg='orange', fg='darkgreen', font=('Lucida', 15, 'bold'), relief=RIDGE, width=10, borderwidth=5, command=wind.quit)
    #frame.pack()
    button.pack()
    wind.mainloop()

# from time import sleep


WIN_WIDTH = 1000    #Largeur de l'ecran
WIN_HEIGHT = 500   #Hauteur de l'ecran
HALF_WIDTH = int(WIN_WIDTH / 2)  #Largeur utilisé opar la caméra
HALF_HEIGHT = int(WIN_HEIGHT / 2)  #Hauteur utilisé opar la caméra

DISPLAY =  (WIN_WIDTH, WIN_HEIGHT)  # Variable qui represente les dimensions de l'écran à l'affichage
DEPTH = 32  #Initialiser la fênetre ????????????
FLAGS = 0   #Initialiser la fênetre ????????????


#CAMERA_SLACK = 30

###############Initialisation du module Pygame #############
pygame.init()
# music = pygame.mixer.music.load('assets/musique/Upstream.mp3')
# pygame.mixer.music.set_volume(0.3)
# pygame.mixer.music.play(-1)


def Main():

    background = pygame.image.load("assets/images/imagesPlateforme/background.png") # Image du font d'écran(arrière plan)


    #---------------------------------------------Image des icônes à gauche de l'écran-------------------------------------------
    crashlife_pic = pygame.image.load('assets/images/imagesPlateforme/iconeCrash.png')
    crashlife_pic_x = 10
    crashlife_pic_y = 10

    wumpafruit_pic = pygame.image.load('assets/images/imagesPlateforme/iconeWumpa.png')
    wumpafruit_x = 10
    wumpafruit_y = 40

    aku_aku_pic = pygame.image.load('assets/images/imagesPlateforme/iconeAku.png')
    aku_aku_pic_x = 10
    aku_aku_pic_y = 70

    # ----------------------------------------------GAME OVER------------------------------------------------
    def gameover(ecran):
        myfont = pygame.font.SysFont("arial", 100)
        texte = myfont.render("GAME OVER", 0, (255, 0, 0))
        texteRect = texte.get_rect()
        texteRect.x = 50
        texteRect.y = 50
        color = (0, 0, 0)
        ecran.fill(color)
        ecran.blit(texte, texteRect)


    #----------------------------------crash_gauche = pygame.image.load("Gauche.png")-----------------------------------
#    aku_face=pygame.image.load('akuaku1.png')
    #crashh = crash_face
    #basic_crate_pic = pygame.image.load('Basic_crate.png')
    #crash_crate_pic = pygame.image.load('Crash_crate.png')

    #----------------------------------------------La police-----------------------------------------------------
    font_text = pygame.font.SysFont("franklingothicmedium", 30)

    #---------------------------------------Création des différents objets ---------------------------------------------
    crash2 = Crash("Crashou", 16 * 3, 16*3*9,life_points=4, damage=2, attack=2)
    aku = Akuaku(name = "Aku", life_points=2, xPos=100, yPos=100)

    #----------------------------------Lancement du jeu -------------------------------------------------------------
    
    launched = True
    while launched:
        menu()
    
        screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)  # Permet de créer la fênetre
        pygame.display.set_caption("Use arrows to move!")   # Permet de titrer le fenêtre
        timer = pygame.time.Clock()  # Fps

        timer.tick(60) # Fixer le Fps ???
    
        up = down = left = right = attack = False  #Etats quand Utilisateur interagit avec les touches du clavier( UP, attack= SPACE)

        entities = pygame.sprite.Group() # Permet de grouper les sprites

        enemygroup = pygame.sprite.Group()
        enemygroup.add(crabe(16*3*6, 16*3*9))

        enemygroup.add(crabe(16 * 3 * 10, 16 * 3 * 9))

        enemygroup.add(crabe(16 * 3 * 75, 16 * 3 * 9))

        enemygroup.add(skunk(16 * 3 * 20, 16 * 3 * 9))
        enemygroup.add(skunk(16 * 3 * 120, 16 * 3 * 9))
        enemygroup.add(skunk(16 * 3 * 90, 16 * 3 * 9))



        platforms = []  #Plateau du jeu
    
        x = y = 0  #Position du depart de la plateforme
        level = [



            "P                                                                                                                                                                              P",
            "P                                                                                                                                                                              P",
            "P                                        B SS                                                                                                                                  P",
            "P                         K                               T BT                                                                 FFFF                                            P",
            "P                      C  K  B      R                SPPPPPPPPPPPP                     BBBB                                                             I                      P",
            "P       B  A          PPPPPPP                     PP                         B                                B        B   E       SES           R      I                      P",
            "P                   PP                             FFF                                                                 PPPPPPPPPPPP                     I                      P",
            "P           S  S                 FFFFF        II                       FFF                                          PP           R                      I                SSS   P",
            "P                      N        I     I       II       I    I      B  N    C         A R      I  SS     I    NR                T      K B K FFFF  I     I                BBB   P",
            "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP     PPPPPPPPPPPPPPPPPP    PPPPPPPPPPPPPWWWWWPPPPWWWWPPPPPPPPP     PPPPPPPPIIIPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP     PPPPPPPPPPPWWWWPPPPPPPPP",
            "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDHHHHHDDDDDDDDDDDDDDDDDDHHHHDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDHHHHHDDDDDDDD   DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDHHHHHDDDDDDDDDDDDDDDDDDDDDDDD",
        ]  #Schema du plateau du jeu

        # build the level
        for row in level:
            for col in row:
                if col == "P":
                    p = Platform(x, y)
                    platforms.append(p)
                    entities.add(p)
                if col == "E":
                    e = CrashBox(x, y)
                    platforms.append(e)
                    entities.add(e)

                if col == "D":
                    e = DirtBlock(x, y)
                    platforms.append(e)
                    entities.add(e)

                if col == "B":
                    b = WumpaBigBox(x, y)
                    platforms.append(b)
                    entities.add(b)

                if col == "I":
                    b = IronBox(x, y)
                    platforms.append(b)
                    entities.add(b)

                if col == "N":
                    b = NitroBox(x, y)
                    platforms.append(b)
                    entities.add(b)

                if col == "T":
                    b = TntBox(x, y)
                    platforms.append(b)
                    entities.add(b)

                if col == "R":
                    b = ArrowBox(x, y)
                    platforms.append(b)
                    entities.add(b)

                if col == "F":
                    b = Wumpa(x, y)
                    platforms.append(b)
                    entities.add(b)

                if col == "A":
                    b = AkuBox(x, y)
                    platforms.append(b)
                    entities.add(b)
                    
                if col == "S":
                    b = WumpaSmallBox(x, y)
                    platforms.append(b)
                    entities.add(b)

                if col == "H":
                    b = Obstacle(x, y)
                    platforms.append(b)
                    entities.add(b)

                if col == "W":
                    b = ObstacleWater(x, y)
                    platforms.append(b)
                    entities.add(b)

                if col == "K":
                    b = ObstacleSpikePillar(x, y)
                    platforms.append(b)
                    entities.add(b)

                # if col == "G":
                #     b = Gagner(x, y)
                #     platforms.append(b)
                #     entities.add(b)


                x += 16 * 3  #Joue sur l'affichage des éléments du plateau du jeu
            y += 16 * 3  #Joue sur l'affichage des éléments du plateau du jeu
            x = 0

        total_level_width = len(level[0]) * 16 * 3  #Permet à la camera de suivre Crash depuis sa position de départ et durant le jeu (Mode Horizontal)
        total_level_height = len(level) * 16 * 3    #Permet à la camera de suivre Crash depuis sa position de départ et durant le jeu (Mode Vertical)
        camera = Camera(complex_camera, total_level_width, total_level_height)  # Création de l'objet camera
        entities.add(crash2)  # Ajout de chaque sprite de Crash dans l'entité
        entities.add(aku)



    ####-----------Permet de gérer différents évén ements après contact avec certaiunes touches du clavier.
        while 1:
            timer.tick(60)
    
            for e in pygame.event.get():
                if e.type == QUIT: raise SystemExit("QUIT")
                if e.type == KEYDOWN and e.key == K_ESCAPE:
                    raise SystemExit("ESCAPE")
                if e.type == KEYDOWN and e.key == K_UP:
                    up = True
                if e.type == KEYDOWN and e.key == K_DOWN:
                    down = True
                if e.type == KEYDOWN and e.key == K_LEFT:
                    left = True
                if e.type == KEYDOWN and e.key == K_RIGHT:
                    right = True
                if e.type == KEYDOWN and e.key == K_SPACE:
                    print("Attack")
                    attack = True
    
                if e.type == KEYUP and e.key == K_UP:
                    up = False
                if e.type == KEYUP and e.key == K_DOWN:
                    down = False
                if e.type == KEYUP and e.key == K_RIGHT:
                    right = False
                if e.type == KEYUP and e.key == K_LEFT:
                    left = False
                if e.type == KEYUP and e.key == K_SPACE:
                    attack = False
    
            screen.blit(background, (0, 0))  #Blite l'image du background

            camera.update(crash2)  #Mise à jour de la caméra afin qu'il puisse toujours suivre les mouvements de Crash


    
            # update player, draw everything else
            #crash2.update(up, down, left, right, attack, platforms)  #Mise à jour des états des mouvements de Crash, collision avec la plateforme
            crash2.update(up, down, left, right, attack, platforms, enemygroup)  # Mise à jour des états des mouvements de Crash, collision avec la plateforme
            aku.update(up, down, left, right, attack, platforms)

             # Permet d'afficher chaque image des sprites de Crash avec la caméra à côté
            for e in entities:
                screen.blit(e.image, camera.apply(e))

            for e in enemygroup:
                screen.blit(e.image, camera.apply(e))
                e.update(platforms, entities)

            if crash2.wumpafruit >=100:
                crash2.life_points +=1
                crash2.wumpafruit = 0


            # if crash2.life_points < 1 :
            #     crashh = crash_over
            # window_surface.blit(crashh, (crash2.xPos, crash2.yPos))
            #screen.blit(aku_face, (aku.xPos, aku.yPos))

            #  Blite au niveau de l'écran les éléments
            screen.blit(crashlife_pic,(crashlife_pic_x, crashlife_pic_y))
            screen.blit(wumpafruit_pic, (wumpafruit_x, wumpafruit_y))
            screen.blit(aku_aku_pic, (aku_aku_pic_x, aku_aku_pic_y))


            # Texte à l'aafichage de l'écran
            points_de_vie_crash = font_text.render(": {}".format(crash2.life), True, (255,255,255))
            wumpa_fruits_gagnes = font_text.render(": {}".format(crash2.wumpafruit), True, (255,255,255))
            aku_aku_life = font_text.render(": {}".format(crash2.aku.life_points), True, (255,255,255))

            #  Blite au niveau de l'écran les éléments
            screen.blit(points_de_vie_crash, [40, 10])
            screen.blit(wumpa_fruits_gagnes, [40, 40])
            screen.blit(aku_aku_life, [40, 70])

            if crash2.life_points < 1:
                gameover(screen)
                pygame.mixer.music.stop()


            #Mise à jour de la fênetre du jeu
            pygame.display.update()



################# Fonctionnalité de la Caméra #######################
# def simple_camera(camera, target_rect):
# #     l, t, _, _ = target_rect
# #     _, _, w, h = camera
# #     return Rect(-l+HALF_WIDTH, -t+HALF_HEIGHT, w, h)

def complex_camera(camera, target_rect):
    l, t, _, _ = target_rect   #left , top
    _, _, w, h = camera
    l, t, _, _ = -l+HALF_WIDTH, -t+HALF_HEIGHT, w, h  #Zoomer

    l = min(0, l)                           # stop scrolling at the left edge
    l = max(-(camera.width-WIN_WIDTH), l)   # stop scrolling at the right edge
    t = max(-(camera.height-WIN_HEIGHT), t) # stop scrolling at the bottom
    t = min(0, t)                           # stop scrolling at the top
    return Rect(l, t, w, h)

if __name__ == '__main__':
    Main()

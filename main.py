from typing import Union, Any

from pygame.surface import Surface, SurfaceType

from settings import *  # connects to file 'settings.py'
from player import *  # connects to file 'player.py'

import pygame as pg
import random
import sys
import os
from os import path

from pygame.locals import *

# world is our screen
# backdrop is our background0

########## SETUP ############
pg.init()  # Initializing Pygame
game_display = pg.display.set_mode((width, height))
player_update = Player()                                            # when player_update is called, Player class is called.


# in our main game class to be called, we define functions (elements) of our game
class Game:
    def __init__(self):
        pg.init()

        # main = True

 # dude = pg.image.load('player_one_sprite.png').convert_alpha()

main = True
while main:
    for event in pg.event.get():
        if event.type == pg.QUIT:                                    # Close Game via window "X"
            main = False

        if event.type == pg.KEYDOWN:                                 # closes game via 'q' key. Later change to escape.
            if event.key == ord('q'):
                main = False

    game_display.blit(background, (0, 0))                            # updates background, loads image at cords (0,0)
    # player_update(x, y)  # updates player, calls class
    # game_display.blit(dude, (x, y))

    player_update.playerLocation()                                   # calling for playerLocation data in player.py

    # pg.display.flip()                                              # allows only a portion of the screen to update instead of the entire area
    pg.display.update()

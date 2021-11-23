import pygame as pg

from main import *
from settings import *


class Player(pg.sprite.Sprite):

    def __init__(self, x, y):
        # initializing the player data
        # self.character.name = "Batteries"
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('player_one_sprite.png').convert_alpha()             # alpha allows for use to transtarent images

        self.rect = self.image.rect()

    def playerLocation(self, x, y):
        print("Reached Player Location Data")
        return game_display.blit(self.image, (x, y))


    def test():
        print("you reached the test print")
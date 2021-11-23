import pygame as pg


fps = 144                                    # Sets frame rate
pg.display.set_caption('Train Game')         # sets the name of the game at the top of the screen
(width, height) = (1920, 1080)               # defines window size
# replace later with size = (window_width, window_height)

# Starting spawn location for Player
x = (width * 0.2)                               # higher value shifts to right
y = (height * 0.25)                             # higher value shift lower


background = pg.image.load('oasis.jpg')     # load image 'oasis.jpg' for background
# may need to set to a further directory later in dev.

# look into x = screen.get_rect()
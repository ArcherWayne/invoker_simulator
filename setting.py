import pygame

window_size = (600, 800)
WIN_WIDTH = window_size[0]
WIN_HEIGTH = window_size[1]
screen = pygame.display.set_mode(window_size)

slot_size = (80, 80)
skill_size = (120, 120)
icon_size = (40, 40)
dead_distance = 650

FPS = 60

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED_transparent = pygame.Color(255, 0, 0, 50)
RED = (255, 0, 0)
BLUE = (0, 255, 0)
GREEN = (0, 0, 255)

Q_COLOR = ('#39d6ff')
W_COLOR = ('#ef46ff')
E_COLOR = ('#ffeb2d')
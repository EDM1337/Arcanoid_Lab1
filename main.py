import pygame
from pygame.locals import *

pygame.init()

screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Arcanoid')

font = pygame.font.SysFont('Constantia', 30)

bg = (234, 218, 184)

block_red = (242, 85, 96)
block_green = (86, 174, 87)
block_blue = (69, 177, 232)

paddle_col = (142, 135, 123)
paddle_outline = (100, 100, 100)

text_col = (78, 81, 139)

cols = 6
rows = 6
clock = pygame.time.Clock()
fps = 60
live_ball = False
game_over = 0
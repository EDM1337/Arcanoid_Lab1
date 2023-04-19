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
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))
class wall():
    def __init__(self):
        self.width = screen_width // cols
        self.height = 50

    def create_wall(self):
        self.blocks = []

        block_individual = []
        for row in range(rows):

            block_row = []

            for col in range(cols):

                block_x = col * self.width
                block_y = row * self.height
                rect = pygame.Rect(block_x, block_y, self.width, self.height)

                if row < 2:
                    strength = 3
                elif row < 4:
                    strength = 2
                elif row < 6:
                    strength = 1

                block_individual = [rect, strength]

                block_row.append(block_individual)

            self.blocks.append(block_row)

    def draw_wall(self):
                for row in self.blocks:
                    for block in row:

                        if block[1] == 3:
                            block_col = block_blue
                        elif block[1] == 2:
                            block_col = block_green
                        elif block[1] == 1:
                            block_col = block_red
                        pygame.draw.rect(screen, block_col, block[0])
                        pygame.draw.rect(screen, bg, (block[0]), 2)

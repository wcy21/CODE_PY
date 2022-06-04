import sys

import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 720))
pygame.display.set_caption("KEY DOWN CASES")

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            print(event.key)
            print(event)

        if event.type == pygame.QUIT:
            sys.exit()

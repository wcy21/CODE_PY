import sys
import time

import pygame

from random import randint

from pygame.sprite import Group, Sprite


class Star(Sprite):
    """星星类"""

    def __init__(self, screen):
        super().__init__()
        self.screen = screen

        self.image = pygame.image.load('images/star.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        """绘制星星"""
        self.screen.blit(self.image, self.rect)


pygame.init()
screen_width = 1200
screen_height = 800
bg_color = (230, 230, 230)

screen = pygame.display.set_mode((screen_width, screen_height))

stars = Group()

star = Star(screen)
# 计算行
available_space_x = screen_width - 2 * star.rect.width
number_stars_x = int(available_space_x / (2 * star.rect.width))
# 计算列
available_space_y = screen_height - 3 * star.rect.height
number_rows = int(available_space_y / (2 * star.rect.height))

for row_number in range(number_rows):
    for alien_number in range(number_stars_x):
        star = Star(screen)
        # 有序
        # star_width = star.rect.width
        # star.x = star_width + 2 * star_width * alien_number
        # star.rect.x = star.x
        # star.rect.y = star.rect.height + 2 * star.rect.height * row_number

        # 随机
        star.rect.x = randint(0, screen_width - star.rect.width)
        star.rect.y = randint(0, screen_height - star.rect.height)
        stars.add(star)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(bg_color)
    stars.draw(screen)

    pygame.display.flip()

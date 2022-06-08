import random
import sys

import pygame
from pygame.sprite import Sprite


class Ball(Sprite):
    """下坠的小球"""

    def __init__(self, screen):
        super(Ball, self).__init__()
        self.screen = screen

        self.image = pygame.image.load('images/ball1.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.y = float(self.rect.y)

    def check_edges(self):
        """如果位于屏幕边缘,返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.top >= screen_rect.bottom:
            return True

    def update(self):
        """球匀速下坠"""
        self.y += 0.1
        self.rect.y = self.y

    def blitme(self):
        """绘制球"""
        self.screen.blit(self.image, self.rect)


def check_fleet_edges(ball, screen, screen_width):
    """到达下边界消失并重新生成球"""
    if ball.check_edges():
        ball.x = random.randint(0, screen_width - ball.rect.width)
        ball.y = -ball.rect.height
        ball.rect.x = ball.x
        ball.rect.y = ball.y


def update_ball(ball, screen, screen_width):
    """检查是否达到下边界，更新位置"""
    check_fleet_edges(ball, screen, screen_width)
    ball.update()


def update_screen(bg_color, screen, ball):
    """更新屏幕，切换新屏幕"""
    screen.fill(bg_color)
    ball.blitme()

    pygame.display.flip()


def run_game():
    pygame.init()
    screen_width = 1200
    screen_height = 800
    bg_color = (124, 200, 230)
    screen = pygame.display.set_mode(
        (screen_width, screen_height))
    pygame.display.set_caption("catch_ball")

    ball = Ball(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        update_ball(ball, screen, screen_width)
        update_screen(bg_color, screen, ball)


run_game()

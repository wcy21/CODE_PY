import pygame
from pygame.sprite import Sprite


class Ball(Sprite):
    """下坠的小球"""

    def __init__(self, ai_settings, screen):
        super().__init__()
        self.ai_settings = ai_settings
        self.screen = screen

        self.image = pygame.image.load('images/ball1.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_edges(self):
        """如果位于屏幕边缘,返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.top >= screen_rect.bottom:
            return True

    def update(self):
        """球匀速下坠"""
        self.y += self.ai_settings.ball_speed_factor
        self.rect.y = self.y

    def blitme(self):
        """绘制球"""
        self.screen.blit(self.image, self.rect)

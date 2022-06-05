import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """表示外星人的类"""

    def __init__(self, ai_settings, screen):
        super().__init__()
        self.ai_settings = ai_settings
        self.screen = screen

        # 加载图像并设置rect
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()

        # 默认位置左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 位置的小数值
        self.x = float(self.rect.x)

    def blitme(self):
        """绘制外星人"""
        self.screen.blit(self.image, self.rect)

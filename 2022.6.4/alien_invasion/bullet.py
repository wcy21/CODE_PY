import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """管理飞船发射的子弹"""

    def __init__(self, ai_settings, screen, ship):
        super().__init__()
        self.screen = screen

        # (0,0)处创建表示子弹的矩形，再设置正确位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 存储小数表示的子弹位置
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """子弹向上移动"""
        # 更新子弹位置的小数值
        self.y -= self.speed_factor
        # 更新表示子弹的rect的位置
        self.rect.y = self.y

    def draw_bullet(self):
        """绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)

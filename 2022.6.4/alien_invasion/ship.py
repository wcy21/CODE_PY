import pygame


class Ship():

    def __init__(self, ai_settings, screen):
        """初始化飞船并设置初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像并获取外接矩形
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每搜新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # center保存小数值
        self.center = float(self.rect.centerx)
        self.height = float(self.rect.centery)

        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        self.moving_up = False

    def update(self):
        """根据移动标志调整飞船位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.height += self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.height -= self.ai_settings.ship_speed_factor

        # 根据self.center 更新rect
        self.rect.centerx = self.center
        self.rect.centery = self.height

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

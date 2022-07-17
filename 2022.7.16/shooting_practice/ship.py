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

        # 将每艘飞船放在屏幕左侧中央
        self.rect.centery = self.screen_rect.centery
        self.rect.left = 0

        # center保存小数值
        self.height = float(self.rect.centery)

        # 移动标志
        self.moving_up = False
        self.moving_down = False

    def center_ship(self):
        """飞船在屏幕上居中"""
        self.height = self.screen_rect.centery
        self.rect.left = 0

    def update(self):
        """根据移动标志调整飞船位置"""
        if self.moving_up and self.rect.top > 0:
            self.height -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.height += self.ai_settings.ship_speed_factor

        # 根据self.height更新rect
        self.rect.centery = self.height

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

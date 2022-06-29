import pygame


class Dog():
    """狗狗类"""

    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载狗狗图像并获取外接矩形
        self.image = pygame.image.load('images/dog.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将狗狗放到屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # center保存小数值
        self.center = float(self.rect.centerx)
        self.height = float(self.rect.centery)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整狗狗位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.dog_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.dog_speed_factor

        # 根据self.center 更新rect
        self.rect.centerx = self.center
        self.rect.centery = self.height

    def blitme(self):
        """在指定位置绘制狗狗"""
        self.screen.blit(self.image, self.rect)

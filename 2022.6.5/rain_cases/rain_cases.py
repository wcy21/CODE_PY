import sys

import pygame
from pygame.sprite import Sprite, Group


class Rain(Sprite):
    """雨滴类"""

    def __init__(self, screen):
        """初始化雨滴"""
        super().__init__()
        self.screen = screen

        # 加载图像
        self.image = pygame.image.load('images/rain.png')
        self.rect = self.image.get_rect()

        # 默认位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 位置的小数值
        self.y = float(self.rect.y)

    def check_edge(self):
        """如果位于屏幕底端，返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.top >= screen_rect.bottom:
            return True

    def update(self):
        """向下移动外星人"""
        self.y += 3
        self.rect.y = self.y

    def blitme(self):
        """绘制雨滴"""
        self.screen.blit(self.image, self.rect)


def get_number_rains_x(screen_width, rain_width):
    """计算每行可容纳多少雨滴"""
    available_space_x = screen_width - rain_width
    number_rains_x = int(available_space_x / (2 * rain_width))
    return number_rains_x


def get_number_rows(screen_height, rain_height):
    """计算可容纳多少行雨滴"""
    available_space_y = screen_height
    number_rows = int(available_space_y / (2 * rain_height))
    return number_rows


def create_rain(screen, rains, rain_number, row_number):
    """创建一个雨滴并放在当前行"""
    rain = Rain(screen)
    rain_width = rain.rect.width
    rain.x = rain_width + 2 * rain_width * rain_number
    rain.y = rain.rect.height + 1.5 * rain.rect.height * row_number
    rain.rect.x = rain.x
    rain.rect.y = rain.y
    rains.add(rain)


def check_fleet_edges(rains, screen):
    """到达下边界消失并重新生成雨滴"""
    # 到达下边界雨滴消失
    # for rain in rains.sprites():
    #     if rain.check_edge():
    #         rains.remove(rain)

    # 重新生成（移动雨滴）
    for rain in rains.sprites():
        if rain.check_edge():
            rain.y = - rain.rect.height


def update_rains(rains, screen):
    """检查是否到达下边界，并更新雨滴位置"""
    check_fleet_edges(rains, screen)
    rains.update()


def update_screen(bg_color, screen, rains):
    """更新屏幕图像，并切换新屏幕"""
    # 重绘屏幕
    screen.fill(bg_color)
    rains.draw(screen)

    # 绘制屏幕可见
    pygame.display.flip()


def run_game():
    """初始化游戏和屏幕对象"""
    pygame.init()
    screen_width = 1200
    screen_height = 800
    bg_color = (230, 230, 230)
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("rain")

    # 创建雨滴编组
    rains = Group()

    # 创建雨滴群
    rain = Rain(screen)
    number_rains_x = get_number_rains_x(screen_width, rain.rect.width)
    number_rows = get_number_rows(screen_height, rain.rect.height)

    for row_number in range(number_rows):
        for rain_number in range(number_rains_x):
            create_rain(screen, rains, rain_number, row_number)

    while True:
        # 响应键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        update_rains(rains, screen)
        update_screen(bg_color, screen, rains)


run_game()

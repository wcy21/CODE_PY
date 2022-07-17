import pygame

import game_functions as gf
from settings import Settings
from ship import Ship


def run_game():
    # 初始化游戏，设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("W的射击练习")

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 游戏的主循环
    while True:
        gf.check_event(ai_settings, screen, ship)

        ship.update()

        gf.update_screen(ai_settings, screen, ship)


run_game()

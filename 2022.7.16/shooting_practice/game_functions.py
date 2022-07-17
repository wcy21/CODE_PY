import sys

import pygame


def check_keydown_events(event, ai_settings, ship):
    """相应按键"""
    if event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    """相应松开"""
    if event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_event(ai_settings, screen, ship):
    """相应键盘和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship):
    """更新屏幕上的图像，并切换新屏幕"""
    # 重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # 绘制屏幕可见
    pygame.display.flip()

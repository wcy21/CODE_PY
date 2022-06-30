import random
import sys
from time import sleep

import pygame

from ball import Ball


def check_keydown_events(event, dog):
    """响应按键"""
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        dog.moving_right = True
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        dog.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, dog):
    """响应松开"""
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        dog.moving_right = False
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        dog.moving_left = False


def check_events(dog):
    """响应键盘和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, dog)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, dog)


def create_ball(ai_settings, screen, balls):
    """创建小球"""
    ball = Ball(ai_settings, screen)
    ball.x = random.randint(0, ai_settings.screen_width - ball.rect.width)
    ball.y = -ball.rect.height
    ball.rect.x = ball.x
    ball.rect.y = ball.y
    balls.add(ball)


def check_fleet_edges(ai_settings, stats, screen, dog, balls):
    """到达下边界消失并重新生成球"""
    check_dog_balls_collections(ai_settings, stats, screen, balls, dog)

    for ball in balls.copy():
        if ball.rect.top >= ai_settings.screen_height:
            # 球到达下边界，执行未接到球的操作
            if stats.ball_not_catch < ai_settings.ball_limit:
                stats.ball_not_catch += 1
                balls.remove(ball)

                sleep(0.5)

            else:
                stats.game_active = False


def check_dog_balls_collections(ai_settings, stats, screen, balls, dog):
    """检查球和狗狗是否相碰"""
    collections = pygame.sprite.spritecollide(dog, balls, True)

    if len(balls) == 0:
        create_ball(ai_settings, screen, balls)


def update_ball(ai_settings, stats, screen, dog, balls):
    """检查是否达到下边界或碰到狗狗，更新位置"""
    check_fleet_edges(ai_settings, stats, screen, dog, balls)
    balls.update()


def update_screen(ai_settings, screen, dog, balls):
    """更新屏幕，切换新屏幕"""
    screen.fill(ai_settings.bg_color)
    dog.blitme()
    balls.draw(screen)

    pygame.display.flip()

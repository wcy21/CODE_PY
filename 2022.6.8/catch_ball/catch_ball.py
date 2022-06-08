import random
import sys

import pygame
from pygame.sprite import Sprite, Group


class Dog():
    """狗狗类"""

    def __init__(self, screen):
        self.screen = screen
        self.speed_factor = 1.5

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
            self.center += self.speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.speed_factor

        # 根据self.center 更新rect
        self.rect.centerx = self.center
        self.rect.centery = self.height

    def blitme(self):
        """在指定位置绘制狗狗"""
        self.screen.blit(self.image, self.rect)


class Ball(Sprite):
    """下坠的小球"""

    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.speed_factor = 1

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

    def create(self, screen_width):
        """重新生成一个小球"""
        self.x = random.randint(0, screen_width - self.rect.width)
        self.y = -self.rect.height
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        """球匀速下坠"""
        self.y += self.speed_factor
        self.rect.y = self.y

    def blitme(self):
        """绘制球"""
        self.screen.blit(self.image, self.rect)


def create_ball(screen, screen_width, balls):
    """创建一个小球"""
    ball = Ball(screen)
    ball.create(screen_width)
    balls.add(ball)


def check_fleet_edges(balls):
    """到达下边界消失并重新生成球"""
    for ball in balls.sprites():
        if ball.check_edges():
            ball.create_again()
            break


def check_ball_dog_collections(screen, balls, dog):
    """检查球和狗狗是否相碰"""
    if pygame.sprite.spritecollideany(dog, balls):
        ball = Ball(screen)
        balls.add(ball)


def update_ball(balls, dog, screen):
    """检查是否达到下边界或碰到狗狗，更新位置"""
    check_fleet_edges(balls)
    check_ball_dog_collections(screen, balls, dog)
    balls.update()


def update_screen(bg_color, screen, dog, balls):
    """更新屏幕，切换新屏幕"""
    screen.fill(bg_color)
    dog.blitme()
    balls.draw(screen)

    pygame.display.flip()


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


def run_game():
    pygame.init()
    screen_width = 1200
    screen_height = 800
    bg_color = (124, 200, 230)
    screen = pygame.display.set_mode(
        (screen_width, screen_height))
    pygame.display.set_caption("catch_ball")

    dog = Dog(screen)
    balls = Group()

    create_ball(screen, screen_width, balls)

    while True:
        check_events(dog)
        dog.update()
        update_ball(balls, screen, screen_width)
        update_screen(bg_color, screen, dog, balls)


run_game()

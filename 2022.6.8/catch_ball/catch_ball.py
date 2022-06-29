import pygame

import game_functions as gf
from pygame.sprite import Group
from settings import Settings
from dog import Dog


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("catch_ball")

    dog = Dog(ai_settings, screen)
    balls = Group()

    gf.create_ball(ai_settings, screen, balls)

    while True:
        gf.check_events(dog)
        dog.update()
        gf.update_ball(ai_settings, screen, dog, balls)
        gf.update_screen(ai_settings, screen, dog, balls)


run_game()

import sys
import pygame
from bullet import Bullet

def check_event(ai_settings,screen,ship,bullets):
    """this function will check events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False
        

def update_screen(ai_setting,screen, ship, bullets):
    screen.fill(ai_setting.bg_color)
    ship.blitme()
    pygame.display.flip()

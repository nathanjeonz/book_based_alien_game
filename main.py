import pygame 
from pygame.sprite import Group
from shipFile import Ship
import game_function as gf
from settings import Settings
from alien import Alien

def run_game():
    pygame.init()
    ai_setting = Settings()

    screen = pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))
    
    ship = Ship(ai_setting, screen)
    bullets = Group()
    aliens = Group()

    gf.create_fleet(ai_setting, screen,ship, aliens)



    running = True
    while running == True:        
        gf.check_event(ai_setting, screen, ship, bullets) 
        ship.update()

        gf.update_bullets(ai_setting, screen, ship, aliens, bullets)

        gf.update_aliens(ai_setting,ship,aliens)
        gf.update_screen(ai_setting,screen,ship, aliens, bullets)


        



run_game()


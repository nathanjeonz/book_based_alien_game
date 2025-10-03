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


import pygame
from pygame.sprite import Group
from shipFile import Ship
import game_function as gf
from settings import Settings
from alien import Alien
from game_stats import GameStats
from scoreboard import Scoreboard

def run_game():
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")

    from game_stats import GameStats
    from scoreboard import Scoreboard

    stats = GameStats(ai_setting)
    sb = Scoreboard(ai_setting, screen, stats)

    ship = Ship(ai_setting, screen)
    bullets = Group()
    aliens = Group()

    gf.create_fleet(ai_setting, screen, ship, aliens)

    running = True
    while running:
        gf.check_event(ai_setting, screen, ship, bullets, stats)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_setting, screen, ship, aliens, bullets, stats, sb)
            gf.update_aliens(ai_setting, ship, aliens, stats, screen, bullets, sb)
        gf.update_screen(ai_setting, screen, ship, aliens, bullets, sb, stats)

run_game()


import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard



def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    play_button = Button(ai_settings, screen, "Play")

    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    gf.creat_fleet(ai_settings, screen, aliens, ship)#这里就是因为alien和ship位置与原函数的位置颠倒就导致出现“Group没有rect属性”的错误报告

    while True:
        gf.check_events(ship, ai_settings, screen, stats, sb, play_button, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.updat_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button, sb)




run_game()



#!/usr/bin/python3
'''
file        : world.py
description : This file manage all game worl stuff.
author      : remi.boivin@epitech.eu
'''

from random import randrange
from ship import Ship
import json
import pygame
import math
from enemy import Enemy


class World():
    """
        The class will contain all game world stuff
    """

    def __init__(self, screen):
        self.world = {}
        self.screen = screen
        self.level = 1
        self.wave_length = 0

    def start(self, x, y):
        self.player = Ship("assets/ship_1.png", (800, 900))
        self.enemies = []

        for i in range(10):
            enemy = Enemy("assets/pixel_ship_red_small.png",
                          (randrange(20, 950), randrange(-800, -10)))
            self.enemies.append(enemy)
        enemy = Enemy("assets/pixel_ship_green_small.png",
                      (randrange(20, 950), randrange(-1800, -30)), 1, 100)
        self.enemies.append(enemy)

    def update(self, x, y):
        keys = pygame.key.get_pressed()
        posX, posY = self.player.get_position()
        level_font = pygame.font.SysFont("comicsans", 45)
        Level_label = level_font.render(f"Level:  {self.level}", 1, (255, 255, 255))
        player_killed_font = pygame.font.SysFont("comicsans", 45)
        player_killed_label = player_killed_font.render(f"Score:  {self.player.score}", 1, (255, 255, 255))
        if len(self.enemies) == 0:
            self.level += 1
            self.player.shield = 30
            self.wave_length += 5
            i = 0
            for i in range(self.wave_length):
                enemy = Enemy("assets/pixel_ship_red_small.png",
                              (randrange(20, 950), randrange(-800, -10)))
                self.enemies.append(enemy)
                i += 1
            enemy = Enemy("assets/pixel_ship_green_small.png",
                          (randrange(20, 950), randrange(-1800, -30)), 1, 100)
            self.enemies.append(enemy)

        if keys[pygame.K_SPACE]:
            self.player.shoot()
        self.player.move(self.screen)
        self.screen.fill((0, 0, 0))
        self.screen.blit(
            self.player.get_item_img(),
            self.player.get_position())
        for enemy in self.enemies:
            enemy.move()
            enemy.draw_lasers(self.screen)
            enemy.move_lasers(4, self.player)
            enemy.health_bar(self.screen)
            if randrange(0, 2 * 60) == 1 and enemy.get_position()[1] >= 0:
                enemy.shoot()
            if enemy.position[1] > y - enemy.img_item.get_height():
                enemy.__del__()
                self.enemies.remove(enemy)
            self.screen.blit(enemy.get_item_img(), enemy.get_position())
        self.player.ship_collisions(self.enemies)
        self.player.draw_lasers(self.screen)
        self.player.move_lasers(8, self.enemies, self.screen)
        self.player.explosion.update(self.screen)
        self.player.health_bar(self.screen)
        self.player.shield_bar(self.screen)
        self.screen.blit(Level_label, (40, 20))
        self.screen.blit(player_killed_label, (650, 20))

        if self.player.is_death():
            return 0

    # def __del__(self):
    #     pass

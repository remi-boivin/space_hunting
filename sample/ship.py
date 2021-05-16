#!/usr/bin/python3
'''
file        : ship.py
description : This file contain ship class stuff.
author      : remi.boivin@epitech.eu
'''

import pygame
from laser import Laser
from random import randrange
from item import Item
import os
from explosion import Explosion

class Ship(Item):

    def __init__(self, ship, position=(800, 900)):
        super().__init__(ship, position)
        self.vel = 6
        self.lasers = []
        self.COOLDOWN = 30
        self.cool_down_counter = 0
        self.score = 0
        self.max_health = 100
        self.shield = 30
        self.max_shield = 30
        self.explosion = Explosion((-800, -900), 23)

    def move(self, screen):
        posX, posY = self.position
        width_img, height_img = self.img_item.get_size()
        keys = pygame.key.get_pressed()
        width, height = screen.get_size()
        if keys[pygame.K_LEFT]:
            if posX - self.vel > 0:
                posX -= self.vel
        elif keys[pygame.K_RIGHT]:
            if posX + self.vel < width - width_img:
                posX += self.vel
        elif keys[pygame.K_UP]:
            if posY - self.vel > 0:
                posY -= self.vel
        elif keys[pygame.K_DOWN]:
            if posY + self.vel < height - (height_img + 40):
                posY += self.vel
        self.set_position((posX, posY))

    def move_lasers(self, vel, objs, screen):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(950):
                self.lasers.remove(laser)
            for obj in objs:
                if laser.collision(obj):
                    try:
                        self.lasers.remove(laser)
                    except BaseException:
                        print("exeption catched")
                    if obj.health > 0:
                        obj.health -= 10
                    else:
                        self.score += 2
                        self.explosion = Explosion(obj.position, 23)

                        obj.__del__()
                        objs.remove(obj)

    def health_bar(self, window):
        pygame.draw.rect(
            window,
            (255,
             0,
             0),
            (self.position[0],
             self.position[1] +
             self.img_item.get_height() +
             30,
             self.img_item.get_width(),
             10))
        pygame.draw.rect(window,
                         (0,
                          245,
                          0),
                         (self.position[0],
                          self.position[1] + self.img_item.get_height() + 30,
                          self.img_item.get_width() * (self.health / self.max_health),
                          12))

    def shield_bar(self, window):
        pygame.draw.rect(
            window,
            (255,
             0,
             0),
            (self.position[0],
             self.position[1] +
             self.img_item.get_height() +
             10,
             self.img_item.get_width(),
             10))
        pygame.draw.rect(window,
                         (0,
                          0,
                          255),
                         (self.position[0],
                          self.position[1] + self.img_item.get_height() + 10,
                          self.img_item.get_width() * (self.shield / self.max_shield),
                          12))

    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def draw_lasers(self, window):
        for laser in self.lasers:
            laser.draw(window)

    def shoot(self, img='assets/pixel_laser_red.png'):
        if self.cool_down_counter == 0:
            position = self.set_center(self.img_item, pygame.image.load(img))
            self.lasers.append(Laser(position, img))
            self.cool_down_counter = 1

    def is_death(self):
        if self.health <= 0:
            return True

    def ship_collisions(self, objs):
        for obj in objs:
            if self.collision(obj):
                obj.__del__()
                objs.remove(obj)
                self.health -= (50 - self.shield)
                self.shield = 0

    # def __del__(self):
        # super().__del__()
        # del self.lasers
        # del self.COOLDOWN
        # del self.cool_down_counter
        # del self.health
        # del self.max_health
        # del self.shield
        # del self.max_shield

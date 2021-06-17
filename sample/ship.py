#!/usr/bin/python3
'''
file        : ship.py
description : This file contain ship class stuff.
author      : remi.boivin@epitech.eu
'''

import pygame
from random import randrange
from entity import Entity
import os
from explosion import Explosion
from heart import Heart

class Ship(Entity):

    def __init__(self, ship, position=(800, 900), velocity=6):
        super().__init__(ship, position, velocity)
        self.score = 0
        self.explosion = Explosion((-800, -900), 23)
        self.hearts = []
        position = (128, 64)
        for i in range(3):
            self.hearts.append(Heart('assets/make_tileset/hearth.png', (position)))
            position = (position[0] + 64, position[1])

    def move(self, screen):
        posX, posY = self.position
        width_img, height_img = self.img_item.get_size()
        keys = pygame.key.get_pressed()
        width, height = screen.get_size()
        if keys[pygame.K_LEFT]:
            if posX - self.velocity > 0:
                posX -= self.velocity
        elif keys[pygame.K_RIGHT]:
            if posX + self.velocity < width - width_img:
                posX += self.velocity
        elif keys[pygame.K_UP]:
            if posY - self.velocity > 0:
                posY -= self.velocity
        elif keys[pygame.K_DOWN]:
            if posY + self.velocity < height - (height_img + 40):
                posY += self.velocity
        self.set_position((posX, posY))

    def move_lasers(self, velocity, objs, shields):
        self.cooldown()
        for laser in self.lasers:
            laser.move(velocity)
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
                        self.score += obj.get_score()
                        self.explosion = Explosion(obj.position, 23)

                        obj.__del__()
                        objs.remove(obj)
            for shield in shields:
                if laser.collision(shield):
                        try:
                            self.lasers.remove(laser)
                        except BaseException:
                            print("exeption catched")


    def ship_collisions(self, objs):
        for obj in objs:
            if self.collision(obj):
                obj.__del__()
                objs.remove(obj)
                self.health -= 50

    # def __del__(self):
        # super().__del__()
        # del self.lasers
        # del self.COOLDOWN
        # del self.cool_down_counter
        # del self.health
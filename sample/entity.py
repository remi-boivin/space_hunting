#!/usr/bin/python3
'''
file        : entity.py
description : This file contain methods for all kind of entities.
author      : remi.boivin@epitech.eu
'''

from item import Item
import pygame
from laser import Laser

class Entity(Item):
    """
        The class will contain all methods for all kind of entities.
    """

    def __init__(self, entity_img, position, vel=0.3, lives=100, xp=0):
        super().__init__(entity_img, position)
        self.lives = lives
        self.xp = xp
        self.velocity = vel
        self.lasers = []
        self.COOLDOWN = 30
        self.cool_down_counter = 0


    def get_damages(self, damage):
        self.lives -= damage
        if is_alive() == False:
            self.lives = 0

    def set_velocity(self, vel = 0.3):
        self.velocity = vel

    def is_alive(self):
        if self.lives > 0:
            return True
        else:
            return False

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
        if len(self.hearts) == 0:
            return True
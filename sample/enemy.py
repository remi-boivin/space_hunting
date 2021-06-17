#!/usr/bin/python3
'''
file        : enemy.py
description : This file contain enemy class stuff.
author      : remi.boivin@epitech.eu
'''

from entity import Entity
import pygame
from laser import Laser


class Enemy(Entity):

    def __init__(self, ship, pos, score=10, velocity=0.3, health=10):
        super().__init__(ship, pos, velocity)
        self.health = health
        self.max_health = health
        self.score = score

    def move_lasers(self, velocity, obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(-velocity)
            if laser.collision(obj):
                if len(obj.hearts) > 0:
                    obj.hearts[-1].__del__()
                    obj.hearts.remove(obj.hearts[-1])
                self.lasers.remove(laser)

    def get_score(self):
        return self.score

    def move(self):
        posX, posY = self.position
        posY += self.velocity
        self.set_position((posX, posY))
        del posX
        del posY

    def shoot(self):
        super().shoot('assets/pixel_laser_blue.png')
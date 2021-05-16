#!/usr/bin/python3
'''
file        : enemy.py
description : This file contain enemy class stuff.
author      : remi.boivin@epitech.eu
'''

from ship import Ship
import pygame
from laser import Laser


class Enemy(Ship):

    def __init__(self, ship, pos, vel=1, health=10):
        super().__init__(ship, pos)
        self.health = health
        self.max_health = health
        self.vel = vel

    def move_lasers(self, vel, obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(-vel)
            if laser.collision(obj):
                if obj.shield > 0:
                    obj.shield -= 10
                else:
                    if obj.health > 0:
                        obj.health -= 5
                self.lasers.remove(laser)

    def move(self):
        posX, posY = self.position
        posY += self.vel
        self.set_position((posX, posY))
        del posX
        del posY

    def shoot(self):
        super().shoot('assets/pixel_laser_blue.png')

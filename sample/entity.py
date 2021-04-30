#!/usr/bin/python3
'''
file        : entity.py
description : This file contain methods for all kind of entities.
author      : remi.boivin@epitech.eu
'''

class Entity():
    """
        The class will contain all methods for all kind of entities.
    """

    def __init__(self, lives=100, xp=0):
        self.lives = lives
        self.xp = xp

    def get_damages(self, damage):
        self.lives -= damage
        if is_alive() == False:
            self.lives = 0

    def is_alive(self):
        if self.lives > 0:
            return True
        else:
            return False
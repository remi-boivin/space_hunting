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

from level import Level


class World():
    """
        The class will contain all game world stuff
    """

    def __init__(self, screen):
        self.world = {}
        self.screen = screen
        self.level = 1

    def start(self, x, y):
        self.level = Level(self.screen)
        self.level.load_level()

    def update(self, x, y):
        if self.level.update(x, y) == 0:
            return 0

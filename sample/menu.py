#!/usr/bin/python3
'''
file        : world.py
description : This file manage all game worl stuff.
author      : remi.boivin@epitech.eu
'''

from world import World
import pygame

if __name__ == "__main__":
    pygame.font.init()
    lost_font = pygame.font.SysFont("comicsans", 60)
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    running = True
    key = False
    scene = World(screen)
    clock = pygame.time.Clock()
    pause = False
    x, y = screen.get_size()

    scene.start(x, y)
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        if scene.update(x, y) == 0:
            lost_label = lost_font.render("You Lost!!", 1, (255, 255, 255))
            screen.blit(lost_label, (y / 2 - lost_label.get_width() / 2, 350))
            pause = True
        while pause:
            e = pygame.event.get()
            for ev in e:
                if ev.type == pygame.QUIT or ev.key == pygame.K_ESCAPE:
                    pause = False
                    running = False

            pygame.display.update()
        pygame.display.update()

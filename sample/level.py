from ship import Ship
from enemy import Enemy
from pytmx import load_pygame
from shield import Shield
from load_bar import LoadBar as LevelBar
from color import Color
import pygame
from random import randrange


class Level():

    def __init__(self, screen, level_map="assets/space_invaders.tmx"):
        self.screen = screen
        self.tmxdata = load_pygame(level_map)

    def load_level(self):
        x = 0
        y = 0

        self.enemies = []
        self.shields = []
        for y in range(17):
            for x in range(30):
                props = self.tmxdata.get_tile_properties(x, y, 0)
                if props != None:
                    position = (x * 64, y * 64)
                    img = f"assets/{props['source']}"
                    id = props['id']
                    if id == 0:
                        self.enemies.append(Enemy(img, position, 10))
                    elif id == 1:
                        self.enemies.append(Enemy(img, position, 20))
                    elif id == 2:
                        self.enemies.append(Enemy(img, position, 25))
                    elif id == 3:
                        self.enemies.append(Enemy(img, position, 30))
                    elif id == 4:
                        self.player = Ship(img, position)
                    elif id == 5:
                        self.shields.append(Shield(img, position))
                    elif id == 11:
                        self.level_bar = LevelBar(img, position)
                    else:
                        print(
                            f"{Color.ERROR} [ERROR]: Unknown id. You should check the map", flush=True)
                else:
                    print(
                        f"{Color.WARNING} [WARING]: No pygame.Surface at this position", flush=True)
                x += 1
            x = 0
            y += 1

    def update_enemies(self, y):
        """ Update enemies on the screen each while iteration"""

        for enemy in self.enemies:
            enemy.move()
            enemy.draw_lasers(self.screen)
            enemy.move_lasers(4, self.player)
            if randrange(0, 2 * 60) == 1 and enemy.get_position()[1] >= 0:
                enemy.shoot()
            if enemy.position[1] > y - enemy.img_item.get_height():
                enemy.__del__()
                self.enemies.remove(enemy)
            self.screen.blit(enemy.get_item_img(), enemy.get_position())

    def update_player(self):
        """ Update player on the screen each while iteration"""

        player_killed_font = pygame.font.SysFont("comicsans", 45)
        player_killed_label = player_killed_font.render(
            f"Score:  {self.player.score}", 1, (255, 255, 255))

        self.player.move(self.screen)
        self.screen.blit(
            self.player.get_item_img(),
            self.player.get_position())
        self.player.ship_collisions(self.enemies)
        self.player.draw_lasers(self.screen)
        self.player.move_lasers(8, self.enemies, self.shields)
        self.player.explosion.update(self.screen)
        self.screen.blit(player_killed_label, (650, 20))
        if self.player.is_death():
            return 0

    def update_shield(self):
        """ Update shields on the screen each while iteration"""

        for shield in self.shields:
            for enemy in self.enemies:
                shield.shield_collision(enemy, self.enemies)
                for laser in enemy.lasers:
                    shield.shield_collision(laser, enemy.lasers, 1)
            shield.is_alive(self.shields)
            shield.shield_bar(self.screen)
            self.screen.blit(shield.get_item_img(), shield.get_position())

    def update(self, x, y):
        keys = pygame.key.get_pressed()
        # TODO add enemy generation

        self.screen.fill((0, 0, 0))
        self.update_enemies(y)
        if keys[pygame.K_SPACE]:
            self.player.shoot()
        if self.update_player() == 0:
            return 0
        self.update_shield()
        self.screen.blit(self.level_bar.get_item_img(),
                         self.level_bar.get_position())

        for heart in self.player.hearts:
            self.screen.blit(heart.get_item_img(), heart.get_position())

    def __del__(self):
        self.screen

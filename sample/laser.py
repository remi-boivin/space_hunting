# from sample.enemy import Enemy
import pygame
import math
from item import Item


class Laser(Item):

    def __init__(
            self,
            position=(
                800,
                900),
            laser='assets/pixel_laser_red.png',
            vel=-8):
        super().__init__(laser, position)
        self.vel = vel

    def move(self, vel):
        posX, posY = self.position
        posY -= vel
        self.set_position((posX, posY))

    def draw(self, window):
        window.blit(self.img_item, self.position)

    def collision(self, obj):
        return self.collide(obj)

    def off_screen(self, height):
        posX, posY = self.position
        return not(posY <= height and posY >= 0)


# def collide(self, obj):
#     posX, posY = self.position
#     posX_obj, posY_obj = obj.position
#     offset_x = int(posX_obj - posX)
#     offset_y = int(posY_obj - posY)
#     return self.mask.overlap(obj.mask, (offset_x, offset_y)) is not None

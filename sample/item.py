from pygame.image import load
from pygame.mask import from_surface
from pygame.time import Clock
import pygame
from explosion import Explosion


class Item():

    def __init__(self, img, position):
        self.position = position
        self.img_item = load(img)
        self.mask = from_surface(self.img_item)
        self.health = 100
        self.max_health = 100
        self.last = pygame.time.get_ticks()
        # self.explosion = [
        #     "assets/explosion/explosion_1.png",
        #     "assets/explosion/explosion_2.png",
        #     "assets/explosion/explosion_3.png",
        #     "assets/explosion/explosion_4.png",
        #     "assets/explosion/explosion_5.png",
        #     "assets/explosion/explosion_6.png",
        #     "assets/explosion/explosion_7.png",
        #     "assets/explosion/explosion_8.png",
        #     "assets/explosion/explosion_9.png",
        #     "assets/explosion/explosion_10.png",
        #     "assets/explosion/explosion_11.png",
        #     "assets/explosion/explosion_12.png"]

    def get_position(self):
        return self.position

    def get_item_img(self):
        return (self.img_item)

    def set_center(self, parent, child):
        child_orig = child.convert()
        parent_rect = parent.get_rect()
        image_rect = child_orig.get_rect(center=parent_rect.center)
        position = (
            self.position[0] -
            parent_rect.center[0] /
            2,
            self.position[1] -
            parent_rect.center[1] /
            2)
        return position

    # def draw_explosion(self, screen, obj):
        # self.explosion.update(screen)
        # pygame.display.update()

    def collision(self, obj):
        return self.collide(obj)

    def collide(self, obj):
        posX, posY = self.position
        posX_obj, posY_obj = obj.position
        offset_x = int(posX_obj - posX)
        offset_y = int(posY_obj - posY)
        return self.mask.overlap(obj.mask, (offset_x, offset_y)) is not None

    def is_in_square_screen(self, screen, posX, posY):
        x, y = screen.get_size()
        if posX > 0 and posX < x and posY > 0 and posY < y:
            return True
        else:
            return False
    def set_damage(self, damage=1):
        if self.health - damage >= 0:
            self.health -= damage
    
    def get_health(self):
        return self.health

    def set_position(self, position):
        if position > (0, 0):
            self.position = position

    def __del__(self):
        pass

from item import Item
import pygame

class Shield(Item):

    def __init__(self, img_shield, pos):
        super().__init__(img_shield, pos)
        # self.health = 30
        # self.max_health = 30


    def shield_bar(self, window):
        pygame.draw.rect(
            window,
            (255,
             0,
             0),
            (self.position[0],
             self.position[1] +
             self.img_item.get_height() +
             10,
             self.img_item.get_width(),
             10))
        pygame.draw.rect(window,
                         (0,
                          0,
                          255),
                         (self.position[0],
                          self.position[1] + self.img_item.get_height() + 10,
                          self.img_item.get_width() * (self.health / self.max_health),
                          12))

    def shield_collision(self, obj, objs, damages=10):
        if self.collision(obj):
            obj.__del__()
            objs.remove(obj)
            self.set_damage(damages)

    def is_alive(self, shields):
        if self.get_health() == 0:
            try:
                self.__del__()
                shields.remove(self)
            except BaseException:
                print("exeption catched")
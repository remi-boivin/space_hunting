from ship import Ship
from enemy import Enemy


class Scene():

    def __init__(self, screen):
        self.screen = screen

    def load_scene(self):
        self.ship = Ship(self.screen)
        # self.ship1 = Ship('assets/ship_1.png', (800,300), self.screen)
        # enemies = Enemy('assets/ship_3.png', (60,40), self.screen)
        # enemies.Ship(self.screen, (90,40))
        # enemies.wave(self.screen, 4, 100, 100)

    def update(self):
        self.screen.fill((0, 0, 0))  # Fills the screen with black
        self.ship.move(self.screen)

    def __del__(self):
        self.screen

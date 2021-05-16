import pygame

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.explosions = []
        for i in range(9):
            filename = 'explosion_{}.png'.format(i)
            img = pygame.image.load(f'assets/explosion/{filename}').convert()
            img.set_colorkey((0,0,0))
            # img_lg = pygame.transform.scale(img, (75, 75))
            self.explosions.append(img)
            # img_sm = pygame.transform.scale(img, (32, 32))
            # explosions].append(img_sm)
            # expl = Explosion(obj.get_position(), 'sm')
        self.image = self.explosions[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50
        self.counter = 0
        self.index = 0

    def update(self, screen):
        explosion_speed = 8
        self.counter += 1
        if self.counter >= explosion_speed and self.index < len(self.explosions) - 1:
            self.counter = 0
            self.index += 1
            screen.blit(self.explosions[self.index], self.rect.center)
        if self.index >= len(self.explosions) - 1 and self.counter >= explosion_speed:
            self.kill()
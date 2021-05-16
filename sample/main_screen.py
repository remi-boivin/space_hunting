import pygame


class MainScreen():

    def __init__(self, texts):
        self.texts = texts

    def aff_menu(self, screen, x, y, color=(255, 255, 255)):
        pygame.font.init()
        font = pygame.font.Font(pygame.font.get_default_font(), 56)
        for text in self.texts:
            img = font.render(text, True, color)
            y -= 90
            screen.blit(img, (x, y))

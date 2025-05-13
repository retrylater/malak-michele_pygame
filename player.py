import pygame

class Nonna:
    def __init__(self, screen, pos, platform):
        self.screen = screen
        self.platform = platform
        self.image = pygame.image.load()
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

        self.vx = 0
        self.vy = 0
        self.g= 0.5
        
import pygame
import random


class Pillola:
    def __init__(self):
        immagine_base = pygame.image.load("pillola.png").convert_alpha()
        self.altezza = 40
        self.larghezza = 40
        self.image = pygame.transform.scale(immagine_base, (self.larghezza, self.altezza))
        self.mask = pygame.mask.from_surface(self.image, 0)
        self.vx = 8
        self.x = 800
        self.y = random.randint(0, 600 - self.altezza)

    def aggiorna_p(self):
        self.x -= self.vx

    def disegna_p(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def fuori_schermo_p(self):
        return self.x + self.larghezza < 0

    def collide_p(self, pos_nonna, mask_nonna):
        offset = (int(self.x - pos_nonna[0]), int(self.y - pos_nonna[1]))
        return self.mask.overlap(mask_nonna, offset) is not None
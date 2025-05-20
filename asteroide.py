import pygame
import random

class Asteroide:
    def __init__(self):
        immagine_base = pygame.image.load("asteroide.png").convert_alpha()
        larghezza_a = 80
        altezza_a = 80
        self.image = pygame.transform.scale(immagine_base, (larghezza_a, altezza_a))
        self.mask = pygame.mask.from_surface(self.image, 0)
        self.vx = 8
        self.x = 800
        self.y = random.randint(0, 600 - int (altezza_a))
        
        self.altezza = altezza_a
        self.larghezza = larghezza_a

    def aggiorna_a(self, Rallentamento):
        if Rallentamento:
            self.x -= (self.vx/2)
        else:
            self.x -= self.vx
 

    def disegna_a(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def fuori_schermo_a(self):
        return self.x + self.larghezza < 0
    
    def collide_a(self, pos_nonna, mask_nonna):
        offset = (int(self.x - pos_nonna[0]), int(self.y - pos_nonna[1]))
        return self.mask.overlap(mask_nonna, offset) is not None

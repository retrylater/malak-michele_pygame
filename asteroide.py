import pygame
import random

class Asteroide:
    def __init__(self):
        immagine_base = pygame.image.load("asteroide.png")
        scala_x = random.uniform(0.5, 1.5)
        scala_y = random.uniform(0.5, 1.5)
        larghezza_base = 100
        altezza_base = 100
        larghezza_a = larghezza_base * scala_x
        altezza_a = altezza_base * scala_y
        self.image = pygame.transform.scale(immagine_base, (larghezza_a, altezza_a))
        self.vx = 8
        
        self.x = 800
        self.y = random.randint(0, 600 - int (altezza_a))

        #self.rect.topleft = (self.x, self.y)
        
        self.altezza = altezza_a
        self.larghezza = larghezza_a


    def aggiorna_a(self):
        self.x -= self.vx

    def disegna(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def fuori_schermo(self):
        return self.x + self.larghezza < 0
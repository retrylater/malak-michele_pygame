import pygame

class Asteroide:
    def __init__(self, pos = []):
        immagine_originale = pygame.image.load("asteroide.png")
        nuova_larghezza = 50
        nuova_altezza = 50
        self.image = pygame.transform.scale(immagine_originale, (nuova_larghezza, nuova_altezza))
        
        self.x = pos[0]
        self.y = pos[1]
        
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

        self.vx = -5

    def aggiorna(self):
        self.x += self.vx
        self.rect.x = self.x

    def disegna(self, screen):
        screen.blit(self.image, (self.x, self.y))